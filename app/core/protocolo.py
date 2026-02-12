from datetime import datetime

def gerar_protocolo(prefixo="SUP"):
    base = datetime.now().strftime("%Y%m%d")
    sequencial = datetime.now().strftime("%H%M%S")
    return f"{prefixo}-{base}-{sequencial}"