# Dr. Antonio Alberti - Professional Website

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-brightgreen)](https://antonioalberti.github.io)
[![Jekyll](https://img.shields.io/badge/Jekyll-4.3-red)](https://jekyllrb.com/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Professional academic website for Dr. Antonio Alberti, Associate Professor in Software Engineering at the University of Leeds.

## 🌐 Live Website

**URL:** https://antonioalberti.github.io

## ✨ Features

- **Multilingual Support**: English, Portuguese (PT), and Spanish (ES)
- **Fibonacci Proportions**: Design based on golden ratio (φ = 1.618...)
- **Responsive Design**: Optimized for desktop, tablet, and mobile
- **SEO Optimized**: Jekyll SEO tag plugin integration
- **Fast Loading**: Static site generation with minimal dependencies
- **Professional Sections**:
  - Hero/Introduction
  - About/Biography
  - Research Areas
  - Collaborations & Opportunities
  - Contact with Social Links

## 🚀 Quick Start

### Prerequisites

- Ruby 2.7+ 
- Bundler gem

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/antonioalberti/antonioalberti.github.io.git
cd antonioalberti.github.io
```

2. Install dependencies:
```bash
bundle install
```

3. Run local server:
```bash
bundle exec jekyll serve
```

4. Open http://localhost:4000 in your browser

### Deploy to GitHub Pages

1. Push to GitHub:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/antonioalberti/antonioalberti.github.io.git
git push -u origin main
```

2. Enable GitHub Pages in repository settings:
   - Go to Settings → Pages
   - Source: Deploy from a branch
   - Branch: main / root
   - Save

3. Your site will be live at: `https://antonioalberti.github.io`

## 📁 Project Structure

```
├── _config.yml              # Site configuration
├── _data/
│   └── i18n.yml            # Translations (EN/PT/ES)
├── _layouts/
│   └── default.html        # Base layout
├── _includes/              # Reusable components
├── assets/
│   ├── css/
│   │   └── main.scss       # Fibonacci-based styles
│   └── js/
│       └── main.js         # Interactivity
├── index.html              # English homepage
├── pt/
│   └── index.html          # Portuguese homepage
├── es/
│   └── index.html          # Spanish homepage
├── Gemfile                 # Ruby dependencies
└── README.md              # This file
```

## 🎨 Design Philosophy

The website uses **Fibonacci proportions** (golden ratio) throughout:
- Typography scale: 8, 13, 21, 34, 55, 89, 144px
- Spacing system based on φ
- Grid layouts using golden ratio divisions
- Color palette: Professional academic blues with gold accent

## 📝 Content Sections

### Research Areas
- 5G/6G Architectures
- Internet of Things (IoT)
- Distributed Systems
- AI/ML Integration
- Blockchain & Digital Monetization
- Digital Transformation

### Collaboration Opportunities
- **Research Partnerships**: Seeking collaborations in convergent ICT
- **Student Supervision**: PhD and MSc opportunities
- **Invited Talks**: Keynotes, panels, and workshops

### Social & Academic Profiles
- [LinkedIn](https://www.linkedin.com/in/antonio-marcos-alberti-31643a1b/)
- [Google Scholar](https://scholar.google.com/citations?user=2L_IXAIAAAAJ)
- [ResearchGate](https://www.researchgate.net/profile/Antonio-Alberti-2)
- [ORCID](https://orcid.org/0000-0002-0947-8575)
- [GitHub](https://github.com/antonioalberti)

## 🔧 Customization

### Update Content
Edit the corresponding language files in `_data/i18n.yml` and page files.

### Update Colors
Modify the SCSS variables in `assets/css/main.scss`:
```scss
$primary: #1a365d;    // Deep blue
$secondary: #2c5282;  // Medium blue  
$accent: #d69e2e;     // Gold accent
```

### Add New Language
1. Add translations to `_data/i18n.yml`
2. Create new folder (e.g., `fr/`)
3. Copy and translate page content

## 📄 License

This project is licensed under the MIT License.

## 👤 Author

**Dr. Antonio Alberti**
- Associate Professor in Software Engineering
- School of Computer Science, University of Leeds
- Email: A.M.Alberti@leeds.ac.uk

---

<p align="center">Built with ❤️ and ☕ using Jekyll & Fibonacci proportions</p>