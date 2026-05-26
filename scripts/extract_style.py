# -*- coding: utf-8 -*-
"""
微信公众号风格提取脚本
功能：从微信公众号文章URL提取排版风格，并生成可复用的模板

使用方法：
    from scripts.extract_style import extract_style_from_url
    
    # 从URL提取风格
    config = extract_style_from_url("https://mp.weixin.qq.com/s/xxxxx")
    
    # 保存到模板库
    from scripts.extract_style import add_style_to_library
    add_style_to_library("我的风格", config)
"""

import re
import os
import sys
import json
import hashlib
from datetime import datetime
from typing import Dict, List, Optional, Tuple

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from styles.style_configs import STYLE_CONFIGS, add_style


# ========== 颜色提取工具 ==========

def extract_colors_from_css(css_text: str) -> Dict[str, str]:
    """
    从CSS文本中提取颜色配置
    
    Args:
        css_text: CSS文本内容
        
    Returns:
        dict: 提取的颜色配置
    """
    colors = {
        "primary_color": None,
        "secondary_color": None,
        "accent_color": None,
        "background_color": "#ffffff",
        "text_color": "#333333",
    }
    
    # 匹配hex颜色
    hex_pattern = r'#[0-9a-fA-F]{3,8}'
    hex_colors = re.findall(hex_pattern, css_text.lower())
    
    # 匹配rgb/rgba颜色
    rgb_pattern = r'rgba?\([^)]+\)'
    rgb_colors = re.findall(rgb_pattern, css_text.lower())
    
    # 合并所有颜色
    all_colors = hex_colors + rgb_colors
    
    # 分类颜色
    dark_colors = []  # 深色（标题、重要元素）
    light_colors = []  # 浅色（背景、辅助）
    accent_colors = []  # 强调色
    
    for color in all_colors:
        if 'rgba' in color:
            # 转换rgba为简化形式
            match = re.search(r'rgba?\((\d+),\s*(\d+),\s*(\d+)', color)
            if match:
                r, g, b = int(match.group(1)), int(match.group(2)), int(match.group(3))
                brightness = (r * 299 + g * 587 + b * 114) / 1000
                color = f"#{r:02x}{g:02x}{b:02x}"
                if brightness > 128:
                    light_colors.append(color)
                else:
                    dark_colors.append(color)
        elif len(color) >= 7:  # #rrggbb
            match = re.search(r'#([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})', color)
            if match:
                r, g, b = int(match.group(1), 16), int(match.group(2), 16), int(match.group(3), 16)
                brightness = (r * 299 + g * 587 + b * 114) / 1000
                if brightness > 200:
                    light_colors.append(color)
                elif brightness < 80:
                    accent_colors.append(color)
                else:
                    dark_colors.append(color)
    
    # 选择主色调（最常用的深色）
    if dark_colors:
        color_counts = {}
        for c in dark_colors:
            color_counts[c] = color_counts.get(c, 0) + 1
        colors["primary_color"] = max(color_counts, key=color_counts.get)
    
    # 选择次要色（最常用的浅色）
    if light_colors:
        color_counts = {}
        for c in light_colors:
            color_counts[c] = color_counts.get(c, 0) + 1
        colors["secondary_color"] = max(color_counts, key=color_counts.get)
    
    # 选择强调色
    if accent_colors:
        colors["accent_color"] = accent_colors[0]
    
    return colors


