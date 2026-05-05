# Market Intelligence - Dados Financeiros

## Objetivo
Este projeto complementa a plataforma de dados do banco digital, adicionando uma camada de inteligência de mercado baseada em notícias financeiras.

## Ideia
Analisar o volume e o tema das notícias relacionadas a indicadores econômicos como SELIC, inflação e juros.

## Arquitetura

```mermaid
flowchart LR
    A[SerpAPI Notícias] --> B[Python Ingestion]
    B --> C[RAW_NOTICIAS]

    C --> D[Lower / Clean Text]
    D --> E[TRUSTED_NOTICIAS]

    E --> F[Classificação por Tema]
    F --> G[REFINED_NOTICIAS]

    G --> H[Insights]
    H --> I[Dashboard]

```

## Tecnologias
- Python
- Oracle
- SQL
- SerpAPI

## Resultados esperados
- Volume de notícias por tema
- Tendência de assuntos financeiros
