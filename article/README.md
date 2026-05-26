# 公众号排版神器 - 宣传文章

这是一篇用于推广 wechat-layout 的微信公众号文章，采用 **活力创意** 风格（红橙黄配色）。

## 文件说明

- `article-creative.html` - 活力创意风格文章（当前版本）
- `article-green.html` - 清新文艺风格文章（备选）

## 使用方法

1. 用浏览器打开 HTML 文件预览
2. 复制 `<div>` 标签内的全部内容
3. 粘贴到微信公众号编辑器

## 微信兼容性说明

本文章已针对微信公众号编辑器进行优化：

- ✅ 使用 `<table>` 布局替代 flex/grid
- ✅ 使用 `<div>` 替代 `<section>`
- ✅ 使用十六进制颜色替代 rgba()
- ✅ 移除表格上的 `border-radius` + `overflow: hidden` 组合
- ✅ 支持 `border-radius`、`box-shadow`、`box-sizing`

## 在线预览

部署后可访问：`https://greatbeing.github.io/wechat-layout/article-creative.html`
