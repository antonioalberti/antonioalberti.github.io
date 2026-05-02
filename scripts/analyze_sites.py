#!/usr/bin/env python3
"""
Script para analisar sites de referência e extrair conteúdo relevante
para o novo website do Dr. Antonio Alberti.
"""

import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime
from urllib.parse import urljoin, urlparse

def log_message(message):
    """Registra mensagem no log"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"
    print(log_entry.strip())
    
    # Adicionar ao log geral
    with open("logs/progress.log", "a", encoding="utf-8") as f:
        f.write(log_entry)
    
    return log_entry

def fetch_page(url):
    """Busca uma página web e retorna o conteúdo HTML"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.0'
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        return response.text
    except Exception as e:
        log_message(f"ERRO ao buscar {url}: {str(e)}")
        return None

def extract_text_content(html, url):
    """Extrai texto relevante de uma página HTML"""
    if not html:
        return None
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # Remover scripts e styles
    for script in soup(["script", "style", "nav", "footer"]):
        script.decompose()
    
    # Extrair título
    title = soup.find('title')
    title_text = title.get_text().strip() if title else "Sem título"
    
    # Extrair headings e parágrafos
    content = {
        'url': url,
        'title': title_text,
        'headings': [],
        'paragraphs': [],
        'links': []
    }
    
    # Extrair headings
    for h in soup.find_all(['h1', 'h2', 'h3', 'h4']):
        text = h.get_text().strip()
        if text:
            content['headings'].append({
                'level': h.name,
                'text': text
            })
    
    # Extrair parágrafos
    for p in soup.find_all('p'):
        text = p.get_text().strip()
        if text and len(text) > 20:  # Filtrar parágrafos muito curtos
            content['paragraphs'].append(text)
    
    # Extrair links importantes
    for a in soup.find_all('a', href=True):
        href = a['href']
        text = a.get_text().strip()
        if text and len(text) > 2:
            full_url = urljoin(url, href)
            content['links'].append({
                'text': text,
                'url': full_url
            })
    
    return content

def analyze_leeds_page():
    """Analisa a página da Universidade de Leeds"""
    url = "https://eps.leeds.ac.uk/computing/staff/15735/dr-antonio-alberti"
    log_message(f"Analisando página da Universidade de Leeds: {url}")
    
    html = fetch_page(url)
    if html:
        content = extract_text_content(html, url)
        if content:
            # Salvar análise
            output_file = "logs/leeds_page_analysis.json"
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(content, f, ensure_ascii=False, indent=2)
            log_message(f"Análise da Leeds salva em {output_file}")
            return content
    
    return None

def analyze_current_website():
    """Analisa o site atual antonioalberti.com"""
    url = "https://antonioalberti.com"
    log_message(f"Analisando site atual: {url}")
    
    html = fetch_page(url)
    if html:
        content = extract_text_content(html, url)
        if content:
            # Salvar análise
            output_file = "logs/current_website_analysis.json"
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(content, f, ensure_ascii=False, indent=2)
            log_message(f"Análise do site atual salva em {output_file}")
            return content
    
    return None

def analyze_reference_site():
    """Analisa o site de referência com proporções de Fibonacci"""
    url = "https://people.idsia.ch/~juergen/"
    log_message(f"Analisando site de referência (Fibonacci): {url}")
    
    html = fetch_page(url)
    if html:
        content = extract_text_content(html, url)
        if content:
            # Salvar análise
            output_file = "logs/reference_site_analysis.json"
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(content, f, ensure_ascii=False, indent=2)
            log_message(f"Análise do site de referência salva em {output_file}")
            return content
    
    return None

def generate_summary_report(leeds_data, current_data, reference_data):
    """Gera relatório de resumo com insights"""
    report = []
    report.append("=" * 80)
    report.append("RELATÓRIO DE ANÁLISE DE SITES DE REFERÊNCIA")
    report.append("=" * 80)
    report.append("")
    
    # Análise da Leeds
    if leeds_data:
        report.append("--- UNIVERSIDADE DE LEEDS ---")
        report.append(f"Título: {leeds_data.get('title', 'N/A')}")
        report.append("\nHeadings encontrados:")
        for h in leeds_data.get('headings', [])[:10]:
            report.append(f"  [{h['level']}] {h['text']}")
        report.append("\nParágrafos relevantes:")
        for p in leeds_data.get('paragraphs', [])[:5]:
            report.append(f"  - {p[:150]}...")
        report.append("")
    
    # Análise do site atual
    if current_data:
        report.append("--- SITE ATUAL (antonioalberti.com) ---")
        report.append(f"Título: {current_data.get('title', 'N/A')}")
        report.append("\nHeadings encontrados:")
        for h in current_data.get('headings', [])[:15]:
            report.append(f"  [{h['level']}] {h['text']}")
        report.append("\nParágrafos relevantes:")
        for p in current_data.get('paragraphs', [])[:8]:
            report.append(f"  - {p[:150]}...")
        report.append("")
    
    # Análise do site de referência
    if reference_data:
        report.append("--- SITE DE REFERÊNCIA (Fibonacci) ---")
        report.append(f"Título: {reference_data.get('title', 'N/A')}")
        report.append("\nHeadings encontrados:")
        for h in reference_data.get('headings', [])[:10]:
            report.append(f"  [{h['level']}] {h['text']}")
        report.append("\nEstrutura observada:")
        for p in reference_data.get('paragraphs', [])[:5]:
            report.append(f"  - {p[:150]}...")
        report.append("")
    
    report.append("=" * 80)
    report.append("FIM DO RELATÓRIO")
    report.append("=" * 80)
    
    report_text = "\n".join(report)
    
    # Salvar relatório
    with open("logs/analysis_report.txt", "w", encoding="utf-8") as f:
        f.write(report_text)
    
    log_message("Relatório de análise gerado em logs/analysis_report.txt")
    return report_text

def main():
    """Função principal"""
    log_message("=" * 60)
    log_message("INICIANDO ANÁLISE DE SITES DE REFERÊNCIA")
    log_message("=" * 60)
    
    # Criar diretório de logs se não existir
    os.makedirs("logs", exist_ok=True)
    os.makedirs("scripts", exist_ok=True)
    
    # Analisar sites
    leeds_data = analyze_leeds_page()
    current_data = analyze_current_website()
    reference_data = analyze_reference_site()
    
    # Gerar relatório
    if any([leeds_data, current_data, reference_data]):
        report = generate_summary_report(leeds_data, current_data, reference_data)
        print("\n" + report)
    else:
        log_message("AVISO: Nenhum site pôde ser analisado")
    
    log_message("=" * 60)
    log_message("ANÁLISE CONCLUÍDA")
    log_message("=" * 60)

if __name__ == "__main__":
    main()