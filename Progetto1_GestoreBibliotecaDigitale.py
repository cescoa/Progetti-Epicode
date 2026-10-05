#Parte 1 – Variabili e tipi di dati ----------------

titolo_libro = "Fattoria degli animali"
numero_copie_disponibili= 15
prezzo_medio = 12.5
disponibilita = True

print(str(titolo_libro))
print(int(numero_copie_disponibili))
print(float(prezzo_medio))
print(bool(disponibilita))

#Parte 2 – Strutture dati --------------------------
print("--------------------------------------------------------------------------------------------")

libri = ["Fattoria degli animali", "Viaggio al centro della terra", "Padre Ricco, Padre Povero", "1984", "Harry Potter e la pietra filosofale"]
libri_disponibilta = {"Fattoria degli animali": 5, "Viaggio al centro della terra" : 8, "Padre Ricco, padre Povero": 2, "1984": 6, "Harry Potter e la pietra filosofale": 11}
utenti_biblioteca = {"Mario Rossi", "Anna Bianchi", "Luca Verdi", "Maria Giallo"}

#Parte 3 – Classi e OOP -----------------------------
print("--------------------------------------------------------------------------------------------")
class Libro:
    def __init__(self, titolo, autore, anno, copie_disponibili):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.copie_disponibili = copie_disponibili

    def info(self):
        return f"Titolo: {self.titolo}\nAutore: {self.autore}\nAnno: {self.anno}\nCopie disponibili: {self.copie_disponibili}"

class Utente:
    def __init__(self, nome, eta, id_utente):
        self.nome = nome
        self.eta = eta
        self.id_utente= id_utente

    def scheda(self):
        return f"Ciao sono {self.nome}, ho {self.eta} anni e il mio ID è {self.id_utente}"

class Prestito:
    def __init__(self, Utente, Libro, giorni):
        self.utente = Utente
        self.libro = Libro
        self.giorni = giorni

    def dettagli(self):
        print (f"L'utente {self.utente.nome} con id {self.utente.id_utente}, ha preso in prestito il libro {self.libro.titolo} per {self.giorni} giorni")
    
def presta_libro(utente, libro, giorni):
    if libro.copie_disponibili >=1:
        libro.copie_disponibili -= 1
        nuovo_prestito = Prestito(utente, libro, giorni)
        print(f"Hai preso in prestito il libro {libro.titolo}, e ora sono disponibili {libro.copie_disponibili} copia/e")
        return nuovo_prestito
    else:
        print(f"Errore! l'utente {utente.nome} non ha trovato il libro {libro.titolo} (Copie esaurite)")
        return None
    

p1 = Utente("Luca", 23, 123)
p2 = Utente("Anna", 26, 124)
p3 = Utente("Mario", 45, 125)
l1 = Libro("Fattoria degli animali", "George Orwell", 1945, 5)
l2 = Libro("Viaggio al centro della terra", "Jules Verne", 2002, 2)
l3 = Libro("Padre Ricco, padre Povero", "Robert Kiyosaki", 2004, 0)
p1_prestito = presta_libro(p1,l1,4)
p2_prestito = presta_libro(p2,l2,5)
p3_prestito = presta_libro(p3,l3,7)
l_list = [l1, l2, l3]
risultato_prestiti = [p1_prestito, p2_prestito, p3_prestito]

print("-------------------------------Dati degli utenti ------------------------------")
print(p1.scheda())
print(p1.scheda())
print(p1.scheda())


print("--------------------------- Prestiti effettuati --------------------------------")
for p in risultato_prestiti:
    if p is not None:
        p.dettagli()
  

print("------------------ Elenco aggiornato libri con disponibilità --------------------")
for libro in l_list:
    print(libro.info())
