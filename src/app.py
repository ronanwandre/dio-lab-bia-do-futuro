"""
🎓 Edu - Educador Financeiro Inteligente
Uma aplicação Streamlit que integra IA generativa para educação financeira personalizada.
"""

import json
import pandas as pd
import requests
import streamlit as st
from datetime import datetime
from pathlib import Path
import logging

# ============ CONFIGURAÇÃO DE LOGGING ============
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ============ CONFIGURAÇÃO DO STREAMLIT ============
st.set_page_config(
    page_title="🎓 Edu - Educador Financeiro",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============ CONFIGURAÇÃO DE IA ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"
MAX_TOKENS = 500
TIMEOUT = 30

# ============ PATHS E CACHE ============
@st.cache_resource
def load_data():
    """Carrega todos os dados necessários com cache."""
    try:
        perfil = json.load(open('./data/perfil_investidor.json', encoding='utf-8'))
        transacoes = pd.read_csv('./data/transacoes.csv')
        historico = pd.read_csv('./data/historico_atendimento.csv')
        produtos = json.load(open('./data/produtos_financeiros.json', encoding='utf-8'))
        return perfil, transacoes, historico, produtos
    except FileNotFoundError as e:
        st.error(f"❌ Erro ao carregar dados: {e}")
        return None, None, None, None

# ============ CARREGAR DADOS ============
perfil, transacoes, historico, produtos = load_data()

if perfil is None:
    st.error("Dados não disponíveis. Verifique os arquivos em ./data/")
    st.stop()

# ============ FUNÇÕES AUXILIARES ============

def montar_contexto():
    """Monta o contexto do cliente para o LLM."""
    # Resumo de gastos por categoria
    transacoes_saida = transacoes[transacoes['tipo'] == 'saida']
    gastos_por_categoria = transacoes_saida.groupby('categoria')['valor'].sum().sort_values(ascending=False)
    
    gastos_resumo = "\n".join([f"- {cat}: R$ {valor:.2f}" for cat, valor in gastos_por_categoria.items()])
    total_gastos = transacoes_saida['valor'].sum()
    
    contexto = f"""
CLIENTE:
- Nome: {perfil['nome']}, {perfil['idade']} anos
- Profissão: {perfil['profissao']}
- Perfil de Investidor: {perfil['perfil_investidor']}
- Renda Mensal: R$ {perfil['renda_mensal']:.2f}

SITUAÇÃO FINANCEIRA:
- Patrimônio Total: R$ {perfil['patrimonio_total']:.2f}
- Reserva de Emergência Atual: R$ {perfil['reserva_emergencia_atual']:.2f}
- Objetivo Principal: {perfil['objetivo_principal']}

METAS FINANCEIRAS:
{json.dumps(perfil.get('metas', []), indent=2, ensure_ascii=False)}

PADRÃO DE GASTOS (Última Transação):
{gastos_resumo}
- Total de Saídas: R$ {total_gastos:.2f}

PRODUTOS FINANCEIROS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}

HISTÓRICO DE ATENDIMENTO:
{historico.to_string(index=False)}
"""
    return contexto

def chamar_ollama(mensagem_usuario, contexto):
    """Chama o Ollama com validação e tratamento de erros."""
    system_prompt = """Você é o Edu, um educador financeiro amigável e didático.

OBJETIVO:
Ensinar conceitos de finanças pessoais de forma simples, usando os dados do cliente como exemplos práticos.

REGRAS CRÍTICAS:
1. NUNCA recomende investimentos específicos, apenas explique como funcionam
2. JAMAIS responda a perguntas fora de finanças pessoais
3. Use os dados fornecidos para dar exemplos personalizados
4. Linguagem simples, como se explicasse para um amigo
5. Se não souber, admita: "Não tenho essa informação, mas posso explicar..."
6. Sempre pergunte se o cliente entendeu
7. Respostas sucintas: máximo 3 parágrafos

SEGURANÇA:
- Nunca compartilhe informações sensíveis
- Nunca simule dados que não existem
- Sempre valide informações com o contexto fornecido"""

    prompt_completo = f"""{system_prompt}

CONTEXTO DO CLIENTE:
{contexto}

PERGUNTA DO CLIENTE: {mensagem_usuario}

RESPOSTA:"""

    try:
        resposta = requests.post(
            OLLAMA_URL,
            json={"model": MODELO, "prompt": prompt_completo, "stream": False},
            timeout=TIMEOUT
        )
        resposta.raise_for_status()
        return resposta.json()['response']
    except requests.exceptions.ConnectionError:
        return "❌ Erro: Não consigo conectar ao Ollama. Verifique se está rodando em http://localhost:11434"
    except requests.exceptions.Timeout:
        return "❌ Erro: Ollama demorou muito para responder. Tente novamente."
    except Exception as e:
        logger.error(f"Erro ao chamar Ollama: {e}")
        return f"❌ Erro: {str(e)}"

# ============ INTERFACE STREAMLIT ============

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/financial-consultant.png", width=80)
    st.title("🎓 Edu")
    st.subheader("Educador Financeiro")
    
    st.divider()
    
    st.info(f"""
    👤 **Cliente:** {perfil['nome']}
    
    💼 **Profissão:** {perfil['profissao']}
    
    💰 **Renda:** R$ {perfil['renda_mensal']:.2f}
    
    🎯 **Perfil:** {perfil['perfil_investidor'].upper()}
    """)
    
    st.divider()
    
    st.subheader("📊 Visão Rápida")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Patrimônio", f"R$ {perfil['patrimonio_total']:.0f}")
    with col2:
        reserva_pct = (perfil['reserva_emergencia_atual'] / perfil['metas'][0]['valor_necessario']) * 100
        st.metric("Reserva", f"{reserva_pct:.0f}%")

# Abas principais
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "💬 Chat com Edu",
    "📊 Dashboard Financeiro",
    "🎲 Simulador",
    "❓ FAQ Inteligente",
    "📚 Educação Básica"
])

