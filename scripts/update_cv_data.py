#!/usr/bin/env python3
"""
Script para extrair dados do CV LaTeX e atualizar os arquivos do site Jekyll
nas três linguas (PT, EN, ES).
"""

import os
import re

# ====== DADOS EXTRAÍDOS DO CV ======

# Emprego atual
employment = {
    "en": {
        "title": "Associate Professor in Software Engineering",
        "institution": "School of Computer Science, University of Leeds",
        "location": "Leeds, Yorkshire, United Kingdom",
        "period": "2024 – Present",
    },
    "pt": {
        "title": "Professor Associado em Engenharia de Software",
        "institution": "School of Computer Science, University of Leeds",
        "location": "Leeds, Yorkshire, Reino Unido",
        "period": "2024 – Presente",
    },
    "es": {
        "title": "Profesor Asociado en Ingeniería de Software",
        "institution": "School of Computer Science, University of Leeds",
        "location": "Leeds, Yorkshire, Reino Unido",
        "period": "2024 – Presente",
    }
}

# Educação
education = {
    "en": [
        {
            "title": "Ph.D. in Electrical Engineering",
            "area": "Telecommunications and Telematics",
            "thesis": "Development of simulation models for analyzing quality of service in ATM networks",
            "institution": "State University of Campinas (Unicamp)",
            "period": "1998 – 2003"
        },
        {
            "title": "M.Sc. in Electrical Engineering",
            "area": "Electronics and Communications",
            "thesis": "SimATM: An Environment for Simulating ATM Networks",
            "institution": "State University of Campinas (Unicamp)",
            "period": "1996 – 1998"
        },
        {
            "title": "B.Sc. in Electrical Engineering",
            "area": "",
            "thesis": "",
            "institution": "Federal University of Santa Maria",
            "period": "1991 – 1996"
        }
    ],
    "pt": [
        {
            "title": "Doutorado em Engenharia Elétrica",
            "area": "Telecomunicações e Telemática",
            "thesis": "Desenvolvimento de modelos de simulação para análise de qualidade de serviço em redes ATM",
            "institution": "Universidade Estadual de Campinas (Unicamp)",
            "period": "1998 – 2003"
        },
        {
            "title": "Mestrado em Engenharia Elétrica",
            "area": "Eletrônica e Comunicações",
            "thesis": "SimATM: Um Ambiente para Simulação de Redes ATM",
            "institution": "Universidade Estadual de Campinas (Unicamp)",
            "period": "1996 – 1998"
        },
        {
            "title": "Graduação em Engenharia Elétrica",
            "area": "",
            "thesis": "",
            "institution": "Universidade Federal de Santa Maria",
            "period": "1991 – 1996"
        }
    ],
    "es": [
        {
            "title": "Doctorado en Ingeniería Eléctrica",
            "area": "Telecomunicaciones y Telemática",
            "thesis": "Desarrollo de modelos de simulación para análisis de calidad de servicio en redes ATM",
            "institution": "Universidad Estatal de Campinas (Unicamp)",
            "period": "1998 – 2003"
        },
        {
            "title": "Maestría en Ingeniería Eléctrica",
            "area": "Electrónica y Comunicaciones",
            "thesis": "SimATM: Un Entorno para Simulación de Redes ATM",
            "institution": "Universidad Estatal de Campinas (Unicamp)",
            "period": "1996 – 1998"
        },
        {
            "title": "Licenciatura en Ingeniería Eléctrica",
            "area": "",
            "thesis": "",
            "institution": "Universidad Federal de Santa María",
            "period": "1991 – 1996"
        }
    ]
}

# Award highlights (selected)
awards = {
    "en": [
        "2023 - Commendation of Merit by ADINATEL for significant services to education",
        "2021 - Best Paper Award at SBCUP (Brazilian Symposium on Ubiquitous Computing)",
        "2021 - Best Paper Award at WPEIF (Workshop on Experimental Internet Research)",
        "2021 - Honored Professor - Telecommunications Engineering at Inatel",
        "2020 - Best Paper Award at WPEIF, SBC",
        "2013 - Best Paper Award at International Conference on CCCM, India",
        "1995 - First place in Electrical Engineering at CRICTE",
        "1993 - First place in Electrical Engineering at CRICTE"
    ],
    "pt": [
        "2023 - Comenda de Mérito da ADINATEL por serviços significativos à educação",
        "2021 - Prêmio de Melhor Artigo no SBCUP (Simpósio Brasileiro de Computação Ubíqua)",
        "2021 - Prêmio de Melhor Artigo na WPEIF (Oficina de Pesquisa Experimental da Internet)",
        "2021 - Professor Homenageado - Engenharia de Telecomunicações no Inatel",
        "2020 - Prêmio de Melhor Artigo na WPEIF, SBC",
        "2013 - Prêmio de Melhor Artigo na Conferência Internacional CCCM, Índia",
        "1995 - Primeiro lugar em Engenharia Elétrica na CRICTE",
        "1993 - Primeiro lugar em Engenharia Elétrica na CRICTE"
    ],
    "es": [
        "2023 - Mención de Mérito de ADINATEL por servicios significativos a la educación",
        "2021 - Premio al Mejor Artículo en SBCUP (Simposio Brasileño de Computación Ubíqua)",
        "2021 - Premio al Mejor Artículo en WPEIF (Taller de Investigación Experimental de Internet)",
        "2021 - Profesor Honorífico - Ingeniería de Telecomunicaciones en Inatel",
        "2020 - Premio al Mejor Artículo en WPEIF, SBC",
        "2013 - Premio al Mejor Artículo en Conferencia Internacional CCCM, India",
        "1995 - Primer lugar en Ingeniería Eléctrica en CRICTE",
        "1993 - Primer lugar en Ingeniería Eléctrica en CRICTE"
    ]
}

