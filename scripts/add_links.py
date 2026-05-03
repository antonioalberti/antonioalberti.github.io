import re

def process_file(filepath, lang):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Leeds link in hero affiliation
    if lang == 'pt':
        content = content.replace(
            'School of Computer Science, University of Leeds, Reino Unido</p>',
            '<a href="https://eps.leeds.ac.uk/computing/staff/15735/dr-antonio-alberti" target="_blank">School of Computer Science, University of Leeds, Reino Unido</a></p>'
        )
        content = content.replace(
            'Sou Professor Associado em Engenharia de Software na School of Computer Science, University of Leeds, Reino Unido.',
            'Sou <a href="https://eps.leeds.ac.uk/computing/staff/15735/dr-antonio-alberti" target="_blank">Professor Associado em Engenharia de Software na School of Computer Science, University of Leeds, Reino Unido</a>.'
        )
        content = content.replace(
            'Sou autor de "Novos Renascimentos"',
            'Sou autor de "<a href="https://clubedeautores.com.br/livro/novos-renascimentos" target="_blank">Novos Renascimentos</a>"'
        )
        content = content.replace(
            'Aprimoramento da arquitetura NovaGenesis Future Internet com capacidades modernas de agentic AI para operação autônoma de redes.</p>',
            'Aprimoramento da arquitetura NovaGenesis Future Internet com capacidades modernas de agentic AI para operação autônoma de redes. <a href="https://chatgpt.com/g/g-11P28r4b3-novagenesis" target="_blank"><strong>Explore o Agente AI NovaGenesis →</strong></a></p>'
        )
        content = content.replace(
            '<h3>Livro Novos Renascimentos</h3>',
            '<h3><a href="https://clubedeautores.com.br/livro/novos-renascimentos" target="_blank">Livro Novos Renascimentos</a></h3>'
        )
        content = content.replace(
            'Projetado para públicos técnicos e não técnicos.</p>',
            'Projetado para públicos técnicos e não técnicos. <a href="https://chatgpt.com/g/g-UENWgftcp-novos-renascimentos" target="_blank"><strong>Pergunte ao Agente AI do Livro →</strong></a></p>'
        )
        content = content.replace(
            '<h3>Movimento Renascidade</h3>',
            '<h3><a href="https://www.youtube.com/@renascidade" target="_blank">Movimento Renascidade</a></h3>'
        )
        # Insert NovaGenesis GitHub card before book card
        content = content.replace(
            '<div class="impact-card">\n        <div class="impact-icon"><i class="fas fa-book"></i></div>\n        <h3><a href="https://clubedeautores.com.br/livro/novos-renascimentos" target="_blank">Livro Novos Renascimentos</a></h3>',
            '<div class="impact-card">\n        <div class="impact-icon"><i class="fab fa-github"></i></div>\n        <h3><a href="https://github.com/antonioalberti/NovaGenesis" target="_blank">NovaGenesis no GitHub</a></h3>\n        <p>Uma arquitetura revolucionária de Internet do Futuro do tipo clean-slate com publish/subscribe, naming hierárquico, auto-organização e in-network computing. Explore o código que está inspirando os padrões 6G da próxima geração.</p>\n      </div>\n      <div class="impact-card">\n        <div class="impact-icon"><i class="fas fa-book"></i></div>\n        <h3><a href="https://clubedeautores.com.br/livro/novos-renascimentos" target="_blank">Livro Novos Renascimentos</a></h3>'
        )
    elif lang == 'es':
        content = content.replace(
            'School of Computer Science, University of Leeds, Reino Unido</p>',
            '<a href="https://eps.leeds.ac.uk/computing/staff/15735/dr-antonio-alberti" target="_blank">School of Computer Science, University of Leeds, Reino Unido</a></p>'
        )
        content = content.replace(
            'Soy Profesor Asociado en Ingeniería de Software en la School of Computer Science, University of Leeds, Reino Unido.',
            'Soy <a href="https://eps.leeds.ac.uk/computing/staff/15735/dr-antonio-alberti" target="_blank">Profesor Asociado en Ingeniería de Software en la School of Computer Science, University of Leeds, Reino Unido</a>.'
        )
        content = content.replace(
            'Soy autor de "Nuevos Renacimientos"',
            'Soy autor de "<a href="https://clubedeautores.com.br/livro/novos-renascimentos" target="_blank">Nuevos Renacimientos</a>"'
        )
        content = content.replace(
            'Mejora de la arquitectura NovaGenesis Future Internet con capacidades modernas de agentic AI para operación autónoma de redes.</p>',
            'Mejora de la arquitectura NovaGenesis Future Internet con capacidades modernas de agentic AI para operación autónoma de redes. <a href="https://chatgpt.com/g/g-11P28r4b3-novagenesis" target="_blank"><strong>Explora el Agente AI NovaGenesis →</strong></a></p>'
        )
        content = content.replace(
            '<h3>Libro Nuevos Renacimientos</h3>',
            '<h3><a href="https://clubedeautores.com.br/livro/novos-renascimentos" target="_blank">Libro Nuevos Renacimientos</a></h3>'
        )
        content = content.replace(
            'Diseñado para públicos técnicos y no técnicos.</p>',
            'Diseñado para públicos técnicos y no técnicos. <a href="https://chatgpt.com/g/g-UENWgftcp-novos-renascimentos" target="_blank"><strong>Pregunta al Agente AI del Libro →</strong></a></p>'
        )
        content = content.replace(
            '<h3>Movimiento Renascidade</h3>',
            '<h3><a href="https://www.youtube.com/@renascidade" target="_blank">Movimiento Renascidade</a></h3>'
        )
        content = content.replace(
            '<div class="impact-card">\n        <div class="impact-icon"><i class="fas fa-book"></i></div>\n        <h3><a href="https://clubedeautores.com.br/livro/novos-renascimentos" target="_blank">Libro Nuevos Renacimientos</a></h3>',
            '<div class="impact-card">\n        <div class="impact-icon"><i class="fab fa-github"></i></div>\n        <h3><a href="https://github.com/antonioalberti/NovaGenesis" target="_blank">NovaGenesis en GitHub</a></h3>\n        <p>Una arquitectura revolucionaria de Internet del Futuro clean-slate con publish/subscribe, naming jerárquico, auto-organización e in-network computing. Explora el código que está inspirando los estándares 6G de próxima generación.</p>\n      </div>\n      <div class="impact-card">\n        <div class="impact-icon"><i class="fas fa-book"></i></div>\n        <h3><a href="https://clubedeautores.com.br/livro/novos-renascimentos" target="_blank">Libro Nuevos Renacimientos</a></h3>'
        )
    elif lang == 'zh':
        content = content.replace(
            '英国利兹大学计算机学院</p>',
            '<a href="https://eps.leeds.ac.uk/computing/staff/15735/dr-antonio-alberti" target="_blank">英国利兹大学计算机学院</a></p>'
        )
        content = content.replace(
            '我是英国利兹大学计算机学院的软件工程副教授。',
            '我是<a href="https://eps.leeds.ac.uk/computing/staff/15735/dr-antonio-alberti" target="_blank">英国利兹大学计算机学院的软件工程副教授</a>。'
        )
        content = content.replace(
            '我是《Novos Renascimentos》一书的作者',
            '我是《<a href="https://clubedeautores.com.br/livro/novos-renascimentos" target="_blank">Novos Renascimentos</a>》一书的作者'
        )
        content = content.replace(
            '使用现代智能体AI能力增强NovaGenesis未来互联网架构，实现网络的自主运行。</p>',
            '使用现代智能体AI能力增强NovaGenesis未来互联网架构，实现网络的自主运行。<a href="https://chatgpt.com/g/g-11P28r4b3-novagenesis" target="_blank"><strong>探索NovaGenesis AI智能体 →</strong></a></p>'
        )
        content = content.replace(
            '<h3>《Novos Renascimentos》书籍</h3>',
            '<h3><a href="https://clubedeautores.com.br/livro/novos-renascimentos" target="_blank">《Novos Renascimentos》书籍</a></h3>'
        )
        content = content.replace(
            '面向技术和非技术读者。</p>',
            '面向技术和非技术读者。<a href="https://chatgpt.com/g/g-UENWgftcp-novos-renascimentos" target="_blank"><strong>向书籍AI智能体提问 →</strong></a></p>'
        )
        content = content.replace(
            '<h3>Renascidade运动</h3>',
            '<h3><a href="https://www.youtube.com/@renascidade" target="_blank">Renascidade运动</a></h3>'
        )
        content = content.replace(
            '<div class="impact-card">\n        <div class="impact-icon"><i class="fas fa-book"></i></div>\n        <h3><a href="https://clubedeautores.com.br/livro/novos-renascimentos" target="_blank">《Novos Renascimentos》书籍</a></h3>',
            '<div class="impact-card">\n        <div class="impact-icon"><i class="fab fa-github"></i></div>\n        <h3><a href="https://github.com/antonioalberti/NovaGenesis" target="_blank">NovaGenesis在GitHub上</a></h3>\n        <p>一种革命性的clean-slate未来互联网架构，具有发布/订阅、分层命名、自组织和网内计算功能。探索正在启发下一代6G标准的代码库。</p>\n      </div>\n      <div class="impact-card">\n        <div class="impact-icon"><i class="fas fa-book"></i></div>\n        <h3><a href="https://clubedeautores.com.br/livro/novos-renascimentos" target="_blank">《Novos Renascimentos》书籍</a></h3>'
        )
    elif lang == 'hi':
        content = content.replace(
            'यूनिवर्सिटी ऑफ लीड्स, यूके कंप्यूटर साइंस स्कूल</p>',
            '<a href="https://eps.leeds.ac.uk/computing/staff/15735/dr-antonio-alberti" target="_blank">यूनिवर्सिटी ऑफ लीड्स, यूके कंप्यूटर साइंस स्कूल</a></p>'
        )
        content = content.replace(
            'मैं यूनिवर्सिटी ऑफ लीड्स, यूके के कंप्यूटर साइंस स्कूल में सॉफ्टवेयर इंजीनियरिंग का एसोसिएट प्रोफेसर हूँ।',
            'मैं <a href="https://eps.leeds.ac.uk/computing/staff/15735/dr-antonio-alberti" target="_blank">यूनिवर्सिटी ऑफ लीड्स, यूके के कंप्यूटर साइंस स्कूल में सॉफ्टवेयर इंजीनियरिंग का एसोसिएट प्रोफेसर हूँ</a>।'
        )
        content = content.replace(
            'मैं "Novos Renascimentos" पुस्तक का लेखक हूँ',
            'मैं "<a href="https://clubedeautores.com.br/livro/novos-renascimentos" target="_blank">Novos Renascimentos</a>" पुस्तक का लेखक हूँ'
        )
        content = content.replace(
            'स्वायंत्र नेटवर्क संचालन के लिए आधुनिक एजेंटिक AI क्षमताओं के साथ NovaGenesis Future Internet आर्किटेक्चर का संवर्धन।</p>',
            'स्वायंत्र नेटवर्क संचालन के लिए आधुनिक एजेंटिक AI क्षमताओं के साथ NovaGenesis Future Internet आर्किटेक्चर का संवर्धन। <a href="https://chatgpt.com/g/g-11P28r4b3-novagenesis" target="_blank"><strong>NovaGenesis AI Agent को एक्सप्लोर करें →</strong></a></p>'
        )
        content = content.replace(
            '<h3>Novos Renascimentos पुस्तक</h3>',
            '<h3><a href="https://clubedeautores.com.br/livro/novos-renascimentos" target="_blank">Novos Renascimentos पुस्तक</a></h3>'
        )
        content = content.replace(
            'तकनीकी और गैर-तकनीकी दर्शकों के लिए डिज़ाइन की गई।</p>',
            'तकनीकी और गैर-तकनीकी दर्शकों के लिए डिज़ाइन की गई। <a href="https://chatgpt.com/g/g-UENWgftcp-novos-renascimentos" target="_blank"><strong>पुस्तक AI Agent से पूछें →</strong></a></p>'
        )
        content = content.replace(
            '<h3>Renascidade आंदोलन</h3>',
            '<h3><a href="https://www.youtube.com/@renascidade" target="_blank">Renascidade आंदोलन</a></h3>'
        )
        content = content.replace(
            '<div class="impact-card">\n        <div class="impact-icon"><i class="fas fa-book"></i></div>\n        <h3><a href="https://clubedeautores.com.br/livro/novos-renascimentos" target="_blank">Novos Renascimentos पुस्तक</a></h3>',
            '<div class="impact-card">\n        <div class="impact-icon"><i class="fab fa-github"></i></div>\n        <h3><a href="https://github.com/antonioalberti/NovaGenesis" target="_blank">NovaGenesis GitHub पर</a></h3>\n        <p>एक क्रांतिकारी clean-slate Future Internet आर्किटेक्चर जिसमें publish/subscribe, hierarchial naming, self-organization और in-network computing है। अगली पीढ़ी के 6G मानकों को प्रेरित करने वाले कोडबेस का अन्वेषण करें।</p>\n      </div>\n      <div class="impact-card">\n        <div class="impact-icon"><i class="fas fa-book"></i></div>\n        <h3><a href="https://clubedeautores.com.br/livro/novos-renascimentos" target="_blank">Novos Renascimentos पुस्तक</a></h3>'
        )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'{filepath} updated successfully')

# Process all language files
files = {
    'pt/index.html': 'pt',
    'es/index.html': 'es',
    'zh/index.html': 'zh',
    'hi/index.html': 'hi'
}

for filepath, lang in files.items():
    process_file(filepath, lang)

print('All files updated!')