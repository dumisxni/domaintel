import pandas as pd


df = pd.read_csv('C:/Users/sdumz/Desktop/domaintel/data/whois-db-download-info-sample.csv')


new_df = df.dropna(axis=1, how='all').copy()
new_df = new_df.drop(['registrant_fax','administrativeContact_fax'], axis=1)
new_df['registrant_organization'] = new_df['registrant_organization'].fillna('unknown')
