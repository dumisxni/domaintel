def state_counts(df):
    return df['registrant_state'].value_counts().sort_values(ascending=False)
def admin_country(df):
    return df['registrant_country'].value_counts().sort_values(ascending=False)
def whois_servers_count(df):
    return df['whoisServer'].value_counts().sort_values(ascending=False)