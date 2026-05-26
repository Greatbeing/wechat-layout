# -*- coding: utf-8 -*-
"""
wechat-layout - 微信公众号AI排版设计器

提供Markdown到微信公众号HTML的转换功能，支持11种预设风格，
以及从微信公众号文章自动提取排版风格的功能。
"""

__version__ = "2.1.0"
__author__ = "wechat-layout contributors"

# 导入核心函数方便使用
from scripts.format_article import format_article, list_styles
from scripts.extract_style import extract_style_from_url, add_style_to_library
from styles.style_configs import STYLE_CONFIGS, get_style_config

__all__ = [
    "format_article",
    "list_styles",
    "extract_style_from_url",
    "add_style_to_library",
    "STYLE_CONFIGS",
    "get_style_config",
]
