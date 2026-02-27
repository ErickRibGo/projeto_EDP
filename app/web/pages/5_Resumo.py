import streamlit as st
import requests
import time

with open("app/web/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.title("🧾 Revisar Pedido")

    if not all(k in st.session_state for k in ("codigo","insumo","qtd","email")):
        st.markdown("<div class='alert-error'>Fluxo interrompido. Volte ao início.</div>", unsafe_allow_html=True)
        st.stop()

    codigo = st.session_state["codigo"]
    insumo = st.session_state["insumo"]
    qtd    = st.session_state["qtd"]
    email  = st.session_state["email"]  # ← EMAIL DO SOLICITANTE

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write(f"**Agência:** {codigo}")
    st.write(f"**Insumo:** {insumo}")
    st.write(f"**Quantidade:** {qtd}")
    st.write(f"**Solicitante:** {email}")  # ← MOSTRA O EMAIL
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("Enviar Pedido"):
        try:
            r = requests.post(
                "http://localhost:8000/registrar_pedido",
                json={
                    "codigo_agencia": codigo,
                    "insumo": insumo,
                    "quantidade": qtd,
                    "solicitante": st.session_state["email"]
                },
                timeout=10
            )

            r.raise_for_status()
            protocolo = r.json().get("protocolo", "N/D")

            st.markdown(
                f"<div class='alert-success'>Pedido registrado!<br>Protocolo: {protocolo}</div>",
                unsafe_allow_html=True
            )

            time.sleep(2)

            # Limpa os dados
            st.session_state.clear()

            # Volta para a tela inicial
            st.switch_page("main.py")

        except Exception as e:
            st.markdown(
                f"<div class='alert-error'>Erro ao registrar: {e}</div>",
                unsafe_allow_html=True
            )