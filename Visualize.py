import matplotlib.pyplot as plt


def plot_bar(data, title, xlabel, ylabel, filename):
    plt.figure(figsize=(14,7))
    data.plot(kind='bar')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(f"visualizations/{filename}")
    plt.close()

def plot_pie(data, title, filename):
    plt.figure(figsize=(8,8))
    data.plot(kind='pie', autopct='%1.2f%%')
    plt.title(title)
    plt.ylabel('')
    plt.savefig(f"visualizations/{filename}")
    plt.close()