import database as db
import funzioni_interfaccia as fi

def menu():

    while True:

        print("\n--- MENU ---")
        print("1. Aggiungi.")
        print("2. Visualizza.")
        print("3. Ricerca.")
        print("4. Modifica.")
        print("5. Elimina.")
        print("6. Elimina più elementi.")
        print("7. Esci.")

        scelta = input("\nDigita un numero corrispondente all'operazione desiderata: ")

        if scelta == "1":
            titolo = input("\nInserisci il titolo del libro: ").title().strip() 
            autore = input("Inserisci l'autore del libro: ").title().strip()
            genere = input("Inserisci il genere del libro: ").capitalize().strip()
            anno = int(input("Inserisci l'anno di pubblicazione del libro: "))
            disponibilita = int(input("Inserisci la disponibilita del libro: "))

            db.aggiungi(titolo=titolo, autore=autore, genere=genere, anno=anno, disponibilita=disponibilita)

        elif scelta == "2":
            db.visualizza()

        elif scelta == "3":
            db.visualizza()
            fi.interfaccia_ricerca()

        elif scelta == "4":
            db.visualizza()
            
            print("\nLa selezione dell'elemento da modificare avviene tramite ID.")
            
            utente = input("Vuoi effettuare una ricerca specifica? (SI/NO) --> ").lower().strip()
            
            if utente == "si" or utente == "sì":
                fi.interfaccia_ricerca()

            id_modifica = int(input("Inserisci ID corrispondente all'elemento a cui apportare modifiche: "))
            
            fi.interfaccia_modifica(id_modifica=id_modifica)

        elif scelta == "5":
            db.visualizza()

            print("\nLa selezione dell'elemento da eliminare avviene tramite ID.")
            
            utente = input("Vuoi effettuare una ricerca specifica? (SI/NO) --> ").lower().strip()
            
            if utente == "si" or utente == "sì":
                fi.interfaccia_ricerca()

            id_elimina = int(input("Inserisci l'ID corrispondente all'elemento che vuoi eliminare: "))
            
            db.elimina(id_elimina)

        elif scelta == "6":
            db.visualizza()

            print("\nLa selezione degli elementi da eliminare avviene tramite ID.")
            
            utente = input("Vuoi effettuare una ricerca specifica? (SI/NO) --> ").lower().strip()
            
            if utente == "si" or utente == "sì":
                fi.interfaccia_ricerca()           

            lista_id_utente = input("Inserisci gli ID che vuoi eliminare separati da una virgola: ")
            lista_id = [int(id.strip()) for id in lista_id_utente.split(",")]  
            
            db.elimina_more(lista_id)

        elif scelta == "7":
            print("Uscita in corso...")
            break