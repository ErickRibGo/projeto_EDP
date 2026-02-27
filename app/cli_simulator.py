# app/cli_simulator.py
from datetime import datetime
from app.io.excel_store import garantir_planilhas, carregar_depara, append_pedido
from app.core.validators import validar_agencia, validar_insumo, validar_quantidade
from app.core.protocolo import gerar_protocolo
from app.core.logger import get_logger

logger = get_logger("cli")

def fluxo_atendimento(df_depara):
    _ = input("Cliente: ")  
    print("\nBot: Qual o código da sua agência?")
    codigo = input("Cliente: ").strip().upper()

    print(f"\nBot: O código informado é realmente este: {codigo}?")
    print("1 - Confirmar")
    print("2 - Corrigir")
    opc = input("Cliente: ").strip()
    if opc == "2":
        print("\nBot: Ok! Digite novamente o código correto:")
        codigo = input("Cliente: ").strip().upper()

    agencia = validar_agencia(codigo, df_depara)
    if not agencia:
        print("\nBot: Código não encontrado. Tente novamente mais tarde.")
        logger.warning(f"Agência inválida informada: {codigo}")
        return

    print(f"\nBot: Agência localizada: {agencia['nome_agencia']} ({agencia['codigo_agencia']})")
    print("\nBot: Escolha o insumo desejado:")
    print("1 - Bobina")
    print("2 - Boleto")

    escolha = input("Cliente: ").strip()
    mapa_insumos = {"1": "BOBINA", "2": "BOLETO"}
    if escolha not in mapa_insumos:
        print("\nBot: Opção inválida.")
        logger.warning(f"Insumo inválido (opção={escolha}) para agencia={codigo}")
        return
    insumo = mapa_insumos[escolha]

    print(f"\nBot: Quantas unidades de {insumo} você deseja solicitar?")
    qtd = input("Cliente: ").strip()
    if not validar_quantidade(qtd):
        print("\nBot: Quantidade inválida.")
        logger.warning(f"Quantidade inválida '{qtd}' informada por agencia={codigo}")
        return

    protocolo = gerar_protocolo()
    registro = {
        "protocolo": protocolo,
        "data_hora": datetime.now().isoformat(timespec="seconds"),
        "codigo_agencia": agencia["codigo_agencia"],
        "nome_agencia": agencia["nome_agencia"],
        "insumo": insumo,
        "quantidade": int(qtd),
        "solicitante": "",
        "canal": "CLI",
        "status": "RECEBIDO",
    }
    append_pedido(registro)

    print(f"\nBot: Pedido registrado com sucesso! Protocolo: {protocolo}")

def main():
    print("=== Simulador de Atendimento (Sprint 2) ===\n")
    try:
        garantir_planilhas()
        df_depara = carregar_depara()
    except Exception:
        print("Bot: Erro ao preparar dados. Verifique o log em /logs/app.log")
        return

    while True:
        try:
            fluxo_atendimento(df_depara)
        except Exception:
            print("Bot: Ocorreu um erro inesperado. Verifique os logs e tente novamente.")
            logger.exception("Erro inesperado no fluxo de atendimento")

        print("\nBot: Deseja realizar outro pedido? 1 - Sim | 2 - Não")
        if input("Cliente: ").strip() != "1":
            print("\nBot: Encerrando. Obrigado!")
            break

if __name__ == "__main__":
    main()