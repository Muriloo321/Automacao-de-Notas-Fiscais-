# Automacao-de-Notas-Fiscais

## Análise de Pedidos SAP (ME80FN x KSB1)

Este projeto realiza a consolidação, tratamento e análise de dados provenientes dos relatórios SAP ME80FN e KSB1, com o objetivo de identificar o status de lançamento de pedidos e analisar o comportamento financeiro ao longo do tempo.

O projeto é inspirado em um contexto real de estágio. No entanto, por questões de confidencialidade, os dados utilizados são simulados e diversos elementos foram modificados, incluindo regras de negócio, nomes de colunas e conteúdos das bases.

---

## Objetivo

- Cruzar pedidos (ME80FN) com lançamentos (KSB1)
- Classificar pedidos conforme regras de negócio
- Identificar atrasos e pendências
- Gerar uma tabela analítica consolidada

---

## Tecnologias Utilizadas

- Python
- Pandas
- Jupyter Notebook

---

## Principais Etapas

- Leitura e atualização incremental das bases
- Tratamento e padronização dos dados
- Criação de chaves de identificação (Documento + Item)
- Integração entre ME80FN e KSB1
- Aplicação de regras de negócio
- Agrupamento e análise temporal
- Geração da tabela analítica final

---

## Saída

O projeto gera uma tabela dinâmica contendo:

- Total de pedidos por mês
- Valor financeiro agregado
- Classificação por status de lançamento
- Indicadores percentuais por categoria

---

## Insights Gerados

- Identificação de pedidos sem lançamento (pendentes)
- Análise de atrasos de lançamento (M+1, M+2 e posteriores)
- Monitoramento da eficiência operacional do processo de compras

---

## Observação

Os dados utilizados neste projeto são simulados e não representam informações reais. O objetivo é reproduzir a estrutura e a lógica de um cenário corporativo, preservando a confidencialidade das informações.

---
