---
name: "wechat-layout"
description: "微信公众号图文排版设计器，提供10种预设风格，生成可直接粘贴到公众号编辑器的内联CSS HTML。/ WeChat article layout designer with 10 preset styles, outputs inline-CSS HTML pasteable into WeChat editor."
---

# 微信公众号排版设计器

设计精美的微信公众号图文排版，提供 10 种预设视觉风格。所有输出使用**内联 CSS**，可直接复制粘贴到微信公众号编辑器。

## 何时调用 / When to Invoke

当用户提到以下任一关键词或意图时，立即调用本技能：

**中文触发词：**
微信公众号排版、公众号排版、公众号美化、排版设计、文章模板、微信推文、推文排版、公众号图文、微信图文排版、公众号文章样式、公众号排版设计、公众号模板、头图设计、图文排版、微信文章排版、推文模板、公众号首图、微信排版工具、公众号排版组件

**English triggers:**
- User asks to design/create WeChat public account article layouts
- User asks for WeChat post templates or formatting
- User wants to create styled HTML content for WeChat articles

## 工作流程

### Step 1: 收集需求

向用户确认（或从上下文推断）以下信息：

1. **风格偏好** — 使用哪些视觉风格（见风格目录）
2. **内容主题** — 文章主题是什么（商务、生活、科技等）
3. **模块范围** — 需要哪些组件模块（见模块目录）
4. **输出模式** — 完整组件库（含导航切换）或单风格输出

若用户未指定，使用 `AskUserQuestion` 工具询问。

### Step 2: 生成 HTML 文件

根据输出模式选择：

**模式 A：完整组件库**（默认）
- 包含导航栏（切换风格）+ 所有选定风格的完整预览
- 每个风格带"复制全部代码"按钮
- JavaScript 实现导航切换和剪贴板复制

**模式 B：单风格输出**
- 仅生成用户选定的一套风格
- 无导航栏，直接输出纯净的内联样式 HTML
- 更轻量，适合直接粘贴使用

将文件保存到用户的工作区文件夹。

### Step 3: 验证

- 在浏览器中打开 HTML 文件验证视觉效果
- 检查导航切换和复制功能是否正常（模式 A）
- 确认所有样式均为内联写法

## 风格目录

| # | 风格名称 | 配色方案 | 适用场景 |
|---|---------|---------|---------|
| 1 | 极简商务 | 深蓝 `#1a1a2e` + 红色点缀 `#e94560` | 企业号、职场、分析报告 |
| 2 | 清新文艺 | 绿色 `#81c784` + `#4caf50`，楷体标题 | 生活方式、阅读、慢生活 |
| 3 | 活力创意 | 红橙黄渐变 `#ff6b6b` → `#feca57` → `#48dbfb` | 年轻品牌、创意内容 |
| 4 | 高端质感 | 深色 `#2c3e50` + 金色 `#d4af37` | 奢侈品、高端品牌 |
| 5 | 复古优雅 | 暖棕 `#8b4513` + `#d2691e`，怀旧色调 | 怀旧、文化、历史 |
| 6 | 科技未来 | 深紫 `#0f0c29` + 青色 `#00d4ff`，等宽字体 | 科技、AI、互联网 |
| 7 | 温柔治愈 | 暖黄 `#fdcb6e` + 珊瑚色 `#e17055` | 情感、心理、治愈 |
| 8 | 杂志编辑 | 黑白 `#000` + 白，粗体排版 | 时尚、生活方式 |
| 9 | 自然生态 | 青色 `#134e5e` + 绿色 `#71b280` | 环保、户外、健康 |
| 10 | 甜美少女 | 粉色 `#ff9a9e` + `#fecfef`，圆角 emoji | 美妆、穿搭、少女 |

### 配色系统

