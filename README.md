# Portfolio Thales Yoshikawa

## Visão Geral

Este repositório reúne um conjunto de projetos que simulam a construção de uma **plataforma de dados completa**, cobrindo desde ingestão até geração de insights e modelos preditivos.

Os projetos foram desenvolvidos com foco em:

* Engenharia de dados
* Modelagem analítica
* Integração de múltiplas fontes
* Geração de valor para o negócio

---

## Objetivo

Demonstrar na prática a construção de pipelines de dados modernos, alinhados com cenários reais de mercado, utilizando conceitos como:

* Arquitetura Medallion (RAW → TRUSTED → REFINED)
* Integração com APIs
* Análise de dados financeiros
* Machine Learning aplicado a comportamento de clientes

---

## Arquitetura Base

```text
Fontes de Dados (APIs, CSV, Google Sheets)
                ↓
            Ingestão
                ↓
        RAW (dados brutos)
                ↓
     TRUSTED (tratamento)
                ↓
     REFINED (analytics + ML)
                ↓
          Dashboards
```

---

## Projetos

### Projeto 1 — Financial Data Pipeline

Pipeline de dados financeiros com ingestão de indicadores econômicos.

**Principais pontos:**

* Consumo de API externa
* Estruturação em camadas (RAW, TRUSTED, REFINED)
* Modelagem analítica

---

### Projeto 2 — Market Intelligence

Enriquecimento de dados com notícias financeiras.

**Principais pontos:**

* Integração com API (SerpAPI)
* Processamento de texto
* Categorização de notícias

---

### Projeto 3 — Stock Market Analysis

Análise de ações utilizando dados do Google Finance.

**Principais pontos:**

* Coleta via Google Sheets
* Cálculo de volatilidade e retorno
* Pipeline simplificado com ingestão em banco

---

### Projeto 4 — Stock Sentiment Analysis

Análise de sentimento de mercado baseada em notícias por ativo.

**Principais pontos:**

* Coleta de dados por ticker
* Classificação simples de sentimento
* Indicadores de percepção de mercado

---

### Projeto 5 — Growth Analytics Platform

Plataforma completa de análise de comportamento de clientes.

**Principais pontos:**

* Arquitetura Medallion completa
* Segmentação RFM
* KPIs de negócio
* Cohort analysis
* Machine Learning para predição de comportamento

---

## Tecnologias Utilizadas

* SQL (Oracle)
* Python (Pandas, Scikit-learn)
* APIs (REST)
* Google Sheets (GoogleFinance)
* Modelagem de dados
* Machine Learning

---

## Diferenciais

* Projetos conectados formando um ecossistema de dados
* Aplicação de conceitos utilizados em ambientes corporativos
* Foco em problemas reais de negócio
* Integração entre engenharia, analytics e ciência de dados

---


## 👨‍💻 Autor

Portfólio desenvolvido com foco em demonstrar habilidades práticas em engenharia de dados, análise e construção de soluções orientadas a dados.
