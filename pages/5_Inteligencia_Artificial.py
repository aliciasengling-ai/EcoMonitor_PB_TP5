import streamlit as st
import requests

st.set_page_config(
    page_title="Inteligência Artificial",
    page_icon="🤖"
)

st.title("🤖 Inteligência Artificial")

st.subheader("Resumo automático de textos ambientais")

st.write(
    "Utilize a inteligência artificial local para "
    "resumir textos sobre sustentabilidade e meio ambiente."
)

st.info("Modelo local: Google FLAN-T5 Small")

texto = st.text_area(
    "Digite ou cole um texto em inglês:",
    height=250,
    max_chars=2000
)

if st.button("Gerar resumo com IA"):

    if len(texto.strip()) < 10:
        st.warning(
            "Digite um texto com pelo menos 10 caracteres."
        )

    else:
        try:
            with st.spinner("Processando texto com IA..."):

                resposta = requests.post(
                    "http://127.0.0.1:8000/processar_texto",
                    json={"texto": texto},
                    timeout=120
                )

            if resposta.status_code == 200:

                dados = resposta.json()

                st.success("Resumo gerado com sucesso!")

                st.subheader("Resultado")
                st.write(dados["resultado"])

                st.caption(
                    "Modelo: " + dados["modelo"]
                )

                st.download_button(
                    "Baixar resumo",
                    data=dados["resultado"],
                    file_name="resumo_ambiental.txt",
                    mime="text/plain"
                )

            else:
                st.error(
                    f"Erro {resposta.status_code}: "
                    f"{resposta.json().get('detail')}"
                )

        except requests.exceptions.Timeout:
            st.error("O processamento demorou demais.")

        except requests.exceptions.ConnectionError:
            st.error("A API está desligada. Inicie o FastAPI.")

        except Exception:
            st.error("Ocorreu um erro inesperado.")

st.divider()

st.caption(
    "EcoMonitor Brasil - TP4 | Inteligência artificial local"
)