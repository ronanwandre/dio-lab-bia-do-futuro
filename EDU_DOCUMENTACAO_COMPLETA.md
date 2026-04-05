# 🎓 Edu - Documentação Completa v2.0

## 📌 Visão Geral

**Edu** é um **Assistente Virtual de IA Generativa** para educação financeira personalizada. Combina:

✅ **Processamento de Linguagem Natural** - Compreende perguntas em português  
✅ **Base de Conhecimento Contextualizada** - Dados reais do cliente  
✅ **Dashboard Analítico** - Visualização de gastos e metas  
✅ **Simulador Financeiro** - Calcule retornos de investimentos  
✅ **FAQ Inteligente** - Perguntas frequentes e personalizadas  
✅ **Módulo Educativo** - Aprenda conceitos básicos

---

## 🎯 Objetivos do Projeto

### Objetivo Principal

Criar uma experiência digital de educação financeira que combine IA, dados e boas práticas de UX.

### Objetivos Secundários

1. Ensinar conceitos financeiros sem recomendar investimentos
2. Personalizar explicações com dados do cliente
3. Oferecer múltiplas formas de aprendizado (chat, dashboard, simulador)
4. Manter segurança e anti-alucinação
5. Proporcionar interface intuitiva e responsiva

---

## 👥 Personas Identificadas

### 1. João Silva (Cliente Padrão)

- **Idade:** 32 anos
- **Profissão:** Analista de Sistemas
- **Renda:** R$ 5.000/mês
- **Perfil:** Moderado
- **Objetivo:** Construir reserva de emergência
- **Características:** Iniciante em investimentos, cauteloso

### 2. Tipos de Usuários

| Tipo              | Características             | Necessidades                        |
| ----------------- | --------------------------- | ----------------------------------- |
| **Iniciante**     | Sem conhecimento financeiro | Educação básica, exemplos simples   |
| **Intermediário** | Conhece conceitos básicos   | Análise de gastos, simulações       |
| **Avançado**      | Investe regularmente        | Comparação de produtos, estratégias |

---

## 🎨 Interface & UX

### Layout Principal

```
┌─────────────────────────────────────────────────┐
│  🎓 Edu - Educador Financeiro      [🎯 ⚙️ 🔔] │
├─────────────────────────────────────────────────┤
│  [📌 Sidebar]          │  [Main Content Area]  │
│                        │                       │
│  👤 João Silva         │  💬 💬 📊 🎲 ❓ 📚  │
│  💼 Analista           │                       │
│  💰 R$ 5.000/mês       │  ┌─────────────────┐ │
│  🎯 Moderado           │  │ Conversa com    │ │
│  ─────────────────     │  │ o Edu           │ │
│  💵 R$ 15.000 | 100%   │  │                 │ │
│  🔃 R$ 10.000 (67%)    │  │ User: "O que é" │ │
│                        │  │ "CDI?"          │ │
│                        │  │                 │ │
│                        │  │ Edu: "CDI é..." │ │
│                        │  │                 │ │
│                        │  └─────────────────┘ │
└─────────────────────────────────────────────────┘
```

### 5 Abas Principais

#### 1️⃣ **Chat com Edu** 💬

- Conversa interativa com histórico
- Contexto persistente na sessão
- Respostas educativas personalizadas
- Histórico limpável

**Interações Esperadas:**

- "O que é CDI?"
- "Onde estou gastando mais?"
- "Como começo a investir?"
- "Qual a diferença entre ações e CDB?"

**Limitações:**

- ❌ "Recomende um investimento" → Edu recusa
- ❌ "Qual a previsão do tempo?" → Fora de escopo
- ❌ "Me passa a senha do banco" → Privacidade

---

#### 2️⃣ **Dashboard Financeiro** 📊

- Análise de gastos por categoria
- Gráficos interativos (Plotly)
- Métricas KPI em tempo real
- Progresso das metas

**Seções:**

1. **Métricas Principais**
   - Total de Gastos: R$ 2.488,90
   - Renda Total: R$ 5.000,00
   - Saldo: R$ 2.511,10

2. **Gráficos**
   - Pizza: Distribuição de gastos
   - Barras: Comparação por categoria

3. **Análise de Metas**
   - Reserva de Emergência: 67% (R$ 10.000 de R$ 15.000)
   - Entrada Apartamento: 0% (Prazo: 2027-12)

**Dados Analisados:**

```
Gastos por Categoria:
├─ Moradia: R$ 1.380 (55%)
├─ Alimentação: R$ 570 (23%)
├─ Transporte: R$ 295 (12%)
├─ Saúde: R$ 188 (8%)
└─ Lazer: R$ 56 (2%)
```

