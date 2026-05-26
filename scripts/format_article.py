# -*- coding: utf-8 -*-
"""
微信公众号排版脚本
功能：将Markdown格式的文章转换为微信公众号可用的HTML
支持11种排版风格

使用方法：
    from scripts.format_article import format_article
    
    html_output = format_article(markdown_text, "清新文艺")
"""

import re
import os
import sys

# 添加项目根目录到路径，以便导入style_configs
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from styles.style_configs import STYLE_CONFIGS, get_style_config


def get_divider(style_name, divider_style):
    """生成不同风格的分割线"""
    dividers = {
        # 中心圆点
        "center": '<p style="text-align:center;margin:40px 0;"><span style="display:inline-block;width:8px;height:8px;background:#d0d0d0;border-radius:50%;"></span><span style="display:inline-block;width:8px;height:8px;background:#d0d0d0;border-radius:50%;margin:0 8px;"></span><span style="display:inline-block;width:8px;height:8px;background:#d0d0d0;border-radius:50%;"></span></p>',
        
        # 经典星号（东方/复古）
        "classic": '<p style="text-align:center;margin:40px 0 32px 0;"><span style="display:inline-block;color:#c4a77d;font-size:16px;letter-spacing:8px;">❋ ❋ ❋</span></p>',
        
        # 专业虚线（商务）
        "professional": '<p style="border-top:1px dashed #d0d8e4;margin:32px 0;"></p>',
        
        # 温暖圆点
        "warm": '<p style="text-align:center;margin:36px 0;"><span style="display:inline-block;color:#e8c4b0;font-size:14px;letter-spacing:6px;">· · ·</span></p>',
        
        # 锐利直线
        "sharp": '<p style="border-top:2px solid #1a1a1a;margin:32px 0;"></p>',
        
        # 简洁细线
        "minimal": '<p style="border-top:1px solid #d0d0d0;margin:32px 0;"></p>',
        
        # 科技风
        "tech": '<p style="text-align:center;margin:32px 0;"><span style="display:inline-block;color:#00d4ff;font-size:12px;letter-spacing:4px;">━━ ◆ ━━</span></p>',
        
        # 自然风
        "nature": '<p style="text-align:center;margin:36px 0;"><span style="display:inline-block;color:#8bc34a;font-size:14px;">❀ ❀ ❀</span></p>',
        
        # Emoji装饰
        "emoji": '<p style="text-align:center;margin:32px 0;font-size:18px;">✨ ━━━━━ ✨</p>',
        
        # 可爱风
        "cute": '<p style="text-align:center;margin:32px 0;"><span style="display:inline-block;font-size:12px;color:#ff9a9e;letter-spacing:4px;">♡ ━━━ ♡ ━━━ ♡</span></p>',
        
        # 钻石装饰（高端知识）
        "diamond": '<p style="text-align:center;margin:40px 0 32px 0;"><span style="display:inline-block;color:#c4a35a;font-size:14px;letter-spacing:6px;">◆ ── ◆ ── ◆</span></p>',
        
        # 优雅风
        "elegant": '<p style="text-align:center;margin:32px 0;"><span style="display:inline-block;width:40px;height:1px;background:#d4af37;"></span><span style="display:inline-block;color:#d4af37;margin:0 12px;">◆</span><span style="display:inline-block;width:40px;height:1px;background:#d4af37;"></span></p>',
    }
    return dividers.get(divider_style, dividers["center"])


