# Avila Transportes - Sistema de Cotação e Ordem de Coleta

🚚 Sistema completo para gestão de cotações e ordens de coleta desenvolvido para a Avila Transportes.

## 🌟 Funcionalidades

### 🏢 Gestão de Clientes
- Cadastro completo de clientes
- Busca e consulta de informações
- Histórico de cotações por cliente

### 🏙️ Gestão de Cidades (Integração IBGE)
- Sincronização automática com API do IBGE
- Todas as 5.570 cidades do Brasil
- Busca inteligente por estado
- Filtros em tempo real

### 📋 Sistema de Cotações
- Cálculo automático de cubagem
- Sugestão de tipo de frete
- Aprovação de cotações
- Histórico completo

### 📦 Ordens de Coleta
- Geração automática de PDFs
- Sistema de rastreamento
- Notificações via WhatsApp
- Status de coleta em tempo real

## 🚀 Tecnologias

- **Frontend**: Streamlit
- **Backend**: Python 3.11
- **Banco de Dados**: SQLite
- **PDF**: FPDF2
- **API Externa**: IBGE (cidades)
- **Deploy**: GitHub Pages + Heroku

## 📱 Acesso Online

- **Produção**: [avilatransportes.com.br](https://avilatransportes.com.br)
- **GitHub Pages**: [avilatransportes.github.io](https://avilatransportes.github.io)

## 🛠️ Instalação Local

```bash
# Clone o repositório
git clone https://github.com/avilatransportes/sistema-coleta.git
cd sistema-coleta

# Instale as dependências
pip install -r requirements.txt

# Execute o sistema
streamlit run main.py
```

## 📊 Estrutura do Projeto

```
sistema-coleta/
├── main.py                 # Aplicação principal
├── requirements.txt        # Dependências Python
├── Procfile               # Configuração Heroku
├── runtime.txt            # Versão Python
├── .streamlit/
│   └── config.toml        # Configurações Streamlit
├── coletas.db             # Banco de dados SQLite
└── README.md              # Documentação
```

## 🔧 Configurações

### Parâmetros de Frete
- Fiorino Fracionado: até 1.0 m³
- Fiorino Dedicado: 1.0 - 3.0 m³
- Van/VUC Fracionado: 1.0 - 7.0 m³
- Van/VUC Dedicado: 7.0 - 15.0 m³

### Valores por KM
- Fiorino: R$ 1,80/km
- Van/VUC: R$ 3,00/km

## 📞 Funcionalidades de Comunicação

### WhatsApp Automático
- Notificação automática para destinatários
- Link direto para WhatsApp
- Mensagem personalizada com número da ordem

### Geração de PDF
- Layout profissional
- Logo personalizado
- Dados completos da coleta
- Assinatura digital

## 🔒 Segurança

- Queries SQL parametrizadas
- Validação de entrada de dados
- Tratamento de erros robusto
- Timeouts para APIs externas

## 📈 Performance

- Cache local de cidades IBGE
- Busca otimizada (máximo 50 resultados)
- Filtros em tempo real
- Interface responsiva

## 🌐 Deploy

### GitHub Pages
1. Push para repositório GitHub
2. Ative GitHub Pages nas configurações
3. Escolha branch main como source

### Domínio Personalizado
1. Configure DNS do domínio para apontar para GitHub Pages
2. Adicione arquivo CNAME com o domínio
3. Ative HTTPS nas configurações

## 📝 Changelog

### v2.0 - Integração IBGE
- ✅ API do IBGE para cidades
- ✅ Busca inteligente
- ✅ Performance otimizada

### v1.0 - Sistema Base
- ✅ Gestão de clientes
- ✅ Sistema de cotações
- ✅ Ordens de coleta
- ✅ Geração de PDF

## 👨‍💻 Desenvolvido por

**Nícolas Rosa Ávila Barros**  
Avila Transportes  
📧 contato@avilatransportes.com.br

---

© 2025 Avila Transportes. Todos os direitos reservados.
