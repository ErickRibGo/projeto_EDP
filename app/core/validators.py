# app/core/validators.py
def validar_agencia(codigo: str, df_depara):
    match = df_depara[df_depara["codigo_agencia"].astype(str).str.upper() == str(codigo).upper()]
    if match.empty:
        return None
    row = match.iloc[0].to_dict()
    return {"codigo_agencia": row["codigo_agencia"], "nome_agencia": row["nome_agencia"], "tipo": row.get("tipo","")}

def validar_insumo(insumo: str):
    catalogo = {"BOBINA","BOLETO"}  # fácil de expandir depois
    return (insumo or "").strip().upper() in catalogo

def validar_quantidade(qtd: str):
    try:
        v = int((qtd or "").strip())
        return v > 0
    except:
        return False