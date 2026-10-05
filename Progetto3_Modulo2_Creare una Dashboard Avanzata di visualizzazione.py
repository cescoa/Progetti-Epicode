import numpy as np
import pandas as pd
import plotly.express as px

np.random.seed(42)
n_samples = 1000

# 1. Date (Order Date e Ship Date)
start_date = pd.to_datetime('2023-01-01')
end_date = pd.to_datetime('2024-12-31')

# Generiamo date casuali per l'ordine
random_days = np.random.randint(0, (end_date - start_date).days, size=n_samples)
order_dates = [start_date + pd.Timedelta(days=int(d)) for d in random_days]

# La data di spedizione è tra 1 e 7 giorni DOPO l'ordine
ship_days = np.random.randint(1, 8, size=n_samples)
ship_dates = [od + pd.Timedelta(days=int(sd)) for od, sd in zip(order_dates, ship_days)]

# 2. Categorie e Sotto-Categorie coerenti
sub_cat_map = {
    'Elettronica': ['Tv', 'Audio', 'Fotocamere'],
    'Telefonia': ['Smartphone', 'Cover', 'Caricatore'],
    'Accessori': ['Mouse', 'Tastiera', 'Cavi', 'Penna USB'],
    'Elettrodomestici': ['Forno', 'Frigorifero', 'Lavatrice', 'Microonde', 'Lavastoviglie']
}

categories = np.random.choice(list(sub_cat_map.keys()), size=n_samples)
sub_categories = [np.random.choice(sub_cat_map[cat]) for cat in categories]

# 3. Regioni e Città coerenti
geo_map = {
    'Italia': ['Milano', 'Roma'],
    'Francia': ['Parigi', 'Nizza'],
    'Spagna': ['Madrid'],
    'Germania': ['Berlino'],
    'Portogallo': ['Lisbona']
}

regions = np.random.choice(list(geo_map.keys()), size=n_samples)
states = [np.random.choice(geo_map[reg]) for reg in regions]

# 4. Quantità, Vendite e Profitti
quantity = np.random.randint(1, 15, size=n_samples) # Quantità realistiche per ordine
unit_price = np.random.uniform(10, 500, size=n_samples)
sales = np.round(quantity * unit_price, 2)

# Profitto basato sul margine di vendita (es. tra -10% e +30%)
profit_margin = np.random.uniform(-0.10, 0.30, size=n_samples)
profit = np.round(sales * profit_margin, 2)

# Creazione del dizionario e del DataFrame
online_store = {
    'Order Date': order_dates,
    'Ship Date': ship_dates,
    'Category': categories,
    'Sub-Category': sub_categories,
    'Sales': sales,
    'Profit': profit,
    'Region': regions,
    'State': states,
    'Quantity': quantity
}

df = pd.DataFrame(online_store)
df.to_csv('online_store_data.csv', index=False)

print(df.head())

# 1 Convertire le colonne data (Order Date, Ship Date) in formato datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# 2 Controllare valori nulli e duplicati
print("--- Controllo Valori Nulli ---")
print(df.isnull().sum())

print("\n--- Controllo Duplicati ---")
print(f"Numero di righe duplicate: {df.duplicated().sum()}")

# 3 Creare la colonna Year dall'Order Date
df['Year'] = df['Order Date'].dt.year

print(df[['Order Date', 'Year', 'Category', 'Sales']].head())

#4 Totale vendite e profitti per anno

analisi_annuale = df.groupby('Year')[['Sales', 'Profit']].sum()
print("--------- Totale vendite e profitti per anno -------------")
print(analisi_annuale)

#5 Top 5 sottocategorie più vendute

sottocategorie_vendute= df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False)
print(sottocategorie_vendute.head(5))



# 1. Raggruppiamo le vendite per Regione
vendite_regione = df.groupby('Region')['Sales'].sum().reset_index()

# 2. Creiamo il grafico interattivo con Plotly
fig = px.bar(
    vendite_regione,
    x='Region',
    y='Sales',
    title='Totale Vendite per Paese',
    color='Sales'
)

# 3. Mostriamo il grafico
fig.show()