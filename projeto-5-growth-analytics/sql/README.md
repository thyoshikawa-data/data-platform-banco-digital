# Growth Analytics Platform

## Visão Geral

Este projeto apresenta a construção de uma **plataforma de dados completa** para análise de comportamento de clientes em um contexto de mobilidade digital (ex: venda de passagens).

A solução foi desenvolvida utilizando **arquitetura Medallion (RAW → TRUSTED → REFINED)**, integrando modelagem de dados, análise de comportamento e machine learning para geração de insights e previsões.

---

## Problema de Negócio

Plataformas digitais possuem:

* Alto volume de usuários
* Grande quantidade de interações
* Baixa conversão em vendas

O desafio é transformar dados brutos em:

*  Insights acionáveis
*  Segmentação de clientes
*  Previsões de comportamento

---

## Arquitetura

```text
RAW (dados brutos)
    ↓
TRUSTED (tratamento e padronização)
    ↓
REFINED (analytics + ML + insights)
```

---

## Camadas de Dados

### RAW

Dados transacionais de compras contendo:

* Identificador do cliente
* Data da compra
* Origem e destino
* Valor da compra (GMV)
* Quantidade de passagens

---

### TRUSTED

Tratamento e enriquecimento dos dados:

* Padronização de rotas
* Identificação de ida e volta
* Limpeza de registros inválidos

---

### REFINED

Camada analítica com alto valor de negócio:

#### KPIs

* Total de clientes
* Total de pedidos
* Receita total
* Ticket médio
* % de viagens ida e volta

---

#### RFM (Recência, Frequência, Monetário)

* Cálculo completo de comportamento de clientes
* Score de 1 a 5
* Base para segmentação

---

#### Segmentação de Clientes

* Campeões
* VIP
* Em risco
* Hibernando
* Regulares

---

#### Cohort Analysis

* Análise de retenção por mês
* Evolução de clientes ao longo do tempo

---

#### Análise de Rotas

* Rotas mais utilizadas
* Receita por rota
* Ticket médio por trajeto

---

#### Predição de Comportamento (Machine Learning)

Modelo desenvolvido em Python com:

* Feature Engineering (RFM)
* Random Forest

Previsões geradas:

* Probabilidade de compra em 7 dias
* Probabilidade de compra em 30 dias
* Rota mais provável

As previsões são persistidas na camada **REFINED** para consumo analítico.

---

## Tecnologias Utilizadas

* SQL (Oracle)
* Python (Pandas, Scikit-learn)
* Modelagem de dados
* Arquitetura Medallion
* Machine Learning

---

## Possibilidades de Uso

* Otimização de campanhas de marketing
* Identificação de clientes de alto valor
* Redução de churn
* Personalização de ofertas
* Recomendação de rotas

---

## Diferenciais do Projeto

* Arquitetura de dados profissional (Medallion)
* Integração de dados + analytics + ML
* Modelagem baseada em problema real de negócio
* Pipeline pronto para evolução em cloud (AWS / Snowflake)