def parse_markdown(markdown_text):
    """
    解析Markdown文本，返回结构化数据
    
    Args:
        markdown_text: Markdown格式的文本
        
    Returns:
        list: 结构化的blocks列表
    """
    lines = markdown_text.split('\n')
    blocks = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # 跳过空行
        if not line.strip():
            i += 1
            continue
        
        # 标题处理
        if line.startswith('# '):
            blocks.append({'type': 'h1', 'content': line[2:].strip()})
        elif line.startswith('## '):
            blocks.append({'type': 'h2', 'content': line[3:].strip()})
        elif line.startswith('### '):
            blocks.append({'type': 'h3', 'content': line[4:].strip()})
        elif line.startswith('#### '):
            blocks.append({'type': 'h4', 'content': line[5:].strip()})
        
        # 引用块处理
        elif line.startswith('> '):
            quote_lines = []
            while i < len(lines) and (lines[i].startswith('> ') or not lines[i].strip()):
                if lines[i].startswith('> '):
                    quote_lines.append(lines[i][2:])
                elif lines[i].strip() == '':
                    quote_lines.append('')
                i += 1
            blocks.append({'type': 'quote', 'content': '\n'.join(quote_lines).strip()})
            continue
        
        # 图片处理
        elif line.startswith('![') and '(' in line:
            match = re.search(r'!\[(.*?)\]\((.*?)\)', line)
            if match:
                alt_text = match.group(1)
                url = match.group(2)
                blocks.append({'type': 'image', 'alt': alt_text, 'url': url})
        
        # 无序列表处理
        elif line.startswith('- ') or line.startswith('* '):
            list_items = []
            while i < len(lines) and (lines[i].startswith('- ') or lines[i].startswith('* ')):
                list_items.append(lines[i][2:].strip())
                i += 1
            blocks.append({'type': 'ul', 'items': list_items})
            continue
        
        # 有序列表处理
        elif re.match(r'^\d+\. ', line):
            list_items = []
            while i < len(lines) and re.match(r'^\d+\. ', lines[i]):
                list_items.append(re.sub(r'^\d+\. ', '', lines[i]).strip())
                i += 1
            blocks.append({'type': 'ol', 'items': list_items})
            continue
        
        # 分割线处理
        elif re.match(r'^---+$', line.strip()) or re.match(r'^\*\*\*+$', line.strip()):
            blocks.append({'type': 'divider'})
        
        # 特殊组件：人物卡片
        elif line.startswith(':::person'):
            card_content = []
            i += 1
            while i < len(lines) and not lines[i].startswith(':::'):
                card_content.append(lines[i])
                i += 1
            blocks.append({'type': 'person_card', 'content': '\n'.join(card_content)})
            continue
        
        # 特殊组件：关键词高亮
        elif line.startswith(':::highlight'):
            highlight_content = []
            i += 1
            while i < len(lines) and not lines[i].startswith(':::'):
                highlight_content.append(lines[i])
                i += 1
            blocks.append({'type': 'highlight', 'content': '\n'.join(highlight_content)})
            continue
        
        # 普通段落处理
        else:
            para_lines = [line]
            while i + 1 < len(lines) and lines[i + 1].strip() and not lines[i + 1].startswith(('#', '- ', '* ', '>', '![', ':::')):
                i += 1
                para_lines.append(lines[i])
            blocks.append({'type': 'p', 'content': ' '.join(para_lines)})
        
        i += 1
    
    return blocks


def parse_inline_styles(text):
    """
    解析行内样式：加粗、斜体、链接、关键词高亮等
    
    Args:
        text: 原始文本
        
    Returns:
        str: 处理后的HTML片段
    """
    # 关键词高亮 [[关键词]]
    text = re.sub(r'\[\[(.+?)\]\]', r'<span style="background:#fff3cd;padding:2px 6px;border-radius:4px;color:#c4a35a;font-weight:bold;">\1</span>', text)
    
    # 加粗 **text** 或 __text__
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'__(.+?)__', r'<strong>\1</strong>', text)
    
    # 斜体 *text* 或 _text_
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'_(.+?)_', r'<em>\1</em>', text)
    
    # 行内代码 `code`
    text = re.sub(r'`(.+?)`', r'<code style="background:#f5f5f5;padding:2px 4px;font-size:13px;border-radius:2px;">\1</code>', text)
    
    # 链接 [text](url)
    text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2" target="_blank" style="color:#3a5a8a;text-decoration:underline;">\1</a>', text)
    
    return text


