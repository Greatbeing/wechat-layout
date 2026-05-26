# -*- coding: utf-8 -*-
"""
微信公众号排版风格配置
所有风格配置集中在此文件，添加新风格只需修改此模块

使用方法：
    from styles.style_configs import STYLE_CONFIGS, get_style_config
    
    config = get_style_config("清新文艺")
    print(config["primary_color"])
"""

# 风格配置字典
STYLE_CONFIGS = {
    # ========== 风格1: 极简商务 ==========
    "极简商务": {
        "name": "极简商务",
        "name_en": "Business Minimal",
        "description": "企业号、职场干货、行业分析",
        "max_width": "677px",
        "container_margin": "0 auto",
        
        # 正文
        "body_font_size": "15px",
        "body_color": "#333333",
        "line_height": "2.0",
        "letter_spacing": "0.3px",
        "paragraph_margin": "0 0 20px 0",
        
        # 标题
        "h1_size": "22px",
        "h1_color": "#1a1a2e",
        "h1_weight": "bold",
        "h1_align": "center",
        "h2_size": "18px",
        "h2_color": "#1a1a2e",
        "h2_weight": "bold",
        "h3_size": "16px",
        "h3_color": "#333333",
        
        # 引用
        "quote_bg": "#f5f7fa",
        "quote_border": "#1a1a2e",
        "quote_color": "#555555",
        "quote_size": "14px",
        
        # 强调
        "emphasis_color": "#e94560",
        
        # 分割线
        "divider_style": "professional",
        
        # 卡片
        "card_bg": "#ffffff",
        "card_border": "#d0d8e4",
        "card_radius": "8px",
        
        # 特色
        "primary_color": "#1a1a2e",
        "secondary_color": "#e94560",
        "features": ["data_card", "timeline", "numbered_list"],
    },
    
    # ========== 风格2: 清新文艺 ==========
    "清新文艺": {
        "name": "清新文艺",
        "name_en": "Natural Artistic",
        "description": "生活方式、读书分享、慢节奏内容",
        "max_width": "677px",
        "container_margin": "0 auto",
        
        # 正文
        "body_font_size": "15px",
        "body_color": "#4a4a4a",
        "line_height": "2.2",
        "letter_spacing": "0.5px",
        "paragraph_margin": "0 0 24px 0",
        
        # 标题
        "h1_size": "24px",
        "h1_color": "#2e7d32",
        "h1_weight": "normal",
        "h1_align": "center",
        "h2_size": "18px",
        "h2_color": "#388e3c",
        "h2_weight": "normal",
        "h3_size": "16px",
        "h3_color": "#4a4a4a",
        
        # 引用
        "quote_bg": "#f1f8e9",
        "quote_border": "#81c784",
        "quote_color": "#5a5a5a",
        "quote_size": "14px",
        
        # 强调
        "emphasis_color": "#2e7d32",
        
        # 分割线
        "divider_style": "nature",
        
        # 卡片
        "card_bg": "#f1f8e9",
        "card_border": "#a5d6a7",
        "card_radius": "12px",
        
        # 特色
        "primary_color": "#2e7d32",
        "secondary_color": "#81c784",
        "features": ["leaf_decoration", "soft_shadow", "rounded_elements"],
    },
    
    # ========== 风格3: 活力创意 ==========
    "活力创意": {
        "name": "活力创意",
        "name_en": "Vibrant Creative",
        "description": "年轻品牌、活动推广、娱乐内容",
        "max_width": "677px",
        "container_margin": "0 auto",
        
        # 正文
        "body_font_size": "15px",
        "body_color": "#333333",
        "line_height": "1.9",
        "letter_spacing": "0.3px",
        "paragraph_margin": "0 0 18px 0",
        
        # 标题
        "h1_size": "26px",
        "h1_color": "#ff6b6b",
        "h1_weight": "bold",
        "h1_align": "center",
        "h2_size": "19px",
        "h2_color": "#ff6b6b",
        "h2_weight": "bold",
        "h3_size": "16px",
        "h3_color": "#feca57",
        
        # 引用
        "quote_bg": "#fff9e6",
        "quote_border": "#feca57",
        "quote_color": "#666666",
        "quote_size": "15px",
        
        # 强调
        "emphasis_color": "#ff6b6b",
        
        # 分割线
        "divider_style": "emoji",
        
        # 卡片
        "card_bg": "#ffffff",
        "card_border": "#ff6b6b",
        "card_radius": "16px",
        
        # 特色
        "primary_color": "#ff6b6b",
        "secondary_color": "#feca57",
        "features": ["emoji_decoration", "gradient_text", "colorful_list"],
    },
    
    # ========== 风格4: 高端质感 ==========
    "高端质感": {
        "name": "高端质感",
        "name_en": "Luxury Premium",
        "description": "奢侈品、高端品牌、精品内容",
        "max_width": "677px",
        "container_margin": "0 auto",
        
        # 正文
        "body_font_size": "15px",
        "body_color": "#2c2c2c",
        "line_height": "1.9",
        "letter_spacing": "0.4px",
        "paragraph_margin": "0 0 20px 0",
        
        # 标题
        "h1_size": "24px",
        "h1_color": "#2c3e50",
        "h1_weight": "bold",
        "h1_align": "center",
        "h2_size": "18px",
        "h2_color": "#2c3e50",
        "h2_weight": "bold",
        "h3_size": "16px",
        "h3_color": "#4a4a4a",
        
        # 引用
        "quote_bg": "#fafafa",
        "quote_border": "#d4af37",
        "quote_color": "#555555",
        "quote_size": "14px",
        
        # 强调
        "emphasis_color": "#d4af37",
        
        # 分割线
        "divider_style": "elegant",
        
        # 卡片
        "card_bg": "#ffffff",
        "card_border": "#d4af37",
        "card_radius": "4px",
        
        # 特色
        "primary_color": "#2c3e50",
        "secondary_color": "#d4af37",
        "features": ["gold_accent", "thin_border", "professional_layout"],
    },
    
    # ========== 风格5: 复古优雅 ==========
    "复古优雅": {
        "name": "复古优雅",
        "name_en": "Vintage Elegant",
        "description": "文化历史、怀旧主题、古典风格",
        "max_width": "677px",
        "container_margin": "0 auto",
        
        # 正文
        "body_font_size": "15px",
        "body_color": "#5d3a1a",
        "line_height": "2.0",
        "letter_spacing": "0.8px",
        "paragraph_margin": "0 0 22px 0",
        
        # 标题
        "h1_size": "24px",
        "h1_color": "#5d3a1a",
        "h1_weight": "bold",
        "h1_align": "center",
        "h2_size": "18px",
        "h2_color": "#8b4513",
        "h2_weight": "bold",
        "h3_size": "16px",
        "h3_color": "#a0522d",
        
        # 引用
        "quote_bg": "#fdf5e6",
        "quote_border": "#d2691e",
        "quote_color": "#5d3a1a",
        "quote_size": "14px",
        
        # 强调
        "emphasis_color": "#d2691e",
        
        # 分割线
        "divider_style": "classic",
        
        # 卡片
        "card_bg": "#fdf5e6",
        "card_border": "#deb887",
        "card_radius": "2px",
        
        # 特色
        "primary_color": "#5d3a1a",
        "secondary_color": "#d2691e",
        "features": ["warm_tone", "classical_decoration", "texture_bg"],
    },
    
    # ========== 风格6: 科技未来 ==========
    "科技未来": {
        "name": "科技未来",
        "name_en": "Tech Future",
        "description": "科技、AI、互联网、数字主题",
        "max_width": "677px",
        "container_margin": "0 auto",
        
        # 正文
        "body_font_size": "15px",
        "body_color": "#e0e0e0",
        "line_height": "1.9",
        "letter_spacing": "0.3px",
        "paragraph_margin": "0 0 18px 0",
        
        # 标题
        "h1_size": "24px",
        "h1_color": "#00d4ff",
        "h1_weight": "bold",
        "h1_align": "center",
        "h2_size": "18px",
        "h2_color": "#00d4ff",
        "h2_weight": "bold",
        "h3_size": "16px",
        "h3_color": "#7c4dff",
        
        # 引用
        "quote_bg": "#1a1a2e",
        "quote_border": "#00d4ff",
        "quote_color": "#b0b0b0",
        "quote_size": "14px",
        
        # 强调
        "emphasis_color": "#00d4ff",
        
        # 分割线
        "divider_style": "tech",
        
        # 卡片
        "card_bg": "#1a1a2e",
        "card_border": "#00d4ff",
        "card_radius": "4px",
        
        # 特色
        "primary_color": "#00d4ff",
        "secondary_color": "#7c4dff",
        "features": ["dark_theme", "glow_effect", "tech_symbols"],
    },
    
    # ========== 风格7: 温柔治愈 ==========
    "温柔治愈": {
        "name": "温柔治愈",
        "name_en": "Gentle Healing",
        "description": "情感心理、生活感悟、陪伴内容",
        "max_width": "677px",
        "container_margin": "0 auto",
        
        # 正文
        "body_font_size": "15px",
        "body_color": "#5a5a5a",
        "line_height": "2.0",
        "letter_spacing": "0.3px",
        "paragraph_margin": "0 0 24px 0",
        
        # 标题
        "h1_size": "23px",
        "h1_color": "#e17055",
        "h1_weight": "normal",
        "h1_align": "center",
        "h2_size": "18px",
        "h2_color": "#e17055",
        "h2_weight": "normal",
        "h3_size": "16px",
        "h3_color": "#74b9ff",
        
        # 引用
        "quote_bg": "#fff5f0",
        "quote_border": "#e17055",
        "quote_color": "#8a7a7a",
        "quote_size": "14px",
        
        # 强调
        "emphasis_color": "#e17055",
        
        # 分割线
        "divider_style": "warm",
        
        # 卡片
        "card_bg": "#fff8f5",
        "card_border": "#fab1a0",
        "card_radius": "20px",
        
        # 特色
        "primary_color": "#e17055",
        "secondary_color": "#fdcb6e",
        "features": ["soft_colors", "rounded_corners", "heart_decoration"],
    },
    
    # ========== 风格8: 杂志编辑 ==========
    "杂志编辑": {
        "name": "杂志编辑",
        "name_en": "Magazine Editorial",
        "description": "时尚美妆、潮流内容、高颜值排版",
        "max_width": "677px",
        "container_margin": "0 auto",
        
        # 正文
        "body_font_size": "15px",
        "body_color": "#000000",
        "line_height": "1.9",
        "letter_spacing": "0.3px",
        "paragraph_margin": "0 0 16px 0",
        
        # 标题
        "h1_size": "28px",
        "h1_color": "#000000",
        "h1_weight": "bold",
        "h1_align": "left",
        "h2_size": "20px",
        "h2_color": "#000000",
        "h2_weight": "bold",
        "h3_size": "17px",
        "h3_color": "#333333",
        
        # 引用
        "quote_bg": "#ffffff",
        "quote_border": "#000000",
        "quote_color": "#000000",
        "quote_size": "16px",
        
        # 强调
        "emphasis_color": "#000000",
        
        # 分割线
        "divider_style": "minimal",
        
        # 卡片
        "card_bg": "#ffffff",
        "card_border": "#000000",
        "card_radius": "0px",
        
        # 特色
        "primary_color": "#000000",
        "secondary_color": "#ffffff",
        "features": ["high_contrast", "large_image", "bold_typography"],
    },
    
    # ========== 风格9: 自然生态 ==========
    "自然生态": {
        "name": "自然生态",
        "name_en": "Eco Nature",
        "description": "环保户外、健康生活、绿色主题",
        "max_width": "677px",
        "container_margin": "0 auto",
        
        # 正文
        "body_font_size": "15px",
        "body_color": "#3d3d3d",
        "line_height": "2.1",
        "letter_spacing": "0.3px",
        "paragraph_margin": "0 0 22px 0",
        
        # 标题
        "h1_size": "24px",
        "h1_color": "#134e5e",
        "h1_weight": "bold",
        "h1_align": "center",
        "h2_size": "18px",
        "h2_color": "#1a6b7c",
        "h2_weight": "bold",
        "h3_size": "16px",
        "h3_color": "#2a8a9e",
        
        # 引用
        "quote_bg": "#e8f5e9",
        "quote_border": "#8bc34a",
        "quote_color": "#3d3d3d",
        "quote_size": "14px",
        
        # 强调
        "emphasis_color": "#8bc34a",
        
        # 分割线
        "divider_style": "nature",
        
        # 卡片
        "card_bg": "#f1f8e9",
        "card_border": "#aed581",
        "card_radius": "12px",
        
        # 特色
        "primary_color": "#134e5e",
        "secondary_color": "#8bc34a",
        "features": ["green_tone", "leaf_symbol", "clean_layout"],
    },
    
    # ========== 风格10: 甜美少女 ==========
    "甜美少女": {
        "name": "甜美少女",
        "name_en": "Sweet Girlie",
        "description": "美妆穿搭、少女心、可爱风格",
        "max_width": "677px",
        "container_margin": "0 auto",
        
        # 正文
        "body_font_size": "15px",
        "body_color": "#666666",
        "line_height": "2.0",
        "letter_spacing": "0.3px",
        "paragraph_margin": "0 0 22px 0",
        
        # 标题
        "h1_size": "24px",
        "h1_color": "#ff9a9e",
        "h1_weight": "normal",
        "h1_align": "center",
        "h2_size": "18px",
        "h2_color": "#ff9a9e",
        "h2_weight": "normal",
        "h3_size": "16px",
        "h3_color": "#ffc3a0",
        
        # 引用
        "quote_bg": "#fff0f5",
        "quote_border": "#ff9a9e",
        "quote_color": "#8a7a7a",
        "quote_size": "14px",
        
        # 强调
        "emphasis_color": "#ff9a9e",
        
        # 分割线
        "divider_style": "cute",
        
        # 卡片
        "card_bg": "#fff8fb",
        "card_border": "#ffd1dc",
        "card_radius": "24px",
        
        # 特色
        "primary_color": "#ff9a9e",
        "secondary_color": "#fecfef",
        "features": ["pink_gradient", "star_decoration", "soft_round"],
    },
    
    # ========== 风格11: 高端知识 ==========
    "高端知识": {
        "name": "高端知识",
        "name_en": "Premium Knowledge",
        "description": "知识付费、人物图谱、深度内容",
        "max_width": "677px",
        "container_margin": "0 auto",
        
        # 正文
        "body_font_size": "15px",
        "body_color": "#3d3d3d",
        "line_height": "2.0",
        "letter_spacing": "0.5px",
        "paragraph_margin": "0 0 20px 0",
        "text_indent": "2em",
        
        # 标题
        "h1_size": "24px",
        "h1_color": "#c4a35a",
        "h1_weight": "bold",
        "h1_align": "center",
        "h2_size": "18px",
        "h2_color": "#c4a35a",
        "h2_weight": "bold",
        "h3_size": "16px",
        "h3_color": "#8b7355",
        
        # 引用
        "quote_bg": "#f5f5f0",
        "quote_border": "#c4a35a",
        "quote_color": "#5a5a5a",
        "quote_size": "14px",
        
        # 强调
        "emphasis_color": "#c4a35a",
        
        # 分割线
        "divider_style": "diamond",
        
        # 卡片
        "card_bg": "#ffffff",
        "card_border": "#c4a35a",
        "card_radius": "50%",
        
        # 特色
        "primary_color": "#c4a35a",
        "secondary_color": "#f5f5f0",
        "features": ["person_card", "wave_divider", "keyword_highlight", "gold_accent"],
    },
}


def get_style_config(style_name):
    """
    获取指定风格的配置
    
    Args:
        style_name: 风格名称
        
    Returns:
        dict: 风格配置，如果不存在返回None
    """
    return STYLE_CONFIGS.get(style_name)


def list_styles():
    """
    列出所有可用风格
    
    Returns:
        list: 风格名称列表
    """
    return list(STYLE_CONFIGS.keys())


def add_style(name, config):
    """
    添加新风格（运行时添加，不持久化）
    
    Args:
        name: 风格名称
        config: 风格配置字典
    """
    STYLE_CONFIGS[name] = config


def remove_style(name):
    """
    移除风格（运行时移除，不持久化）
    
    Args:
        name: 风格名称
    """
    if name in STYLE_CONFIGS:
        del STYLE_CONFIGS[name]


# 导出所有配置供直接访问
__all__ = [
    'STYLE_CONFIGS',
    'get_style_config', 
    'list_styles',
    'add_style',
    'remove_style',
]