def extract_typography(html_content: str) -> Dict[str, any]:
    """
    从HTML内容中提取排版参数
    
    Args:
        html_content: HTML文本内容
        
    Returns:
        dict: 排版参数
    """
    typography = {
        "body_font_size": "15px",
        "h1_size": "22px",
        "h2_size": "18px",
        "h3_size": "16px",
        "line_height": "1.8",
        "paragraph_margin": "20px 0",
    }
    
    # 提取字体大小
    size_pattern = r'font-size:\s*(\d+)px'
    sizes = [int(s) for s in re.findall(size_pattern, html_content)]
    
    if sizes:
        # 分类尺寸
        large_sizes = [s for s in sizes if s >= 20]  # 标题
        medium_sizes = [s for s in sizes if 14 <= s < 20]  # 正文/小标题
        small_sizes = [s for s in sizes if s < 14]  # 辅助文字
        
        if large_sizes:
            typography["h1_size"] = f"{max(large_sizes)}px"
        if medium_sizes:
            # 找中间值作为正文字号
            median_size = sorted(medium_sizes)[len(medium_sizes) // 2]
            if median_size >= 15:
                typography["body_font_size"] = f"{median_size}px"
    
    # 提取行高
    lh_pattern = r'line-height:\s*([\d.]+)'
    lh_matches = re.findall(lh_pattern, html_content)
    if lh_matches:
        # 取最常见的行高值
        lh_counts = {}
        for lh in lh_matches:
            lh_counts[lh] = lh_counts.get(lh, 0) + 1
        max_lh = max(lh_counts, key=lh_counts.get)
        typography["line_height"] = max_lh
    
    return typography


def detect_features(html_content: str) -> List[str]:
    """
    检测文章中的特色组件
    
    Args:
        html_content: HTML文本内容
        
    Returns:
        list: 检测到的特色组件列表
    """
    features = []
    
    # 人物卡片检测（圆形头像 + 姓名标签）
    if re.search(r'(border-radius:\s*50%|圆形|avatar)', html_content):
        features.append("person_card")
    
    # 引用块检测
    if re.search(r'<blockquote', html_content):
        features.append("quote_block")
    
    # 分割线检测
    if re.search(r'(分割线|divider|◆|━━)', html_content):
        features.append("divider")
    
    # 关键词高亮检测
    if re.search(r'(highlight|高亮|标注)', html_content):
        features.append("keyword_highlight")
    
    # 卡片检测
    if re.search(r'(card|卡片)', html_content):
        features.append("card")
    
    # 图片画廊检测
    if html_content.count('<img') > 3:
        features.append("image_gallery")
    
    # 时间轴检测
    if re.search(r'(timeline|时间轴|步骤)', html_content):
        features.append("timeline")
    
    # 表格检测
    if re.search(r'<table', html_content):
        features.append("table")
    
    return features


def analyze_color_harmony(primary: str, secondary: str = None) -> str:
    """
    分析配色和谐度并推荐风格类型
    
    Args:
        primary: 主色
        secondary: 次色
        
    Returns:
        str: 推荐风格类型
    """
    if not primary:
        return "custom"
    
    # 分析主色调
    if primary.startswith('#'):
        r = int(primary[1:3], 16)
        g = int(primary[3:5], 16)
        b = int(primary[5:7], 16)
    else:
        return "custom"
    
    brightness = (r * 299 + g * 587 + b * 114) / 1000
    
    # 分析色相
    max_rgb = max(r, g, b)
    min_rgb = min(r, g, b)
    
    if max_rgb == min_rgb:
        hue = "neutral"  # 灰色系
    elif max_rgb == r:
        hue = "red" if g >= b else "purple"
    elif max_rgb == g:
        hue = "green"
    else:
        hue = "blue"
    
    # 根据颜色推荐风格
    if brightness < 50:
        return "tech"  # 深色科技风
    elif hue in ["green", "teal"]:
        return "nature"  # 自然绿色系
    elif hue in ["red", "orange", "pink"]:
        if brightness > 150:
            return "healing"  # 温暖治愈
        else:
            return "creative"  # 活力创意
    elif hue == "neutral":
        return "business"  # 商务灰色系
    else:
        return "custom"


def generate_style_name(colors: Dict, features: List[str]) -> str:
    """
    根据提取的颜色和特征生成风格名称
    
    Args:
        colors: 颜色配置
        features: 检测到的特征
        
    Returns:
        str: 生成的风格名称
    """
    # 基于颜色和特征组合名称
    harmony = analyze_color_harmony(colors.get("primary_color"), colors.get("secondary_color"))
    
    names = {
        "tech": "科技未来",
        "nature": "自然生态",
        "healing": "温柔治愈",
        "creative": "活力创意",
        "business": "极简商务",
        "custom": "自定义风格",
    }
    
    base_name = names.get(harmony, "自定义风格")
    
    # 添加特征后缀
    if "person_card" in features:
        base_name = "高端知识"
    elif "card" in features and "healing" in harmony:
        base_name = "甜美少女"
    
    return base_name


# ========== HTML解析工具 ==========

def extract_text_content(html: str) -> str:
    """去除HTML标签，提取纯文本"""
    # 移除script和style标签
    html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL | re.IGNORECASE)
    # 移除HTML标签
    html = re.sub(r'<[^>]+>', ' ', html)
    # 清理空白
    html = re.sub(r'\s+', ' ', html)
    return html.strip()


