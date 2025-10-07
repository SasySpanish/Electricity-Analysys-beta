import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Impostazioni grafiche
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (16,10)

data = pd.read_csv("2005-2023_prod.csv")




# -------------------------
# 2. Statistiche descrittive
# -------------------------
print("Statistiche generali:")
print(data.describe())

# Statistiche per fonte
print("\nStatistiche per fonte:")
print(data.groupby('Fonte').describe())

# Statistiche per regione
print("\nStatistiche per regione:")
print(data.groupby('Regione').describe())

# -------------------------
# 3. Trend nel tempo per fonte
# -------------------------
plt.figure()
sns.lineplot(data=data, x='Anno', y='Produzione(GWh)', hue='Fonte', marker='o')
plt.title("Trend temporale della produzione per Fonte")
plt.ylabel("GWh")
plt.xlabel("Anno")
plt.legend(title="Fonte")
plt.tight_layout()
plt.show()

# -------------------------
# 4. Trend nel tempo per regione (totale fonti)
# -------------------------
data_region_year = data.groupby(['Anno','Regione'])['Produzione(GWh)'].sum().reset_index()
plt.figure()
sns.lineplot(data=data_region_year, x='Anno', y='Produzione(GWh)', hue='Regione', marker='o')
plt.title("Trend totale della produzione per Regione")
plt.ylabel("GWh")
plt.xlabel("Anno")
plt.legend(title="Regione", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()



da=data[(data['Anno'] >= 2005) & (data['Anno'] <= 2015)].head(200)
data.groupby('Anno')['Copertura(GWh)'].sum()
# Controlla righe duplicate esatte
duplicates = data.duplicated()
print("Numero di righe duplicate:", duplicates.sum())

# Controlla valori sospetti (0 o null)
print(data[(data['Copertura(GWh)'] == 0) | (data['Copertura(GWh)'].isna())])


# -------------------------
# 5. Boxplot per Fonte
# -------------------------
plt.figure()
sns.boxplot(data=data, x='Fonte', y='Produzione(GWh)')
plt.title("Distribuzione della produzione per Fonte (2005-2023)")
plt.ylabel("GWh")
plt.xlabel("Fonte")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -------------------------
# 6. Boxplot per Regione
# -------------------------
plt.figure()
sns.boxplot(data=data, x='Regione', y='Copertura(GWh)')
plt.title("Distribuzione della copertura per Regione (2005-2023)")
plt.ylabel("GWh")
plt.xlabel("Regione")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -------------------------
# 7. Heatmap della copertura per regione e anno
# -------------------------
pivot_table = data_region_year.pivot(index='Regione', columns='Anno', values='Produzione(GWh)')
plt.figure(figsize=(14,8))
sns.heatmap(pivot_table, annot=True, fmt=".0f", cmap="YlGnBu")
plt.title("Heatmap della produzione per Regione e Anno")
plt.ylabel("Regione")
plt.xlabel("Anno")
plt.tight_layout()
plt.show()

# -------------------------
# 8. Percentuale di ciascuna fonte per anno
# -------------------------
data_year_source = data.groupby(['Anno','Fonte'])['Produzione(GWh)'].sum().reset_index()
data_year_total = data_year_source.groupby('Anno')['Produzione(GWh)'].sum().reset_index().rename(columns={'CoperturaGWh':'TotaleGWh'})
data_merge = pd.merge(data_year_source, data_year_total, on='Anno')
data_merge['Percentuale'] = data_merge['Produzione(GWh)_x'] / data_merge['Produzione(GWh)_y'] * 100


plt.figure()
sns.lineplot(data=data_merge, x='Anno', y='Percentuale', hue='Fonte', marker='o')
plt.title("Percentuale di ciascuna Fonte per Anno")
plt.ylabel("% sul totale annuo")
plt.xlabel("Anno")
plt.legend(title="Fonte")
plt.tight_layout()
plt.show()


print(data_merge.columns)