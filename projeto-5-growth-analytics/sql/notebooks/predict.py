import pandas as pd
import joblib
from feature_engineering import build_features

df = pd.read_csv("../data/raw.csv")

features = build_features(df)

X = features[['recency', 'frequency', 'monetary']]

model_7d = joblib.load("model_7d.pkl")
model_30d = joblib.load("model_30d.pkl")

features['prob_compra_7d'] = model_7d.predict_proba(X)[:, 1]
features['prob_compra_30d'] = model_30d.predict_proba(X)[:, 1]

route = df.groupby('fk_contact')['place_origin_departure'] \
          .agg(lambda x: x.value_counts().index[0]) \
          .reset_index()

route.columns = ['fk_contact', 'rota_prevista']

final = features.merge(route, on='fk_contact')

final.to_csv("predictions.csv", index=False)
