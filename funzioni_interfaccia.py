import database as db

def interfaccia_ricerca():
    
        print("\n1. Ricerca tramite ID.")
        print("2. Ricerca per altri criteri (es. titolo, autore ecc..).")
        print("3. ANNULLA.")
    
        fai_ricerca = input("\nDigita un numero corrispondente all'operazione desiderata: ")

        if fai_ricerca == "1":
            ricerca_id = int(input("\nInserisci l'ID del libro che vuoi filtrare: "))
            libro_trovato = db.ricerca(id_libro=ricerca_id, titolo=None, autore=None, genere=None, anno=None, disponibilita=None)
            db.visualizza(record=libro_trovato)

        elif fai_ricerca == "2":
            titolo = input("\nInserisci il titolo del libro (lascia vuoto se non vuoi cercare per titolo): ").title().strip()
            autore = input("Inserisci l'autore del libro (lascia vuoto se non vuoi cercare per autore): ").title().strip()
            genere = input("Inserisci il genere del libro (lascia vuoto se non vuoi cercare per genere): ").capitalize().strip()
            anno = input("Inserisci l'anno di pubblicazione del libro (lascia vuoto se non vuoi cercare per anno): ").strip()
            disponibilita = input("Inserisci la disponibilità (lascia vuoto se non vuoi cercare per disponibilità): ").strip()

            anno = int(anno) if anno else None
            disponibilita = int(disponibilita) if disponibilita else None
            
            risultati = db.ricerca(id_libro=None, titolo=titolo, autore=autore, genere=genere, anno=anno, disponibilita=disponibilita)
            db.visualizza(record=risultati)
        
        elif fai_ricerca == "3":
            print("Ricerca annullata. Torno al menu principale.")
            return
    
def interfaccia_modifica(id_modifica):
    
    libro_trovato = db.ricerca(id_libro=id_modifica, titolo=None, autore=None, genere=None, anno=None, disponibilita=None)
    
    if libro_trovato:
        record = libro_trovato[0]  
        
        print("\nDettagli del record selezionato:")
        print(f"ID: {record[0]}")
        print(f"Titolo: {record[1]}")
        print(f"Autore: {record[2]}")
        print(f"Genere: {record[3]}")
        print(f"Anno: {record[4]}")
        print(f"Disponibilità: {record[5]}")

        print(f"\nModifica i campi (lascia vuoto per mantenere il valore attuale):")
        
        nuovo_titolo = input(f"\nTitolo attuale ({record[1]}): ").title().strip()
        nuovo_autore = input(f"Autore attuale ({record[2]}): ").title().strip()
        nuovo_genere = input(f"Genere attuale ({record[3]}): ").capitalize().strip()
        nuovo_anno = input(f"Anno attuale ({record[4]}): ").strip()
        nuova_disponibilita = input(f"Disponibilità attuale ({record[5]}): ").strip()

        titolo = nuovo_titolo if nuovo_titolo else record[1]
        autore = nuovo_autore if nuovo_autore else record[2]
        genere = nuovo_genere if nuovo_genere else record[3]
        anno = int(nuovo_anno) if nuovo_anno and nuovo_anno.strip() else record[4]
        disponibilita = int(nuova_disponibilita) if nuova_disponibilita and nuova_disponibilita.strip() else record[5]

        db.modifica(id_modifica, titolo, autore, genere, anno, disponibilita)

    else:
        print(f"Nessun record trovato con ID {id_modifica}.")
