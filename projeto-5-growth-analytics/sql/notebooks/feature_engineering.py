import pandas as pd

def build_features(df):

    df['date_purchase'] = pd.to_datetime(df['date_purchase'])

    features = df.groupby('fk_contact').agg({
        'date_purchase': ['max', 'count'],
        'gmv_success': 'sum'
    }).reset_index()

    features.columns = ['fk_contact', 'last_purchase', 'frequency', 'monetary']

    features['recency'] = (pd.Timestamp.today() - features['last_purchase']).dt.days

    return features