```
Style 1 (极简商务):  primary=#1a1a2e, secondary=#16213e, accent=#e94560, text=#333
Style 2 (清新文艺):  primary=#2e7d32, secondary=#81c784, accent=#a5d6a7, text=#444
Style 3 (活力创意):  primary=#ff6b6b, secondary=#feca57, accent=#48dbfb, text=#444
Style 4 (高端质感):  primary=#2c3e50, secondary=#1a1a1a, accent=#d4af37, text=#444
Style 5 (复古优雅):  primary=#5d3a1a, secondary=#8b4513, accent=#d2691e, text=#5d3a1a
Style 6 (科技未来):  primary=#0f0c29, secondary=#302b63, accent=#00d4ff, text=#ccc
Style 7 (温柔治愈):  primary=#d63031, secondary=#e17055, accent=#fdcb6e, text=#555
Style 8 (杂志编辑):  primary=#000000, secondary=#333333, accent=#000, text=#333
Style 9 (自然生态):  primary=#134e5e, secondary=#71b280, accent=#8bc34a, text=#444
Style 10 (甜美少女): primary=#d63031, secondary=#ff6b6b, accent=#ff9a9e, text=#555
```

## 模块目录

### 必选模块

| # | 模块 | 说明 |
|---|------|------|
| 1 | 头图 Banner | 全宽渐变背景 + 标题 + 副标题 + 装饰元素 |
| 2 | 导语 | 开篇引用或摘要，各风格样式不同 |
| 3 | 一级标题 | 主章节标题，带风格化装饰 |
| 4 | 二级标题 | 子章节标题 |
| 5 | 正文段落 | 15px 字号、2.0+ 行高、两端对齐、2em 首行缩进 |
| 6 | 引用块 | 带出处的引用，各风格独特处理 |
| 7 | 多图排版 | 双图 / 三图 / 四宫格，每张图带说明文字 |
| 8 | 时间轴 | 纵向时间线，日期标签 + 描述 |
| 9 | Q&A 问答 | 问答对，Q 和 A 视觉区分明确 |
| 10 | 数据卡片 | 2-3 个关键指标，大数字 + 标签 |
| 11 | 作者卡片 | 头像 + 姓名 + 头衔 + 简介 |
| 12 | 底部引导 | 点赞、留言、分享引导 |

### 可选模块

| # | 模块 | 说明 |
|---|------|------|
| 13 | 延伸阅读 | 相关文章链接列表 |
| 14 | 分割线 | 章节间的视觉分隔 |
| 15 | 高亮提示框 | 重要信息强调（如注意事项、小贴士） |

## 技术规范（重要）

### ⚠️ 微信编辑器兼容性

微信公众号编辑器对 HTML/CSS 有严格限制，以下是经过验证的兼容性规则：

#### ✅ 安全可用

| 属性/特性 | 说明 |
|----------|------|
| `border-radius` | 圆角完全支持 |
| `box-shadow` | 阴影完全支持 |
| `linear-gradient` | 简单渐变基本支持（写在 `background` 或 `background-image` 中） |
| `position: relative` | 支持 |
| `border` / `border-left` 等 | 完全支持 |
| `padding` / `margin` | 完全支持 |
| `font-size` / `color` / `line-height` | 完全支持 |
| `text-align` / `text-indent` | 完全支持 |
| `background-color` | 完全支持 |
| `width` / `height` / `max-width` | 完全支持 |
| `opacity` | 支持 |
| `letter-spacing` | 支持 |
| `font-weight` / `font-style` | 支持 |
| Emoji 字符 | 原生支持，可自由使用 |
| `<table>` / `<td>` / `<tr>` | **最安全的布局方式** |

#### ❌ 不可用 / 不稳定

| 属性/特性 | 说明 |
|----------|------|
| `display: grid` | **完全不支持**，会被过滤 |
| `display: flex` | **不稳定**，部分场景可用但不可靠，**不要作为主要布局手段** |
| `position: absolute` | **不稳定**，可能被过滤 |
| `position: fixed` / `sticky` | **不支持** |
| `::before` / `::after` 伪元素 | **不支持** |
| `:hover` / `:nth-child` 等伪类 | **不支持** |
| `@keyframes` / `animation` | **不支持** |
| `transition` | 通常被忽略 |
| `@media` 媒体查询 | **不支持** |
| `<style>` 标签 | **会被过滤**，所有样式必须内联 |
| `<script>` 标签 | **会被过滤**（仅预览页面可用） |
| 外部 CSS / JS | **不支持** |
| `float` | 表现不稳定，不推荐 |

