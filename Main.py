from LoadAndClean import *
from Analyze import *
from Visualize import *

def main():
    input_path = 'C:/Users/sdumz/Desktop/domaintel/data/whois-db-download-info-sample.csv'
    # outputPath = 'C:/Users/sdumz/Desktop/domaintel/data/whois-db-download-info-cleaned.csv'
    df = load_and_clean(input_path)
    # print(df.head(20).to_string())
    states = state_counts(df)
    admin_countries = admin_country(df)
    whois_servers = whois_servers_count(df)
    domains = whois_servers_domains(df)
    # print(whois_servers)
    plot_bar(states,"Domains per Registrant State","State","Domains","registrant_state_counts.png")
    plot_pie(admin_countries,'Majority of Administrative Countries','major_admin_countries.png')
    plot_pie(whois_servers,'whois Servers Domination','major_whois_servers.png')
    plot_bar(domains,'Most abused TLDs','Domains','','whois_servers_domains.png')


if __name__ == '__main__':
    main()