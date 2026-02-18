# app/dashboard/app_streamlit.py
import pandas as pd
import streamlit as st
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "pedidos.xlsx"

st.set_page_config(page_title="Consumo de Insumos (MVP)", layout="wide")
st.title("DASHBOARD – CONSUMO AGÊNCIAS")

@st.cache_data(ttl=10)
def carregar_pedidos():
    try:
        return pd.read_excel(DATA, engine="openpyxl")
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return pd.DataFrame(columns=["protocolo","data_hora","codigo_agencia","nome_agencia",
                                     "insumo","quantidade","solicitante","canal","status"])

df = carregar_pedidos()

col1, col2, col3 = st.columns(3)
agencias = ["(todas)"] + sorted(df["codigo_agencia"].dropna().astype(str).unique().tolist())
insumos = ["(todos)"] + sorted(df["insumo"].dropna().astype(str).unique().tolist())
status = ["(todos)"] + sorted(df["status"].dropna().astype(str).unique().tolist())

ag = col1.selectbox("Agência", agencias)
ins = col2.selectbox("Insumo", insumos)
stt = col3.selectbox("Status", status)

f = df.copy()
if ag != "(todas)": f = f[f["codigo_agencia"] == ag]
if ins != "(todos)": f = f[f["insumo"] == ins]
if stt != "(todos)": f = f[f["status"] == stt]

m1, m2, m3 = st.columns(3)
m1.metric("Total de Pedidos", len(f))
m2.metric("Quantidade Total", int(f["quantidade"].sum() if not f.empty else 0))
m3.metric("Agências Únicas", f["codigo_agencia"].nunique() if not f.empty else 0)

st.write(" ")
st.subheader("Pedidos (mais recentes primeiro)")
st.dataframe(f.sort_values("data_hora", ascending=False), use_container_width=True)

# Gráfico simples: soma de quantidades por insumo
st.write(" ")
st.subheader("Distribuição por insumo")
if f.empty:
    st.info("Sem dados filtrados para exibir.")
else:
    g = f.groupby("insumo")["quantidade"].sum().sort_values(ascending=False)
    st.bar_chart(g)