---

#### 3️⃣ **Simulador Financeiro** 🎲

- Calculadora de investimentos
- Comparação de produtos
- Visualização de crescimento

**Funcionalidades:**

1. **Simulação de Investimento**
   - Entrada: Aporte inicial, Taxa anual, Período
   - Cálculo: Juros compostos mensais
   - Saída: Gráfico + Resultados numéricos

2. **Fórmula**

   ```
   Valor Final = Aporte × (1 + taxa_mensal)^meses
   taxa_mensal = taxa_anual / 12 / 100
   meses = anos × 12
   ```

3. **Tabela de Produtos**
   - Tesouro Selic
   - CDB Liquidez Diária
   - LCI/LCA
   - Fundo Imobiliário (FII)
   - Fundo de Ações

**Exemplo:**

```
Aporte: R$ 1.000
Taxa: 10% a.a.
Período: 10 anos

Resultado:
Valor Final: R$ 2.707
Ganho: R$ 1.707
Retorno: 170,7%
```

---

#### 4️⃣ **FAQ Inteligente** ❓

- 5 perguntas pré-respondidas
- Ferramenta para perguntas personalizadas
- Respostas educativas contextualizadas

**FAQs Pré-carregadas:**

1. O que é uma Reserva de Emergência?
2. Qual a diferença entre CDI e Selic?
3. Como começar a investir?
4. Renda fixa é segura?
5. Como organizar meus gastos?

**Pergunta Personalizada:**

- Campo de texto
- Botão "Obter Resposta Educativa"
- Integração com IA (Ollama)

---

#### 5️⃣ **Guia de Educação Financeira** 📚

- Conceitos fundamentais
- Passo a passo para educação financeira
- Conteúdo estruturado e expandível

**Conceitos Cobertos:**

1. **Renda** - Ativa vs Passiva
2. **Gastos** - Essenciais vs Variáveis
3. **Fluxo de Caixa** - Positivo vs Negativo
4. **Risco x Retorno** - Trade-off

**Passo a Passo:**

1. Conheça sua situação
2. Organize seus gastos
3. Crie reserva de emergência
4. Defina objetivos claros
5. Estude investimentos
6. Comece pequeno

---

## 🔄 Fluxos de Usuário

### Fluxo 1: Educação Financeira Completa

```
1. Cliente abre Edu
2. Lê o Guia de Educação Financeira
3. Consulta Dashboard para conhecer situação
4. Usa Simulador para explorar cenários
5. Faz perguntas no Chat
6. Consulta FAQ para dúvidas específicas
7. Retorna periodicamente para acompanhar
```

### Fluxo 2: Esclarecimento Rápido

```
1. Cliente abre Edu
2. Va para FAQ ou Chat
3. Faz pergunta específica
4. Obtém resposta educativa
5. Sai com dúvida esclarecida
```

### Fluxo 3: Análise Financeira

```
1. Cliente abre Edu
2. Consulta Dashboard
3. Identifica áreas de melhoria
4. Usa Simulador para planejar
5. Conversa com Edu sobre estratégias
```

---

## 🤖 Inteligência Artificial

### LLM Utilizado: GPT-OSS via Ollama

**Características:**

- 🏠 **100% Local** - Não envia dados para APIs externas
- 📦 **Self-hosted** - Controlo total
- 🔐 **Seguro** - Dados protegidos
- 💰 **Grátis** - Open source

**Configuração:**

```python
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"
TIMEOUT = 30
```

### System Prompt

```
Você é o Edu, um educador financeiro amigável e didático.

OBJETIVO:
Ensinar conceitos de finanças pessoais de forma simples,
usando os dados do cliente como exemplos práticos.

REGRAS CRÍTICAS:
1. NUNCA recomende investimentos específicos
2. JAMAIS responda sobre tópicos fora de finanças
3. Use dados reais para exemplos personalizados
4. Linguagem simples e acessível
5. Admita quando não souber algo
6. Pergunte se o cliente entendeu
7. Máximo 3 parágrafos por resposta
```

### Estratégias Anti-Alucinação

1. **Contexto Estruturado**
   - Dados do cliente no prompt
   - Produtos disponíveis listados
   - Histórico de transações

2. **Regras Explícitas**
   - "NUNCA recomende..."
   - "JAMAIS responda sobre..."
   - "Se não souber..."

3. **Validação de Resposta**
   - Checklist mental antes de enviar
   - Rejeição de prompts suspeitos
   - Recovery de erros

---

## 📊 Dados & Contexto

### Perfil do Cliente