def extract_inline_styles(html: str) -> str:
    """提取所有内联样式"""
    styles = re.findall(r'style="([^"]*)"', html)
    return ' '.join(styles)


def clean_wechat_html(html: str) -> str:
    """
    清理微信公众号HTML，移除不支持的元素
    
    Args:
        html: 原始HTML
        
    Returns:
        str: 清理后的HTML
    """
    # 移除class属性（微信不支持）
    html = re.sub(r'class="[^"]*"', '', html)
    
    # 移除不支持的CSS属性
    unsupported_attrs = [
        r'position:\s*absolute',
        r'position:\s*fixed',
        r'transform:',
        r'display:\s*grid',
        r'display:\s*flex',
        r'::before',
        r'::after',
    ]
    
    for attr in unsupported_attrs:
        html = re.sub(rf'style="([^"]*{attr}[^"]*)"', 'style=""', html)
    
    return html


# ========== 风格配置生成 ==========

def generate_style_config(
    html_content: str,
    url: str = None,
    title: str = None
) -> Dict:
    """
    从HTML内容生成风格配置
    
    Args:
        html_content: 文章HTML内容
        url: 文章URL（可选）
        title: 文章标题（可选）
        
    Returns:
        dict: 风格配置
    """
    # 提取样式文本
    css_text = extract_inline_styles(html_content)
    
    # 提取颜色
    colors = extract_colors_from_css(css_text)
    
    # 提取排版参数
    typography = extract_typography(html_content)
    
    # 检测特色组件
    features = detect_features(html_content)
    
    # 生成风格名称
    style_name = generate_style_name(colors, features)
    
    # 构建配置
    config = {
        "name": title or style_name,
        "name_en": "Extracted Style",
        "description": f"从微信公众号文章提取的风格 - {title or '未命名'}",
        "url": url,
        "extracted_at": datetime.now().isoformat(),
        
        # 容器
        "max_width": "677px",
        "container_margin": "0 auto",
        
        # 排版
        "body_font_size": typography.get("body_font_size", "15px"),
        "body_color": colors.get("text_color", "#333333"),
        "line_height": typography.get("line_height", "1.8"),
        "letter_spacing": "0.3px",
        "paragraph_margin": typography.get("paragraph_margin", "0 0 20px 0"),
        
        # 标题
        "h1_size": typography.get("h1_size", "22px"),
        "h1_color": colors.get("primary_color", "#1a1a1a"),
        "h1_weight": "bold",
        "h1_align": "center",
        "h2_size": typography.get("h2_size", "18px"),
        "h2_color": colors.get("primary_color", "#1a1a1a"),
        "h2_weight": "bold",
        "h3_size": typography.get("h3_size", "16px"),
        "h3_color": colors.get("secondary_color", "#333333"),
        
        # 引用
        "quote_bg": "#f5f5f5",
        "quote_border": colors.get("primary_color", "#999999"),
        "quote_color": colors.get("text_color", "#555555"),
        "quote_size": "14px",
        
        # 强调
        "emphasis_color": colors.get("accent_color") or colors.get("primary_color", "#e94560"),
        
        # 分割线
        "divider_style": "center",
        
        # 卡片
        "card_bg": colors.get("secondary_color", "#ffffff"),
        "card_border": colors.get("primary_color", "#d0d0d0"),
        "card_radius": "8px",
        
        # 颜色
        "primary_color": colors.get("primary_color", "#333333"),
        "secondary_color": colors.get("secondary_color", "#f5f5f5"),
        "accent_color": colors.get("accent_color"),
        
        # 特色组件
        "features": features,
    }
    
    return config