# ============ TAB 1: CHAT ============
with tab1:
    st.header("💬 Conversa com o Edu")
    st.write("Faça suas dúvidas sobre finanças pessoais e o Edu responderá de forma educativa.")
    
    # Histórico de chat em session state
    if "mensagens" not in st.session_state:
        st.session_state.mensagens = []
    
    # Exibir histórico
    for msg in st.session_state.mensagens:
        if msg["role"] == "user":
            st.chat_message("user").write(msg["content"])
        else:
            st.chat_message("assistant").write(msg["content"])
    
    # Input do usuário
    if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
        # Adicionar pergunta ao histórico
        st.session_state.mensagens.append({"role": "user", "content": pergunta})
        st.chat_message("user").write(pergunta)
        
        # Gerar resposta
        with st.spinner("🤔 Edu está pensando..."):
            contexto = montar_contexto()
            resposta = chamar_ollama(pergunta, contexto)
        
        # Adicionar resposta ao histórico
        st.session_state.mensagens.append({"role": "assistant", "content": resposta})
        st.chat_message("assistant").write(resposta)
    
    # Botão para limpar histórico
    if st.button("🗑️ Limpar Histórico", key="clear_chat"):
        st.session_state.mensagens = []
        st.rerun()

# ============ TAB 2: DASHBOARD ============
with tab2:
    st.header("📊 Dashboard Financeiro")
    
    # Análise de Gastos
    st.subheader("📈 Análise de Gastos")
    transacoes_saida = transacoes[transacoes['tipo'] == 'saida']
    gastos_por_categoria = transacoes_saida.groupby('categoria')['valor'].sum().sort_values(ascending=False)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total de Gastos", f"R$ {gastos_por_categoria.sum():.2f}")
    with col2:
        renda = transacoes[transacoes['tipo'] == 'entrada']['valor'].sum()
        st.metric("Renda Total", f"R$ {renda:.2f}")
    with col3:
        saldo = renda - gastos_por_categoria.sum()
        st.metric("Saldo", f"R$ {saldo:.2f}", delta="Superávit" if saldo > 0 else "Déficit")
    
    # Gráficos
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💸 Gastos por Categoria")
        fig_pizza = {
            "data": [{"labels": list(gastos_por_categoria.index), 
                     "values": list(gastos_por_categoria.values),
                     "type": "pie"}],
            "layout": {"title": "Distribuição de Gastos"}
        }
        st.plotly_chart(fig_pizza, use_container_width=True)
    
    with col2:
        st.subheader("📊 Gastos Detalhados")
        st.dataframe(
            gastos_por_categoria.reset_index().rename(columns={'categoria': 'Categoria', 'valor': 'Valor (R$)'}),
            use_container_width=True
        )
    
    # Análise de Metas
    st.subheader("🎯 Progresso das Metas")
    for meta in perfil.get('metas', []):
        valor_necessario = meta['valor_necessario']
        valor_economizado = perfil['reserva_emergencia_atual']
        progresso = (valor_economizado / valor_necessario) * 100
        
        st.write(f"**{meta['meta']}** (Prazo: {meta['prazo']})")
        st.progress(min(progresso / 100, 1.0))
        st.caption(f"R$ {valor_economizado:.2f} / R$ {valor_necessario:.2f} ({progresso:.1f}%)")

