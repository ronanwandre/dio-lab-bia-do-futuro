# 🗺️ Mapa Mental do Projeto Edu

## Estrutura Geral

```
EDU v2.0 - Assistente Virtual com IA Generativa
│
├─ 🎯 OBJETIVO
│  ├─ Educação financeira personalizada
│  ├─ IA generativa local (100% privado)
│  ├─ Interface intuitiva e responsiva
│  └─ Foco em ensinar, não recomendar
│
├─ 📱 INTERFACE (Streamlit)
│  ├─ 💬 Chat com Edu
│  │  ├─ Histórico persistente
│  │  ├─ Contexto personalizado
│  │  └─ Respostas educativas
│  │
│  ├─ 📊 Dashboard Financeiro
│  │  ├─ Análise de gastos
│  │  ├─ Gráficos interativos
│  │  └─ Progresso de metas
│  │
│  ├─ 🎲 Simulador Financeiro
│  │  ├─ Calculadora de juros
│  │  ├─ Visualização de crescimento
│  │  └─ Comparação de produtos
│  │
│  ├─ ❓ FAQ Inteligente
│  │  ├─ 5 perguntas pré-respondidas
│  │  ├─ Perguntas personalizadas
│  │  └─ Respostas contextualizadas
│  │
│  └─ 📚 Guia Educativo
│     ├─ Conceitos fundamentais
│     ├─ Passo a passo
│     └─ Dicas práticas
│
├─ 🤖 IA & PROCESSAMENTO
│  ├─ LLM: GPT-OSS (Ollama)
│  ├─ System Prompt customizado
│  ├─ Context Manager
│  ├─ Anti-Alucinação
│  └─ Error Handling
│
├─ 💾 DATA LAYER
│  ├─ perfil_investidor.json
│  ├─ transacoes.csv
│  ├─ historico_atendimento.csv
│  ├─ produtos_financeiros.json
│  └─ Session State Cache
│
├─ 🔐 SEGURANÇA
│  ├─ 100% Local (Ollama)
│  ├─ Nunca recomenda
│  ├─ Valida entradas
│  ├─ Trata erros
│  └─ Logs de debug
│
└─ 📚 DOCUMENTAÇÃO
   ├─ GUIA_EXECUCAO.md
   ├─ TESTES_VALIDACAO.md
   ├─ ARQUITETURA_TECNICA.md
   ├─ EDU_DOCUMENTACAO_COMPLETA.md
   └─ RESUMO_EXECUTIVO.md
```

---

## 🔄 Ciclo de Vida de uma Interação

```
USUÁRIO ABRE EDU
    ↓
┌─────────────────────────────────┐
│ 1. INICIALIZAÇÃO               │
│ - Load data (cache)            │
│ - Renderizar UI (5 abas)       │
│ - Exibir sidebar com perfil    │
└─────────────────────────────────┘
    ↓
USUÁRIO INTERAGE (Chat)
    ↓
┌─────────────────────────────────┐
│ 2. INPUT PROCESSING            │
│ - Recebe pergunta              │
│ - Valida tamanho/formato       │
│ - Display user message         │
└─────────────────────────────────┘
    ↓
┌─────────────────────────────────┐
│ 3. CONTEXT BUILDING            │
│ - Mount cliente profile        │
│ - Adiciona transações resumidas│
│ - Inclui histórico             │
│ - Lista produtos disponíveis   │
└─────────────────────────────────┘
    ↓
┌─────────────────────────────────┐
│ 4. PROMPT ENGINEERING          │
│ - System prompt                │
│ - Assemble final prompt        │
│ - Validar tamanho              │
└─────────────────────────────────┘
    ↓
┌─────────────────────────────────┐
│ 5. AI PROCESSING               │
│ - Call Ollama LLM             │
│ - Timeout 30s                  │
│ - Get response                 │
│ - Handle errors                │
└─────────────────────────────────┘
    ↓
┌─────────────────────────────────┐
│ 6. RESPONSE DISPLAY            │
│ - Parse response               │
│ - Display assistant message    │
│ - Store in history             │
│ - Update session state         │
└─────────────────────────────────┘
    ↓
USUÁRIO VEJO RESPOSTA
```

---

## 📊 Estrutura de Dados

### Client Profile Context

```
{
  "cliente": {
    "nome": "João Silva",
    "idade": 32,
    "profissao": "Analista de Sistemas",
    "renda_mensal": 5000.00,
    "perfil_investidor": "moderado"
  },
  "situacao_financeira": {
    "patrimonio_total": 15000.00,
    "reserva_emergencia": 10000.00,
    "meta_reserva": 15000.00,
    "progresso": "67%"
  },
  "gastos": {
    "moradia": 1380.00,
    "alimentacao": 570.00,
    "transporte": 295.00,
    "saude": 188.00,
    "lazer": 56.00,
    "total": 2488.90
  },
  "metas": [
    {
      "meta": "Reserva de Emergência",
      "prazo": "2026-06",
      "progresso": "67%"
    }
  ]
}
```

