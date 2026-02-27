# app/core/validators.py
def validar_agencia(codigo: str, df_depara):

    match = df_depara[
        df_depara["codigo_agencia"]
        .astype(str)
        .str.upper() == str(codigo).upper()
    ]

    if match.empty:
        return None

    row = match.iloc[0]

    return {
        "codigo_agencia": row["codigo_agencia"],
        "nome_agencia": row["nome_agencia"],
        "email": row.get("email_responsavel", ""),
        "dono": row.get("dono_area", "")
    }

def validar_insumo(insumo: str):
    catalogo = {
        "BOBINA 57MM",
        "BOBINA 80MM",
        "BOLETO",
        "PAPEL A4",
        "ENVELOPE",
        "LACRE MALOTE",
        "FORMULÁRIO",
        "TONER",
        "OUTRO"
    }
    return (insumo or "").strip().upper() in catalogo

def validar_quantidade(qtd: str):
    try:
        v = int((qtd or "").strip())
        return v > 0
    except:
        return False