#!/usr/bin/env python3
"""
Script para sincronizar posts do Notion para Jekyll
Converte páginas do Notion em arquivos Markdown compatíveis com Jekyll
"""

import os
import re
from datetime import datetime
from notion_client import Client
import requests

# Configuração
NOTION_TOKEN = os.environ.get('NOTION_TOKEN')
NOTION_DATABASE_ID = os.environ.get('NOTION_DATABASE_ID')
POSTS_DIR = '_posts'  # Pasta padrão do Jekyll para posts

# Inicializar cliente Notion
notion = Client(auth=NOTION_TOKEN)


def sanitize_filename(text):
    """Sanitiza texto para usar como nome de arquivo"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')


def download_image(url, folder='assets/images'):
    """Baixa imagem e retorna o path local"""
    os.makedirs(folder, exist_ok=True)
    
    filename = url.split('/')[-1].split('?')[0]
    if not filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):
        filename += '.jpg'
    
    filepath = os.path.join(folder, filename)
    
    # Baixar imagem
    response = requests.get(url)
    if response.status_code == 200:
        with open(filepath, 'wb') as f:
            f.write(response.content)
        return '/' + filepath
    
    return url  # Retorna URL original se falhar


def block_to_markdown(block, level=0):
    """Converte um bloco do Notion para Markdown"""
    block_type = block['type']
    content = []
    
    try:
        if block_type == 'paragraph':
            text = rich_text_to_markdown(block['paragraph']['rich_text'])
            if text:
                content.append(text)
        
        elif block_type == 'heading_1':
            text = rich_text_to_markdown(block['heading_1']['rich_text'])
            content.append(f"# {text}")
        
        elif block_type == 'heading_2':
            text = rich_text_to_markdown(block['heading_2']['rich_text'])
            content.append(f"## {text}")
        
        elif block_type == 'heading_3':
            text = rich_text_to_markdown(block['heading_3']['rich_text'])
            content.append(f"### {text}")
        
        elif block_type == 'bulleted_list_item':
            text = rich_text_to_markdown(block['bulleted_list_item']['rich_text'])
            indent = '  ' * level
            content.append(f"{indent}- {text}")
        
        elif block_type == 'numbered_list_item':
            text = rich_text_to_markdown(block['numbered_list_item']['rich_text'])
            indent = '  ' * level
            content.append(f"{indent}1. {text}")
        
        elif block_type == 'code':
            code_text = rich_text_to_markdown(block['code']['rich_text'])
            language = block['code'].get('language', '')
            content.append(f"```{language}\n{code_text}\n```")
        
        elif block_type == 'quote':
            text = rich_text_to_markdown(block['quote']['rich_text'])
            content.append(f"> {text}")
        
        elif block_type == 'image':
            image_url = block['image'].get('file', {}).get('url') or \
                       block['image'].get('external', {}).get('url')
            if image_url:
                # Baixar imagem localmente
                local_path = download_image(image_url)
                caption = rich_text_to_markdown(block['image'].get('caption', []))
                if caption:
                    content.append(f"![{caption}]({local_path})")
                else:
                    content.append(f"![]({local_path})")
        
        elif block_type == 'divider':
            content.append("---")
    
    except Exception as e:
        print(f"Erro ao processar bloco {block_type}: {e}")
    
    return '\n'.join(content)


def rich_text_to_markdown(rich_text_array):
    """Converte rich text do Notion para Markdown"""
    result = []
    
    for text_obj in rich_text_array:
        text = text_obj.get('plain_text', '')
        annotations = text_obj.get('annotations', {})
        
        # Aplicar formatação
        if annotations.get('bold'):
            text = f"**{text}**"
        if annotations.get('italic'):
            text = f"*{text}*"
        if annotations.get('code'):
            text = f"`{text}`"
        if annotations.get('strikethrough'):
            text = f"~~{text}~~"
        
        # Link
        if text_obj.get('href'):
            text = f"[{text}]({text_obj['href']})"
        
        result.append(text)
    
    return ''.join(result)


def get_page_content(page_id):
    """Obtém todo o conteúdo de uma página do Notion"""
    blocks = []
    has_more = True
    start_cursor = None
    
    while has_more:
        response = notion.blocks.children.list(
            block_id=page_id,
            start_cursor=start_cursor
        )
        blocks.extend(response['results'])
        has_more = response['has_more']
        start_cursor = response.get('next_cursor')
    
    markdown_content = []
    for block in blocks:
        md = block_to_markdown(block)
        if md:
            markdown_content.append(md)
    
    return '\n\n'.join(markdown_content)


def get_property_value(properties, prop_name):
    """Extrai valor de uma propriedade do Notion"""
    prop = properties.get(prop_name, {})
    prop_type = prop.get('type')
    
    if prop_type == 'title':
        return ''.join([t['plain_text'] for t in prop['title']])
    elif prop_type == 'rich_text':
        return ''.join([t['plain_text'] for t in prop['rich_text']])
    elif prop_type == 'date':
        date_obj = prop.get('date')
        return date_obj['start'] if date_obj else None
    elif prop_type == 'checkbox':
        return prop.get('checkbox', False)
    elif prop_type == 'multi_select':
        return [item['name'] for item in prop.get('multi_select', [])]
    elif prop_type == 'select':
        select_obj = prop.get('select')
        return select_obj['name'] if select_obj else None
    
    return None


def sync_notion_to_jekyll():
    """Sincroniza posts do Notion para Jekyll"""
    print("🔄 Iniciando sincronização Notion → Jekyll...")
    
    # Criar pasta de posts se não existir
    os.makedirs(POSTS_DIR, exist_ok=True)
    
    # Buscar todos os posts publicados do Notion
    response = notion.databases.query(
        database_id=NOTION_DATABASE_ID,
        filter={
            "property": "Published",
            "checkbox": {
                "equals": True
            }
        }
    )
    
    posts_synced = 0
    
    for page in response['results']:
        try:
            properties = page['properties']
            
            # Extrair dados
            title = get_property_value(properties, 'Title') or get_property_value(properties, 'Name')
            slug = get_property_value(properties, 'Slug')
            date = get_property_value(properties, 'Date')
            tags = get_property_value(properties, 'Tags') or []
            
            if not title:
                print(f"⚠️  Post sem título, pulando...")
                continue
            
            # Gerar slug se não existir
            if not slug:
                slug = sanitize_filename(title)
            
            # Usar data atual se não especificada
            if not date:
                date = datetime.now().strftime('%Y-%m-%d')
            
            # Obter conteúdo
            content = get_page_content(page['id'])
            
            # Criar frontmatter Jekyll
            frontmatter = f"""---
layout: post
title: "{title}"
date: {date}
"""
            if tags:
                frontmatter += f"tags: [{', '.join(tags)}]\n"
            
            frontmatter += "---\n\n"
            
            # Nome do arquivo Jekyll: YYYY-MM-DD-slug.md
            date_prefix = date.split('T')[0]  # Pega apenas YYYY-MM-DD
            filename = f"{date_prefix}-{slug}.md"
            filepath = os.path.join(POSTS_DIR, filename)
            
            # Escrever arquivo
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(frontmatter)
                f.write(content)
            
            print(f"✅ Post sincronizado: {filename}")
            posts_synced += 1
        
        except Exception as e:
            print(f"❌ Erro ao processar post: {e}")
            continue
    
    print(f"\n🎉 Sincronização completa! {posts_synced} posts sincronizados.")


if __name__ == '__main__':
    if not NOTION_TOKEN or not NOTION_DATABASE_ID:
        print("❌ NOTION_TOKEN ou NOTION_DATABASE_ID não configurados!")
        exit(1)
    
    sync_notion_to_jekyll()
