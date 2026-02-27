import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")


def enviar_email(destinatario, pedido):

    if not destinatario:
        print("Sem email para envio")
        return

    corpo = f"""
📦 NOVO PEDIDO DE INSUMO

🏢 Agência: {pedido['nome_agencia']}
🔢 Código: {pedido['codigo_agencia']}

📋 Insumo: {pedido['insumo']}
📦 Quantidade: {pedido['quantidade']}

👤 Solicitante: {pedido['solicitante']}

📅 Data: {pedido['data_hora']}
🧾 Protocolo: {pedido['protocolo']}

---
Sistema de Insumos EDP
"""

    msg = MIMEText(corpo)

    msg["Subject"] = f"Pedido de Insumo - {pedido['nome_agencia']}"
    msg["From"] = EMAIL_USER
    msg["To"] = destinatario

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            load_dotenv(dotenv_path=".env")  
            server.login(
                EMAIL_USER,
                EMAIL_PASS
            )

            server.send_message(msg)

        print("Email enviado para:", destinatario)

    except Exception as e:
        print("Erro ao enviar email:", e)