# Skills highlighted
skills = {
    "en": {
        "areas": [
            "Future Internet Architectures (5G, 6G, ICN, SDN, NFV)",
            "IoT, M2M, Smart Cities, Digital Twins",
            "Distributed Systems, Cloud/Edge Computing",
            "Blockchain and Distributed Ledger Technologies",
            "Telecommunications and Network Protocols",
            "AI/ML for Network Intelligence",
            "Software Engineering and System Design"
        ],
        "tools": "Advanced C++, C, Python; AI tools: ChatGPT, Claude, Midjourney, Copilot",
        "teaching": "20+ years of teaching at undergraduate, master's and doctoral levels",
        "keynotes": "60+ lectures on technological disruptions at major Brazilian events"
    },
    "pt": {
        "areas": [
            "Arquiteturas de Internet do Futuro (5G, 6G, ICN, SDN, NFV)",
            "IoT, M2M, Cidades Inteligentes, Gêmeos Digitais",
            "Sistemas Distribuídos, Computação em Nuvem/Edge",
            "Blockchain e Tecnologias de Ledger Distribuído",
            "Protocolos de Telecomunicações e Redes",
            "AI/ML para Inteligência em Redes",
            "Engenharia de Software e Design de Sistemas"
        ],
        "tools": "C++, C avançados, Python; Ferramentas de IA: ChatGPT, Claude, Midjourney, Copilot",
        "teaching": "20+ anos de experiência em ensino de graduação, mestrado e doutorado",
        "keynotes": "60+ palestras sobre disrupções tecnológicas em grandes eventos brasileiros"
    },
    "es": {
        "areas": [
            "Arquitecturas de Internet del Futuro (5G, 6G, ICN, SDN, NFV)",
            "IoT, M2M, Ciudades Inteligentes, Gemelos Digitales",
            "Sistemas Distribuidos, Computación en Nube/Edge",
            "Blockchain y Tecnologías de Ledger Distribuido",
            "Protocolos de Telecomunicaciones y Redes",
            "AI/ML para Inteligencia en Redes",
            "Ingeniería de Software y Diseño de Sistemas"
        ],
        "tools": "C++, C avanzados, Python; Herramientas de IA: ChatGPT, Claude, Midjourney, Copilot",
        "teaching": "20+ años de experiencia enseñando a nivel pregrado, maestría y doctorado",
        "keynotes": "60+ conferencias sobre disrupciones tecnológicas en grandes eventos brasileños"
    }
}

# Books
books = {
    "en": {
        "title": "Novos Renascimentos (New Renaissances)",
        "description": "A book covering hundreds of technologies and their impacts on society, summarizing years of research on ICT convergence"
    },
    "pt": {
        "title": "Novos Renascimentos",
        "description": "Um livro que abrange centenas de tecnologias e seus impactos na sociedade, resumindo anos de pesquisa sobre convergência de TIC"
    },
    "es": {
        "title": "Nuevos Renacimientos",
        "description": "Un libro que cubre cientos de tecnologías y sus impactos en la sociedad, resumiendo años de investigación sobre convergencia de TIC"
    }
}

# Research highlights
research = {
    "en": [
        "Chief Architect of NovaGenesis Future Internet project (2008-2024)",
        "Contributor to Future Internet initiatives in South Korea",
        "Architecture design of the Brazil 6G Project",
        "Over 100 peer-reviewed papers in high-impact journals and conferences",
        "90+ talks on technology and disruptive impacts"
    ],
    "pt": [
        "Arquiteto Chefe do projeto NovaGenesis Future Internet (2008-2024)",
        "Contribuidor de iniciativas de Internet do Futuro na Coreia do Sul",
        "Design da arquitetura do Projeto 6G Brasil",
        "Mais de 100 artigos revisados por pares em revistas e conferências de alto impacto",
        "Mais de 90 palestras sobre tecnologia e impactos disruptivos"
    ],
    "es": [
        "Arquitecto Jefe del proyecto NovaGenesis Future Internet (2008-2024)",
        "Contribuidor de iniciativas de Internet del Futuro en Corea del Sur",
        "Diseño de arquitectura del Proyecto 6G Brasil",
        "Más de 100 artículos revisados por pares en revistas y conferencias de alto impacto",
        "Más de 90 conferencias sobre tecnología e impactos disruptivos"
    ]
}

