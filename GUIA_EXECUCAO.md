# 🚀 Guia de Execução - Edu

## 📋 Pré-requisitos

1. **Python 3.8+** instalado
2. **Ollama** instalado e rodando
3. **Git** para clonar o repositório

## 🔧 Instalação

### 1. Instalar Ollama

```bash
# Baixar em: https://ollama.ai
# Após instalar, execute o comando para baixar o modelo:
ollama pull gpt-oss
```

### 2. Iniciar Ollama (em outro terminal)

```bash
ollama serve
```

Isso iniciará o Ollama em `http://localhost:11434`

### 3. Clonar o Repositório

```bash
git clone <seu-repositorio>
cd dio-lab-bia-do-futuro
```

### 4. Criar Ambiente Virtual (Recomendado)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 5. Instalar Dependências

```bash
pip install -r requirements.txt
```

## ▶️ Executar a Aplicação

```bash
streamlit run src/app.py
```

A aplicação abrirá automaticamente no navegador em `http://localhost:8501`

## 📱 Funcionalidades

### 1. **💬 Chat com Edu**

- Chat interativo com histórico persistente na sessão
- Respostas personalizadas com contexto do cliente
- Educação financeira sem recomendações específicas

### 2. **📊 Dashboard Financeiro**

- Análise de gastos por categoria
- Gráficos de distribuição
- Progresso das metas financeiras
- Métricas de renda e saldo

### 3. **🎲 Simulador Financeiro**

- Simule investimentos com diferentes taxas
- Visualize crescimento do patrimônio
- Compare produtos financeiros disponíveis

### 4. **❓ FAQ Inteligente**

- Perguntas frequentes pré-respondidas
- Ferramenta para fazer perguntas personalizadas
- Respostas educativas contextualizadas

### 5. **📚 Guia de Educação Financeira**

- Conceitos fundamentais explicados
- Passo a passo para educação financeira
- Dicas práticas de gestão de finanças

## 🔍 Troubleshooting

### ❌ "Erro: Não consigo conectar ao Ollama"

**Solução:**

1. Verifique se Ollama está rodando: `http://localhost:11434/api/tags`
2. Inicie o Ollama: `ollama serve`
3. Reinicie a aplicação Streamlit

### ❌ "ModuleNotFoundError: No module named 'streamlit'"

**Solução:**

```bash
pip install streamlit
# ou
pip install -r requirements.txt
```

### ❌ "FileNotFoundError: ./data/perfil_investidor.json"

**Solução:**

1. Verifique se está na pasta correta: `dio-lab-bia-do-futuro/`
2. Verifique se a pasta `data/` existe com os 4 arquivos JSON/CSV
3. Execute: `pwd` (Linux/Mac) ou `cd` (Windows) para confirmar a pasta

## 💾 Estrutura de Dados

```
data/
├── perfil_investidor.json      # Dados do cliente
├── transacoes.csv              # Histórico de transações
├── historico_atendimento.csv   # Histórico de interações
└── produtos_financeiros.json   # Produtos disponíveis
```

## 🎯 Personalizações Possíveis

### Alterar Cliente

Edite `data/perfil_investidor.json` com seus dados:

```json
{
  "nome": "Seu Nome",
  "idade": 25,
  "profissao": "Sua profissão",
  ...
}
```

### Adicionar Transações

Adicione linhas em `data/transacoes.csv`:

```csv
data,descricao,categoria,valor,tipo
2025-11-01,Salário,receita,5000.00,entrada
```

### Personalizar Produtos

Edite `data/produtos_financeiros.json` para adicionar/remover produtos.

## 🚨 Limitações Conhecidas

1. **Ollama Offline**: Se Ollama cair, a aplicação não consegue responder
2. **Rate Limit**: Dependendo da máquina, o Ollama pode ser lento
3. **Memória**: O gpt-oss usa bastante RAM (2-4GB recomendado)
4. **Anti-Alucinação**: O modelo pode às vezes inventar informações

## 📞 Suporte

Para problemas ou sugestões, abra uma issue no repositório.

## 📚 Referências

- [Streamlit Docs](https://docs.streamlit.io/)
- [Ollama Docs](https://github.com/ollama/ollama)
- [Plotly Python](https://plotly.com/python/)
- [Pandas Documentation](https://pandas.pydata.org/)

---

**Última atualização:** Abril de 2026  
**Versão:** 2.0 (Versão Melhorada com Múltiplas Funcionalidades)
