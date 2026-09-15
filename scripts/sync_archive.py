#!/usr/bin/env python3
"""Manually archive Juya originals, Python 3.10+, standard library only.

No credentials, issue export, scheduler or mail. --dry-run never writes.
Existing articles are immutable. archive-index.json holds source receipts.
"""
import argparse
import concurrent.futures
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

SITE = "https://daily.juya.uk"
BASE_REPO = "CarverXx/juya-ai-daily"
BASE_REV = "f78252dc7f3bf9bfbcd35eacf4b76cd3faa7daf3"
MIRRORS = (
    ("Baldman-JYH/juya-ai-daily", "a91cbef50bd05e1c9032ca2c2bd76010eeaae008", "2026-04-18", "2026-06-08"),
    ("Baldman-JYH/juya-ai-daily-new", "9b50d713ad32ee1e2487b48094ad5b6a0e6306ab", "2026-06-12", "2026-06-17"),
)
FILE_RE = re.compile(r"^(?:\d+_)?(\d{4}-\d{2}-\d{2})\.md$")
BEGIN = "<!-- archive-status:start -->"
END = "<!-- archive-status:end -->"


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def fetch(url):
    for attempt in range(3):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (JuyaPersonalArchive/1.0)", "Accept": "*/*"})
            with urllib.request.urlopen(request, timeout=35) as response:
                body = response.read(8_000_001)
                if len(body) > 8_000_000:
                    raise ValueError("source exceeds 8 MB limit")
                return body
        except (urllib.error.URLError, TimeoutError):
            if attempt == 2:
                raise
            time.sleep(attempt + 1)


def validate_markdown(data, date):
    dt.date.fromisoformat(date)
    body = data.decode("utf-8-sig", errors="strict")
    if len(data) < 500 or "\x00" in body or re.search(r"<!doctype\s+html|<html(?:\s|>)", body[:2000], re.I):
        raise ValueError(f"{date}: empty, binary, or HTML response")
    headings = re.findall(r"^#{1,3}\s+(.+)$", body[:1000], re.M)
    if not headings or date not in headings[0]:
        raise ValueError(f"{date}: first Markdown heading has the wrong date")
    return body


def local_articles(root):
    result = {}
    for path in sorted((root / "BACKUP").glob("*.md")):
        match = FILE_RE.fullmatch(path.name)
        if not match:
            continue  # Preserve non-news fixtures such as 1_test2.md.
        date = match[1]
        if date in result:
            raise ValueError(f"duplicate local date: {date}")
        data = path.read_bytes()
        validate_markdown(data, date)
        result[date] = {"path": path.relative_to(root).as_posix(), "data": data}
    return result


def discover():
    sources = {}
    for repo, revision, start, end in MIRRORS:
        tree = json.loads(fetch(f"https://api.github.com/repos/{repo}/git/trees/{revision}?recursive=1"))
        if tree.get("truncated") or tree.get("sha") != revision:
            raise ValueError(f"incomplete or wrong pinned tree: {repo}")
        for entry in tree["tree"]:
            path = entry["path"]
            match = FILE_RE.fullmatch(Path(path).name)
            if entry["type"] == "blob" and path.startswith("BACKUP/") and match and start <= match[1] <= end:
                if match[1] in sources:
                    raise ValueError(f"duplicate source date: {match[1]}")
                sources[match[1]] = {"kind": "pinned-github-mirror", "repository": repo, "revision": revision,
                                    "source_path": path, "git_blob_sha1": entry["sha"],
                                    "url": f"https://raw.githubusercontent.com/{repo}/{revision}/{path}"}
        expected = {str(dt.date.fromisoformat(start) + dt.timedelta(days=i))
                    for i in range((dt.date.fromisoformat(end) - dt.date.fromisoformat(start)).days + 1)}
        if not expected.issubset(sources):
            raise ValueError(f"pinned mirror missing expected dates: {repo}")
    archive = fetch(f"{SITE}/archive/").decode("utf-8")
    dates = sorted(set(re.findall(r"/issues/(\d{4}-\d{2}-\d{2})/", archive)))
    if not dates:
        raise ValueError("author archive has no dated issue links")
    today = dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).date().isoformat()
    for date in dates:
        dt.date.fromisoformat(date)
        if date < "2026-06-18" or date > today:
            raise ValueError(f"unexpected author archive date: {date}")
        sources[date] = {"kind": "author-website", "url": f"{SITE}/markdown/{date}.md", "issue_url": f"{SITE}/issues/{date}/"}
    return sources


def validate_rss(data, dates):
    root = ET.fromstring(data)
    if root.tag != "rss":
        raise ValueError("invalid RSS root")
    items = root.findall("./channel/item")
    titles = [item.findtext("title", "") for item in items]
    if not titles or titles[0] != max(dates) or any(title not in dates for title in titles):
        raise ValueError("RSS dates disagree with author archive")
    for item in items:
        if item.findtext("link", "") != f"{SITE}/issues/{item.findtext('title')}/":
            raise ValueError("unexpected RSS item URL")
    return titles


def gaps(dates):
    first, last = dt.date.fromisoformat(min(dates)), dt.date.fromisoformat(max(dates))
    return [str(first + dt.timedelta(days=i)) for i in range((last - first).days + 1)
            if str(first + dt.timedelta(days=i)) not in dates]


def load_previous(root, local):
    path = root / "archive-index.json"
    if not path.exists():
        return {}
    records = json.loads(path.read_text())["articles"]
    entries = {entry["date"]: entry for entry in records}
    if len(entries) != len(records):
        raise ValueError("duplicate date in saved manifest")
    for date, entry in entries.items():
        article = local.get(date)
        if not article or article["path"] != entry["path"] or sha256(article["data"]) != entry["sha256"]:
            raise ValueError(f"saved archive was changed or removed: {date}; restore or review manually")
    return entries


def download_one(item):
    date, source = item
    data = fetch(source["url"])
    validate_markdown(data, date)
    if source.get("git_blob_sha1"):
        blob_hash = hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()
        if blob_hash != source["git_blob_sha1"]:
            raise ValueError(f"{date}: pinned Git blob hash mismatch")
    return date, data


def write_changed(path, data):
    if path.exists() and path.read_bytes() == data:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=".archive-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as file:
            file.write(data)
        os.chmod(temporary, 0o644)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
    return True


def build_manifest(local, previous, sources, downloaded):
    articles = []
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    for date in sorted(local):
        if date in previous:
            articles.append(previous[date])
            continue
        article = local[date]
        if date in downloaded:
            source, record = sources[date], {"retrieved_at": now}
        else:
            if not "2026-02-18" <= date <= "2026-04-17":
                raise ValueError(f"untracked article without a source receipt: {date}")
            source = {"kind": "original-fork", "repository": BASE_REPO, "revision": BASE_REV,
                      "source_path": article["path"], "url": f"https://raw.githubusercontent.com/{BASE_REPO}/{BASE_REV}/{article['path']}"}
            record = {}
        articles.append({"date": date, "path": article["path"], "sha256": sha256(article["data"]),
                         "bytes": len(article["data"]), "source": source, **record})
    return {"schema_version": 1, "author": "橘鸦 / Juya (@imjuya)", "author_site": SITE,
            "content_license": "CC BY-NC 4.0; third-party materials retain their own rights",
            "count": len(articles), "first_date": min(local), "latest_date": max(local), "missing_dates": gaps(local),
            "rss": {"url": f"{SITE}/rss.xml", "mode": "author feed snapshot, latest items only"}, "articles": articles}


def render_index(manifest):
    lines = ["# 橘鸦 AI 早报日期目录", "", "原作者：橘鸦 / Juya（@imjuya）。内容许可见 [LICENSE-CONTENT](LICENSE-CONTENT)。",
             "", f"共 **{manifest['count']} 篇**，{manifest['first_date']} 至 **{manifest['latest_date']}**。",
             "", "已知缺口：" + "、".join(manifest["missing_dates"]) + "。", "",
             "原文及 SHA-256、来源地址和固定版本见 [archive-index.json](archive-index.json)。历史 Issue 链接可能已失效，以下本地副本可读。", "",
             "| 日期 | 原文 | 取得来源 | SHA-256 前 12 位 |", "|---|---|---|---|"]
    labels = {"original-fork": "原 fork", "pinned-github-mirror": "固定版本历史副本", "author-website": "作者官网"}
    for entry in reversed(manifest["articles"]):
        lines.append(f"| {entry['date']} | [Markdown]({entry['path']}) | [{labels[entry['source']['kind']]}]({entry['source']['url']}) | `{entry['sha256'][:12]}` |")
    return ("\n".join(lines) + "\n").encode()


def render_readme_status(readme, manifest):
    if BEGIN not in readme or END not in readme or readme.index(BEGIN) >= readme.index(END):
        raise ValueError("README needs archive-status markers")
    items = "\n".join(f"- [{entry['date']}]({entry['path']})" for entry in reversed(manifest["articles"][-5:]))
    status = f"{BEGIN}\n原文 **{manifest['count']} 篇**，覆盖 {manifest['first_date']} 至 **{manifest['latest_date']}**。\n\n已知缺口：{'、'.join(manifest['missing_dates'])}。非日报测试文件不计入。\n\n{items}\n{END}"
    return (readme[:readme.index(BEGIN)] + status + readme[readme.index(END) + len(END):]).encode()


def sync(root, dry_run=False, verify_only=False, workers=4):
    local = local_articles(root)
    if not local:
        raise ValueError("restore the original fork before syncing")
    previous = load_previous(root, local)
    if verify_only:
        if not previous or set(previous) != set(local):
            raise ValueError("manifest does not cover every local article")
        manifest = json.loads((root / "archive-index.json").read_text())
        if (manifest["count"], manifest["first_date"], manifest["latest_date"], manifest["missing_dates"]) != (len(local), min(local), max(local), gaps(local)):
            raise ValueError("manifest coverage metadata is inconsistent")
        validate_rss((root / "rss.xml").read_bytes(), local)
        return {"mode": "verify", "verified": len(local), "latest": max(local), "missing_dates": gaps(local)}
    sources = discover()
    rss = fetch(f"{SITE}/rss.xml")
    validate_rss(rss, sources)
    pending = [(date, source) for date, source in sorted(sources.items()) if date not in local]
    planned = set(local) | set(sources)
    result = {"mode": "dry-run" if dry_run else "sync", "existing": len(local), "new": len(pending),
              "total": len(planned), "latest": max(planned), "missing_dates": gaps(planned)}
    if dry_run:
        return result
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        downloaded = dict(pool.map(download_one, pending))
    for date, data in downloaded.items():
        local[date] = {"path": f"BACKUP/{date}.md", "data": data}
    manifest = build_manifest(local, previous, sources, downloaded)
    readme = render_readme_status((root / "README.md").read_text(), manifest)
    changed = 0
    for date in downloaded:
        changed += write_changed(root / local[date]["path"], local[date]["data"])
    for name, data in {"archive-index.json": (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode(),
                       "ARCHIVE.md": render_index(manifest), "rss.xml": rss, "README.md": readme}.items():
        changed += write_changed(root / name, data)
    result["files_changed"] = changed
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--dry-run", action="store_true", help="inspect public indexes and local hashes without writing")
    modes.add_argument("--verify-only", action="store_true", help="verify all local hashes, coverage and RSS offline")
    parser.add_argument("--workers", type=int, default=4, choices=range(1, 9))
    args = parser.parse_args()
    try:
        print(json.dumps(sync(args.root.resolve(), args.dry_run, args.verify_only, args.workers), ensure_ascii=False, indent=2))
    except (ValueError, KeyError, OSError, ET.ParseError) as error:
        print(f"sync stopped: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