# Social/Entrepreneurship
soc_ent = {
    "en": "Creator of Renascidade movement for digital, creative, collaborative and cultural transformation",
    "pt": "Criador do movimento Renascidade para transformação digital, criativa, colaborativa e cultural",
    "es": "Creador del movimiento Renascidade para transformación digital, creativa, colaborativa y cultural"
}

# Scopus & IDs
ids = {
    "en": {"orcid": "0000-0002-0947-8575", "researcher_id": "E-8534-2012", "scopus": "8907441700"},
    "pt": {"orcid": "0000-0002-0947-8575", "researcher_id": "E-8534-2012", "scopus": "8907441700"},
    "es": {"orcid": "0000-0002-0947-8575", "researcher_id": "E-8534-2012", "scopus": "8907441700"}
}

def generate_html_content(lang):
    """Gera o conteúdo HTML completo para um idioma específico"""
    
    emp = employment[lang]
    edu = education[lang]
    awd = awards[lang]
    skl = skills[lang]
    bk = books[lang]
    res = research[lang]
    soc = soc_ent[lang]
    
    # Títulos de seções
    titles = {
        "en": {
            "about": "About Me",
            "bio": "Biography",
            "edu": "Education",
            "research": "Research",
            "awards": "Awards & Honors",
            "skills": "Skills & Expertise",
            "books": "Publications",
            "collab": "Collaborations & Opportunities",
            "contact": "Contact",
            "partnerships": "Research Partnerships",
            "supervision": "Student Supervision",
            "talks": "Invited Talks"
        },
        "pt": {
            "about": "Sobre Mim",
            "bio": "Biografia",
            "edu": "Formação Acadêmica",
            "research": "Pesquisa",
            "awards": "Prêmios e Honrarias",
            "skills": "Habilidades e Expertise",
            "books": "Publicações",
            "collab": "Colaborações e Oportunidades",
            "contact": "Contato",
            "partnerships": "Parcerias de Pesquisa",
            "supervision": "Orientação de Alunos",
            "talks": "Palestras Convidadas"
        },
        "es": {
            "about": "Sobre Mí",
            "bio": "Biografía",
            "edu": "Formación Académica",
            "research": "Investigación",
            "awards": "Premios y Honores",
            "skills": "Habilidades y Experiencia",
            "books": "Publicaciones",
            "collab": "Colaboraciones y Oportunidades",
            "contact": "Contacto",
            "partnerships": "Colaboraciones de Investigación",
            "supervision": "Supervisión de Estudiantes",
            "talks": "Conferencias Invitadas"
        }
    }[lang]
    
    # Montar HTML
    html = f""".hero {{
  background: linear-gradient(135deg, #1a365d 0%, #2c5282 100%);
  color: white;
  padding: 144px 0 89px;
  margin-top: 89px;
  position: relative;
  overflow: hidden;
}}

.hero-content {{
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 21px;
}}

.hero-badge {{
  display: inline-block;
  background: var(--accent);
  color: var(--primary);
  padding: 8px 21px;
  border-radius: 4px;
  font-weight: 600;
  font-size: 14px;
  margin-bottom: 21px;
  letter-spacing: 1px;
  text-transform: uppercase;
}}

.hero-title {{
  font-size: 55px;
  color: white;
  margin-bottom: 13px;
  font-family: 'Merriweather', Georgia, serif;
}}

.hero-subtitle {{
  font-size: 34px;
  color: rgba(255,255,255,0.9);
  margin-bottom: 8px;
  font-weight: 400;
}}

.hero-affiliation {{
  font-size: 21px;
  color: rgba(255,255,255,0.8);
  margin-bottom: 34px;
}}

.hero-cta {{
  display: flex;
  gap: 21px;
}}

.btn {{
  padding: 13px 34px;
  border-radius: 4px;
  font-weight: 600;
  transition: all 0.3s ease;
  display: inline-block;
}}

.btn-primary {{
  background: var(--accent);
  color: var(--primary);
}}

.btn-primary:hover {{
  background: #b7791f;
  transform: translateY(-2px);
}}

.btn-secondary {{
  background: transparent;
  color: white;
  border: 2px solid rgba(255,255,255,0.5);
}}

.btn-secondary:hover {{
  border-color: white;
  background: rgba(255,255,255,0.1);
}}

/* Stats bar */
.stats-bar {{
  background: rgba(255,255,255,0.05);
  backdrop-filter: blur(10px);
  padding: 34px 0;
  margin-top: 55px;
  border-top: 1px solid rgba(255,255,255,0.1);
}}

.stats-grid {{
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 21px;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 21px;
  text-align: center;
}}

.stat-item h3 {{
  font-size: 34px;
  color: var(--accent);
  margin-bottom: 8px;
}}

.stat-item p {{
  color: rgba(255,255,255,0.8);
  margin: 0;
  font-size: 14px;
}}