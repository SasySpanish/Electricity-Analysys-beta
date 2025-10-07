import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Carico e pulisco nan
dataprod = pd.read_csv("C:/Users/Utente/Desktop/datacoperturadomanda/produzione/2005-2023_prod.csv")
dataprod["Anno"] = dataprod["Anno"].dropna()
dataprod["Anno"] = pd.to_numeric(dataprod["Anno"], errors="coerce")
dataprod = dataprod[dataprod["Anno"].notna()]
dataprod["Anno"] = dataprod["Anno"].astype(int)
dataprod = dataprod[dataprod["Anno"] != 2005]
dataprod = dataprod[~dataprod["Produzione(GWh)"].astype(str).str.startswith("nan")]

datacover = pd.read_csv("C:/Users/Utente/Desktop/datacoperturadomanda/copertura/2005-2023.csv")
datacover["Anno"] = datacover["Anno"].dropna()
datacover = datacover[~datacover["Copertura(GWh)"].astype(str).str.startswith("nan")]
datacover = datacover[~datacover["Anno"].astype(str).str.startswith("A")]
datacover["Anno"] = datacover["Anno"].astype(int)

#Rimuovo o sommo variabili
#dataprod
dataprod["Fonte"] = dataprod["Fonte"].replace({
    "Termoelettrico": "Geotermoelettrico"
})

#datacover
datacover["Fonte"] = datacover["Fonte"].replace({
    "Termoelettrico tradizionale": "Geotermoelettrico"
})
datacover["Fonte"] = datacover["Fonte"].replace({
    "Idrico tradizionale": "Idrico",
    "Idrico rinnovabile": "Idrico"
})

datacover = datacover[datacover["Fonte"].str.strip().str.lower() != "saldo import/export"]
datacover = datacover[datacover["Fonte"].str.strip().str.lower() != "bioenergie"]


#Riunisco per anno reg e fonte

dataprod_grouped = (
    dataprod.groupby(["Anno", "Regione", "Fonte"], as_index=False)["Produzione(GWh)"]
    .sum()
)
datacover_grouped = (
    datacover.groupby(["Anno", "Regione", "Fonte"], as_index=False)["Copertura(GWh)"]
    .sum()
)



dataprod_grouped["Anno"] = dataprod_grouped["Anno"].astype(int)
datacover_grouped["Anno"] = datacover_grouped["Anno"].astype(int)

#######Merge
df_copertura = datacover_grouped
df_produzione = dataprod_grouped

# Uniformiamo il tipo di dato della colonna 'Anno'
#df_copertura["Anno"] = df_copertura["Anno"].astype(str).str.extract(r'(\d{4})')[0].astype(int)
#df_produzione["Anno"] = df_produzione["Anno"].astype(str).str.extract(r'(\d{4})')[0].astype(int)



# Merge dei due dataset
df_merged = pd.merge(df_copertura, df_produzione, on=["Regione", "Anno","Fonte"], how="inner")

# Calcolo del saldo energetico (positivo = esportatore, negativo = importatore)
df_merged["SaldoEnergetico"] = df_merged["Produzione(GWh)"] - df_merged["Copertura(GWh)"]

# Crea una nuova colonna con il tasso di copertura in percentuale
df_merged["Tasso_copertura(%)"] = (
    df_merged["Copertura(GWh)"] / df_merged["Produzione(GWh)"] * 100
)

df_finale=df_merged

import numpy as np

df_finale["Tasso_copertura(%)"] = np.where(
    (df_finale["Produzione(GWh)"].isna()) | (df_finale["Produzione(GWh)"] == 0),
    np.nan,
    df_finale["Copertura(GWh)"] / df_finale["Produzione(GWh)"] * 100
)

df_finale.to_csv("merge_produzione_copertura_con_tasso.csv", index=False)
df_finale.to_excel("merge_produzione_copertura_con_tasso.xlsx", index=False)


