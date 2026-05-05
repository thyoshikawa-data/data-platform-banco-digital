import os
import pandas as pd
import oracledb
from datetime import datetime

# =========================
# CONFIG VIA ENV
# =========================

DB_CONFIG = {
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "dsn": os.getenv("DB_DSN")
}

# =========================
# LOAD CSV
# =========================

df = pd.read_csv("data/stocks_raw.csv")

df.columns = ["ticker", "date", "open", "high", "low", "close", "volume"]
df['date'] = pd.to_datetime(df['date'])

# =========================
# CONEXÃO
# =========================

conn = oracledb.connect(**DB_CONFIG)
cursor = conn.cursor()

# =========================
# INSERT
# =========================

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
