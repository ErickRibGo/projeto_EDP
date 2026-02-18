from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

from app.io.excel_store import carregar_depara, append_pedido, garantir_planilhas
from app.core.validators import validar_agencia, validar_quantidade
from app.core.protocolo import gerar_protocolo

app = FastAPI(title="API Suprimentos")

class Pedido(BaseModel):
    codigo_agencia: str
    insumo: str
    quantidade: int

@app.get("/validar_agencia/{codigo}")
def validar(codigo: str):
    garantir_planilhas()
    df = carregar_depara()
    agencia = validar_agencia(codigo, df)
    return {"valido": bool(agencia)}

@app.post("/registrar_pedido")
def registrar(pedido: Pedido):
    protocolo = gerar_protocolo()
    registro = {
        "protocolo": protocolo,
        "data_hora": datetime.now().isoformat(timespec="seconds"),
        "codigo_agencia": pedido.codigo_agencia,
        "nome_agencia": "",
        "insumo": pedido.insumo,
        "quantidade": pedido.quantidade,
        "solicitante": "",
        "canal": "WEB",
        "status": "RECEBIDO",
    }
    append_pedido(registro)
    return {"protocolo": protocolo}