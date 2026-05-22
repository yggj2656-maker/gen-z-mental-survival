# 完整工作流程 — Always Online, Never Here

同步 GitHub 后即可继续的任何操作。

---

## 1. 同步 GitHub → 继续工作

```bash
cd c:/Users/a/Desktop/书
git pull origin master
```

---

## 2. 生成 KDP 封面

### 方式 A：GPT / DALL-E（推荐）

1. 把以下提示词贴到 ChatGPT：
```
A professional book cover design for a 6x9 inch paperback. Near-black deep navy background. In the center, a single dim amber glowing smartphone-shaped rectangle floats in darkness, its light soft and melancholic — like the only source of warmth in a void. The glow diffuses outward into the dark. Cinematic volumetric lighting. Editorial, minimalist, atmospheric. No text, no letters, no typography, no words at all. No human figures or faces. Clean composition. Premium publishing quality. The mood is quiet, introspective, late-night, slightly unsettling but beautiful. Leave the top 40% and bottom 15% as empty dark space for text placement.
```

2. ChatGPT 生成图片后保存到 `c:/Users/a/Desktop/书/`

3. 修改 `scripts/add_typography.py` 中的 `INPUT` 路径为新的文件名

4. 运行：
```bash
python scripts/add_typography.py
```

5. 输出：`output/cover_final.jpg`（1800×2700px @300DPI，KDP就绪）

### 方式 B：Midjourney / ComfyUI

用 `covers/commercial/prompt.txt` 作为正向提示词，`covers/commercial/negative_prompt.txt` 作为负向。出图后用同上的 `add_typography.py` 叠文字。

### 方式 C：本地 SD（仅当 GPU 内存 >= 12GB）

不推荐。之前 RTX 5060 8GB 出现 OOM（exit 137）。如需重试，参考 `covers/commercial/` 下的设计规格。

---

## 3. 生成 EPUB

所有章节在 `drafts/chapter_01.md` ~ `drafts/chapter_08.md`。

```bash
cd "c:/Users/a/Desktop/书"

# Pandoc 路径：
PANDOC="/c/Users/a/AppData/Local/Microsoft/WinGet/Packages/JohnMacFarlane.Pandoc_Microsoft.Winget.Source_8wekyb3d8bbwe/pandoc-3.9.0.2/pandoc.exe"

# 生成 EPUB：
"$PANDOC" \
  drafts/front_matter.md \
  drafts/chapter_01.md \
  drafts/chapter_02.md \
  drafts/chapter_03.md \
  drafts/chapter_04.md \
  drafts/chapter_05.md \
  drafts/chapter_06.md \
  drafts/chapter_07.md \
  drafts/chapter_08.md \
  -o "output/Always_Online_Never_Here.epub" \
  --metadata-file=kdp/epub_metadata.yaml \
  --toc --toc-depth=1
```

---

## 4. KDP 上传清单

登录 [kdp.amazon.com](https://kdp.amazon.com)。

### 基本信息
| 项目 | 内容 |
|------|------|
| 书名 | Always Online, Never Here |
| 副标题 | A Philosophy of Attention, Presence, and Survival for the Exhausted Generation |
| 作者 | Moon |
| 语言 | English |

### 分类（2个）
1. Philosophy > Existentialism
2. Self-Help > Personal Transformation

### 关键词（7个）
```
gen z mental health philosophy
digital loneliness young adults
attention focus recovery book
existential psychology modern life
social media detox gen z
dopamine burnout self help
meaning of life for students
```

### 定价
- $3.99（70% 版权费区间）
- 上线前 5 天 $0.99 促销

### 上传文件
| 文件 | 路径 |
|------|------|
| 电子书 | `output/Always_Online_Never_Here.epub` |
| 封面 | `output/cover_final.jpg` |

### 勾选项
- [x] AI 生成内容声明（在 `drafts/front_matter.md` 中已写）
- [x] 版权归属确认

---

## 5. 同步到 GitHub

```bash
cd "c:/Users/a/Desktop/书"
git add -A
git commit -m "描述你做了什么"
git push origin master
```

---

## 项目文件结构

```
书/
├── drafts/              ← 8章 + front_matter
├── output/              ← EPUB + 封面
├── kdp/                 ← 元数据、关键词、描述、上传清单
├── covers/              ← 三种风格的 AI 提示词 + 设计规格
├── scripts/             ← add_typography.py（封面叠文字）
├── research/            ← 市场调研、受众分析
├── outlines/            ← 章节大纲、书名候选
├── prompts/             ← DeepSeek/Claude 提示词模板
├── WORKFLOW.md          ← 本文件
└── README.md            ← 写作风格规则
```

---

## 环境依赖

```bash
# Python 库（仅封面叠文字需要）
pip install Pillow

# Pandoc（EPUB 生成）
winget install --id JohnMacFarlane.Pandoc
# 安装路径需确认，见上面生成 EPUB 部分

# GitHub（同步）
winget install --id GitHub.cli
# 代理已配置：http://127.0.0.1:7897
```
