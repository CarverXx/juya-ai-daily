# 橘鸦AI早报

> 本仓库将AI早报备份为Markdown存档并保存作者的RSS快照。资讯内容由AI辅助生成，可能存在错误，请以原始信息出处和官方信息为准。内容从互联网上获取，如有侵权请联系删除。

作者现行入口：[官网](https://daily.juya.uk/) · [日期目录](https://daily.juya.uk/archive/) · [RSS](https://daily.juya.uk/rss.xml)。旧 GitHub 上游及旧 Pages 已不可访问，不再作为同步来源。

## Links

| Platform | Link |
| :--- | :--- |
| RSS Feed | [Subscribe](https://daily.juya.uk/rss.xml) |
| Markdown 备份 | [BACKUP](https://github.com/CarverXx/juya-ai-daily/tree/master/BACKUP) |
| 作者官网 | [View](https://daily.juya.uk/) |
| 第三方多功能阅读器（@ViggoZ 制作） | [juya-daily](https://viggoz.github.io/juya-daily/) |
| AI早报 视频版-Bilibili | [Bilibili](https://space.bilibili.com/285286947) |
| AI早报 视频版-YouTube | [YouTube](https://www.youtube.com/@imjuya) |

---


## 存档状态

<!-- archive-status:start -->
原文 **207 篇**，覆盖 2026-02-18 至 **2026-09-15**。

已知缺口：2026-06-09、2026-06-10、2026-06-11。非日报测试文件不计入。

- [2026-09-15](BACKUP/2026-09-15.md)
- [2026-09-14](BACKUP/2026-09-14.md)
- [2026-09-13](BACKUP/2026-09-13.md)
- [2026-09-12](BACKUP/2026-09-12.md)
- [2026-09-11](BACKUP/2026-09-11.md)
<!-- archive-status:end -->

完整目录：[ARCHIVE.md](ARCHIVE.md)。逐日来源、固定版本和 SHA-256：[archive-index.json](archive-index.json)。`BACKUP/1_test2.md` 是原仓库测试文件，保留但不计入日报期数。

## 手动同步

本个人 fork 保留原 Git 历史。Python 3.10+，仅使用标准库，不需要 API key：

```bash
python3 scripts/sync_archive.py --dry-run
python3 scripts/sync_archive.py
python3 scripts/sync_archive.py --verify-only
```

- 预演检查公开来源目录、RSS 和本地原文哈希，显示新增数量与缺口；不写文件，也不下载新增正文。
- 正式同步先获取并验证全部新增正文，再保存原始字节、日期目录、来源回执和官网 RSS 快照。历史文件不改名、不覆盖；重复日期、错误页或哈希变化会终止并报错，被改动的原文须人工核查。
- 再次运行只导入新日期；来源不变时文件不变。`--verify-only` 离线核对全部原文哈希、日期覆盖和 RSS。
- 默认最多 4 个并行下载，可用 `--workers 1` 降低频率。来源失败时修复网络或稍后重试，不把错误页存成日报。
- `rss.xml` 是作者当前 RSS 快照（最近若干期），全量历史原文在 `BACKUP/`。

## 来源与历史保留

| 日期范围 | 来源 |
|---|---|
| 2026-02-18—04-17 | 本 fork 原有 59 篇，基线 `f78252dc7f3bf9bfbcd35eacf4b76cd3faa7daf3` |
| 2026-04-18—06-08 | `Baldman-JYH/juya-ai-daily`，固定 `a91cbef50bd05e1c9032ca2c2bd76010eeaae008` |
| 2026-06-09—06-11 | 已知缺口，已核实来源没有原文，不补造 |
| 2026-06-12—06-17 | `Baldman-JYH/juya-ai-daily-new`，固定 `9b50d713ad32ee1e2487b48094ad5b6a0e6306ab` |
| 2026-06-18 起 | 作者官网 `/markdown/YYYY-MM-DD.md` |

历史镜像下载核对固定 Git tree 的 blob SHA-1，全部存档另记 SHA-256。第三方副本只用于恢复历史。原文含 AI 辅助整理，新闻事实应回查官方原始来源。

旧 `main.py`、Zola 配置及 `.github/workflows/` 保留供 gitblog 模式研究；它们针对 GitHub Issues，不适用于当前官网来源。本同步脚本不运行旧程序、不启用旧 workflow 或部署 Pages。邮箱与定时早报由独立云端任务管理，本公开仓库不存账户、凭据或邮件记录。

---

## License

- 代码（脚本与站点生成逻辑，基于 [yihong0618/gitblog](https://github.com/yihong0618/gitblog)）：[MIT](./LICENSE)
- 文章内容（`BACKUP/`、`rss.xml`）：[CC BY-NC 4.0](./LICENSE-CONTENT)
- 转载要求：署名，禁止商用
- 第三方素材除外，按原权利声明

---

## Credits

Built with [gitblog](https://github.com/yihong0618/gitblog) by [@yihong0618](https://github.com/yihong0618)