def generate_html_template(config: Dict, sample_content: str = None) -> str:
    """
    根据配置生成HTML模板
    
    Args:
        config: 风格配置
        sample_content: 示例内容
        
    Returns:
        str: HTML模板代码
    """
    primary = config.get("primary_color", "#333333")
    secondary = config.get("secondary_color", "#f5f5f5")
    emphasis = config.get("emphasis_color", primary)
    
    template = f'''<section style="margin:0 auto;max-width:{config.get("max_width", "677px")};">
    
    <!-- 文章标题 -->
    <h1 style="font-size:{config.get("h1_size", "22px")};font-weight:bold;color:{config.get("h1_color", "#1a1a1a")};text-align:center;letter-spacing:2px;margin:40px 0 30px 0;line-height:1.5;">
        {sample_content or "文章标题"}
    </h1>
    
    <!-- 正文段落 -->
    <p style="font-size:{config.get("body_font_size", "15px")};color:{config.get("body_color", "#333333")};text-align:justify;line-height:{config.get("line_height", "1.8")};margin:{config.get("paragraph_margin", "0 0 20px 0")};letter-spacing:{config.get("letter_spacing", "0.3px")};">
        {sample_content or "正文内容，请替换为您的文章内容。"}
    </p>
    
    <!-- 二级标题 -->
    <h2 style="font-size:{config.get("h2_size", "18px")};font-weight:bold;color:{config.get("h2_color", "#1a1a1a")};margin:36px 0 20px 0;padding-left:16px;border-left:3px solid {config.get("h2_color", "#1a1a1a")};line-height:1.4;">
        小节标题
    </h2>
    
    <!-- 引用块 -->
    <blockquote style="margin:24px 0;padding:16px 20px;background:{config.get("quote_bg", "#f5f5f5")};border-left:3px solid {config.get("quote_border", "#999999")};">
        <p style="font-size:{config.get("quote_size", "14px")};color:{config.get("quote_color", "#555555")};line-height:1.8;margin:0;">
            引用内容，可以用来强调重要观点。
        </p>
    </blockquote>
    
    <!-- 列表 -->
    <ul style="margin:24px 0;padding-left:0;list-style-type:none;">
        <li style="font-size:{config.get("body_font_size", "15px")};color:{config.get("body_color", "#333333")};line-height:{config.get("line_height", "1.8")};margin:0 0 12px 0;">
            <span style="color:{emphasis};">◆ </span>列表项一
        </li>
        <li style="font-size:{config.get("body_font_size", "15px")};color:{config.get("body_color", "#333333")};line-height:{config.get("line_height", "1.8")};margin:0 0 12px 0;">
            <span style="color:{emphasis};">◆ </span>列表项二
        </li>
        <li style="font-size:{config.get("body_font_size", "15px")};color:{config.get("body_color", "#333333")};line-height:{config.get("line_height", "1.8")};margin:0 0 12px 0;">
            <span style="color:{emphasis};">◆ </span>列表项三
        </li>
    </ul>
    
    <!-- 分割线 -->
    <p style="text-align:center;margin:40px 0;">
        <span style="display:inline-block;width:8px;height:8px;background:{primary};border-radius:50%;"></span>
        <span style="display:inline-block;width:8px;height:8px;background:{primary};border-radius:50%;margin:0 8px;"></span>
        <span style="display:inline-block;width:8px;height:8px;background:{primary};border-radius:50%;"></span>
    </p>
    
    <!-- 底部留白 -->
    <p style="height:40px;"></p>
    
</section>'''
    
    return template


# ========== 主函数 ==========