### 布局方案

#### 首选：`<table>` 布局（最安全）

```html
<!-- 双列布局 -->
<table style="width:100%; border-collapse:collapse;">
  <tr>
    <td style="width:50%; padding:0 8px 0 0; vertical-align:top;">
      <img src="..." style="width:100%; border-radius:8px;">
    </td>
    <td style="width:50%; padding:0 0 0 8px; vertical-align:top;">
      <img src="..." style="width:100%; border-radius:8px;">
    </td>
  </tr>
</table>

<!-- 三列布局 -->
<table style="width:100%; border-collapse:collapse;">
  <tr>
    <td style="width:33.33%; padding:0 6px 0 0; vertical-align:top;">
      <img src="..." style="width:100%; border-radius:8px;">
    </td>
    <td style="width:33.33%; padding:0 6px; vertical-align:top;">
      <img src="..." style="width:100%; border-radius:8px;">
    </td>
    <td style="width:33.33%; padding:0 0 0 6px; vertical-align:top;">
      <img src="..." style="width:100%; border-radius:8px;">
    </td>
  </tr>
</table>
```

#### 备选：`<section>` + 内联样式

```html
<!-- 简单的纵向堆叠用 section 即可 -->
<section style="padding:20px; background:#f5f5f5; border-radius:8px; margin:15px 0;">
  <p style="font-size:15px; color:#333; line-height:2;">内容</p>
</section>
```

#### ⚠️ 关于 flex 的使用

`display: flex` 在微信编辑器中**不稳定**。如果使用：
- 仅用于简单的水平/垂直排列
- 始终提供 `<table>` 作为降级方案
- 不要依赖 `flex-wrap`、`order`、`align-self` 等高级属性

### 内容区宽度

- **设计宽度：677px**（微信公众号内容区标准宽度）
- 图片建议宽度：不超过 640px（超过会被微信压缩）
- 手机端会自动缩放适配屏幕，无需针对 375px 设计

### 字体

微信编辑器不支持外部字体加载，使用系统字体栈：

```
font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
```

特殊风格可使用系统自带的中文字体：
- 楷体：`'STKaiti', 'KaiTi', serif`
- 宋体：`'STSong', 'SimSun', serif`
- 等宽：`'Courier New', monospace`

### 图片规范

| 项目 | 建议 |
|------|------|
| 图片宽度 | ≤ 640px（推荐 400-600px） |
| 图片格式 | JPG / PNG |
| 图片来源 | Unsplash（加 `?w=600` 参数优化加载） |
| base64 嵌入 | 小图标可用 base64，大图不建议（增加体积） |
| 默认占位图 | 使用 Unsplash 相关主题图片，而非纯色占位 |

### HTML 结构模板

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>公众号排版</title>
    <style>
        /* 仅预览页面使用的样式（不会被复制到微信） */
    </style>
</head>
<body>
    <div class="container">
        <div class="nav"><!-- 风格切换按钮（仅模式A） --></div>
        
        <div class="style-section" id="style-N">
            <div class="preview-box" id="preview-N">
                <!-- ★ 此区域内所有样式必须内联 ★ -->
                <!-- 使用 <section> + <table> + 内联 style -->
                <!-- 不要使用 class、伪元素、flex 布局 -->
            </div>
        </div>
    </div>
    
    <script>
    // 仅预览页面使用，不会被复制到微信
    function switchStyle(n) { /* 切换风格显示 */ }
    function copyStyle(n) {
        var code = document.getElementById('preview-' + n).innerHTML;
        navigator.clipboard.writeText(code).then(function() {
            // 显示复制成功提示
        });
    }
    </script>
</body>
</html>
```

## 输出规范

- **文件格式**：单个 `.html` 文件
- **文件命名**：`公众号排版组件库.html` 或根据用户主题命名
- **核心功能**：
  - 模式 A：导航切换 + 一键复制代码
  - 模式 B：纯净内联 HTML，直接全选复制
- **粘贴方式**：复制后直接在微信公众号后台编辑器中 Ctrl+V 粘贴