```json
{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.0,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.0,
  "reserva_emergencia_atual": 10000.0,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.0,
      "prazo": "2026-06"
    }
  ]
}
```

### Transações (Últimas)

```csv
data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5000.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
...
```

### Produtos Financeiros

5 produtos descritos com características:

- **Tesouro Selic** - Baixo risco, 100% Selic
- **CDB Liquidez Diária** - Baixo risco, 102% CDI
- **LCI/LCA** - Baixo risco, isento IR
- **FII** - Risco médio, 6-12% dividend yield
- **Fundo de Ações** - Alto risco, variável

---

## 🔐 Segurança & Privacidade

### Princípios Implementados

1. **Dados Locais**
   - ✅ Todos dados armazenados localmente
   - ✅ Nenhuma chamada externa por dados sensíveis
   - ✅ Ollama local (sem cloud)

2. **Anti-Recomendação**
   - ✅ Nunca recomenda investimentos
   - ✅ Apenas educa sobre produtos
   - ✅ Deixa decisão com cliente

3. **Validação de Entrada**
   - ✅ Rejeita perguntas fora de escopo
   - ✅ Protege contra prompt injection
   - ✅ Limita tamanho de mensagens

4. **Tratamento de Erros**
   - ✅ Mensagens de erro amigáveis
   - ✅ Logging para debugging
   - ✅ Recovery automático

---

## 📈 Métricas de Sucesso

### KPIs de Negócio

| Métrica            | Target | Atual       |
| ------------------ | ------ | ----------- |
| Taxa de satisfação | > 85%  | [A validar] |
| Tempo resposta     | < 5s   | [A validar] |
| Taxa de erro       | < 2%   | [A validar] |
| Retenção           | > 70%  | [A validar] |

### KPIs de Qualidade de IA

| Métrica           | Descrição                           | Score |
| ----------------- | ----------------------------------- | ----- |
| **Assertividade** | Responde o que foi perguntado?      | 0-10  |
| **Segurança**     | Evita alucinações e recomendações?  | 0-10  |
| **Clareza**       | Resposta educativa e compreensível? | 0-10  |
| **Coerência**     | Mantém contexto e consistência?     | 0-10  |

---

## 🚀 Como Começar

### Requisitos Mínimos

- Python 3.8+
- Ollama 0.1+ (com modelo gpt-oss)
- 2GB RAM livre
- 50MB disco disponível

### 3 Passos Rápidos

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Iniciar Ollama (outro terminal)
ollama serve

# 3. Rodar aplicação
streamlit run src/app.py
```

### Acessar

- 🌐 http://localhost:8501
- 💬 Fazer primeira pergunta
- 📊 Explorar dashboard
- 🎲 Testar simulador

---

## 📚 Documentação Relacionada

| Documento                                                        | Conteúdo                   |
| ---------------------------------------------------------------- | -------------------------- |
| [GUIA_EXECUCAO.md](GUIA_EXECUCAO.md)                             | Instruções passo-a-passo   |
| [TESTES_VALIDACAO.md](TESTES_VALIDACAO.md)                       | Plano completo de testes   |
| [ARQUITETURA_TECNICA.md](ARQUITETURA_TECNICA.md)                 | Detalhes técnicos e fluxos |
| [docs/01-documentacao-agente.md](docs/01-documentacao-agente.md) | Especificação da persona   |
| [docs/03-prompts.md](docs/03-prompts.md)                         | Prompts e exemplos         |

---

## 🎓 Aprendizados Consolidados

Este projeto consolida:

✅ **IA Generativa** - Integração com LLMs, prompt engineering, anti-alucinação  
✅ **Python** - Streamlit, Pandas, APIs HTTP, estrutura OOP  
✅ **Dados** - Análise de transações, contexto estruturado, cache  
✅ **UX** - Interface limpa, múltiplos fluxos, dashboard intuitivo  
✅ **Boas Práticas** - Segurança, logging, tratamento de erros

---

## 🎯 Próximas Melhorias

1. **Curto Prazo** (v2.1)
   - [ ] Persistência de histórico em BD
   - [ ] Exportação de relatórios PDF
   - [ ] Multi-idioma

2. **Médio Prazo** (v3.0)
   - [ ] Integração com APIs de bancos
   - [ ] Alertas automáticos
   - [ ] Gamificação com pontos

3. **Longo Prazo** (v4.0)
   - [ ] Fine-tuning com domain knowledge
   - [ ] Multi-agente specializado
   - [ ] Análise preditiva

---

**Versão:** 2.0  
**Última atualização:** Abril de 2026  
**Status:** ✅ Completo e Testado
