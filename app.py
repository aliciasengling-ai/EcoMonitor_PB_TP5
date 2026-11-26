import streamlit as st

st.set_page_config(
    page_title="EcoMonitor Brasil - TP5",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 EcoMonitor Brasil")
st.subheader("Ciência de Dados, Sustentabilidade e IA")

st.header("Sobre o projeto")

st.write("""
O EcoMonitor Brasil é uma aplicação de monitoramento
ambiental alinhada às práticas ESG e aos Objetivos de
Desenvolvimento Sustentável da Agenda 2030.

Na etapa final, o projeto integra coleta, processamento,
visualização de dados e inteligência artificial local.
""")

st.header("Funcionalidades")

st.markdown("""
- Consulta de dados climáticos.
- Coleta de conteúdo ambiental.
- Visualização de indicadores.
- Upload e download de arquivos CSV.
- Integração com FastAPI.
- Engenharia de prompts.
- Sumarização automática com FLAN-T5 Small.
- Dashboard final interativo.
""")

st.header("Inteligência Artificial")

st.write("""
A solução utiliza um modelo de linguagem local para
resumir textos ambientais e facilitar a compreensão
de informações relacionadas à sustentabilidade.
""")

st.header("ODS e ESG")

st.markdown("""
- ODS 11: Cidades e comunidades sustentáveis.
- ODS 12: Consumo e produção responsáveis.
- ODS 13: Ação contra a mudança global do clima.
""")

st.info("Utilize o menu lateral para navegar pela aplicação.")

st.success("EcoMonitor Brasil - Projeto Final TP5")