from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
from datetime import datetime

from app.io.excel_store import carregar_depara, append_pedido, garantir_planilhas
from app.core.validators import validar_agencia, validar_quantidade
from app.core.protocolo import gerar_protocolo
from app.services.email_service import enviar_email

app = FastAPI(title="API Suprimentos")


class Pedido(BaseModel):
    codigo_agencia: str
    insumo: str
    quantidade: int
    solicitante: str


# 🔹 ROTA DE VALIDAÇÃO (FALTAVA ESSA)
@app.get("/validar_agencia/{codigo}")
def validar(codigo: str):

    garantir_planilhas()
    df = carregar_depara()

    agencia = validar_agencia(codigo, df)

    if agencia:
        return {
            "valido": True,
            "nome_agencia": agencia["nome_agencia"]
        }

    return {"valido": False}


# 🔹 REGISTRAR PEDIDO
@app.post("/registrar_pedido")
def registrar(pedido: Pedido, background_tasks: BackgroundTasks):

    garantir_planilhas()
    df = carregar_depara()

    agencia = validar_agencia(pedido.codigo_agencia, df)

    if not agencia:
        raise HTTPException(status_code=400, detail="Agência inválida")

    if not validar_quantidade(str(pedido.quantidade)):
        raise HTTPException(status_code=400, detail="Quantidade inválida")

    protocolo = gerar_protocolo()

    registro = {
    "protocolo": protocolo,
    "data_hora": datetime.now().isoformat(timespec="seconds"),
    "codigo_agencia": agencia["codigo_agencia"],
    "nome_agencia": agencia["nome_agencia"],
    "insumo": pedido.insumo,
    "quantidade": pedido.quantidade,
    "solicitante": pedido.solicitante,
    "canal": "WEB",
    "status": "RECEBIDO",
    }

    append_pedido(registro)

    # ENVIO EMAIL
    if agencia.get("email"):
        background_tasks.add_task(
            enviar_email,
            agencia["email"],
            registro
        )

    return {
        "protocolo": protocolo,
        "agencia": agencia["nome_agencia"],
        "email": agencia["email"]
    }