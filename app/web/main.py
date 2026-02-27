import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Suprimentos – EDP", page_icon="🏷️", layout="centered")

with open("app/web/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# layout central
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.title("Solicitação de Suprimentos EDP")
    st.write("Automação de pedidos com validação, rastreabilidade e protocolo.")
    st.markdown("<div class='card'>Clique no botão abaixo para iniciar um novo pedido.</div>", unsafe_allow_html=True)
    if st.button("Entrar no Sistema"):
        st.switch_page("pages/1_Login.py")