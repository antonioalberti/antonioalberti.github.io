#!/bin/bash
# Script de deploy para GitHub Pages

echo "=========================================="
echo "DEPLOY DO SITE DR. ANTONIO ALBERTI"
echo "=========================================="
echo ""

# Verificar se está em um repositório git
if [ ! -d ".git" ]; then
    echo "Inicializando repositório Git..."
    git init
    git branch -M main
fi

# Verificar remote
REMOTE=$(git remote get-url origin 2>/dev/null)
if [ -z "$REMOTE" ]; then
    echo "Configurando remote..."
    git remote add origin https://github.com/antonioalberti/antonioalberti.github.io.git
fi

# Adicionar todos os arquivos
echo "Adicionando arquivos..."
git add .

# Commit
echo "Criando commit..."
git commit -m "Deploy: $(date '+%Y-%m-%d %H:%M:%S')"

# Push
echo "Enviando para GitHub..."
git push -u origin main

echo ""
echo "=========================================="
echo "DEPLOY CONCLUÍDO!"
echo "=========================================="
echo ""
echo "Seu site estará disponível em:"
echo "https://antonioalberti.github.io"
echo ""
echo "Para configurar domínio customizado:"
echo "1. Crie um arquivo CNAME com seu domínio"
echo "2. Configure os DNS do seu domínio apontando para GitHub Pages"
echo ""