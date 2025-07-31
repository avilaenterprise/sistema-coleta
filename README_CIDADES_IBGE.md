# 🏙️ Integração com IBGE - Sistema de Cidades

## 📋 Funcionalidades Otimizadas

### 1. Busca Inteligente (Recomendado)
- **🔍 Busca Manual**: Digite o nome da cidade e adicione conforme necessário
- **🏙️ Busca por UF**: Importe todas as cidades de um estado específico
- **✏️ Cadastro Manual**: Adicione cidades manualmente quando necessário

### 2. Sincronização Completa (Uso Restrito)
- **⚠️ Função Administrativa**: Disponível apenas no modo desenvolvedor
- **🚨 Limitações**: Faz mais de 5.000 requisições à API do IBGE
- **💡 Recomendação**: Use apenas uma vez na configuração inicial

### 3. Como Usar de Forma Eficiente

#### Para Uso Normal:
1. **Busca por Estado**: Selecione uma UF e importe as cidades necessárias
2. **Busca Específica**: Digite o nome da cidade e adicione diretamente
3. **Cadastro Manual**: Para cidades não encontradas ou casos especiais

#### Apenas para Configuração Inicial:
1. **Ative "Modo Desenvolvedor"**
2. **Confirme que entende as limitações**
3. **Execute "Sincronização Completa" apenas uma vez**

### 4. Vantagens da Nova Abordagem
- ✅ Menos requisições à API do IBGE
- ✅ Carregamento mais rápido
- ✅ Uso responsável da API pública
- ✅ Flexibilidade para adicionar cidades conforme necessário
- ✅ Interface mais intuitiva

### 5. API do IBGE - Uso Responsável
```
Base URL: https://servicodados.ibge.gov.br/api/v1/localidades/
Uso Recomendado:
- /estados/{UF}/municipios - Cidades por estado (27 requisições máximo)
- Busca manual com filtros locais
- Timeout de 8 segundos para evitar sobrecarga
```

### 6. Formato das Cidades
As cidades são salvas no formato: `NomeCidade - UF`
Exemplo: `São Paulo - SP`, `Rio de Janeiro - RJ`

### 7. Performance e Estatísticas
- **Dashboard integrado** com métricas em tempo real
- **Paginação automática** para listas grandes
- **Filtros dinâmicos** para busca rápida
- **Contadores inteligentes** por estado

### 8. Boas Práticas
- 🚀 **Use busca por UF** para importar estados completos
- 🔍 **Use busca manual** para cidades específicas
- ✏️ **Use cadastro manual** para casos especiais
- ⚠️ **Evite sincronização completa** após configuração inicial

### 9. Troubleshooting
- **Erro de timeout**: Aguarde alguns minutos e tente novamente
- **Cidade não encontrada**: Use cadastro manual
- **API indisponível**: Sistema funciona offline com cidades já cadastradas

---
**Otimizado para uso eficiente e responsável da API do IBGE** 🌐
