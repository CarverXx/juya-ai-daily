# [2026-06-06](https://github.com/imjuya/juya-ai-daily/issues/113)

![](http://testtttt.oss-cn-guangzhou.aliyuncs.com/imagehub/20260606/2026060608362516762672d7_cover_dca0.png)

# AI 早报 2026-06-06

**视频版**：[哔哩哔哩](https://www.bilibili.com/video/BV1Wu7m6WEQ6) ｜ [YouTube](https://www.youtube.com/watch?v=QPvXN2gmm1c)

## 概览
### 要闻
- OpenAI 确认系统 Bug 导致部分账户被误封 [↗](https://x.com/OpenAI/status/2062927046448431587) `#1`
- OpenAI 发布 Codex 更新：新增设置搜索与状态保存功能 [↗](https://x.com/OpenAIDevs/status/2062987643286438337) `#2`
- ChatGPT web端writing blocks新增直接发送邮件功能 [↗](https://x.com/ChatGPTapp/status/2062944254591430917) `#3`
### 模型发布
- Google 发布 Gemma 4 QAT 权重及全新移动端量化格式 [↗](https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/) `#4`
- 小红书 rednote-hilab 开源 20 亿参数 dots.tts [↗](https://rednote-hilab.github.io/dots.tts-demo/) `#5`
- OpenRouter上线图像模型Riverflow 2.5并提供限时免费调用 [↗](https://x.com/OpenRouter/status/2062951474406240687) `#6`
- Miso Labs 推出 8B 参数文本转语音模型 MisoTTS `#7`
### 开发生态
- Vercel 上线 skills.sh API 支持查询超 60 万开源技能 [↗](https://vercel.com/changelog/the-skills-sh-api-is-now-available) `#8`
- Cursor 更新 Design Mode 支持可视化修改 UI [↗](https://cursor.com/blog/browser-visual-editor) `#9`
- 阿里巴巴推出 Open Code Review 混合架构代码审查工具 [↗](https://alibaba.github.io/open-code-review/) `#10`
- Google 推出开源工具 Google Colab CLI [↗](https://developers.googleblog.com/introducing-the-google-colab-cli/) `#11`
- Google 推出面向企业的 Agentic RAG 框架 [↗](https://research.google/blog/unlocking-dependable-responses-with-gemini-enterprise-agent-platforms-agentic-rag/) `#12`
### 产品应用
- Claude 限时提供 Claude Cowork 翻倍使用量限额，面向所有付费用户 [↗](http://claude.com/cowork) `#13`
- Kimi Work 桌面端 Windows 版已可用 [↗](https://www.kimi.com/zh-cn/products/kimi-work) `#14`
- 抖音副总裁回应豆包误判蘑菇传闻 [↗](https://weibo.com/7965906915/R2HT50wwm) `#15`
### 技术与洞察
- 腾讯混元与人大团队开源 PlanningBench 规划基准 [↗](https://github.com/Tencent-Hunyuan/PlanningBench) `#16`
- 通义实验室开源通用智能体评测基准 PawBench [↗](https://agentscope-ai.github.io/PawBench) `#17`
- Anthropic 发表白皮书：Claude Opus 4.7 在 NMR 光谱预测中比肩专业软件 [↗](https://www.anthropic.com/research/making-claude-a-chemist) `#18`
### 行业动态
- Google将向SpaceX支付每月9.2亿美元用于算力租赁 [↗](https://www.sec.gov/Archives/edgar/data/1181412/000162828026041150/spacexagreementfwp.htm) `#19`
- 多家巨头 AI 预算超支，行业转向成本管控 [↗](https://techcrunch.com/2026/06/05/the-token-bill-comes-due-inside-the-industry-scramble-to-manage-ais-runaway-costs) `#20`
- 基于阿里千问微调，NBA官方大模型“NBA Chat”上线 [↗](https://mp.weixin.qq.com/s/BAfhxzLLa1m6xQ-cBCaxxw) `#21`
### 前瞻与传闻
- 报道称 Meta 拟在路易斯安那州建 2000 亿美元数据中心并考虑发售新股融资 [↗](https://www.bloomberg.com/news/videos/2026-06-05/the-200-billion-data-center-transforming-louisiana-video) `#22`

---

## [OpenAI 确认系统 Bug 导致部分账户被误封](https://x.com/OpenAI/status/2062927046448431587) `#1`
> **OpenAI** 官方确认，系统 `Bug` 导致部分用户账户被错误暂停，目前已恢复访问，但仍在处理受影响用户的订阅和额度异常，并将发送邮件通知。

**OpenAI** 官方确认，系统出现的一个技术问题导致部分用户账户被错误暂停。

官方现已恢复了相关账户的访问，但仍在核查受影响用户的订阅及额度状态。

此前，社区曾大量反馈遭遇误封，部分用户表示恢复后发现付费订阅状态丢失或变更为免费计划。

此外，官方日志显示同期还存在 `微软个人账号` 无法登录及免费用户报错率升高等异常。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260606/20260606081622_12a1379031.png)

相关链接：
- [https://x.com/OpenAI/status/2062927046448431587](https://x.com/OpenAI/status/2062927046448431587)
- [https://status.openai.com/incidents/01KTBZDS20E3PZ53DH2SCKXN49](https://status.openai.com/incidents/01KTBZDS20E3PZ53DH2SCKXN49)

---

## [OpenAI 发布 Codex 更新：新增设置搜索与状态保存功能](https://x.com/OpenAIDevs/status/2062987643286438337) `#2`
> **OpenAI**为`Codex`应用发布了多项更新。新版新增带分类结果的设置搜索，支持全屏下侧边聊天可见，重启后也会自动恢复提示词草稿以及`工作树`上下文等工作状态。

**OpenAI Developers** 为 `Codex` 应用发布了多项使用体验更新。

官方表示，此次更新新增了带有分类结果的设置搜索功能。

更新支持侧边聊天在全屏模式下保持可见，并优化了通知路由与 `Escape` 键的停止交互。

同时，应用在重启后会恢复提示词草稿、缩放级别以及工作树上下文等更多工作状态。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/dca051de-fe4f-45bb-8664-a045f45a1c2e/7ec83162-5b03-49e8-9cff-8a07e15ced3a/m001.gif)

相关链接：
- [https://x.com/OpenAIDevs/status/2062987643286438337](https://x.com/OpenAIDevs/status/2062987643286438337)

---

## [ChatGPT web端writing blocks新增直接发送邮件功能](https://x.com/ChatGPTapp/status/2062944254591430917) `#3`
> **ChatGPT** 宣布一项web端新功能：现在可以在对话界面的`writing blocks`中直接起草邮件、进行修改，并一键发送，所有操作无需离开当前聊天会话。

近日，`ChatGPT`官方宣布其web平台上的`writing blocks`现已集成邮件发送功能。

用户可以在与`AI`对话时，利用`writing blocks`起草、调整并直接发送电子邮件。

无需跳出`ChatGPT`界面或打开其他邮件客户端。该功能已面向**web用户**开放。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/dca051de-fe4f-45bb-8664-a045f45a1c2e/c0680af2-0b2b-4dfe-86ce-17201f18989d/m001.gif)

相关链接：
- [https://x.com/ChatGPTapp/status/2062944254591430917](https://x.com/ChatGPTapp/status/2062944254591430917)

---

## [Google 发布 Gemma 4 QAT 权重及全新移动端量化格式](https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/) `#4`
> **Google DeepMind**发布`Gemma 4`量化感知训练checkpoints。同时官方引入全新移动端量化格式，利用定向`2-bit`压缩等技术，将`Gemma 4 E2B`模型内存占用降至约**1GB**。相关模型权重已上线**Hugging Face**，支持多种工具链部署。

**Google**官方发布了 **`Gemma 4`** 全系模型及其 **`Drafters`** 的量化感知训练检查点，通过在训练阶段模拟压缩来减少精度损失。

此次发布包含面向消费级 `GPU` 的 `Q4_0`格式和专为移动端定制的新型格式。

官方称新格式结合静态激活与定向 `2-bit`压缩等技术，将 **`Gemma 4 E2B`** 模型的内存需求降至约 **1GB**，若仅部署文本且不含 **`Per-Layer Embeddings`** 则低于 **1GB**。

目前相关权重已在 **Hugging Face** 开放，并支持 `llama.cpp`、`Ollama`、`LiteRT-LM` 及 **`MLX`** 等多种工具链。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/dca051de-fe4f-45bb-8664-a045f45a1c2e/cc7d54ee-d3f3-4595-b6b5-982c0666ced6/m001.png)

相关链接：
- [https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/](https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/)
- [https://huggingface.co/collections/google/gemma-4-qat-q4-0](https://huggingface.co/collections/google/gemma-4-qat-q4-0)

---

## [小红书 rednote-hilab 开源 20 亿参数 dots.tts](https://rednote-hilab.github.io/dots.tts-demo/) `#5`
> 小红书 `rednote-hilab` 开源了 **20** 亿参数的端到端文本转语音模型 `dots.tts`。官方称其在多项基准测试中达开源 `SOTA`。该模型的多版本权重与推理代码已基于 **Apache 2.0** 协议发布。

**小红书 rednote-hilab** 团队正式发布了名为 `dots.tts` 的 **20 亿** 参数全连续、端到端自回归文本转语音系统。

该系统的主干网络由语义编码器、基于 `Qwen2.5-1.5B-Base` 初始化的大语言模型，以及基于 `48 kHz AudioVAE` 的自回归流匹配声学头组成，且在整个处理流程中未使用离散 `token`。

根据官方提供的数据，`dots.tts` 在 `Seed-TTS-Eval` 测试集中取得最佳平均性能，并在 **24** 语言的 `MiniMax` 多语言基准测试中获得最高平均说话人相似度，展现出开源领域最优的表现及较强的声音克隆与情感表达能力。

目前，该项目的预训练、自我纠正对齐以及 `MeanFlow` 蒸馏等多个版本的检查点，连同完整的推理与微调代码，已在 `GitHub` 和 `Hugging Face` 上以 `Apache 2.0` 协议开源，并同步提供了在线体验 `Demo`。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260606/20260606081044_ec129b2a3d.png)

相关链接：
- [https://rednote-hilab.github.io/dots.tts-demo/](https://rednote-hilab.github.io/dots.tts-demo/)
- [https://github.com/rednote-hilab/dots.tts](https://github.com/rednote-hilab/dots.tts)
- [https://huggingface.co/collections/rednote-hilab/dotstts](https://huggingface.co/collections/rednote-hilab/dotstts)
- [https://huggingface.co/spaces/rednote-hilab/dots.tts](https://huggingface.co/spaces/rednote-hilab/dots.tts)

---

## [OpenRouter上线图像模型Riverflow 2.5并提供限时免费调用](https://x.com/OpenRouter/status/2062951474406240687) `#6`
> OpenRouter 上线首个可自定义评分标准的图像模型 `Riverflow 2.5`。用户可控制评分准则引导思维与编辑。该模型在 **6 月 9 日**前免费开放使用。

**OpenRouter** 近日上线了由 **riverflow ai** 开发的 `Riverflow 2.5` 图像模型，这是首个支持用户通过独立评分标准（`Scoring Rubric`）引导模型思维与编辑过程的产品。

该模型允许用户调节低、中、高（`Pro` 版含超高）四档推理努力程度，以实现生成速度与画质的灵活平衡。

目前提供 `Fast` 和 `Pro` 两个版本，支持最高 `4K` 输出及 **10** 张图片输入，并在 **6 月 9 日**前对所有用户免费开放。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260606/20260606085527_bfce1649dd.png)

相关链接：
- [https://x.com/OpenRouter/status/2062951474406240687](https://x.com/OpenRouter/status/2062951474406240687)

---

## Miso Labs 推出 8B 参数文本转语音模型 MisoTTS `#7`
> **Miso Labs** 近期推出了 **8B** 参数的文本转语音模型 `MisoTTS 8B`，该模型采用 `RVQ Transformer` 架构以提升情感表达能力，目前已开源权重但仅支持英文。

**Miso Labs** 近期发布了 `MisoTTS 8B` 语音模型，官方称其能够实现高表现力的情感语音和对话生成。

该模型由 **7.7B 参数**的主干网络和 **300M 参数**的解码器组成。

采用 `RVQ` 架构将音频词汇寻址空间扩展至约 **2048** 的 **32** 次方，支持根据文本和音频上下文进行语音合成。

`MisoTTS 8B` 目前已在 **Hugging Face** 上以修改后的 `MIT` 许可证开源权重，但仅支持英文。

且生成的音频默认通过 `SilentCipher` 添加水印。

---

## [Vercel 上线 skills.sh API 支持查询超 60 万开源技能](https://vercel.com/changelog/the-skills-sh-api-is-now-available) `#8`
> **Vercel** 宣布 `skills.sh` **API** 现已上线。开发者使用 **Vercel** `OIDC token` 认证，即可查询开源生态中超 **60 万** 个 `skills` 的详情与安全审计。

Vercel 宣布其 `skills.sh` API 现已正式可用。

该服务允许开发者搜索并获取开源生态系统中超过 **60 万个** `skills` 的详细信息与安全审计结果。

开发者需使用自动轮换的短期 `Vercel OIDC token` 进行身份验证。

系统对每个团队和项目设置了每分钟 **600 次** 请求的速率限制。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/dca051de-fe4f-45bb-8664-a045f45a1c2e/2b1beeb5-e768-401f-980f-c83cf4ccb0d1/m001.png)

相关链接：
- [https://vercel.com/changelog/the-skills-sh-api-is-now-available](https://vercel.com/changelog/the-skills-sh-api-is-now-available)
- [https://skills.sh/](https://skills.sh/)

---

## [Cursor 更新 Design Mode 支持可视化修改 UI](https://cursor.com/blog/browser-visual-editor) `#9`
> **Cursor** 更新 **Design Mode**，允许开发者在内置浏览器中通过点击、绘制或语音提示修改 UI，并交由 `Agent` 直接编辑底层源代码。

**Cursor** 正式推出 `Design Mode` 更新，将可视化交互与底层代码编辑相结合。

开发者可在 **Cursor browser** 中直接对运行中的应用进行点选、多选、圈注或使用语音描述修改意图。

系统会捕获相关的元素标识和视觉截图作为上下文，由 `Agent` 完成源代码修改。

该功能允许用户在 `Agent` 处理首个任务时连续发送后续指令，应用可实时热重载。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/dca051de-fe4f-45bb-8664-a045f45a1c2e/f7a0a62d-72c9-4bf9-99bd-1d4fc866cafe/m001.png)

相关链接：
- [https://cursor.com/blog/browser-visual-editor](https://cursor.com/blog/browser-visual-editor)

---

## [阿里巴巴推出 Open Code Review 混合架构代码审查工具](https://alibaba.github.io/open-code-review/) `#10`
> **阿里巴巴**近期在 **GitHub** 开源了其内部 AI 代码审查工具 `Open Code Review`，采用确定性工程管线与 `LLM Agent` 混合架构，兼容 `OpenAI` 与 `Anthropic` **API**。

**阿里巴巴**近期在 **GitHub** 开源 `Open Code Review`，这是一款 **AI** 驱动的代码审查 **CLI** 工具，源自该公司过去两年内部服务数万名开发者、识别数百万代码缺陷的官方审查助手。

该工具采用确定性工程管线与 `LLM Agent` 混合架构，能读取 `Git diff`、完整文件内容及仓库上下文，生成行级精度的结构化审查评论，并内置针对 `NPE`、线程安全、`XSS`、`SQL` 注入等问题的微调规则集。

用户通过 `npm` 安装后配置 `OpenAI` 或 `Anthropic` 兼容的模型端点即可使用，支持与 `Claude Code` 等编程 `Agent` 集成以及 `GitHub Actions`、`GitLab CI` 等 `CI/CD` 流程。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260605/20260605173051_839cdf2ec3.png)

相关链接：
- [https://alibaba.github.io/open-code-review/](https://alibaba.github.io/open-code-review/)
- [https://github.com/alibaba/open-code-review](https://github.com/alibaba/open-code-review)

---

## [Google 推出开源工具 Google Colab CLI](https://developers.googleblog.com/introducing-the-google-colab-cli/) `#11`
> **Google** 宣布推出轻量级开源工具 **Google Colab CLI**，打通本地终端与远程 `Colab` 运行时，支持开发者及 AI Agent 直接调用 `GPU`/`TPU` 算力执行 `ML` 流水线。

**Google** 宣布推出轻量级命令行工具 `Google Colab CLI`，旨在将本地终端与远程 **Colab** 运行时环境无缝连接。

该工具允许开发者及具备终端访问权限的 `AI Agent` 零摩擦地申请并使用高算力 `GPU` 或 `TPU`，通过 `colab exec` 等命令直接在远端运行本地 `Python` 脚本及复杂的机器学习流水线。

为方便 `AI Agent` 集成，`CLI` 包含了预打包的 **Colab** 技能文件。目前 **Google Colab CLI** 已在 `GitHub` 仓库开源。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/dca051de-fe4f-45bb-8664-a045f45a1c2e/151034b3-b3cb-430c-b6cb-94a3daafe568/m001.gif)

相关链接：
- [https://developers.googleblog.com/introducing-the-google-colab-cli/](https://developers.googleblog.com/introducing-the-google-colab-cli/)
- [https://github.com/googlecolab/google-colab-cli/](https://github.com/googlecolab/google-colab-cli/)

---

## [Google 推出面向企业的 Agentic RAG 框架](https://research.google/blog/unlocking-dependable-responses-with-gemini-enterprise-agent-platforms-agentic-rag/) `#12`
> **Google Research** 与 **Google Cloud** 联合推出全新的 Agentic RAG 框架，该系统采用多智能体架构，通过核心的 `Sufficient Context Agent` 评估上下文完整性并触发迭代检索，官方称其比标准 `RAG` 准确率最高提升 **34%**。

**Google Research** 与 **Google Cloud** 合作推出了全新的 Agentic RAG 框架。

针对传统单步 `RAG` 在处理跨数据源、多跳复杂查询时易出现信息遗漏的问题，该框架引入了包含 `Orchestrator`、`Planner Agent`、`Query Rewriter`、`Search Fanout Agent` 和 `Synthesis Agent` 的多智能体工作流。

其核心创新在于 `Sufficient Context Agent`，该智能体会审查已检索的文本块和中间草稿。

若发现信息缺失则会生成具体反馈并触发新一轮检索，直到收集到足够的上下文才生成最终回答。

根据官方在 `FramesQA` 数据集上的测试数据，该框架相比标准 `RAG` 准确率最高提升 **34%**。

在跨语料库检索任务中准确率达到 **90.1%**，且检索延迟与单次检索相比平均仅增加约 **3%**。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/dca051de-fe4f-45bb-8664-a045f45a1c2e/661f6e43-a776-4cd7-8fc0-b4f87e00e86b/m001.gif)

相关链接：
- [https://research.google/blog/unlocking-dependable-responses-with-gemini-enterprise-agent-platforms-agentic-rag/](https://research.google/blog/unlocking-dependable-responses-with-gemini-enterprise-agent-platforms-agentic-rag/)
- [https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/cross-corpus-retrieval](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/cross-corpus-retrieval)

---

## [Claude 限时提供 Claude Cowork 翻倍使用量限额，面向所有付费用户](http://claude.com/cowork) `#13`
> **Claude** 官方宣布已将 `Claude Cowork` 的使用限额翻倍，即日起面向所有付费计划生效，持续至 **7 月 5 日**。

**Claude** 官方宣布将 **Claude Cowork** 的使用量限额翻倍，该调整即日起对所有付费计划生效，持续至 **7 月 5 日**。

据 **Anthropic** 工程师 **Boris Cherny** 补充说明，此次翻倍具体适用于 `5 小时速率`限额。

官方建议用户利用这一窗口将更大、更复杂的项目委托给 **Claude** 处理，例如跨多账户的调研、周期性报告生成、收件箱分类与回复草拟等工作。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260606/20260606083323_84ff0cb910.png)

相关链接：
- [http://claude.com/cowork](http://claude.com/cowork)
- [https://x.com/claudeai/status/2063018337567670285](https://x.com/claudeai/status/2063018337567670285)

---

## [Kimi Work 桌面端 Windows 版已可用](https://www.kimi.com/zh-cn/products/kimi-work) `#14`
> **Kimi Work** 的 **Windows** 版已正式上线。该产品内置 `300` 个 **Agent**，可全天候自动化执行任务。

**Kimi** 推出的桌面端 AI 智能体工作台 `Kimi Work` 其 `Windows` 版目前已可用。

该产品定位为知识工作者提供办公辅助，全面覆盖**金融投研、科研学术与白领办公**场景。

`Kimi Work` 内置 **300** 个 `Agent`，能够全天候替用户完成整理文件、操作网页、自动化任务以及生成精美的 `Office` 产物等操作。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260605/20260605172858_ea05412374.png)

相关链接：
- [https://www.kimi.com/zh-cn/products/kimi-work](https://www.kimi.com/zh-cn/products/kimi-work)

---

## [抖音副总裁回应豆包误判蘑菇传闻](https://weibo.com/7965906915/R2HT50wwm) `#15`
> **抖音**副总裁**李亮**回应“**豆包**误判蘑菇致中毒”传闻称，`豆包`识别时已提示**剧毒混淆风险**并建议**勿食**，强调`AI`**仅供参考**，涉及**安全**务必多方求证。

**6月5日**，**抖音集团副总裁李亮**发文回应“`豆包`误判蘑菇导致用户中毒”传闻，称`豆包`团队已联系当事用户进行核实。

根据反馈，`豆包`将用户拍摄的蘑菇识别为“**鸡腿菇**”的同时，已在回复中明确提示该蘑菇极易与剧毒品种混淆，强烈建议不要食用野外采摘的品种，并指出仅凭图片无法完全排除有毒相似种的可能。

**李亮**表示`AI`目前仍在发展中，涉及人身安全的问题应多方求证，`AI`回答仅供参考。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/20260605/20260605173203_7bdad56e7b.png)

相关链接：
- [https://weibo.com/7965906915/R2HT50wwm](https://weibo.com/7965906915/R2HT50wwm)

---

## [腾讯混元与人大团队开源 PlanningBench 规划基准](https://github.com/Tencent-Hunyuan/PlanningBench) `#16`
> **腾讯混元**与**人大**团队开源 `PlanningBench` 基准，用于大模型复杂规划任务的评估与训练，现已发布 **467** 个合成评估实例。

**腾讯混元**与**中国人民大学**团队联合开源了 `PlanningBench`，这是一个用于评估和训练大语言模型处理复杂规划任务的合成基准与数据构建框架。

该框架将现实规划场景抽象为包含**排班调度**、**路线规划**等 **6** 大家族和超过 **30** 种具体任务的分类体系，并通过约束驱动的流水线生成带有验证清单的规划问题。

研究团队在对前沿模型进行测试后发现，当前大模型在耦合约束条件下生成完整解决方案的能力依然有限，但基于该数据的强化学习能显著提升模型在未知任务上的表现。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/dca051de-fe4f-45bb-8664-a045f45a1c2e/09ac36f4-66d3-4480-beea-76a7b5442e78/m001.png)

相关链接：
- [https://github.com/Tencent-Hunyuan/PlanningBench](https://github.com/Tencent-Hunyuan/PlanningBench)
- [https://arxiv.org/abs/2605.20873](https://arxiv.org/abs/2605.20873)
- [https://huggingface.co/datasets/tencent/PlanningBench](https://huggingface.co/datasets/tencent/PlanningBench)

---

## [通义实验室开源通用智能体评测基准 PawBench](https://agentscope-ai.github.io/PawBench) `#17`
> **通义实验室**推出并开源评测基准 `PawBench`。该基准面向通用智能体，通过 **150** 道任务评测底座模型与运行框架的联合效果，帮助开发者精准定位问题。

**通义实验室**推出了面向个人助理与通用智能体场景的评测基准 `PawBench`，并已全面开源。

该基准将底座模型与运行框架纳入同一评测体系，构建了包含 **150** 道任务和 **4050** 个测试单元的评测集。

通过混合自动评分器与 `LLM-as-judge`，`PawBench` 不仅能评出最佳组合，还发现运行框架的校验机制与默认工具可用性对模型最终表现有显著影响。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/dca051de-fe4f-45bb-8664-a045f45a1c2e/c81a12a7-d6e6-47b3-a1b1-b59b9fa76018/m001.png)

相关链接：
- [https://agentscope-ai.github.io/PawBench](https://agentscope-ai.github.io/PawBench)
- [https://github.com/agentscope-ai/PawBench](https://github.com/agentscope-ai/PawBench)
- [https://mp.weixin.qq.com/s/Q1fa3KwT63HBOF2fmWKzlg?poc_token=HDCfImqjPcG4Q1Z2daJQA9HYZbdKEfADwg5czkk8](https://mp.weixin.qq.com/s/Q1fa3KwT63HBOF2fmWKzlg?poc_token=HDCfImqjPcG4Q1Z2daJQA9HYZbdKEfADwg5czkk8)

---

## [Anthropic 发表白皮书：Claude Opus 4.7 在 NMR 光谱预测中比肩专业软件](https://www.anthropic.com/research/making-claude-a-chemist) `#18`
> **Anthropic** 发表白皮书称，未做化学专属微调的 `Claude Opus` **4.7**，在 **NMR** 氢谱前向预测中平均误差与专业软件 `ChemDraw` 和 `MestReNova` 相当或更优，还可从一维谱图反推分子结构。

**Anthropic** 官方博客发布了由该公司化学家 **David Kamber** 撰写的研究文章及配套白皮书。评估了三个 `Claude` 模型（`Opus 4.7`、`Opus 4.6`、`Sonnet 4.6`）与专业 `NMR` 软件 `ChemDraw`、`MestReNova` 的对比表现。

前向预测测试使用 **20** 个来自 `ChemRxiv` 预印本的化合物。结果显示 `Opus 4.7` 在氢谱上最准确（平均误差 **±0.079 ppm**）。碳谱上与 `MestReNova` 基本持平（分别为 **±1.37 ppm** 和 **±1.48 ppm**）。且峰型裂分匹配率和亚峰间距预测均优于两款专业工具。

在 **15** 道反向结构解析题中，`Opus 4.7` 对 **8** 个简单分子全部正确还原。**7** 个复杂分子在有起始原料提示时也多数成功。

官方同时承认评估规模较小。未覆盖 `2D NMR` 和立体化学，模型表现应视为参考性而非精确结论。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/dca051de-fe4f-45bb-8664-a045f45a1c2e/abfcfb99-f2fd-449e-9fd6-63fb50bdc4eb/m001.png)

相关链接：
- [https://www.anthropic.com/research/making-claude-a-chemist](https://www.anthropic.com/research/making-claude-a-chemist)

---

## [Google将向SpaceX支付每月9.2亿美元用于算力租赁](https://www.sec.gov/Archives/edgar/data/1181412/000162828026041150/spacexagreementfwp.htm) `#19`
> 据监管文件披露， **SpaceX** 与 **Google** 签署新的云计算服务协议， **Google** 将支付每月 **9.2 亿美元**，以获取位于 **Memphis** 数据中心约 **11 万** 个 `NVIDIA GPU` 的算力资源。

**SpaceX** 在提交给监管机构的文件中披露，已与 **Google** 签署了一项新的云计算服务协议。

根据协议条款，**Google** 将在 **2026 年 10 月** 至 **2029 年 6 月** 期间，**每月**向 **SpaceX** 支付 **9.2 亿美元**。

作为回报，**Google** 将获得位于 `Memphis` 的 `Colossus` 数据中心内大约 **11 万个** `NVIDIA GPU` 及相关组件的访问权。

该数据中心原由 `SpaceXAI` 建造，目前隶属于 `SpaceX`。

协议包含一项条款，允许双方在 **2026 年 12 月 31 日** 之后提前 **90 天** 通知终止合同。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/dca051de-fe4f-45bb-8664-a045f45a1c2e/74b4393f-479b-452a-8825-dbcb6b90b9f8/m001.png)

相关链接：
- [https://www.sec.gov/Archives/edgar/data/1181412/000162828026041150/spacexagreementfwp.htm](https://www.sec.gov/Archives/edgar/data/1181412/000162828026041150/spacexagreementfwp.htm)

---

## [多家巨头 AI 预算超支，行业转向成本管控](https://techcrunch.com/2026/06/05/the-token-bill-comes-due-inside-the-industry-scramble-to-manage-ais-runaway-costs) `#20`
> 据报道，随着 **AI** 智能体导致 **Token** 消耗剧增，多家科技企业因预算失控开始限制内部 `AI` 支出。**Linux Foundation** 宣布成立 `Tokenomics Foundation` 旨在制定计费标准。

据 **TechCrunch** 报道，随着企业广泛采用 `AI` 智能体工具，尽管单价下降但总消耗量激增，导致行业重心从追求发展速度转向设置成本护栏。

包括 **Uber** 耗尽全年预算、**Microsoft** 收回开发者许可以及个别公司面临巨额账单在内的事件，正迫使企业紧急控制支出。

为解决标准缺失问题，**Linux Foundation** 宣布成立 **Tokenomics Foundation** 以制定 `Token` 计费标准和经济指标，并计划于 **7** 月正式推出。

与此同时，市场正快速催生出成本监控、智能模型路由等优化方案，**Datadog**、**Ramp** 等厂商及多家初创企业已布局相关工具。

相关链接：
- [https://techcrunch.com/2026/06/05/the-token-bill-comes-due-inside-the-industry-scramble-to-manage-ais-runaway-costs](https://techcrunch.com/2026/06/05/the-token-bill-comes-due-inside-the-industry-scramble-to-manage-ais-runaway-costs)
- [https://www.datadoghq.com/blog/manage-ai-cost-and-performance-with-datadog/](https://www.datadoghq.com/blog/manage-ai-cost-and-performance-with-datadog/)
- [https://newrelic.com/blog/apm/ai-monitoring](https://newrelic.com/blog/apm/ai-monitoring)

---

## [基于阿里千问微调，NBA官方大模型“NBA Chat”上线](https://mp.weixin.qq.com/s/BAfhxzLLa1m6xQ-cBCaxxw) `#21`
> NBA中国与**阿里**联合打造的首个官方大模型 `NBA Chat` 正式上线，球迷现可在官方APP内体验基于**千问**大模型的智能篮球问答服务。

**NBA中国**与**阿里巴巴**联合打造的首个官方大模型 `NBA Chat` 正式上线。

球迷可在“**NBA中国**”APP中体验该功能。

该模型基于`阿里千问`大模型，并融合了**NBA**篮球历史数据与球员深度分析等数字资产进行微调。

目前可提供战术拆解与赛事数据等智能问答服务。

后续计划升级`Agent`能力。

![](https://cdn.jsdelivr.net/gh/imjuya/picx-images-hosting@master/imagehub/aidaily/dca051de-fe4f-45bb-8664-a045f45a1c2e/2257a0b7-8103-49fc-949c-ce38c3f82f04/m001.png)

相关链接：
- [https://mp.weixin.qq.com/s/BAfhxzLLa1m6xQ-cBCaxxw](https://mp.weixin.qq.com/s/BAfhxzLLa1m6xQ-cBCaxxw)

---

## [报道称 Meta 拟在路易斯安那州建 2000 亿美元数据中心并考虑发售新股融资](https://www.bloomberg.com/news/videos/2026-06-05/the-200-billion-data-center-transforming-louisiana-video) `#22`
> 媒体报道称 **Meta** 将在**路易斯安那州**建设投资额达 **2000 亿美元**的数据中心。另有消息称，为维持 `AI` 支出，该公司正考虑发售数百亿美元新股。

媒体报道指出，**Meta** 正在**路易斯安那州**推进一项价值 **2000 亿美元**的大型数据中心建设项目，这一合作经历了大量谈判与保密运作。

此外，据社交平台账号引述**英国《金融时报》** 的消息称，为了持续增加人工智能领域的资本支出，**Meta** 正在考虑发售价值**数百亿美元**的新股。

这一潜在的融资动向发生在 `Google` 进行大规模股权融资之后，相关讨论目前仅为外界传闻。

相关链接：
- [https://www.bloomberg.com/news/videos/2026-06-05/the-200-billion-data-center-transforming-louisiana-video](https://www.bloomberg.com/news/videos/2026-06-05/the-200-billion-data-center-transforming-louisiana-video)
- [https://x.com/gurgavin/status/2062961764736655515](https://x.com/gurgavin/status/2062961764736655515)

---

**提示**：内容由AI辅助创作，可能存在**幻觉**和**错误**。