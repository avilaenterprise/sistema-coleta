# Deploy para avilatransportes.com.br

Este guia te ajudará a fazer o deploy do sistema para os domínios:
- `avilatransportes.com.br` (domínio principal)
- `avilatransportes.github.io` (GitHub Pages)

## 🚀 Opções de Deploy

### 1. Streamlit Cloud (Recomendado)

**Vantagens:**
- ✅ Gratuito
- ✅ Deploy automático via GitHub
- ✅ Suporte nativo ao Streamlit
- ✅ HTTPS automático
- ✅ Fácil configuração

**Passos:**

1. **Criar repositório no GitHub:**
```bash
cd "c:\Users\NicolasAvila\Desktop\Avila DevOps\ordem de coleta"
git init
git add .
git commit -m "Initial commit - Avila Transportes System"
git branch -M main
git remote add origin https://github.com/avilatransportes/sistema-coleta.git
git push -u origin main
```

2. **Deploy no Streamlit Cloud:**
   - Acesse [share.streamlit.io](https://share.streamlit.io)
   - Conecte com GitHub
   - Selecione o repositório `avilatransportes/sistema-coleta`
   - Branch: `main`
   - Main file: `main.py`
   - URL personalizada: `avilatransportes-sistema`

3. **Configurar domínio personalizado:**
   - No painel do Streamlit Cloud, vá em Settings
   - Configure custom domain: `avilatransportes.com.br`
   - Adicione CNAME no seu provedor DNS apontando para `avilatransportes-sistema.streamlit.app`

### 2. GitHub Pages + Landing Page

**Para avilatransportes.github.io:**

1. **Ativar GitHub Pages:**
   - Vá em Settings do repositório
   - Scroll até "Pages"
   - Source: Deploy from a branch
   - Branch: main
   - Folder: / (root)

2. **Configurar domínio personalizado:**
   - Em Pages settings, adicione: `avilatransportes.com.br`
   - Marque "Enforce HTTPS"

### 3. Heroku (Alternativa)

**Passos:**

1. **Instalar Heroku CLI:**
```bash
# Download em: https://devcenter.heroku.com/articles/heroku-cli
```

2. **Deploy:**
```bash
heroku login
heroku create avilatransportes-sistema
git push heroku main
```

3. **Configurar domínio:**
```bash
heroku domains:add avilatransportes.com.br
```

## 🌐 Configuração de DNS

### No seu provedor de domínio (ex: Registro.br, Hostinger, etc):

```
Tipo: CNAME
Nome: www
Valor: avilatransportes-sistema.streamlit.app

Tipo: A
Nome: @
Valor: 185.199.108.153 (GitHub Pages)
```

### Para subdominío:
```
Tipo: CNAME
Nome: sistema
Valor: avilatransportes-sistema.streamlit.app
```

## 📱 URLs Finais

Após o deploy, seu sistema estará disponível em:

- **Principal**: https://avilatransportes.com.br
- **Sistema**: https://avilatransportes-sistema.streamlit.app
- **GitHub**: https://avilatransportes.github.io

## 🔧 Configurações Específicas

### 1. Variáveis de Ambiente (se necessário)

No Streamlit Cloud, adicione em Settings > Secrets:
```toml
[database]
sqlite_path = "coletas.db"

[api]
ibge_timeout = 10
```

### 2. Certificado SSL

- Streamlit Cloud: Automático
- GitHub Pages: Automático (Let's Encrypt)
- Domínio personalizado: Configurado automaticamente

## 🛠️ Comandos Úteis

### Git Commands:
```bash
# Atualizar sistema
git add .
git commit -m "Update: nova funcionalidade"
git push origin main

# Ver status
git status

# Ver logs
git log --oneline
```

### Streamlit Local:
```bash
# Testar localmente
streamlit run main.py

# Com configurações específicas
streamlit run main.py --server.port 8501
```

## 🔍 Monitoramento

### Analytics (Opcional)

Adicione Google Analytics no `index.html`:
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

### Logs do Sistema

O Streamlit Cloud fornece logs em tempo real:
- Acesse o dashboard
- Clique em "Manage app"
- Vá em "Logs"

## 🚨 Troubleshooting

### Problemas Comuns:

1. **Erro de dependências:**
   - Verifique `requirements.txt`
   - Teste localmente primeiro

2. **Domínio não funciona:**
   - Aguarde propagação DNS (até 48h)
   - Verifique configurações CNAME

3. **App não carrega:**
   - Verifique logs no Streamlit Cloud
   - Teste localmente

### Suporte:
- Documentação Streamlit: [docs.streamlit.io](https://docs.streamlit.io)
- GitHub Pages: [docs.github.com/pages](https://docs.github.com/pages)

---

## ✅ Checklist Final

- [ ] Repositório GitHub criado
- [ ] Deploy no Streamlit Cloud
- [ ] DNS configurado
- [ ] HTTPS ativado
- [ ] Domínio personalizado funcionando
- [ ] Sistema testado em produção

**Tempo estimado:** 30-60 minutos
**Custo:** Gratuito (Streamlit Cloud + GitHub Pages)
