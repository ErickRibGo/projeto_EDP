# app/io/excel_store.py
import pandas as pd
from pathlib import Path
from .paths import PEDIDOS_XLSX, DEPARA_XLSX, DATA_DIR
from app.core.logger import get_logger

ENGINE = "openpyxl"
logger = get_logger("excel_store")

def garantir_planilhas():
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        if not PEDIDOS_XLSX.exists():
            cols = ["protocolo","data_hora","codigo_agencia","nome_agencia",
                    "insumo","quantidade","solicitante","canal","status"]
            pd.DataFrame(columns=cols).to_excel(PEDIDOS_XLSX, index=False, engine=ENGINE)
            logger.info(f"Criado {PEDIDOS_XLSX.name} com cabeçalho padrão.")

        if not DEPARA_XLSX.exists():
            df = pd.DataFrame([
                {"codigo_agencia":"A001","nome_agencia":"Agência Centro","tipo":"Normal"},
                {"codigo_agencia":"A002","nome_agencia":"Agência Praia","tipo":"Independente"},
            ])
            df.to_excel(DEPARA_XLSX, index=False, engine=ENGINE)
            logger.info(f"Criado {DEPARA_XLSX.name} com 2 registros de exemplo.")

    except Exception as e:
        logger.exception(f"Erro garantindo planilhas: {e}")
        raise

def carregar_depara():
    try:
        df = pd.read_excel(DEPARA_XLSX, engine=ENGINE)
        logger.info(f"DE-PARA carregado: {len(df)} agências.")
        return df
    except FileNotFoundError:
        logger.error("Arquivo de DE-PARA não encontrado. Executando garantir_planilhas().")
        garantir_planilhas()
        return pd.read_excel(DEPARA_XLSX, engine=ENGINE)
    except Exception as e:
        logger.exception(f"Erro ao carregar DE-PARA: {e}")
        raise

def append_pedido(registro: dict):
    try:
        df = pd.read_excel(PEDIDOS_XLSX, engine=ENGINE)
        df = pd.concat([df, pd.DataFrame([registro])], ignore_index=True)
        df.to_excel(PEDIDOS_XLSX, index=False, engine=ENGINE)
        logger.info(
            f"Pedido registrado | protocolo={registro.get('protocolo')} "
            f"| agencia={registro.get('codigo_agencia')} "
            f"| insumo={registro.get('insumo')} "
            f"| qtd={registro.get('quantidade')}"
        )
    except Exception as e:
        logger.exception(f"Erro ao gravar pedido: {e}")
        raise