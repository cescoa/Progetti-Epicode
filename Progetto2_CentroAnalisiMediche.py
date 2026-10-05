import numpy as np

"""Parte 1 – Variabili e Tipi di Dati"""

nome= "Luca"
cognome = "Rossi"
età = "38"
codice_fiscale = "qwerty27gb23"
peso_paziente = 70.5
analisi = ["emocromo", "glicemia", "colesterolo"]

nome1= "Mario"
cognome1 = "Verdi"
età1 = "24"
codice_fiscale1 = "qwerty27gb23"
peso_paziente1 = 65.8
analisi1 = ["transaminasi", "urine", "colesterolo"]

nome2= "Anna"
cognome2 = "Bianchi"
età2 = "33"
codice_fiscale2 = "qwerty27gb23"
peso_paziente2 = 56.5
analisi2 = ["creatinina", "emocromo"]

"""Parte 2 – Classi e OOP"""
print("\n Parte 2 del progetto \n")

class Paziente:
    def __init__(self, nome, cognome, codice_fiscale, eta, peso, analisi_effettuate, risultati_analisi):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.eta = eta
        self.peso = peso
        self.analisi_effettuate = analisi_effettuate
        self.risultati_analisi = risultati_analisi

    def scheda_personale(self):
        return(f"I dati del paziente sono: \n Nome: {self.nome}\n Cognome: {self.cognome} \n Età: {self.eta} \n Codice Fiscale: {self.codice_fiscale}")

    def statistiche_analisi(self):
        return(f"Le statistiche per il paziente {self.nome} sono: \n Il valore minimo è {self.risultati_analisi.min()} \n Il valore massimo è {self.risultati_analisi.max()} \n La devizione standard è {self.risultati_analisi.std()} \n")

class Medico:
    def __init__(self, nome, cognome, specializzazione):
        self.nome = nome
        self.cognome = cognome
        self.specializzazione = specializzazione

    def visita_paziente(self,paziente):
        print(f"Il/la Dott/Dott.ssa {self.cognome} sta visitando il paziente {paziente.nome} \n")

class Analisi:
    def __init__(self, tipo, risultato):
        self.tipo = tipo
        self.risultato = risultato

    def valuta(self):
        if self.tipo.lower() == "colesterolo":
            if self.risultato <= 100:
                return "Nella norma"
            else:
                return "Valore alto"
        else:
            if self.risultato <= 200:
                return "Nella norma"
            else:
                return "Valore alto"

analisi1 = Analisi("glicemia", 90)
analisi2 = Analisi("colesterolo", 210)        
medico1 = Medico("Giulio", "Verde", "Fisioterapista")
risultati_paziente1 = np.array([78, 100])
paziente1 = Paziente("Marco", "Rossi", "qwerty749sb", 36, 76.8, [analisi1, analisi2], risultati_paziente1)
print(paziente1.scheda_personale())
medico1.visita_paziente(paziente1)
print(paziente1.statistiche_analisi())

for a in paziente1.analisi_effettuate:
    print(f"Analisi: {a.tipo}, Risultato: {a.risultato} -> Esito: {a.valuta()}")


    """Parte 3 – Uso di NumPy"""
print("\n Parte 3 del progetto \n")

risultati_emocromo = np.array([112, 129, 200, 89, 53, 178, 250, 265, 100, 98])


valore_medio = risultati_emocromo.mean()
valore_minimo = risultati_emocromo.min()
valore_massimo = risultati_emocromo.max()
valore_deviazione_standard = risultati_emocromo.std()
print(f"Il valore minimo è {valore_minimo} \n Il valore massimo è {valore_massimo} \n La devizione standard è {valore_deviazione_standard}")

"""Parte 5 – Applicazione completa"""

print("\n----------------------Gestione Clinica--------------------------------")

pazienti = [Paziente("Luca", "Rossi", "RSSLCU88", 38, 70.5, [Analisi("Glicemia", 90)], np.array([80, 95, 110])),
    Paziente("Anna", "Bianchi", "BNCNNA93", 33, 56.0, [Analisi("Colesterolo", 210)], np.array([190, 215, 230])),
    Paziente("Mario", "Verdi", "VRDMRA02", 24, 65.8, [Analisi("Urine", 10)], np.array([12, 15, 9])),
    Paziente("Elena", "Gialli", "GLLLN85", 41, 62.3, [Analisi("Glicemia", 105)], np.array([100, 108, 112])),
    Paziente("Paolo", "Neri", "NREPLA75", 51, 88.4, [Analisi("Colesterolo", 180)], np.array([170, 175, 190]))]
medici  = [Medico("Luca", "Bianco", "Cardiologo"), 
           Medico("Marco", "Viola", "Fisioterapista"), 
           Medico("Anna", "Giallo", "Endocrinologa")]


for i in range(len(pazienti)):
    p = pazienti[i]
    
    # Scegliamo un medico a rotazione 
    # Usiamo l'operatore % per distribuire i pazienti tra i 3 medici
    medico_di_turno = medici[i % 3] 
    
    print("-" * 30)
    # Stampa scheda 
    print(p.scheda_personale())
    
    # Mostra visita 
    medico_di_turno.visita_paziente(p)
    
    # Stampa statistiche 
    print("Statistiche Analisi:")
    print(p.statistiche_analisi())
    print("-" * 30 + "\n")