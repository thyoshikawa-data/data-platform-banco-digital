import requests
import pandas as pd

# API SELIC diária
URL = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json"

def extract():
    response = requests.get(URL)
    response.raise_for_status()
    return response.json()

def transform(data):
    df = pd.DataFrame(data)

    # ajuste de tipos
    df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
    df['valor'] = df['valor'].astype(float)

    # ordenação
    df = df.sort_values('data')

    return df

def load(df):
    # grava
    df.to_csv("selic_raw.csv", index=False)
    print("Arquivo salvo como selic_raw.csv")

if __name__ == "__main__":
    data = extract()
    df = transform(data)
    load(df)

    print(df.head())
