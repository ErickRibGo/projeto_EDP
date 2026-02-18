import streamlit as st

with open("app/web/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.title("🔢 Quantidade")
    st.write("Informe a quantidade desejada do insumo selecionado.")

    with st.form("form_qtd"):
        qtd = st.number_input("Quantidade:", min_value=1, step=1)
        ok = st.form_submit_button("Confirmar")

    if ok:
        st.session_state["qtd"] = int(qtd)
        st.switch_page("pages/5_Resumo.py")