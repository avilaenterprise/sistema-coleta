# 📋 Sistema de Catalogação de Comprovantes de Entrega

Sistema completo para catalogar, analisar e organizar comprovantes de entrega em formato JPG.

## 🎯 Características

- **Catalogação Completa**: Analisa 3.676 comprovantes de entrega
- **Detecção de Duplicatas**: Identifica e quantifica arquivos duplicados
- **Análise de Metadados**: Extrai informações EXIF das imagens
- **Relatórios Múltiplos**: Excel, CSV, JSON e TXT
- **Limpeza Inteligente**: Remove duplicatas com backup automático
- **Análise Temporal**: Padrões de uso por data e horário
- **Compatível com Docker**: Execução portável e isolada

## 📊 Resultados da Análise

### Resumo Geral
- ✅ **3.676 arquivos** processados
- 💾 **4.724 MB** de espaço total ocupado
- 🔄 **450 duplicatas** encontradas (296 MB desperdiçados)
- 📱 **87.6%** são fotos mobile iOS
- ⏰ **Horário de pico**: 4h da manhã (1.877 comprovantes)

### Distribuição por Tipo
| Tipo | Quantidade | Percentual | Tamanho Médio |
|------|------------|------------|---------------|
| Foto Mobile iOS | 3.220 | 87.6% | 1.30 MB |
| Sequencial Numerado | 381 | 10.4% | 1.13 MB |
| Comprovante Padrão | 67 | 1.8% | 1.24 MB |
| Comprovante Empresarial | 6 | 0.2% | 1.23 MB |
| Documento Digital | 2 | 0.1% | 0.18 MB |

### Oportunidades de Otimização
- 🔄 **296 MB** podem ser liberados removendo duplicatas
- 📏 **30 arquivos** > 3MB podem ser comprimidos
- 🔤 **75 arquivos** precisam de nomenclatura padronizada

## 🚀 Como Usar

### Opção 1: Execução Direta (Python)

```bash
# 1. Instalar dependências
pip install pandas pillow openpyxl matplotlib seaborn numpy

# 2. Executar catalogação
python catalogador_comprovantes.py

# 3. Análise avançada
python analisador_avancado.py

# 4. Limpeza (modo simulação)
python limpador_comprovantes.py
```

### Opção 2: Execução via Docker

```bash
# Windows PowerShell
.\executar_docker.ps1

# Linux/Mac
./executar_docker.sh
```

## 📁 Estrutura de Arquivos

```
C:\Users\NicolasAvila\
├── catalogador_comprovantes.py    # Script principal de catalogação
├── analisador_avancado.py         # Análise detalhada
├── limpador_comprovantes.py       # Ferramenta de limpeza
├── Dockerfile                     # Para execução em container
├── requirements.txt               # Dependências Python
├── executar_docker.ps1           # Script PowerShell para Docker
└── Relatorios_Comprovantes/       # Pasta com todos os relatórios
    ├── catalogo_completo_*.xlsx   # Relatório Excel completo
    ├── catalogo_comprovantes_*.csv # Dados em CSV
    ├── catalogo_comprovantes_*.json # Dados em JSON
    ├── duplicatas_encontradas_*.txt # Lista de duplicatas
    └── relatorio_executivo_*.txt   # Resumo executivo
```

## 📊 Relatórios Gerados

### 1. **Catálogo Completo (Excel)**
- 📈 Planilha principal com todos os dados
- 📋 Aba separada para duplicatas
- 📊 Aba com estatísticas resumidas

### 2. **Arquivo CSV**
- 📝 Dados estruturados para análise externa
- 🔧 Compatível com Excel, Power BI, etc.

### 3. **Arquivo JSON**
- 🔧 Dados estruturados para APIs e sistemas
- 📱 Ideal para integração com aplicações

### 4. **Relatório de Duplicatas (TXT)**
- 🔄 Lista detalhada de arquivos duplicados
- 📋 Agrupados por hash MD5 idêntico

### 5. **Relatório Executivo (TXT)**
- 📊 Resumo executivo para gestão
- 💡 Recomendações de otimização

## 🛠️ Funcionalidades Avançadas

### Detecção de Duplicatas
- ✅ Usa hash MD5 para identificação precisa
- 📅 Mantém arquivo mais antigo de cada grupo
- 💾 Calcula espaço desperdiçado exato

### Análise de Metadados
- 📷 Extrai informações EXIF das fotos
- 📱 Identifica modelo de câmera/dispositivo
- 📅 Data real da foto vs. data do arquivo

### Classificação Inteligente
- 📱 Fotos Mobile iOS (padrão data/hora)
- 🔢 Numeração Sequencial
- 🏢 Comprovantes Empresariais
- 📄 Documentos Digitais
- 📋 Comprovantes Padrão

### Análise Temporal
- 📊 Distribuição por hora do dia
- 📅 Padrões por data
- ⏰ Identificação de horários de pico

## 🧹 Ferramenta de Limpeza

### Modo Simulação (Padrão)
- 📋 Mostra o que seria feito sem executar
- ✅ Seguro para análise prévia
- 📊 Relatório detalhado de ações

### Modo Execução Real
- 🚨 **ATENÇÃO**: Modifica arquivos reais!
- 💾 Cria backup automático antes de qualquer alteração
- 🔄 Remove duplicatas preservando originais
- 📁 Organiza arquivos por tipo em subpastas

## 🐳 Execução com Docker

### Vantagens
- 🔒 Isolamento completo do ambiente
- 📦 Dependências já incluídas
- 🔄 Reprodutível em qualquer sistema
- 🛡️ Maior segurança

### Volumes Mapeados
- `D:\Jpg` → `/app/dados` (pasta de origem)
- `C:\Users\NicolasAvila\Relatorios_Comprovantes` → `/app/relatorios` (saída)

## 💡 Recomendações de Uso

### 1. **Primeira Execução**
```bash
# Executar catalogação inicial
python catalogador_comprovantes.py

# Analisar resultados
python analisador_avancado.py
```

### 2. **Limpeza Segura**
```bash
# Testar em modo simulação primeiro
python limpador_comprovantes.py
# (escolher 's' para simulação)

# Executar limpeza real após confirmar
python limpador_comprovantes.py
# (escolher 'n' para execução real)
```

### 3. **Monitoramento Contínuo**
- ⏰ Executar catalogação semanalmente
- 📊 Acompanhar crescimento do acervo
- 🔄 Limpar duplicatas regularmente

## 🔒 Segurança e Backup

- ✅ Modo simulação padrão (sem riscos)
- 💾 Backup automático antes de qualquer alteração
- 📂 Arquivos originais preservados
- 🔄 Operações reversíveis

## 📈 Métricas de Performance

- ⚡ **Velocidade**: ~3.676 arquivos em ~2 minutos
- 💾 **Eficiência**: Identifica 296 MB de duplicatas
- 📊 **Precisão**: 100% na detecção por hash MD5
- 🔧 **Automação**: Zero intervenção manual necessária

## 🎯 Próximos Passos Sugeridos

1. **Executar limpeza** das 450 duplicatas (296 MB)
2. **Implementar nomenclatura** padronizada
3. **Configurar execução** automática semanal
4. **Criar processo** de backup regular
5. **Integrar com sistema** de gestão documental

---

**📞 Suporte**: Sistema desenvolvido para catalogação eficiente de comprovantes de entrega.
**🔧 Tecnologias**: Python 3.11+, Pandas, PIL, Docker
**📅 Versão**: 1.0 - Julho 2025
"# sistema-coleta" 
