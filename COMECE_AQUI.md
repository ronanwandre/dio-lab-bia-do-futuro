# 🎓 BEM-VINDO AO EDU - Educador Financeiro com IA!

> **Assistente Virtual com Inteligência Artificial Generativa para Educação Financeira**

---

## 🚀 COMECE AGORA EM 3 PASSOS

### 1️⃣ Instale as Dependências

```bash
pip install -r requirements.txt
```

### 2️⃣ Inicie o Ollama (Adicione outro terminal)

```bash
ollama serve
```

### 3️⃣ Execute a Aplicação

```bash
streamlit run src/app.py
```

**Pronto!** Abra http://localhost:8501 no seu navegador 🌐

---

## 📱 O Que Você Encontrará

### 💬 Chat com Edu

Converse com um assistente de IA que ensina finanças de forma simples e personalizada.

- Histórico persistente
- Contexto do seu perfil
- Respostas educativas

### 📊 Dashboard Financeiro

Visualize sua situação financeira em tempo real.

- Análise de gastos por categoria
- Gráficos interativos
- Progresso das metas

### 🎲 Simulador de Investimentos

Calcule como seu dinheiro cresceria com diferentes investimentos.

- Juros compostos precisos
- Visualização em gráfico
- Comparação de produtos

### ❓ FAQ Inteligente

Perguntas frequentes + respostas personalizadas

- 5 FAQs pré-respondidas
- Perguntas customizadas
- Respostas contextualizadas

### 📚 Guia de Educação Financeira

Aprenda conceitos básicos de finanças de forma didática

- Conceitos fundamentais
- 6 passos para educação
- Dicas práticas

---

## 📚 DOCUMENTAÇÃO COMPLETA

| Documento                                                        | O Quê Você Aprenderá                           |
| ---------------------------------------------------------------- | ---------------------------------------------- |
| **[GUIA_EXECUCAO.md](GUIA_EXECUCAO.md)**                         | Como instalar, configurar e resolver problemas |
| **[TESTES_VALIDACAO.md](TESTES_VALIDACAO.md)**                   | Como testar a aplicação completamente          |
| **[ARQUITETURA_TECNICA.md](ARQUITETURA_TECNICA.md)**             | Como a aplicação funciona internamente         |
| **[EDU_DOCUMENTACAO_COMPLETA.md](EDU_DOCUMENTACAO_COMPLETA.md)** | Documentação abrangente e visão geral          |
| **[RESUMO_EXECUTIVO.md](RESUMO_EXECUTIVO.md)**                   | Sumário executivo e KPIs                       |
| **[MAPA_MENTAL.md](MAPA_MENTAL.md)**                             | Estrutura visual do projeto                    |
| **[ENTREGA_FINAL.md](ENTREGA_FINAL.md)**                         | Checklist de entrega                           |

---

## ❓ PERGUNTAS COMUNS

### Qual é a primeira coisa que devo fazer?

1. Certifique-se de ter Python 3.8+ instalado: `python --version`
2. Instale Ollama de https://ollama.ai
3. Siga os 3 passos acima para iniciar

### Posso usar isso sem Ollama?

Não. O Ollama é essencial para a IA funcionar. É grátis e local!

### Meus dados estão seguros?

Sim! 100% local. Nenhuma informação sai do seu computador.

### E se tiver erro de conexão com Ollama?

Verifique se Ollama está rodando: `http://localhost:11434/api/tags`
Se não estiver, execute `ollama serve` em outro terminal.

### Como faço para mudar o cliente?

Edite `data/perfil_investidor.json` com seus dados pessoais.

### Posso adicionar mais transações?

Sim! Edite `data/transacoes.csv` e adicione novas linhas.

---

## 🎯 EXEMPLOS DE PERGUNTAS

Tente fazer essas perguntas no Chat:

1. **"O que é CDI?"**
   → Edu explicará a taxa com exemplos

2. **"Qual é minha situação financeira?"**
   → Edu analisará seu perfil e transações

3. **"Como começar a investir?"**
   → Edu dará uma explicação educativa

4. **"Qual a diferença entre Selic e CDI?"**
   → Edu explicará conceitos financeiros

5. **"Onde estou gastando mais?"**
   → Edu analisará seu padrão de gastos

---

## ⚙️ CONFIGURAÇÃO DO SISTEMA

```
Python: 3.8+
Ollama: latest
Streamlit: 1.28+
Pandas: 2.0+
Plotly: 5.17+
Memoria: 2GB recomendado
Disco: 50MB disponível
```

