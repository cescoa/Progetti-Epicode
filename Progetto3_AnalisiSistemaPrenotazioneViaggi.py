
"""Progetto 3 di Python Analisi per un Sistema di Prenotazione Viaggi"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


"""Parte 1 – Variabili e Tipi di Dati"""

nome = "Mario Rossi"
età = 20
saldo_conto = 500.45
vip = True
destinazioni = ["Roma", "Londra", "New York", "Parigi", "Madrid"]
destinazione_prezzo = {"Roma" : 200, "Londra" : 800, "New York" : 20000, "Parigi" : 450, "Madrid" : 500}


"""Punto 2 - Programmazione ad Oggetti (OOP)"""


class Clienti:
    def __init__(self, nome, eta, vip):
        self.nome = nome
        self.eta = eta
        self.vip = vip

    def info_clienti(self):
        print(f"Nome cliente: {self.nome} \n Età: {self.eta} \n Utente VIP: {self.vip}")

class Viaggio:
    def __init__(self, destinazione, prezzo, durata_giorni):
        self.destinazione = destinazione
        self.prezzo = prezzo
        self.durata_giorni = durata_giorni

class Prenotazione:
    def __init__(self, cliente, viaggio):
        self.cliente = cliente
        self.viaggio = viaggio
        self.prezzo_viaggio = 0

    def calcolo_prezzo(self):
        if self.cliente.vip == True:
            self.prezzo_viaggio = self.viaggio.prezzo * 0.90
            print(f"Sei un utente VIP, il prezzo del viaggio è: {self.prezzo_viaggio}")
        else:
            prezzo_viaggio = self.viaggio.prezzo
            print(f"Non sei un utente VIP, il prezzo del viaggio è: {self.prezzo_viaggio}")

        return self.prezzo_viaggio

    def dettagli(self):
        print(f"L'utente {self.cliente.nome} ha aquistato il viaggio a {self.viaggio.destinazione} e ha pagato {self.prezzo_viaggio}€ \n")

cliente1 = Clienti("Luca Verdi", 25, True)
viaggio1 = Viaggio("Parigi", 500, 5)
prenotazione1 = Prenotazione(cliente1, viaggio1)
prenotazione1.calcolo_prezzo()
print("\n I dettagli del viaggio sono: \n")
prenotazione1.dettagli()


"""Parte 3 – NumPy"""

prenotazioni_ricevute = np.random.randint(200, 2001, 100)

prezzo_medio=np.mean(prenotazioni_ricevute)
prezzo_massimo = np.max(prenotazioni_ricevute)
prezzo_minimo = np.min(prenotazioni_ricevute)
prezzo_deviazione_standard = np.std(prenotazioni_ricevute)
numero_prenotazioni_sopra_media = np.sum(prenotazioni_ricevute > prezzo_medio)
percentuale_sopra_media = (numero_prenotazioni_sopra_media/len(prenotazioni_ricevute))*100
print(prenotazioni_ricevute)
print(f"\n Il prezzo medio è: {prezzo_medio} \n")
print(f"\n Il prezzo minimo è: {prezzo_minimo} \n")
print(f"\n Il prezzo massimo è: {prezzo_massimo} \n")
print(f"\n La deviazione standard  è: {prezzo_deviazione_standard} \n")
print(f"La percentuale di prenotazioni sopra la media è: {percentuale_sopra_media}% \n")

""" Parte 4 – Pandas """

dati = {
    "Cliente" : ["Luca Bianchi", "Giulia Ferrari", "Andrea Esposito", "Francesca Romano", "Alessandro Ricci", "Elena Marino", "Matteo Greco", "Sara Bruno", "Federico Galli", "Chiara Conti"],
    "Destinazione": ["Madrid", "Parigi", "Roma", "New York", "Madrid", "Berlino", "Tokyo", "Madrid", "Roma", "Amsterdam"],
    "Prezzo" : [850, 1000, 1110, 1250, 850, 1150, 1500, 370, 800, 1100],
    "Giorno_Partenza" : ["2026-01-01", "2026-04-05", "2026-05-01", "2026-06-02", "2026-06-08", "2026-07-19", "2026-08-12", "2026-08-15", "2026-11-01", "2026-12-25"],  
    "Durata" : [5, 4, 6, 3, 5, 7, 8, 2, 4, 4],
    "Incasso" : [850, 1000, 1110, 1250, 850, 1150, 1500, 370, 800, 1100]
}

df = pd.DataFrame(dati)
totale_incasso = df["Incasso"].sum()
incasso_medio_destinazione = df.groupby("Destinazione")["Incasso"].mean()
top_3 = df['Destinazione'].value_counts().head(3)
print(df)
print(f"L'incasso totale è : {totale_incasso}")
print(f"L'incasso medio per destinazione è: {incasso_medio_destinazione}")
print(f"Le 3 destinazioni più vendute sono: {top_3}")


""" Parte 5 – Matplotlib """

incasso_per_destinazione = df.groupby("Destinazione")["Incasso"].sum()

plt.bar(incasso_per_destinazione.index, incasso_per_destinazione.values, color = "green")
plt.title("Incasso per ogni destinazione")
plt.show()

# Andamento basato sull'ordine delle righe nel dataframe
plt.plot(df['Incasso'], marker='o', linestyle='-', color='green')
plt.title('Andamento Giornaliero degli Incassi')
plt.ylabel('Incasso (€)')
plt.xlabel('Ordine Temporale / Giorno')
plt.grid(True)
plt.show()

# Contiamo le occorrenze
vendite_count = df['Destinazione'].value_counts()

# Creazione del grafico a torta
plt.pie(vendite_count, labels=vendite_count.index, autopct='%1.1f%%', startangle=140)
plt.title('Percentuale di Vendite per Destinazione')
"""plt.ylabel('') # Rimuove l'etichetta verticale per estetica"""
plt.show()


