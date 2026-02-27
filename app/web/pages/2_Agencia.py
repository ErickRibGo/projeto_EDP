import streamlit as st

with open("app/web/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.title("🏷️ ID Agência")
    st.write("Digite o código da agência para continuar.")

    with st.form("form_agencia", clear_on_submit=False):
        codigo = st.text_input("Código da Agência:")
        submit = st.form_submit_button("Validar")

    if submit:
        import requests
        try:
            r = requests.get(f"http://localhost:8000/validar_agencia/{codigo}", timeout=10)
            r.raise_for_status()
            if r.json().get("valido"):
                st.session_state["codigo"] = codigo
                st.markdown("<div class='alert-success'>Agência validada!</div>", unsafe_allow_html=True)
                st.switch_page("pages/3_Insumo.py")
            else:
                st.markdown("<div class='alert-error'>Código inválido.</div>", unsafe_allow_html=True)
        except Exception as e:
            st.markdown(f"<div class='alert-error'>Erro na validação: {e}</div>", unsafe_allow_html=True)