def extract_style_from_url(url: str) -> Dict:
    """
    从微信公众号URL提取风格配置
    
    Args:
        url: 微信公众号文章URL
        
    Returns:
        dict: 风格配置（包含HTML模板）
    """
    try:
        from scripts.extract_style import fetch_wechat_article
        
        # 获取文章内容
        html_content, title = fetch_wechat_article(url)
        
        if not html_content:
            print(f"警告：无法获取文章内容，使用默认配置")
            return generate_default_config(url)
        
        # 生成配置
        config = generate_style_config(html_content, url, title)
        
        # 生成HTML模板
        config["html_template"] = generate_html_template(config)
        
        return config
        
    except ImportError:
        # 如果无法获取，使用手动输入模式
        print("提示：无法自动获取文章内容，请提供文章的HTML代码或手动描述风格")
        return {
            "name": "待定义风格",
            "manual_input_required": True,
            "instructions": "请提供文章的HTML代码或详细描述颜色、字体等风格特征"
        }


def extract_style_from_html(html_content: str, name: str = None) -> Dict:
    """
    从HTML内容提取风格配置
    
    Args:
        html_content: 文章HTML内容
        name: 风格名称（可选）
        
    Returns:
        dict: 风格配置（包含HTML模板）
    """
    config = generate_style_config(html_content, title=name)
    config["html_template"] = generate_html_template(config)
    return config


def fetch_wechat_article(url: str) -> Tuple[str, str]:
    """
    获取微信公众号文章内容
    
    Args:
        url: 文章URL
        
    Returns:
        tuple: (HTML内容, 标题)
    """
    try:
        import requests
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        }
        
        response = requests.get(url, headers=headers, timeout=30)
        response.encoding = 'utf-8'
        
        html = response.text
        
        # 提取标题
        title_match = re.search(r'<h1[^>]*id="activity-name"[^>]*>([^<]+)</h1>', html)
        if not title_match:
            title_match = re.search(r'<title>([^<]+)</title>', html)
        
        title = title_match.group(1).strip() if title_match else "未命名文章"
        
        # 提取正文内容
        content_match = re.search(r'<div[^>]*id="js_content"[^>]*>(.*?)</div>', html, re.DOTALL)
        if content_match:
            content = content_match.group(1)
        else:
            content = html
        
        return content, title
        
    except Exception as e:
        print(f"获取文章失败: {e}")
        return None, None


def generate_default_config(url: str = None) -> Dict:
    """生成默认配置"""
    return {
        "name": "自定义风格",
        "description": "手动定义的排版风格",
        "url": url,
        
        "max_width": "677px",
        "container_margin": "0 auto",
        
        "body_font_size": "15px",
        "body_color": "#333333",
        "line_height": "1.8",
        "letter_spacing": "0.3px",
        "paragraph_margin": "0 0 20px 0",
        
        "h1_size": "22px",
        "h1_color": "#333333",
        "h1_weight": "bold",
        "h1_align": "center",
        "h2_size": "18px",
        "h2_color": "#333333",
        "h2_weight": "bold",
        "h3_size": "16px",
        "h3_color": "#555555",
        
        "quote_bg": "#f5f5f5",
        "quote_border": "#999999",
        "quote_color": "#555555",
        "quote_size": "14px",
        
        "emphasis_color": "#e94560",
        "divider_style": "center",
        
        "card_bg": "#ffffff",
        "card_border": "#d0d0d0",
        "card_radius": "8px",
        
        "primary_color": "#333333",
        "secondary_color": "#f5f5f5",
        "features": [],
    }


# ========== 模板库管理 ==========

TEMPLATE_LIBRARY_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'templates',
    'extracted_styles.json'
)


