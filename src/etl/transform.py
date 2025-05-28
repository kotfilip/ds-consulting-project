def preprocess_data(df):
    df['covid_period'] = (df['year'] >= 2020).astype(int)
    # Dodaj inne przekształcenia według potrzeb
    return df