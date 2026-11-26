
import streamlit as st
import pandas as pd
import requests
from pathlib import Path

st.set_page_config(
    page_title="EcoMonitor Brasil - TP5",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 EcoMonitor Brasil - Dashboard Final")
st.subheader("Ciência de Dados, Sustentabilidade e IA")

st.markdown("""
Aplicação de monitoramento ambiental alinhada
às práticas ESG e aos Objetivos de Desenvolvimento
Sustentável da Agenda 2030.
""")

API = "http://127.0.0.1:8000"

DATA = Path(__file__).resolve().parents[1] / "data"

st.header("1. Dados coletados")

arquivos = sorted(DATA.rglob("*.csv"))

if not arquivos:
    st.warning("Nenhum arquivo CSV encontrado.")
    st.stop()

arquivo = st.selectbox(
    "Selecione uma base de dados",
    arquivos,
    format_func=lambda x: str(x.relative_to(DATA))
)

try:
    df = pd.read_csv(arquivo, sep=None, engine="python")
except Exception as erro:
    st.error(f"Erro na leitura: {erro}")
    st.stop()

st.header("2. Processamento dos dados")

total_original = len(df)

df = df.drop_duplicates().dropna(how="all")

c1, c2, c3 = st.columns(3)

c1.metric("Registros válidos", len(df))
c2.metric("Variáveis", len(df.columns))
c3.metric("Registros removidos", total_original - len(df))

st.dataframe(df, use_container_width=True)

st.header("3. Análise e visualização")

numericas = df.select_dtypes(include="number").columns.tolist()

if numericas:
    indicador = st.selectbox(
        "Selecione um indicador",
        numericas
    )

    st.line_chart(df[indicador])
    st.dataframe(df[numericas].describe())

else:
    st.info("Esta base possui dados predominantemente textuais.")

st.header("4. Engenharia de prompts e IA")

st.write("""
O modelo local Google FLAN-T5 Small utiliza
instruções de sumarização para transformar
os dados coletados em informações sintetizadas.
""")

textuais = df.select_dtypes(
    include=["object", "string"]
).columns.tolist()

if textuais:

    coluna = st.selectbox("Coluna textual", textuais)

    textos = df[coluna].dropna().astype(str).tolist()

    quantidade = st.slider(
        "Quantidade de registros para analisar",
        1, 20, 5
    )

    if st.button("Gerar resumos com IA"):

        resultados = []

        with st.spinner("Processando textos localmente..."):

            for texto in textos[:quantidade]:

                if not texto.strip():
                    continue

                try:
                    resposta = requests.post(
                        f"{API}/processar_texto",
                        json={"texto": texto},
                        timeout=120
                    )

                    resposta.raise_for_status()

                    resultado = resposta.json()["resultado"]

                    resultados.append({
                        "Texto original": texto,
                        "Resumo IA": resultado,
                        "Palavras originais": len(texto.split()),
                        "Palavras resumo": len(resultado.split())
                    })

                except Exception as erro:
                    st.error(f"Falha no processamento: {erro}")
                    break

        if resultados:
            st.session_state["resultados_ia"] = resultados

else:
    st.info("Selecione uma base com conteúdo textual.")

if "resultados_ia" in st.session_state:

    resultados = pd.DataFrame(
        st.session_state["resultados_ia"]
    )

    st.header("5. Resultados gerados pela IA")

    st.metric("Textos processados", len(resultados))

    st.dataframe(resultados, use_container_width=True)

    st.bar_chart(
        resultados[["Palavras originais", "Palavras resumo"]]
    )

    st.download_button(
        "Baixar resultados da IA",
        resultados.to_csv(index=False).encode("utf-8-sig"),
        "resultados_ia.csv",
        "text/csv"
    )

st.header("6. ESG e Agenda 2030")

st.markdown("""
- **ODS 7:** Energia limpa e acessível.
- **ODS 11:** Cidades e comunidades sustentáveis.
- **ODS 12:** Consumo e produção responsáveis.
- **ODS 13:** Ação contra a mudança global do clima.

A solução facilita o acesso a informações ambientais
e apoia a análise de dados para tomada de decisão.

Os resumos gerados pela IA devem ser revisados,
pois podem omitir informações importantes.
""")
