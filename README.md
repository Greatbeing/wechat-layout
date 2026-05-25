# wechat-layout

> 微信公众号图文排版设计器 — AI Agent Skill

[English](#english) | [中文](#中文)

---

## 中文

### 简介

`wechat-layout` 是一个通用的 AI Agent Skill，能够自动生成精美的微信公众号图文排版。提供 **10 种预设视觉风格**，输出使用**内联 CSS** 的 HTML，可直接复制粘贴到微信公众号编辑器。

适用于任何支持 Skill/Plugin 机制的 AI Agent 平台（如 SOLO、Coze、GPTs、Dify 等）。

### 10 种预设风格

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

### 包含的组件模块

每个风格包含 12+ 个完整组件：头图 Banner、导语、一级/二级标题、正文段落、引用块、多图排版（双图/三图/四宫格）、时间轴、Q&A 问答、数据卡片、作者卡片、底部引导等。

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

### 示例

查看 `examples/` 目录获取完整的排版示例输出。

### 技术特点

- 所有样式使用**内联 CSS**，兼容微信公众号编辑器
- 布局采用 `<table>` + `<section>`，确保最大兼容性
- 基于微信编辑器实际兼容性测试（2025-2026）
- 设计宽度 677px，自动适配移动端

### 许可证

[MIT License](LICENSE)

---

## English

### Overview

`wechat-layout` is a universal AI Agent Skill that automatically generates beautifully designed WeChat public account article layouts. It offers **10 preset visual styles** and outputs **inline-CSS HTML** that can be directly pasted into the WeChat editor.

Compatible with any AI Agent platform that supports Skill/Plugin mechanisms (SOLO, Coze, GPTs, Dify, etc.).

### 10 Preset Styles

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

### Component Modules

Each style includes 12+ complete components: Header Banner, Opening Quote, Headings (H1/H2), Body Text, Quote Block, Multi-Image Layouts (2-col/3-col/4-grid), Timeline, Q&A, Data Cards, Author Card, Footer CTA, and more.

### Installation

Import `skill/SKILL.md` into your AI Agent platform:

| Platform | How to Import |
|----------|--------------|
| **SOLO** | Place in `.trae/skills/wechat-layout/SKILL.md` |
| **Coze** | Create a Plugin, paste SKILL.md content into Prompt |
| **GPTs** | Paste SKILL.md content into Instructions |
| **Dify** | Create a Tool, use SKILL.md as Prompt template |
| **Others** | Use SKILL.md as part of your System Prompt |

### Usage

Type any of these keywords in your AI Agent to trigger the Skill:

> WeChat article layout, 公众号排版, WeChat post template, 排版设计, article template …

### Examples

See the `examples/` directory for full layout sample outputs.

### Technical Highlights

- All styles use **inline CSS** for maximum WeChat editor compatibility
- Layout uses `<table>` + `<section>` for reliable rendering
- Based on actual WeChat editor compatibility testing (2025-2026)
- Design width: 677px, auto-adapts to mobile

### License

[MIT License](LICENSE)
