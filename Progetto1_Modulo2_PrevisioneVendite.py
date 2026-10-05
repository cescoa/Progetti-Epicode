import pandas as pd
import numpy as np

'''intervallo_date = pd.date_range(start="2025-01-01", end="2025-12-31", freq="D")
dati = {
    "Data": np.random.choice(intervallo_date, size = 100, replace = False ),
    "Prodotto" : np.random.choice(["Televisore", "Computer", "Smartphone", "Cuffie", "Mouse", None, "Tastiera", "Casse"], 100) ,
    "Quantità Vendite" : np.random.randint(1, 10, 100),
    "Prezzo Unitario" : np.round(np.random.uniform(10.5, 1500, 100), 2)
}

df = pd.DataFrame(dati)
print(df)'''

#Parte 1

df = pd.read_csv('Dati_Vendite.csv')
print(df.head())
print(df.info())
print(df.describe())

#Parte 2
media_prezzo = df["Prezzo Unitario"].mean()
df ["Prodotto"] = df["Prodotto"].fillna("Sconosciuto")
df ["Quantità Vendite"] = df["Quantità Vendite"].fillna(0)
df ["Prezzo Unitario"] = df["Prezzo Unitario"].fillna(media_prezzo)

df = df.drop_duplicates()

df['Data'] = pd.to_datetime(df['Data'])
df['Quantità Vendite'] = df['Quantità Vendite'].astype(int)
df['Prezzo Unitario'] = df['Prezzo Unitario'].astype(float)

print(df.info())


#Parte 3

vendite_per_prodotto = df.groupby('Prodotto')['Quantità Vendite'].sum()
print("Vendite totali per prodotto:\n", vendite_per_prodotto)


prodotto_top = vendite_per_prodotto.idxmax()
quantita_top = vendite_per_prodotto.max()
prodotto_flop = vendite_per_prodotto.idxmin()
quantita_flop = vendite_per_prodotto.min()
print(f"Il prodotto più venduto è '{prodotto_top}' con {quantita_top} unità.")
print(f"Il prodotto meno venduto è '{prodotto_flop}' con {quantita_flop} unità.")


vendite_giornaliere = df.groupby('Data')['Quantità Vendite'].sum()
media_giornaliera = vendite_giornaliere.mean()
print(f"La media delle vendite giornaliere è: {media_giornaliera:.2f} unità.")