---

## 🎯 Fluxos Principais

### Fluxo 1: Chat Educativo

```
Pergunta → Validação → Context Built → Prompt → Ollama → Response → Display → History
```

### Fluxo 2: Dashboard Analytics

```
Load Data → Filter → Calculate → Aggregate → Visualize → Display
```

### Fluxo 3: Simulação

```
Input (Aporte, Taxa, Período) → Calculate → Chart → Display Results
```

### Fluxo 4: FAQ

```
Pre-loaded → Display → User asks → Call AI → Display Response
```

### Fluxo 5: Education

```
Load Content → Display Concepts → User reads → Expand sections
```

---

## 🎨 Layout Visual

```
┌──────────────────────────────────────────────────────────────┐
│ 🎓 Edu - Educador Financeiro              [⚙️] [🔔] [👤]    │
├───────────────┬──────────────────────────────────────────────┤
│               │                                              │
│  SIDEBAR      │         💬 | 📊 | 🎲 | ❓ | 📚              │
│  ────────     │                                              │
│               │  ┌────────────────────────────────────────┐ │
│  👤 João      │  │ CHAT COM EDU                          │ │
│  💼 Analista  │  │                                        │ │
│  💰 5k/mês    │  │ User: "O que é CDI?"                 │ │
│  🎯 Moderado  │  │                                        │ │
│               │  │ Edu: "CDI é uma taxa de referência   │ │
│  ─────────    │  │ usada pelos bancos..."               │ │
│               │  │                                        │ │
│  📊 KPIs      │  │ [Seu pergunta...]  📨 Enviar         │ │
│  ─────────    │  │                                        │ │
│  Patrimônio   │  └────────────────────────────────────────┘ │
│  R$ 15.000    │                                              │
│               │                                              │
│  Reserva      │                                              │
│  R$ 10.000    │                                              │
│  67% ████▒▒   │                                              │
│               │                                              │
└───────────────┴──────────────────────────────────────────────┘
```

---

## 🔧 Configuração E Stack

### Requirements

```
streamlit>=1.28.0
pandas>=2.0.0
requests>=2.31.0
plotly>=5.17.0
python>=3.8
```

### Environment

```
OLLAMA_URL = http://localhost:11434
MODELO = gpt-oss
TIMEOUT = 30s
```

### Data Files

```
./data/
├── perfil_investidor.json
├── transacoes.csv
├── historico_atendimento.csv
└── produtos_financeiros.json
```

---

## 📈 Escalabilidade & Evolução

```
Versão Atual: 2.0 (Funcional Completo)
    ↓
V2.1 → Persistência em BD + Exportação PDF
    ↓
V3.0 → APIs de Bancos + Alertas + Gamificação
    ↓
V4.0 → Multi-agente + Preditiva + Cloud Deploy
```

---

## 🎓 Tecnologias Utilizadas

### Frontend

- **Streamlit** - UI web interativa
- **Plotly** - Gráficos avançados
- **Python** - Backend logic

### AI/ML

- **Ollama** - LLM executor
- **GPT-OSS** - Language model
- **Prompt Engineering** - Context optimization

### Data

- **Pandas** - Data manipulation
- **JSON/CSV** - Data storage
- **Cache** - Performance optimization

### DevOps

- **Python venv** - Environment management
- **Git** - Version control
- **Logging** - Debug tracking

---

## ✨ Diferenciais

| Aspecto          | Diferencial                        |
| ---------------- | ---------------------------------- |
| **Privacidade**  | 100% local, sem APIs externas      |
| **Segurança**    | Anti-alucinação, sem recomendações |
| **UX**           | 5 abas, múltiplos fluxos           |
| **Performance**  | Cache, otimização                  |
| **Educação**     | Ensina, não vende                  |
| **Documentação** | 8+ arquivos completos              |

---

## 🚀 Quick Start

```bash
# 1. Setup
pip install -r requirements.txt

# 2. Start Ollama
ollama serve

# 3. Run App
streamlit run src/app.py

# 4. Access
http://localhost:8501
```

---

## 🎯 KPIs de Sucesso

| Métrica         | Target |
| --------------- | ------ |
| Taxa de Sucesso | > 95%  |
| Tempo Resposta  | < 5s   |
| Taxa de Erro    | < 2%   |
| Satisfação      | > 85%  |
| Uptime          | > 99%  |

---

**Mapa Mental Versão:** 1.0  
**Último Update:** Abril 2026  
**Status:** ✅ Completo
