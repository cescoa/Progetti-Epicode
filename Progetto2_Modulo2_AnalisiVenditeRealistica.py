import pandas as pd
import numpy as np

#creare DataFrame partendo dai file csv e json

df_ordini = pd.read_csv("ordini.csv")
df_clienti = pd.read_csv("clienti.csv")
df_prodotti = pd.read_json("prodotti.json")

#unire i dataframe

ordini_prodotti = pd.merge(df_ordini, df_prodotti, on ="ProdottoID", how="inner")
df_completo = pd.merge( ordini_prodotti, df_clienti, on = "ClienteID", how="inner")

#ottimizzare i dati

print("Memoria prima dell'ottimizzazione:")
df_completo.info(memory_usage="deep")

df_completo["Quantità"] = df_completo["Quantità"].astype("int32")
df_completo["PrezzoUnitario"] =df_completo["PrezzoUnitario"].astype("float32")
df_completo["ClienteID"] = df_completo["ClienteID"].astype("category")
df_completo["Regione"] = df_completo["Regione"].astype("category")
df_completo["Segmento"] = df_completo["Segmento"].astype("category")
df_completo["ProdottoID"] = df_completo["ProdottoID"].astype("category")
df_completo["DataOrdine"] = pd.to_datetime(df_completo["DataOrdine"])
df_completo["NomeProdotto"] = df_completo["NomeProdotto"].astype("category")
df_completo["Categoria"] = df_completo["Categoria"].astype("category")
df_completo["Fornitore"] = df_completo["Fornitore"].astype("category")

print("\nMemoria dopo l'ottimizzazione:")
df_completo.info(memory_usage="deep")

#creare colonne e filtrare dati

df_completo["ValoreTotale"] = df_completo["PrezzoUnitario"] * df_completo["Quantità"]
print(df_completo)

filtro = df_completo[df_completo["ValoreTotale"] > 100]

print("Acquisti con valore superiore a 100 sono:\n", filtro)