def load_style_library() -> Dict:
    """加载已保存的风格库"""
    if os.path.exists(TEMPLATE_LIBRARY_PATH):
        with open(TEMPLATE_LIBRARY_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def save_style_library(library: Dict):
    """保存风格库"""
    os.makedirs(os.path.dirname(TEMPLATE_LIBRARY_PATH), exist_ok=True)
    with open(TEMPLATE_LIBRARY_PATH, 'w', encoding='utf-8') as f:
        json.dump(library, f, ensure_ascii=False, indent=2)


def add_style_to_library(name: str, config: Dict, description: str = None):
    """
    将提取的风格添加到模板库
    
    Args:
        name: 风格名称
        config: 风格配置
        description: 风格描述
    """
    library = load_style_library()
    
    # 生成唯一ID
    style_id = hashlib.md5(name.encode()).hexdigest()[:8]
    
    # 添加到库
    library[style_id] = {
        "name": name,
        "description": description or config.get("description", ""),
        "config": config,
        "added_at": datetime.now().isoformat(),
    }
    
    save_style_library(library)
    
    # 同时添加到运行时配置
    add_style(name, config)
    
    print(f"✓ 风格 '{name}' 已添加到模板库")
    print(f"  位置: {TEMPLATE_LIBRARY_PATH}")


def remove_style_from_library(style_id: str):
    """从模板库移除风格"""
    library = load_style_library()
    
    if style_id in library:
        name = library[style_id]["name"]
        del library[style_id]
        save_style_library(library)
        print(f"✓ 风格 '{name}' 已从模板库移除")
    else:
        print(f"错误：未找到风格 ID '{style_id}'")


def list_extracted_styles():
    """列出所有提取的风格"""
    library = load_style_library()
    
    if not library:
        print("模板库为空，尚未提取任何风格")
        print("\n使用方法：")
        print("  from scripts.extract_style import extract_style_from_url, add_style_to_library")
        print("  config = extract_style_from_url('https://mp.weixin.qq.com/s/xxxxx')")
        print("  add_style_to_library('我的风格', config)")
        return
    
    print("=" * 60)
    print("已提取的风格库：")
    print("=" * 60)
    
    for style_id, info in library.items():
        print(f"\n【{info['name']}】")
        print(f"  ID: {style_id}")
        print(f"  描述: {info.get('description', '无')}")
        print(f"  添加时间: {info.get('added_at', '未知')}")
        
        config = info.get('config', {})
        print(f"  主色: {config.get('primary_color', '未定义')}")
        print(f"  特色: {', '.join(config.get('features', [])) or '无'}")


# ========== CLI入口 ==========

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='微信公众号风格提取工具')
    parser.add_argument('--url', type=str, help='微信公众号文章URL')
    parser.add_argument('--html', type=str, help='HTML文件路径')
    parser.add_argument('--name', type=str, help='风格名称')
    parser.add_argument('--save', action='store_true', help='保存到模板库')
    parser.add_argument('--list', action='store_true', help='列出所有提取的风格')
    
    args = parser.parse_args()
    
    if args.list:
        list_extracted_styles()
    elif args.url:
        print(f"正在提取风格: {args.url}")
        config = extract_style_from_url(args.url)
        print("\n" + "=" * 50)
        print("提取的风格配置：")
        print("=" * 50)
        print(f"名称: {config.get('name', '未命名')}")
        print(f"主色: {config.get('primary_color', '未定义')}")
        print(f"次色: {config.get('secondary_color', '未定义')}")
        print(f"强调色: {config.get('emphasis_color', '未定义')}")
        print(f"正文字号: {config.get('body_font_size', '15px')}")
        print(f"行高: {config.get('line_height', '1.8')}")
        print(f"特色组件: {', '.join(config.get('features', [])) or '无'}")
        
        if args.save:
            name = args.name or config.get('name', '提取风格')
            add_style_to_library(name, config)
    elif args.html:
        with open(args.html, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        config = extract_style_from_html(html_content, args.name)
        print("风格提取完成！")
        print(json.dumps(config, ensure_ascii=False, indent=2))
    else:
        print("""
╔════════════════════════════════════════════════════════════╗
║          微信公众号风格提取工具 v1.0.0                       ║
╠════════════════════════════════════════════════════════════╣
║  功能：从微信公众号文章提取排版风格                         ║
║  用法：python extract_style.py [选项]                       ║
╠════════════════════════════════════════════════════════════╣
║  命令行选项：                                              ║
║    --url <url>     微信公众号文章URL                        ║
║    --html <file>   HTML文件路径                             ║
║    --name <name>   风格名称                                 ║
║    --save          保存到模板库                             ║
║    --list          列出已提取的风格                         ║
║                                                         ║
║  示例：                                                   ║
║    python extract_style.py --url "https://mp.weixin.qq..."  ║
║    python extract_style.py --url "..." --save --name "我的风格" ║
║    python extract_style.py --list                           ║
╚════════════════════════════════════════════════════════════╝
        """)
