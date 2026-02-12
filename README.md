# ⚡ Automação de Suprimentos – EDP (MVP)

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-ff4b4b.svg)
![Status](https://img.shields.io/badge/Status-MVP%20Funcional-success)

> **Solução escalável para registro automatizado de pedidos de insumos por agências de arrecadação.**

Este projeto substitui processos manuais (ligações e anotações informais) por um fluxo estruturado, rastreável e automatizado, focado na eficiência operacional das agências da **EDP**.

---

## 🧩 O Problema
O processo manual de solicitação de insumos (bobinas, boletos, etc.) gerava:
* **Interrupções constantes** na gestão.
* **Falta de histórico** consolidado para auditoria.
* **Erros de digitação** e anotações incorretas.

## 🚀 A Solução
O sistema oferece um fluxo automatizado que garante:
- [x] **Fluxo Conversacional:** Interface via CLI simulando a experiência do WhatsApp.
- [x] **Validação Inteligente:** Cruzamento automático de agências via base DE-PARA.
- [x] **Protocolo Automático:** Gerado instantaneamente para o solicitante.
- [x] **Dashboard de Gestão:** Visão analítica em tempo real com filtros e métricas.

---

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python
* **Interface Web:** Streamlit (Dashboard)
* **Manipulação de Dados:** Pandas / OpenPyXL
* **Logs & Auditoria:** Logging nativo do Python

---

## 📂 Estrutura do Projeto
```text
automacao_suprimentos/
├── app/
│   ├── core/           # Regras de negócio, validações e logger
│   ├── io/             # Manipulação de arquivos (Excel)
│   ├── dashboard/      # Frontend em Streamlit
│   └── cli_simulator.py# Simulador de fluxo de conversa
├── data/               # Bases de dados (DE-PARA e Pedidos)
├── logs/               # Registros de execução da aplicação
├── requirements.txt    # Dependências do projeto
└── README.md
