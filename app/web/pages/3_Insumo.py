import streamlit as st

with open("app/web/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.title("📦 Insumos")
    st.write("Escolha o insumo que deseja solicitar.")

    insumos = [
        "Bobina 57mm",
        "Bobina 80mm",
        "Boleto",
        "Papel A4",
        "Envelope",
        "Lacre Malote",
        "Formulário",
        "Toner",
        "Caneta",
        "Grampo",
        "Clips",
        "Pasta",
        "Etiqueta",
        "Outro"
    ]

    # FORMULÁRIO
    with st.form("form_insumo"):

        # Container com scroll
        with st.container(height=200):
            insumo = st.radio("Insumo:", insumos)

        ok = st.form_submit_button("Avançar")

    # FORA do form
    if ok:
        st.session_state["insumo"] = insumo.upper()
        st.switch_page("pages/4_Quantidade.py")