def convert_to_html(blocks, style_name="清新文艺"):
    """
    将Markdown结构转换为HTML
    
    Args:
        blocks: parse_markdown返回的结构化数据
        style_name: 风格名称
        
    Returns:
        str: HTML代码
    """
    config = get_style_config(style_name)
    if not config:
        print(f"警告：未找到风格 '{style_name}'，使用默认风格 '清新文艺'")
        config = get_style_config("清新文艺")
    
    html_parts = []
    
    # 开始标签
    html_parts.append(f'<section style="margin:{config["container_margin"]};max-width:{config["max_width"]};">')
    
    for block in blocks:
        block_type = block['type']
        
        # ========== H1 标题 ==========
        if block_type == 'h1':
            content = parse_inline_styles(block['content'])
            align = config.get("h1_align", "center")
            if style_name == "活力创意":
                html_parts.append(
                    f'<h1 style="font-size:{config["h1_size"]};font-weight:{config["h1_weight"]};color:{config["h1_color"]};'
                    f'text-align:{align};letter-spacing:3px;margin:40px 0 30px 0;line-height:1.4;">{content}</h1>'
                )
            elif style_name == "高端知识":
                html_parts.append(
                    f'<h1 style="font-size:{config["h1_size"]};font-weight:{config["h1_weight"]};color:{config["h1_color"]};'
                    f'text-align:center;letter-spacing:4px;margin:40px 0 30px 0;line-height:1.5;padding-bottom:16px;border-bottom:2px solid {config["h1_color"]};display:inline-block;">{content}</h1>'
                )
            else:
                html_parts.append(
                    f'<h1 style="font-size:{config["h1_size"]};font-weight:{config["h1_weight"]};color:{config["h1_color"]};'
                    f'text-align:{align};letter-spacing:2px;margin:40px 0 30px 0;line-height:1.5;">{content}</h1>'
                )
        
        # ========== H2 标题 ==========
        elif block_type == 'h2':
            content = parse_inline_styles(block['content'])
            
            if style_name == "高端知识":
                html_parts.append(
                    f'<h2 style="font-size:{config["h2_size"]};font-weight:{config["h2_weight"]};color:{config["h2_color"]};'
                    f'margin:40px 0 20px 0;text-align:center;letter-spacing:3px;">◆ {content} ◆</h2>'
                )
            elif style_name == "活力创意":
                html_parts.append(
                    f'<h2 style="font-size:{config["h2_size"]};font-weight:{config["h2_weight"]};color:{config["h2_color"]};'
                    f'margin:32px 0 16px 0;padding:8px 16px;background:#fff5f5;'
                    f'border-left:4px solid {config["h2_color"]};line-height:1.4;">{content}</h2>'
                )
            elif style_name == "清新文艺":
                html_parts.append(
                    f'<h2 style="font-size:{config["h2_size"]};font-weight:{config["h2_weight"]};color:{config["h2_color"]};'
                    f'margin:36px 0 20px 0;text-align:center;letter-spacing:2px;">🌿 {content} 🌿</h2>'
                )
            elif style_name == "科技未来":
                html_parts.append(
                    f'<h2 style="font-size:{config["h2_size"]};font-weight:{config["h2_weight"]};color:{config["h2_color"]};'
                    f'margin:32px 0 16px 0;padding-left:20px;border-left:3px solid {config["h2_color"]};'
                    f'line-height:1.4;">{content}</h2>'
                )
            elif style_name == "甜美少女":
                html_parts.append(
                    f'<h2 style="font-size:{config["h2_size"]};font-weight:{config["h2_weight"]};color:{config["h2_color"]};'
                    f'margin:36px 0 20px 0;text-align:center;letter-spacing:2px;">♡ {content} ♡</h2>'
                )
            else:
                html_parts.append(
                    f'<h2 style="font-size:{config["h2_size"]};font-weight:{config["h2_weight"]};color:{config["h2_color"]};'
                    f'margin:36px 0 20px 0;padding-left:16px;border-left:3px solid {config["h2_color"]};line-height:1.4;">{content}</h2>'
                )
        
        # ========== H3 标题 ==========
        elif block_type == 'h3':
            content = parse_inline_styles(block['content'])
            
            if style_name == "高端知识":
                html_parts.append(
                    f'<h3 style="font-size:{config["h3_size"]};font-weight:600;color:{config["h3_color"]};'
                    f'margin:28px 0 14px 0;padding-left:14px;border-left:2px solid {config["h3_color"]};'
                    f'letter-spacing:1px;line-height:1.4;">{content}</h3>'
                )
            elif style_name == "活力创意":
                html_parts.append(
                    f'<h3 style="font-size:{config["h3_size"]};font-weight:bold;color:{config["h3_color"]};'
                    f'margin:24px 0 12px 0;line-height:1.4;">◆ {content}</h3>'
                )
            else:
                html_parts.append(
                    f'<h3 style="font-size:{config["h3_size"]};font-weight:600;color:{config["h3_color"]};'
                    f'margin:28px 0 12px 0;line-height:1.4;">{content}</h3>'
                )
        
        # ========== H4 标题 ==========
        elif block_type == 'h4':
            content = parse_inline_styles(block['content'])
            html_parts.append(
                f'<h4 style="font-size:15px;font-weight:600;color:{config["h3_color"]};'
                f'margin:24px 0 10px 0;line-height:1.4;">{content}</h4>'
            )
        
        # ========== 段落 ==========
        elif block_type == 'p':
            content = parse_inline_styles(block['content'])
            text_indent = config.get("text_indent", "0")
            html_parts.append(
                f'<p style="font-size:{config["body_font_size"]};color:{config["body_color"]};'
                f'text-align:justify;line-height:{config["line_height"]};margin:{config["paragraph_margin"]};'
                f'letter-spacing:{config["letter_spacing"]};text-indent:{text_indent};">{content}</p>'
            )
        
        # ========== 引用块 ==========
        elif block_type == 'quote':
            content = parse_inline_styles(block['content'].replace('\n', '<br/>'))
            
            if style_name == "高端知识":
                html_parts.append(
                    f'<blockquote style="margin:28px 0;padding:20px 24px;background:{config["quote_bg"]};'
                    f'border-radius:8px;border:1px solid #e0e0e0;">'
                    f'<p style="font-size:{config["quote_size"]};color:{config["quote_color"]};line-height:1.9;margin:0;'
                    f'text-align:center;font-style:italic;">「{content}」</p></blockquote>'
                )
            elif style_name == "温柔治愈":
                html_parts.append(
                    f'<blockquote style="margin:28px 0;padding:20px 24px;background:{config["quote_bg"]};'
                    f'border-radius:16px;border:1px solid #f0e0e0;">'
                    f'<p style="font-size:{config["quote_size"]};color:{config["quote_color"]};line-height:1.9;margin:0;'
                    f'text-align:center;font-style:italic;">「{content}」</p></blockquote>'
                )
            elif style_name == "活力创意":
                html_parts.append(
                    f'<blockquote style="margin:24px 0;padding:16px 20px;background:{config["quote_bg"]};'
                    f'border-left:4px solid {config["quote_border"]};border-radius:0 8px 8px 0;">'
                    f'<p style="font-size:{config["quote_size"]};color:{config["quote_color"]};line-height:1.8;margin:0;font-weight:500;">'
                    f'「{content}」</p></blockquote>'
                )
            elif style_name == "科技未来":
                html_parts.append(
                    f'<blockquote style="margin:24px 0;padding:16px 20px;background:{config["quote_bg"]};'
                    f'border:1px solid {config["quote_border"]};border-radius:4px;">'
                    f'<p style="font-size:{config["quote_size"]};color:{config["quote_color"]};line-height:1.8;margin:0;">'
                    f'// {content}</p></blockquote>'
                )
            else:
                html_parts.append(
                    f'<blockquote style="margin:24px 0;padding:16px 20px;background:{config["quote_bg"]};'
                    f'border-left:3px solid {config["quote_border"]};">'
                    f'<p style="font-size:{config["quote_size"]};color:{config["quote_color"]};line-height:1.8;margin:0;">'
                    f'{content}</p></blockquote>'
                )
        
        # ========== 无序列表 ==========
        elif block_type == 'ul':
            list_html = '<ul style="margin:24px 0;padding-left:0;list-style-type:none;">'
            
            for item in block['items']:
                item = parse_inline_styles(item)
                
                if style_name == "活力创意":
                    list_html += f'<li style="font-size:15px;color:{config["body_color"]};line-height:1.9;margin:0 0 14px 0;' \
                                f'padding:12px 16px;background:#fff;border-radius:8px;border:1px solid #f0f0f0;">' \
                                f'🔸 {item}</li>'
                elif style_name == "高端知识":
                    list_html += f'<li style="font-size:14px;color:{config["body_color"]};line-height:1.9;margin:0 0 12px 0;">' \
                                f'<span style="color:#c4a35a;">◆ </span>{item}</li>'
                elif style_name == "清新文艺":
                    list_html += f'<li style="font-size:14px;color:{config["body_color"]};line-height:1.9;margin:0 0 12px 0;">' \
                                f'<span style="color:#81c784;font-size:16px;">❀ </span>{item}</li>'
                elif style_name == "甜美少女":
                    list_html += f'<li style="font-size:14px;color:#7a7a7a;line-height:1.9;margin:0 0 12px 0;">' \
                                f'<span style="color:#ff9a9e;font-size:14px;">♡ </span>{item}</li>'
                elif style_name == "科技未来":
                    list_html += f'<li style="font-size:14px;color:{config["body_color"]};line-height:1.8;margin:0 0 10px 0;">' \
                                f'<span style="color:#00d4ff;">▸ </span>{item}</li>'
                else:
                    list_html += f'<li style="font-size:{config["body_font_size"]};color:{config["body_color"]};line-height:{config["line_height"]};' \
                                f'margin:0 0 12px 0;">' \
                                f'<span style="color:#888888;">· </span>{item}</li>'
            
            list_html += '</ul>'
            html_parts.append(list_html)
        
        # ========== 有序列表 ==========
        elif block_type == 'ol':
            list_html = '<ol style="margin:24px 0;padding-left:0;list-style-type:none;">'
            
            for idx, item in enumerate(block['items'], 1):
                item = parse_inline_styles(item)
                
                if style_name == "活力创意":
                    if idx == len(block['items']):
                        list_html += f'<li style="font-size:15px;color:{config["body_color"]};line-height:1.9;margin:0 0 14px 0;' \
                                    f'padding:14px 18px;background:#fff;border:2px solid {config["primary_color"]};border-radius:8px;font-weight:600;color:{config["primary_color"]};">' \
                                    f'<span style="display:inline-block;width:28px;height:28px;background:{config["primary_color"]};color:#fff;text-align:center;' \
                                    f'line-height:28px;font-size:14px;margin-right:12px;border-radius:50%;">{idx}</span>{item}</li>'
                    else:
                        list_html += f'<li style="font-size:15px;color:{config["body_color"]};line-height:1.9;margin:0 0 14px 0;' \
                                    f'padding:14px 18px;background:#fff;border:2px solid #e0e0e0;border-radius:8px;font-weight:600;">' \
                                    f'<span style="display:inline-block;width:28px;height:28px;background:#e0e0e0;color:#666;text-align:center;' \
                                    f'line-height:28px;font-size:14px;margin-right:12px;border-radius:50%;">{idx}</span>{item}</li>'
                elif style_name == "高端知识":
                    list_html += f'<li style="font-size:14px;color:{config["body_color"]};line-height:1.9;margin:0 0 12px 0;' \
                                f'padding:12px 16px;background:{config["quote_bg"]};border-left:3px solid {config["primary_color"]};">' \
                                f'<span style="display:inline-block;width:22px;height:22px;background:{config["primary_color"]};color:#fff;text-align:center;' \
                                f'line-height:22px;font-size:12px;margin-right:12px;border-radius:2px;">{idx}</span>{item}</li>'
                else:
                    list_html += f'<li style="font-size:{config["body_font_size"]};color:{config["body_color"]};line-height:{config["line_height"]};' \
                                f'margin:0 0 12px 0;">' \
                                f'<span style="color:#888888;">{idx}. </span>{item}</li>'
            
            list_html += '</ol>'
            html_parts.append(list_html)
        
        # ========== 图片 ==========
        elif block_type == 'image':
            alt = block.get('alt', '')
            url = block.get('url', '')
            
            if style_name == "高端知识":
                html_parts.append(
                    f'<p style="text-align:center;margin:24px 0;">'
                    f'<img src="{url}" alt="{alt}" style="max-width:100%;border:1px solid #e0e0e0;" />'
                    f'</p><p style="font-size:12px;color:#999999;text-align:center;margin:0 0 28px 0;letter-spacing:1px;">'
                    f'◇ {alt} ◇</p>'
                )
            elif style_name == "温柔治愈":
                html_parts.append(
                    f'<p style="text-align:center;margin:24px 0;">'
                    f'<img src="{url}" alt="{alt}" style="max-width:100%;border-radius:16px;border:1px solid #f0f0f0;" />'
                    f'</p><p style="font-size:12px;color:#aaaaaa;text-align:center;margin:0 0 28px 0;letter-spacing:0.5px;">'
                    f'🌿 {alt}</p>'
                )
            elif style_name == "清新文艺":
                html_parts.append(
                    f'<p style="text-align:center;margin:24px 0;">'
                    f'<img src="{url}" alt="{alt}" style="max-width:100%;border-radius:8px;border:1px solid #e0e0e0;" />'
                    f'</p><p style="font-size:12px;color:#888888;text-align:center;margin:0 0 28px 0;letter-spacing:0.5px;">'
                    f'{alt}</p>'
                )
            else:
                html_parts.append(
                    f'<p style="text-align:center;margin:24px 0;">'
                    f'<img src="{url}" alt="{alt}" style="max-width:100%;border-radius:4px;" />'
                    f'</p><p style="font-size:12px;color:#999999;text-align:center;margin:0 0 24px 0;">{alt}</p>'
                )
        
        # ========== 分割线 ==========
        elif block_type == 'divider':
            html_parts.append(get_divider(style_name, config["divider_style"]))
        
        # ========== 人物卡片（高端知识风格） ==========
        elif block_type == 'person_card':
            html_parts.append(block['content'])  # 保持原始HTML
            continue
        
        # ========== 关键词高亮 ==========
        elif block_type == 'highlight':
            content = parse_inline_styles(block['content'])
            html_parts.append(
                f'<p style="font-size:{config["body_font_size"]};color:{config["body_color"]};'
                f'line-height:{config["line_height"]};margin:{config["paragraph_margin"]};'
                f'text-align:center;letter-spacing:{config["letter_spacing"]};">{content}</p>'
            )
            continue
    
    # 结束标签
    html_parts.append('<p style="height:40px;"></p>')
    html_parts.append('</section>')
    
    return '\n'.join(html_parts)


