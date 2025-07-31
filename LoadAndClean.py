import pandas as pd

def load_and_clean(inputPath,outputpath):
    df = pd.read_csv(inputPath)
    new_df = df.dropna(axis=1, how='all').copy()
    new_df = new_df.drop(['registrant_fax','administrativeContact_fax'], axis=1)
    new_df['registrant_organization'] = new_df['registrant_organization'].fillna('unknown')
    new_df = new_df.dropna()
    # print(new_df.head(1000).to_string())
    new_df.to_csv(outputpath)

inputPath = 'C:/Users/sdumz/Desktop/domaintel/data/whois-db-download-info-sample.csv'
outputPath = 'C:/Users/sdumz/Desktop/domaintel/data/whois-db-download-info-cleaned1.csv'

load_and_clean(inputPath,outputPath)