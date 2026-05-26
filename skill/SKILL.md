# wechat-layout - 微信公众号AI排版设计器

**版本**: 2.1.0  
**类型**: 内容创作辅助工具  
**适用场景**: 微信公众号图文排版、内容创作

---

## 一、技能简介

专为微信公众号打造的 AI 排版设计器，提供：
- **11种预设风格** — 覆盖商务、文艺、创意、高端、知识等多种场景
- **Markdown转换** — 输入Markdown，自动生成可直接粘贴到微信公众号的HTML
- **风格提取** — 发送任意微信公众号文章，自动提取并生成排版模板
- **技术兼容** — 所有输出严格遵守微信HTML/CSS限制，确保100%正常显示

### 核心能力

✅ **Markdown转换**：输入Markdown，自动套用风格转HTML  
✅ **风格提取**：发送文章URL，自动提取风格并生成模板  
✅ **即用模板**：每个风格附带完整的HTML模板，可直接修改使用  
✅ **模块化扩展**：添加新风格只需增加配置，无需修改核心代码

---

## 二、文件结构

```
wechat-layout/
├── SKILL.md                        # 技能主文件（本文档）
├── README.md                       # 项目说明
├── LICENSE                         # MIT许可证
├── index.html                      # 风格展示页面
│
├── scripts/                        # 核心脚本
│   ├── format_article.py           # Markdown转HTML脚本
│   └── extract_style.py           # 从文章提取风格脚本
│
├── styles/                         # 风格配置
│   └── style_configs.py           # 11种风格配置（添加新风格只需修改此文件）
│
├── templates/                      # 风格HTML模板
│   ├── style_01_极简商务.html     # 极简商务模板
│   ├── style_11_高端知识.html      # 高端知识模板
│   └── extracted_styles.json       # 提取风格存储
│
└── examples/                       # 示例文件
    ├── 组件库-微信兼容版.html      # 微信兼容组件库
    └── 公众号排版组件库.html       # 完整组件库（参考用）
```

---

## 三、快速开始

### 3.1 Markdown转HTML

```python
from scripts.format_article import format_article

# 基本用法
html_output = format_article(markdown_text, "清新文艺")

# 列出所有可用风格
from scripts.format_article import list_styles
list_styles()
```

### 3.2 风格提取

```python
from scripts.extract_style import extract_style_from_url

# 从URL提取风格
config = extract_style_from_url("https://mp.weixin.qq.com/s/xxxxx")

# 保存到模板库
from scripts.extract_style import add_style_to_library
add_style_to_library("我的风格", config, "描述")
```

### 3.3 命令行使用

```bash
# 列出所有可用风格
python scripts/format_article.py --list

# 转换文件
python scripts/format_article.py --input article.md --output article.html --style 高端知识

# 提取文章风格
python scripts/extract_style.py --url "https://mp.weixin.qq.com/s/xxxxx" --save
```

---

## 四、11种预设风格

### 4.1 风格总览

| # | 风格 | 配色 | 适用场景 |
|---|------|------|---------|
| 1 | 极简商务 | 深蓝 #1a1a2e + 红 #e94560 | 企业号、职场、分析报告 |
| 2 | 清新文艺 | 绿色 #2e7d32 + 浅绿 #81c784 | 生活方式、读书分享 |
| 3 | 活力创意 | 红橙 #ff6b6b + 黄 #feca57 | 年轻品牌、活动推广 |
| 4 | 高端质感 | 深灰 #2c3e50 + 金 #d4af37 | 奢侈品、高端品牌 |
| 5 | 复古优雅 | 暖棕 #5d3a1a + 橙棕 #d2691e | 文化历史、怀旧主题 |
| 6 | 科技未来 | 深紫 #0f0c29 + 青 #00d4ff | 科技、AI、互联网 |
| 7 | 温柔治愈 | 珊瑚 #e17055 + 暖黄 #fdcb6e | 情感心理、生活感悟 |
| 8 | 杂志编辑 | 纯黑 #000 + 白 #fff | 时尚美妆、潮流内容 |
| 9 | 自然生态 | 青绿 #134e5e + 草绿 #8bc34a | 环保户外、健康生活 |
| 10 | 甜美少女 | 粉红 #ff9a9e + 浅粉 #fecfef | 美妆穿搭、少女心 |
| 11 | 高端知识 | 金棕 #c4a35a + 米白 #f5f5f0 | 知识付费、人物图谱 |

### 4.2 风格详细说明

#### 风格1: 极简商务 💼
**适用**：企业号、职场干货、行业分析
**配色**：深蓝底色 + 红色点缀
**特色**：数据卡片、时间轴、专业严谨

#### 风格2: 清新文艺 🌿
**适用**：生活方式、读书分享、慢节奏内容
**配色**：绿色渐变背景
**特色**：楷体标题、圆角元素、文艺淡雅

#### 风格3: 活力创意 🚀
**适用**：年轻品牌、活动推广、娱乐内容
**配色**：红橙黄渐变色彩
**特色**：大emoji装饰、活力节奏

#### 风格11: 高端知识 📚
**适用**：知识付费、人物图谱、深度内容
**配色**：金棕 #c4a35a + 米白 #f5f5f0
**特色**：
- 圆形头像 + 胶囊身份标签
- 关键词金色高亮
- 波浪装饰线（◆ ── ◆）

---

## 五、风格配置（添加新风格）

所有风格配置集中在 `styles/style_configs.py`，采用统一参数结构：

```python
STYLE_CONFIGS = {
    "我的新风格": {
        "name": "我的新风格",
        "description": "风格描述",
        "max_width": "677px",
        
        # 排版参数
        "body_font_size": "15px",
        "body_color": "#333333",
        "line_height": "1.8",
        "paragraph_margin": "0 0 20px 0",
        
        # 标题
        "h1_size": "22px",
        "h1_color": "#主色调",
        "h2_size": "18px",
        "h2_color": "#主色调",
        
        # 特色
        "primary_color": "#主色调",
        "features": ["quote_block", "divider"],
    },
}
```

### 添加新风格步骤

1. 在 `styles/style_configs.py` 中添加风格配置
2. 可选：在 `templates/` 创建HTML模板
3. 风格自动生效

---

## 六、技术规范

### 6.1 微信排版核心限制

⚠️ **禁止使用**：
- `display: flex` / `display: grid`
- `position: absolute` / `position: fixed`
- `transform` / `::before` / `::after`
- JavaScript
- class选择器（仅内联style）

✅ **安全CSS**：
```
文字: font-size, color, font-weight, line-height, letter-spacing
盒模型: margin, padding, border, border-radius, box-shadow
背景: background-color（纯色）
布局: display (block, inline, inline-block)
```

### 6.2 字号规范

| 元素 | 推荐值 |
|------|--------|
| 正文 | 15px |
| 一级标题 | 22-26px |
| 二级标题 | 18-20px |
| 行高 | 1.8-2.2倍 |

---

## 七、版本记录

| 版本 | 日期 | 更新内容 |
|------|------|---------|
| 2.1.0 | 2026-05 | 新增风格提取功能，模块化重构，微信兼容优化 |
| 2.0.0 | 2026-05 | 11种预设风格 |
| 1.0.0 | 2024 | 初始版本，10种风格 |

---

*本技能专为微信公众号内容创作者设计，遵循微信平台技术规范。*
