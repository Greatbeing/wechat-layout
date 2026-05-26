# wechat-layout

> 微信公众号图文排版设计器 — AI Agent Skill

[🎨 在线预览](https://greatbeing.github.io/wechat-layout/) · [English](#english) | [中文](#中文)

---

## 中文

### 简介

`wechat-layout` 是一个通用的 AI Agent Skill，能够自动生成精美的微信公众号图文排版。提供 **11 种预设视觉风格**，支持**自动提取微信公众号风格**，输出使用**内联 CSS** 的 HTML，可直接复制粘贴到微信公众号编辑器。

适用于任何支持 Skill/Plugin 机制的 AI Agent 平台（如 SOLO、Coze、GPTs、Dify 等）。

### 核心功能

- 🎨 **11 种预设风格** — 覆盖商务、文艺、创意、高端、知识等多种场景
- 🤖 **风格自动提取** — 发送任意微信公众号文章 URL，自动提取排版风格并生成模板
- 📝 **Markdown 转 HTML** — 输入 Markdown，自动套用风格转微信公众号兼容 HTML
- ✅ **100% 微信兼容** — 所有输出严格遵守微信 CSS 限制，确保正常显示

### 11 种预设风格

| # | 风格 | 适用场景 |
|---|------|---------|
| 1 | 极简商务 | 企业号、职场、分析报告 |
| 2 | 清新文艺 | 生活方式、阅读、慢生活 |
| 3 | 活力创意 | 年轻品牌、创意内容 |
| 4 | 高端质感 | 奢侈品、高端品牌 |
| 5 | 复古优雅 | 怀旧、文化、历史 |
| 6 | 科技未来 | 科技、AI、互联网 |
| 7 | 温柔治愈 | 情感、心理、治愈 |
| 8 | 杂志编辑 | 时尚、生活方式 |
| 9 | 自然生态 | 环保、户外、健康 |
| 10 | 甜美少女 | 美妆、穿搭、少女 |
| 11 | 高端知识 | 知识付费、人物图谱 |

### 使用方式

#### 1. Markdown 转 HTML

```python
from scripts.format_article import format_article

# 基本用法
html_output = format_article(markdown_text, "清新文艺")

# 列出所有可用风格
from scripts.format_article import list_styles
list_styles()
```

#### 2. 风格自动提取

```python
from scripts.extract_style import extract_style_from_url

# 从 URL 提取风格
config = extract_style_from_url("https://mp.weixin.qq.com/s/xxxxx")

# 保存到模板库
from scripts.extract_style import add_style_to_library
add_style_to_library("我的风格", config)
```

#### 3. 命令行使用

```bash
# 列出所有可用风格
python scripts/format_article.py --list

# 转换文件
python scripts/format_article.py --input article.md --output article.html --style 高端知识

# 提取文章风格
python scripts/extract_style.py --url "https://mp.weixin.qq.com/s/xxxxx" --save
```

### 安装

将 `skill/SKILL.md` 的内容导入到你的 AI Agent 平台：

| 平台 | 导入方式 |
|------|---------|
| **SOLO** | 放入 `.trae/skills/wechat-layout/SKILL.md` |
| **Coze** | 创建 Plugin，将 SKILL.md 内容填入 Prompt |
| **GPTs** | 将 SKILL.md 内容粘贴到 Instructions |
| **Dify** | 创建工具，将 SKILL.md 作为 Prompt 模板 |
| **其他** | 将 SKILL.md 作为 System Prompt 的一部分 |

### 使用

在 AI Agent 中输入以下任意关键词即可触发：

> 微信公众号排版、公众号排版、公众号美化、排版设计、文章模板、微信推文、推文排版、公众号图文、头图设计 …

### 技术特点

- 所有样式使用**内联 CSS**，兼容微信公众号编辑器
- 布局采用 `<section>` + `<table>`，确保最大兼容性
- **100% 微信 CSS 兼容** — 无 flex/grid/position/transform
- 基于微信编辑器实际兼容性测试（2025-2026）
- 设计宽度 677px，自动适配移动端
- **支持添加自定义风格** — 只需修改 `styles/style_configs.py`

### 许可证

[MIT License](LICENSE)

---

## English

### Overview

`wechat-layout` is a universal AI Agent Skill that automatically generates beautifully designed WeChat public account article layouts. It offers **11 preset visual styles** with **automatic style extraction** from any WeChat article URL, and outputs **inline-CSS HTML** that can be directly pasted into the WeChat editor.

Compatible with any AI Agent platform that supports Skill/Plugin mechanisms (SOLO, Coze, GPTs, Dify, etc.).

### Core Features

- 🎨 **11 Preset Styles** — Business, literary, creative, premium, knowledge, and more
- 🤖 **Auto Style Extraction** — Send any WeChat article URL, automatically extract and generate layout template
- 📝 **Markdown to HTML** — Input Markdown, automatically apply style and convert to WeChat-compatible HTML
- ✅ **100% WeChat Compatible** — All output strictly follows WeChat CSS restrictions

### 11 Preset Styles

| # | Style | Best For |
|---|-------|----------|
| 1 | Minimalist Business | Corporate, workplace, analysis |
| 2 | Fresh Literary | Lifestyle, reading, slow living |
| 3 | Vibrant Creative | Youth brands, creative content |
| 4 | Premium Luxury | Luxury brands, premium content |
| 5 | Vintage Elegant | Nostalgia, culture, history |
| 6 | Tech Future | Tech, AI, internet, startups |
| 7 | Warm Healing | Emotional, psychology, wellness |
| 8 | Magazine Editorial | Fashion, lifestyle, editorial |
| 9 | Nature Eco | Environment, outdoors, health |
| 10 | Sweet Girly | Beauty, fashion, girly content |
| 11 | Premium Knowledge | Knowledge payment, person profiles |

### Usage

#### 1. Markdown to HTML

```python
from scripts.format_article import format_article

# Basic usage
html_output = format_article(markdown_text, "Fresh Literary")

# List all available styles
from scripts.format_article import list_styles
list_styles()
```

#### 2. Style Auto Extraction

```python
from scripts.extract_style import extract_style_from_url

# Extract style from URL
config = extract_style_from_url("https://mp.weixin.qq.com/s/xxxxx")

# Save to template library
from scripts.extract_style import add_style_to_library
add_style_to_library("My Style", config)
```

#### 3. CLI Usage

```bash
# List all styles
python scripts/format_article.py --list

# Convert file
python scripts/format_article.py --input article.md --output article.html --style "Premium Knowledge"

# Extract article style
python scripts/extract_style.py --url "https://mp.weixin.qq.com/s/xxxxx" --save
```

### Installation

Import `skill/SKILL.md` into your AI Agent platform:

| Platform | How to Import |
|----------|--------------|
| **SOLO** | Place in `.trae/skills/wechat-layout/SKILL.md` |
| **Coze** | Create a Plugin, paste SKILL.md content into Prompt |
| **GPTs** | Paste SKILL.md content into Instructions |
| **Dify** | Create a Tool, use SKILL.md as Prompt template |
| **Others** | Use SKILL.md as part of your System Prompt |

### Technical Highlights

- All styles use **inline CSS** for maximum WeChat editor compatibility
- Layout uses `<section>` + `<table>` for reliable rendering
- **100% WeChat CSS Compatible** — No flex/grid/position/transform
- Based on actual WeChat editor compatibility testing (2025-2026)
- Design width: 677px, auto-adapts to mobile
- **Customizable Styles** — Just modify `styles/style_configs.py` to add new styles

### License

[MIT License](LICENSE)
