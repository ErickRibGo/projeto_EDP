import streamlit as st
with open("app/web/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
st.title("📧 Identificação")

email = st.text_input("Digite seu email corporativo")

if st.button("Continuar"):

    if "@edp.com" not in email.lower():
        st.error("Use seu email corporativo")
    else:
        st.session_state["email"] = email
        st.switch_page("pages/2_Agencia.py")