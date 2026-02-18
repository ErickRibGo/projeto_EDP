import requests
API = "http://localhost:8000"

def validar_agencia(codigo):
    r = requests.get(f"{API}/validar_agencia/{codigo}")
    r.raise_for_status()
    return r.json()

def registrar_pedido(codigo, insumo, quantidade):
    payload = {"codigo_agencia": codigo, "insumo": insumo, "quantidade": quantidade}
    r = requests.post(f"{API}/registrar_pedido", json=payload)
    r.raise_for_status()
    return r.json()