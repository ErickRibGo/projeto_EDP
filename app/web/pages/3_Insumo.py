import streamlit as st

with open("app/web/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.title("📦 Insumos")
    st.write("Escolha o insumo que deseja solicitar.")

    with st.form("form_insumo"):
        insumo = st.radio("Insumo:", ["Bobina", "Boleto"], index=0)
        ok = st.form_submit_button("Avançar")

    if ok:
        st.session_state["insumo"] = insumo.upper()
        st.switch_page("pages/4_Quantidade.py")