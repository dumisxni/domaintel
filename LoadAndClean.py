import pandas as pd


def load_and_clean(inputPath):
    df = pd.read_csv(inputPath)
    new_df = df.dropna(axis=1, how='all').copy()
    new_df = new_df.drop(['registrant_fax', 'administrativeContact_fax'], axis=1)
    new_df['registrant_organization'] = new_df['registrant_organization'].fillna('unknown')
    new_df = new_df.dropna()
    return new_df