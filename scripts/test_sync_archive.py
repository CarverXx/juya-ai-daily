"""Offline regression tests for archive integrity and no-write guarantees."""
import hashlib
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import sync_archive as archive


def article(date):
    return (f"# AI 早报 {date}\n\n" + "Public news and original source links.\n" * 30).encode()


def rss(date):
    return f'<rss><channel><item><title>{date}</title><link>{archive.SITE}/issues/{date}/</link></item></channel></rss>'.encode()


def snapshot(root):
    return {str(p.relative_to(root)): (p.read_bytes(), p.stat().st_mtime_ns) for p in root.rglob("*") if p.is_file()}


class SyncTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "BACKUP").mkdir()
        (self.root / "BACKUP/62_2026-04-17.md").write_bytes(article("2026-04-17"))
        (self.root / "README.md").write_text(archive.BEGIN + "\npending\n" + archive.END)
        self.sources = {"2026-04-18": {"kind": "author-website", "url": "https://example.test/new.md"}}

    def fake_fetch(self, url):
        return rss("2026-04-18") if url.endswith("rss.xml") else article("2026-04-18")

    def test_dry_run_does_not_write_or_download_articles(self):
        before = snapshot(self.root)
        with patch.object(archive, "discover", return_value=self.sources), patch.object(archive, "fetch", return_value=rss("2026-04-18")) as fetch:
            result = archive.sync(self.root, dry_run=True)
        self.assertEqual(result["new"], 1)
        fetch.assert_called_once_with(archive.SITE + "/rss.xml")
        self.assertEqual(snapshot(self.root), before)

    def test_import_idempotence_and_offline_verification(self):
        with patch.object(archive, "discover", return_value=self.sources), patch.object(archive, "fetch", side_effect=self.fake_fetch):
            self.assertEqual(archive.sync(self.root)["new"], 1)
            before = snapshot(self.root)
            self.assertEqual(archive.sync(self.root)["files_changed"], 0)
            self.assertEqual(snapshot(self.root), before)
        self.assertEqual(archive.sync(self.root, verify_only=True)["verified"], 2)

    def test_corrupted_existing_article_is_rejected(self):
        with patch.object(archive, "discover", return_value=self.sources), patch.object(archive, "fetch", side_effect=self.fake_fetch):
            archive.sync(self.root)
        path = self.root / "BACKUP/2026-04-18.md"
        path.write_bytes(path.read_bytes() + b"changed")
        with self.assertRaisesRegex(ValueError, "changed or removed"):
            archive.sync(self.root, verify_only=True)

    def test_bad_download_leaves_archive_untouched(self):
        before = snapshot(self.root)
        def bad_fetch(url):
            return rss("2026-04-18") if url.endswith("rss.xml") else b"<!DOCTYPE html>" + b"error" * 200
        with patch.object(archive, "discover", return_value=self.sources), patch.object(archive, "fetch", side_effect=bad_fetch):
            with self.assertRaisesRegex(ValueError, "HTML response"):
                archive.sync(self.root)
        self.assertEqual(snapshot(self.root), before)

    def test_duplicate_local_date_is_rejected(self):
        (self.root / "BACKUP/2026-04-17.md").write_bytes(article("2026-04-17"))
        with self.assertRaisesRegex(ValueError, "duplicate local date"):
            archive.local_articles(self.root)

    def test_pinned_blob_verification(self):
        body = article("2026-04-18")
        correct = hashlib.sha1(f"blob {len(body)}\0".encode() + body).hexdigest()
        source = {"url": "https://example.test/news.md", "git_blob_sha1": correct}
        with patch.object(archive, "fetch", return_value=body):
            self.assertEqual(archive.download_one(("2026-04-18", source))[1], body)
            source["git_blob_sha1"] = "0" * 40
            with self.assertRaisesRegex(ValueError, "hash mismatch"):
                archive.download_one(("2026-04-18", source))

    def test_wrong_date_and_stale_rss_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "wrong date"):
            archive.validate_markdown(article("2026-04-17"), "2026-04-18")
        with self.assertRaisesRegex(ValueError, "RSS dates disagree"):
            archive.validate_rss(rss("2026-04-17"), {"2026-04-17", "2026-04-18"})


if __name__ == "__main__":
    unittest.main()
