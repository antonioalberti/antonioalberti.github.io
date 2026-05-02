#!/usr/bin/env python3
"""
Script para gerar versão HTML estática do site para preview.
Compila os templates Jekyll manualmente.
"""

import os
import re
import yaml
from datetime import datetime

def load_config():
    """Carrega configuração do Jekyll"""
    with open('_config.yml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def load_i18n():
    """Carrega traduções"""
    with open('_data/i18n.yml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def read_file(path):
    """Lê arquivo"""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return None

def process_liquid_template(content, variables):
    """Processa templates Liquid básicos"""
    # Substituir variáveis simples {{ var }}
    def replace_var(match):
        var_path = match.group(1).strip()
        keys = var_path.split('.')
        value = variables
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return match.group(0)
        return str(value) if value is not None else ''
    
    content = re.sub(r'\{\{\s*([^\}]+)\s*\}\}', replace_var, content)
    
    # Processar assign
    content = re.sub(r'\{%\s*assign\s+\w+\s*=\s*[^\}]+\s*%\}', '', content)
    
    # Processar for loops básicos
    def process_for(match):
        var_name = match.group(1)
        collection_path = match.group(2).strip()
        loop_content = match.group(3)
        
        keys = collection_path.split('.')
        collection = variables
        for key in keys:
            if isinstance(collection, dict) and key in collection:
                collection = collection[key]
            else:
                return ''
        
        if not isinstance(collection, list):
            return ''
        
        result = ''
        for item in collection:
            item_vars = variables.copy()
            item_vars[var_name] = item
            item_html = loop_content
            # Substituir item.property
            for prop_match in re.finditer(r'\{\{\s*' + var_name + r'\.([^\}]+)\s*\}\}', item_html):
                prop = prop_match.group(1).strip()
                if isinstance(item, dict) and prop in item:
                    item_html = item_html.replace(prop_match.group(0), str(item[prop]))
                else:
                    item_html = item_html.replace(prop_match.group(0), '')
            result += item_html
        
        return result
    
    content = re.sub(r'\{%\s*for\s+(\w+)\s+in\s+([^\}]+)\s*%\}(.*?)\{%\s*endfor\s*%\}', process_for, content, flags=re.DOTALL)
    
    # Processar case/when
    def process_case(match):
        var_path = match.group(1).strip()
        cases = match.group(2)
        
        keys = var_path.split('.')
        value = variables
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                value = None
                break
        
        # Procurar when correspondente
        when_pattern = r'\{%\s*when\s+([^\}]+)\s*%\}(.*?)(?=\{%\s*when|\{%\s*else|\{%\s*endcase)'
        else_pattern = r'\{%\s*else\s*%\}(.*?)\{%\s*endcase'
        
        for when_match in re.finditer(when_pattern, cases, re.DOTALL):
            when_values = [v.strip().strip('"\'') for v in when_match.group(1).split('or')]
            if str(value) in when_values:
                return when_match.group(2)
        
        # Procurar else
        else_match = re.search(else_pattern, cases, re.DOTALL)
        if else_match:
            return else_match.group(1)
        
        return ''
    
    content = re.sub(r'\{%\s*case\s+([^\}]+)\s*%\}(.*?)\{%\s*endcase\s*%\}', process_case, content, flags=re.DOTALL)
    
    # Remover outros tags Liquid
    content = re.sub(r'\{%\s*[^\}]+\s*%\}', '', content)
    
    return content

def build_page(page_file, config, i18n, layout_content):
    """Constrói uma página HTML completa"""
    # Ler front matter e conteúdo
    with open(page_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extrair front matter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            front_matter = yaml.safe_load(parts[1])
            page_content = parts[2]
        else:
            front_matter = {}
            page_content = content
    else:
        front_matter = {}
        page_content = content
    
    lang = front_matter.get('lang', 'en')
    t = i18n.get(lang, i18n.get('en', {}))
    
    # Variáveis para substituição
    variables = {
        'site': config,
        'page': front_matter,
        't': t,
        'content': page_content
    }
    
    # Processar conteúdo da página
    processed_content = process_liquid_template(page_content, variables)
    
    # Inserir no layout
    variables['content'] = processed_content
    html = process_liquid_template(layout_content, variables)
    
    return html

def main():
    print("=" * 60)
    print("BUILD DO SITE ESTÁTICO")
    print("=" * 60)
    
    config = load_config()
    i18n = load_i18n()
    layout = read_file('_layouts/default.html')
    
    if not layout:
        print("ERRO: Layout não encontrado!")
        return
    
    # Criar diretório de saída
    os.makedirs('_site', exist_ok=True)
    os.makedirs('_site/pt', exist_ok=True)
    os.makedirs('_site/es', exist_ok=True)
    
    # Copiar assets
    import shutil
    if os.path.exists('assets'):
        if os.path.exists('_site/assets'):
            shutil.rmtree('_site/assets')
        shutil.copytree('assets', '_site/assets')
    
    # Construir páginas
    pages = [
        ('index.html', 'index.html'),
        ('pt/index.html', 'pt/index.html'),
        ('es/index.html', 'es/index.html')
    ]
    
    for src, dst in pages:
        print(f"Construindo: {src} -> _site/{dst}")
        html = build_page(src, config, i18n, layout)
        
        # Ajustar caminhos relativos
        depth = dst.count('/')
        prefix = '../' * depth if depth > 0 else './'
        html = html.replace('href="/', f'href="{prefix}')
        html = html.replace('src="/', f'src="{prefix}')
        
        # Ajustar links de idioma
        if depth == 0:
            html = html.replace('href="./"', 'href="./index.html"')
            html = html.replace('href="./pt/"', 'href="./pt/index.html"')
            html = html.replace('href="./es/"', 'href="./es/index.html"')
        elif depth == 1:
            html = html.replace('href="../"', 'href="../index.html"')
            html = html.replace('href="../pt/"', 'href="./index.html"')
            html = html.replace('href="../es/"', 'href="../es/index.html"')
        
        with open(f'_site/{dst}', 'w', encoding='utf-8') as f:
            f.write(html)
    
    print("")
    print("=" * 60)
    print("BUILD CONCLUÍDO!")
    print("=" * 60)
    print("")
    print("Arquivos gerados em: _site/")
    print("")
    print("Para visualizar, abra: _site/index.html")
    print("")

if __name__ == "__main__":
    main()