""" Parte 6 – Analisi Avanzata """

mappa_categorie = {
    "Madrid" : "Europa",
    "Roma" : "Europa",
    "Parigi": "Europa",
    "Tokyo" : "Asia",
    "Amsterdam" : "Europa",
    "New York" : "America"
}

df["Categoria"] = df["Destinazione"].map(mappa_categorie)

analisi = df.groupby("Categoria").agg({
    "Incasso" : "sum",
    "Durata" : "mean"
})

print("\n--- Analisi per Categoria ---")
print(analisi)

df.to_csv("prenotazioni_analizzate.csv", index=False)
print("\nFile 'prenotazioni_analizzate.csv' creato con successo!")

""" Parte 7 – Estensioni """

def top_clienti(dataframe, n):
    return dataframe['Cliente'].value_counts().head(n)

n = 3
print(f"\nI {n} clienti con più prenotazioni sono:")
print(top_clienti(df, n))


# --- Parte 7: Grafico Combinato ---

# 1. Prepariamo i dati calcolando le medie per categoria
stats_grafico = df.groupby("Categoria").agg({
    "Incasso": "mean",
    "Durata": "mean"
})

# 2. Creiamo la figura e il primo asse (ax1)
fig, ax1 = plt.subplots(figsize=(10, 6))

# BARRE: asse X = i nomi delle categorie, asse Y = l'incasso medio
ax1.bar(stats_grafico.index, stats_grafico['Incasso'], color='skyblue', label='Incasso Medio (€)')
ax1.set_xlabel('Categoria')
ax1.set_ylabel('Incasso Medio (€)', color='blue')

# 3. Creiamo il secondo asse (ax2) che condivide la stessa X
ax2 = ax1.twinx()

# LINEA: asse X = i nomi, asse Y = la durata media
ax2.plot(stats_grafico.index, stats_grafico['Durata'], color='red', marker='o', linewidth=2, label='Durata Media (Giorni)')
ax2.set_ylabel('Durata Media (Giorni)', color='red')

plt.title('Analisi Incasso e Durata per Categoria')
plt.show()