def format_article(markdown_text, style_name="清新文艺", extracted_config=None):
    """
    主函数：将Markdown格式的文章转换为微信公众号HTML
    
    Args:
        markdown_text: Markdown格式的文章内容
        style_name: 排版风格名称
        extracted_config: 可选的提取配置（用于自定义风格）
    
    Returns:
        str: 排版后的HTML代码，可直接粘贴到微信公众号编辑器
    """
    # 如果有提取的配置，使用提取的配置覆盖
    if extracted_config:
        # 临时添加自定义配置
        custom_style_name = extracted_config.get("name", "自定义风格")
        STYLE_CONFIGS[custom_style_name] = extracted_config
        style_name = custom_style_name
    
    if style_name not in STYLE_CONFIGS:
        print(f"警告：未找到风格 '{style_name}'，使用默认风格 '清新文艺'")
        style_name = "清新文艺"
    
    blocks = parse_markdown(markdown_text)
    html = convert_to_html(blocks, style_name)
    return html


def format_file(input_file, output_file, style_name="清新文艺"):
    """
    处理文件：将输入的Markdown文件转换为HTML并保存
    
    Args:
        input_file: 输入的Markdown文件路径
        output_file: 输出的HTML文件路径
        style_name: 排版风格名称
    """
    if not os.path.exists(input_file):
        print(f"错误：输入文件不存在 '{input_file}'")
        return
    
    with open(input_file, 'r', encoding='utf-8') as f:
        markdown_text = f.read()
    
    html = format_article(markdown_text, style_name)
    
    # 添加完整HTML包装（可选，用于本地预览）
    full_html = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>微信公众号排版预览</title>
    <style>
        body {{ margin: 0; padding: 20px; background: #f5f5f5; }}
        .preview-container {{ max-width: 677px; margin: 0 auto; background: #fff; padding: 20px; }}
    </style>
</head>
<body>
    <div class="preview-container">
        {html}
    </div>
</body>
</html>'''
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"转换完成！")
    print(f"输入文件: {input_file}")
    print(f"输出文件: {output_file}")
    print(f"使用风格: {style_name}")


def list_styles():
    """列出所有可用的排版风格"""
    print("=" * 60)
    print("可用的排版风格：")
    print("=" * 60)
    
    descriptions = {
        "极简商务": "企业号、职场干货、行业分析",
        "清新文艺": "生活方式、读书分享、慢节奏内容",
        "活力创意": "年轻品牌、活动推广、娱乐内容",
        "高端质感": "奢侈品、高端品牌、精品内容",
        "复古优雅": "文化历史、怀旧主题、古典风格",
        "科技未来": "科技、AI、互联网、数字主题",
        "温柔治愈": "情感心理、生活感悟、陪伴内容",
        "杂志编辑": "时尚美妆、潮流内容、高颜值排版",
        "自然生态": "环保户外、健康生活、绿色主题",
        "甜美少女": "美妆穿搭、少女心、可爱风格",
        "高端知识": "知识付费、人物图谱、深度内容",
    }
    
    for idx, style in enumerate(STYLE_CONFIGS.keys(), 1):
        desc = descriptions.get(style, STYLE_CONFIGS[style].get("description", ""))
        primary = STYLE_CONFIGS[style].get("primary_color", "#000")
        print(f"{idx:2d}. {style}")
        print(f"    配色: {primary} | {desc}")
        print()


def show_style_preview(style_name):
    """显示指定风格的预览信息"""
    config = get_style_config(style_name)
    if not config:
        print(f"错误：未找到风格 '{style_name}'")
        return
    
    print(f"\n{'=' * 50}")
    print(f"风格: {style_name}")
    print(f"{'=' * 50}")
    print(f"配色: {config.get('primary_color', '#000')}")
    print(f"最大宽度: {config.get('max_width', '677px')}")
    print(f"正文字号: {config.get('body_font_size', '15px')}")
    print(f"行高: {config.get('line_height', '2.0')}")
    print(f"特色: {', '.join(config.get('features', []))}")
    print()


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='微信公众号排版工具')
    parser.add_argument('--list', action='store_true', help='列出所有可用风格')
    parser.add_argument('--input', type=str, help='输入的Markdown文件')
    parser.add_argument('--output', type=str, help='输出的HTML文件')
    parser.add_argument('--style', type=str, default='清新文艺', help='排版风格')
    parser.add_argument('--preview', type=str, help='预览指定风格的详情')
    
    args = parser.parse_args()
    
    if args.list:
        list_styles()
    elif args.preview:
        show_style_preview(args.preview)
    elif args.input and args.output:
        format_file(args.input, args.output, args.style)
    elif args.input:
        # 输出到stdout
        with open(args.input, 'r', encoding='utf-8') as f:
            markdown_text = f.read()
        html = format_article(markdown_text, args.style)
        print(html)
    else:
        # 显示帮助信息
        print("""
╔════════════════════════════════════════════════════════════╗
║          微信公众号排版工具 v2.0.0                         ║
╠════════════════════════════════════════════════════════════╣
║  功能：将Markdown转换为微信公众号可用的HTML                ║
║  用法：python format_article.py [选项]                     ║
╠════════════════════════════════════════════════════════════╣
║  命令行选项：                                              ║
║    --list          列出所有可用风格                         ║
║    --preview <名>  预览指定风格的详情                       ║
║    --input <file>  输入的Markdown文件                       ║
║    --output <file> 输出的HTML文件                          ║
║    --style <name>  排版风格（默认：清新文艺）               ║
║                                                         ║
║  可用风格：                                               ║
║    极简商务 | 清新文艺 | 活力创意 | 高端质感 | 复古优雅    ║
║    科技未来 | 温柔治愈 | 杂志编辑 | 自然生态 | 甜美少女     ║
║    高端知识                                               ║
║                                                         ║
║  示例：                                                   ║
║    python format_article.py --list                         ║
║    python format_article.py --input article.md --style 高端知识 ║
╚════════════════════════════════════════════════════════════╝
        """)
