import pandas as pd
import matplotlib.pyplot as plt
# pd.options.display.max_rows = 10

df = pd.read_csv('C:/Users/sdumz/Desktop/domaintel/data/whois-db-download-info-sample.csv')

# print(df.head(6).to_string())
# print(df.info())

new_df = df.dropna(axis=1, how='all').copy()
new_df = new_df.drop(['registrant_fax','administrativeContact_fax'], axis=1)
# new_df.fillna({"administrativeContact_fax": 'unknown'}, inplace=True)
new_df['registrant_organization'] = new_df['registrant_organization'].fillna('unknown')
new_df = new_df.dropna()
# printf'('new_df.head(6).to_string()')'
print(new_df.head(1000).to_string())
new_df.to_csv('C:/Users/sdumz/Desktop/domaintel/data/whois-db-download-info-cleaned.csv')
# df.plot(kind = 'scatter', x = 'administrativeContact_telephone', y = 'registrant_telephone')

# plt.show()