# ============ TAB 3: SIMULADOR ============
with tab3:
    st.header("🎲 Simulador Financeiro")
    
    st.subheader("💰 Simulação de Investimento")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        aporte_inicial = st.number_input("Aporte Inicial (R$)", value=1000.0, min_value=1.0, step=100.0)
    with col2:
        taxa_anual = st.number_input("Taxa Anual (%)", value=10.0, min_value=0.1, max_value=100.0, step=0.5)
    with col3:
        anos = st.number_input("Período (anos)", value=5, min_value=1, max_value=50)
    
    # Cálculo de investimento
    taxa_mensal = taxa_anual / 12 / 100
    meses = anos * 12
    
    valores = []
    for mes in range(meses + 1):
        valor = aporte_inicial * ((1 + taxa_mensal) ** mes)
        valores.append(valor)
    
    # Gráfico de simulação
    import plotly.graph_objects as go
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=valores, mode='lines', name='Valor Investido', 
                            line=dict(color='#1f77b4', width=3)))
    fig.update_layout(
        title=f"Simulação: R$ {aporte_inicial:.2f} a {taxa_anual:.1f}% a.a.",
        xaxis_title="Meses",
        yaxis_title="Valor (R$)",
        hovermode="x unified"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Resultado final
    rendimento = valores[-1] - aporte_inicial
    st.info(f"""
    💵 **Resultado Final:**
    - Valor Final: R$ {valores[-1]:.2f}
    - Ganho: R$ {rendimento:.2f}
    - Taxa de Retorno: {((rendimento/aporte_inicial)*100):.1f}%
    """)
    
    # Comparador de Produtos
    st.subheader("🏦 Comparação de Produtos")
    produtos_df = pd.DataFrame(produtos)
    
    colunas_exibicao = ['nome', 'categoria', 'risco', 'rentabilidade', 'aporte_minimo']
    st.dataframe(
        produtos_df[colunas_exibicao].rename(columns={
            'nome': 'Produto',
            'categoria': 'Categoria',
            'risco': 'Risco',
            'rentabilidade': 'Rentabilidade',
            'aporte_minimo': 'Aporte Mínimo'
        }),
        use_container_width=True
    )

# ============ TAB 4: FAQ ============
with tab4:
    st.header("❓ FAQ Inteligente")
    
    st.write("Perguntas comuns sobre finanças pessoais, respondidas de forma educativa.")
    
    perguntas_faq = [
        ("📌 O que é uma Reserva de Emergência?", 
         "Uma reserva de emergência é um fundo guardado para cobrir despesas inesperadas. Especialistas recomendam ter entre 3 a 6 meses de gastos."),
        
        ("📌 Qual a diferença entre CDI e Selic?",
         "Selic é a taxa básica de juros definida pelo Banco Central. CDI (Certificado de Depósito Interbancário) é uma taxa média entre bancos."),
        
        ("📌 Como começar a investir?",
         "Comece com uma reserva de emergência, depois estude os produtos (Tesouro, CDB), e invista de acordo com seu perfil."),
        
        ("📌 Renda fixa é segura?",
         "Renda fixa tem menor risco que renda variável, mas nenhum investimento é 100% seguro. Diversificação é importante."),
        
        ("📌 Como organizar meus gastos?",
         "A regra 50/30/20 é comum: 50% necessidades, 30% desejos, 20% investimento/economia. Adapte seu contexto."),
    ]
    
    for pergunta, resposta in perguntas_faq:
        with st.expander(pergunta):
            st.write(resposta)
    
    st.divider()
    
    st.subheader("❓ Fazer Pergunta Personalizada")
    pergunta_custom = st.text_area("Sua pergunta sobre finanças:")
    
    if st.button("🔍 Obter Resposta Educativa", key="faq_button"):
        if pergunta_custom:
            with st.spinner("Consultando base de conhecimento..."):
                contexto = montar_contexto()
                resposta = chamar_ollama(pergunta_custom, contexto)
            st.success("Resposta do Edu:")
            st.write(resposta)
        else:
            st.warning("Por favor, digite uma pergunta.")

# ============ TAB 5: EDUCAÇÃO ============
with tab5:
    st.header("📚 Guia de Educação Financeira")
    
    st.subheader("🎯 Conceitos Fundamentais")
    
    conceitos = {
        "💰 Renda": """
        É o dinheiro que você recebe. Pode ser:
        - **Ativa:** Trabalho, freelance, negócio
        - **Passiva:** Investimentos, aluguel
        """,
        
        "💸 Gastos": """
        Dinheiro que sai do bolso. Categorias:
        - **Essenciais:** Moradia, alimentação
        - **Variáveis:** Lazer, compras
        - **Investimentos:** Poupança, investimentos
        """,
        
        "📊 Fluxo de Caixa": """
        A diferença entre renda e gastos.
        - **Positivo:** Superávit (bom!)
        - **Negativo:** Déficit (precisa melhorar)
        """,
        
        "🎲 Risco x Retorno": """
        Todo investimento tem um trade-off:
        - **Baixo risco:** Retorno menor, mais seguro
        - **Alto risco:** Retorno maior, mais arriscado
        """,
    }
    
    for titulo, conteudo in conceitos.items():
        with st.expander(titulo):
            st.markdown(conteudo)
    
    st.divider()
    
    st.subheader("📖 Passos para Educação Financeira")
    
    passos = [
        ("1️⃣ **Conheça sua situação**", "Faça um diagnóstico: renda, gastos, dívidas, patrimônio."),
        ("2️⃣ **Organize seus gastos**", "Categorize e identifique onde pode economizar."),
        ("3️⃣ **Crie reserva de emergência**", "Guarde 3-6 meses de gastos antes de investir."),
        ("4️⃣ **Defina objetivos claros**", "Saiba o que quer alcançar e em quanto tempo."),
        ("5️⃣ **Estude investimentos**", "Aprenda sobre renda fixa, variável, fundos, etc."),
        ("6️⃣ **Comece pequeno**", "Não precisa de muito; começa com pouco e vai crescendo."),
    ]
    
    for passo, descricao in passos:
        st.write(f"{passo}  \n{descricao}")

# ============ RODAPÉ ============
st.divider()
col1, col2, col3 = st.columns(3)
with col1:
    st.caption("🎓 Edu - Educador Financeiro")
with col2:
    st.caption("Powered by Ollama + Streamlit")
with col3:
    st.caption(f"Atualizado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