---

## 🔐 SEGURANÇA & PRIVACIDADE

✅ **100% Local**

- Dados não saem do seu computador
- Ollama roda localmente
- Sem APIs externas

✅ **Anti-Alucinação**

- IA validada contra contexto real
- Nunca recomenda investimentos
- Apenas educa

✅ **Valor da Privacidade**

- Dados financeiros são sensíveis
- Você manter controle total
- Sem terceiros envolvidos

---

## 📈 PRÓXIMOS PASSOS

### Agora:

1. ✅ Execute a aplicação
2. ✅ Explore o Dashboard
3. ✅ Faça uma pergunta no Chat
4. ✅ Teste o Simulador

### Depois:

1. 🎓 Leia o guia educativo
2. 📊 Analise seus gastos
3. 🎯 Use o simulador para planejar
4. 💬 Converse com Edu sobre suas dúvidas

### Evolução:

1. 📚 Aprrofunde conhecimento
2. 💰 Comece a aplicar conceitos
3. 📈 Acompanhe progresso mensal
4. 🚀 Expanda para investimentos

---

## 🎓 O QUE VOCÊ VAI APRENDER

Com Edu, você aprenderá:

1. **Conceitos Básicos**
   - Receita, despesa, fluxo de caixa
   - Perfis de investidor
   - Risco vs retorno

2. **Organização Financeira**
   - Como organizar gastos
   - Criar reserva de emergência
   - Definir metas realistas

3. **Investimentos**
   - Tipos de renda fixa
   - Fundos e ações
   - Como começar pequeno

4. **Planejamento**
   - Usar simulador para cenários
   - Acompanhar progresso
   - Tomar decisões informadas

---

## 🤖 SOBRE A IA

### O Coração do Projeto: Ollama + GPT-OSS

- **Ollama**: Executor de LLM local, grátis e open source
- **GPT-OSS**: Modelo de linguagem generalista
- **Localização**: Roda 100% no seu computador
- **Privacidade**: Zero dados em cloud

### System Prompt do Edu

Edu segue regras rigorosas:

- ✅ Ensina, não recomenda
- ✅ Usa seus dados como exemplos
- ✅ Explica conceitos simples
- ✅ Admite quando não sabe
- ✅ Rejeita perguntas fora de escopo

---

## 💡 RECURSOS ESPECIAIS

### Dashboard Inteligente

Veja seus gastos em gráficos interativos e acompanhe metas em tempo real.

### Simulador Preciso

Calcule juros compostos mensais e veja quanto economizaria em diferentes cenários.

### FAQ Contextualizado

Perguntas personalizadas são respondidas considerando SUA situação financeira.

### Educação Contínua

Aprenda no ritmo próprio com conteúdo estruturado e expandível.

### Histórico Persistente

Seu histórico de conversa fica salvo na sessão para contexto.

---

## 🐛 PRECISA DE AJUDA?

### Erro de Conexão?

✅ [GUIA_EXECUCAO.md](GUIA_EXECUCAO.md) → Seção Troubleshooting

### Dúvida Técnica?

✅ [ARQUITETURA_TECNICA.md](ARQUITETURA_TECNICA.md)

### Como Testar?

✅ [TESTES_VALIDACAO.md](TESTES_VALIDACAO.md)

### Visão Geral?

✅ [EDU_DOCUMENTACAO_COMPLETA.md](EDU_DOCUMENTACAO_COMPLETA.md)

---

## 📞 SUPORTE

1. **Leia a documentação** - Respostas para 99% das dúvidas
2. **Consulte FAQ** - Perguntas comuns respondidas
3. **Verifique Troubleshooting** - Problemas técnicos
4. **Explore o Código** - `src/app.py` é bem comentado

---

## 🎯 MISSÃO DO EDU

> Capacitar pessoas a entender e gerenciar suas finanças através de educação acessível, personalizada e segura, usando inteligência artificial generativa 100% local.

---

## 🚀 VAMOS COMEÇAR?

```bash
# Terminal 1
ollama serve

# Terminal 2
pip install -r requirements.txt
streamlit run src/app.py
```

**Acesse:** http://localhost:8501

**Bem-vindo ao futuro da educação financeira! 🎉**

---

**Desenvolvido com ❤️ usando Python, Streamlit, Ollama e IA Generativa**

_Versão 2.0 | Abril 2026 | Status: ✅ Completo e Pronto_
