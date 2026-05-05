import pandas as pd
import oracledb
from datetime import datetime

# carregar CSV
df = pd.read_csv("data/stocks_raw.csv")

# ajustar colunas
df.columns = ["ticker", "date", "open", "high", "low", "close", "volume"]

df['date'] = pd.to_datetime(df['date'])

# conexão
conn = oracledb.connect(
    user="SEU_USER",
    password="SUA_SENHA",
    dsn="oracle.fiap.com.br:1521/ORCL"
)

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO RAW_STOCKS 
        (ticker, data, open, high, low, close, volume, data_carga)
        VALUES (:1, :2, :3, :4, :5, :6, :7, :8)
    """, [
        row['ticker'],
        row['date'],
        row['open'],
        row['high'],
        row['low'],
        row['close'],
        row['volume'],
        datetime.now()
    ])

conn.commit()
cursor.close()
conn.close()
