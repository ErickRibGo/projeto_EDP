📘 README — Automação de Suprimentos (MVP)
⚡ Automação de Suprimentos – EDP
MVP para registro automatizado de pedidos de insumos por agências
Este projeto implementa uma solução simples e escalável para automatizar o registro de pedidos de suprimentos (como bobinas e boletos) realizados pelas agências da EDP.
O sistema substitui processos manuais (ex.: ligações e anotações informais) por um fluxo estruturado e rastreável.

Status: MVP funcional — Sprint 1 e Sprint 2 concluídos
Tecnologias: Python · FastAPI · Streamlit · Pandas · OpenPyXL


🧩 Objetivo do Projeto
As agências da EDP solicitam insumos operacionalmente. O processo manual gera:

Interrupções constantes à gestão
Falta de histórico consolidado
Dificuldade de auditoria
Riscos de anotação incorreta

Este MVP resolve isso criando um sistema automatizado com:
✔ Fluxo conversacional estruturado
✔ Validação automática de agências via DE-PARA
✔ Registro centralizado de pedidos
✔ Geração de protocolo
✔ Dashboard interativo para visualização dos dados

🧱 Funcionalidades (Sprint 1 + Sprint 2)
✅ Sprint 1 – Fundação da Solução

Validação de agência via planilha DE‑PARA
Seleção de insumo (Bobina / Boleto)
Validação de quantidade
Geração de protocolo automático
Registro completo do pedido em Excel (pedidos.xlsx)
Simulador CLI com fluxo orientado
Estrutura modular e organizada

🚀 Sprint 2 – Maturidade e Observabilidade

Adição de sistema de logs (/logs/app.log)
Tratamento de erros (try/except)
Melhorias de UX no simulador
Criação de dashboard Streamlit com:

filtros
métricas
gráficos
tabela ordenada


Criação de camada de persistência robusta
Criação automática das planilhas, se ausentes


📂 Estrutura do Projeto
automacao_suprimentos/
│
├─ app/
│  ├─ core/                # Regras de negócio (validações, protocolo, logger)
│  ├─ io/                  # Entrada/saída de dados (planilhas)
│  ├─ dashboard/           # Aplicação Streamlit
│  ├─ cli_simulator.py     # Simulador de conversa (WhatsApp-like)
│
├─ data/                   # Planilhas usadas no MVP (DE-PARA e pedidos)
├─ logs/                   # Arquivos de log
├─ requirements.txt        # Dependências do projeto
└─ README.md
