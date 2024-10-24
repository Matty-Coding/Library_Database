import sqlite3
import funzioni_interfaccia as fi

def connessione():
    
    conn = sqlite3.connect("Biblioteca.db")
    c = conn.cursor()

    return conn, c

def crea_tabella():
    
    conn, c = connessione()
    
    c.execute("""CREATE TABLE IF NOT EXISTS Libri(
              ID INTEGER PRIMARY KEY AUTOINCREMENT,
              Titolo TEXT NOT NULL,
              Autore TEXT NOT NULL,
              Genere TEXT NOT NULL,
              Anno INTEGER,
              Disponibilita INTEGER
            )""")
    
    conn.commit()
    conn.close()
 
def aggiungi(titolo, autore, genere, anno, disponibilita):
    
    print("\n --- Apertura della sezione AGGIUNGI...")
    
    conn, c = connessione()
    
    try:
        c.execute("""INSERT INTO Libri(Titolo, Autore, Genere, Anno, Disponibilita) 
                  VALUES (?, ?, ?, ?, ?)
                  """, (titolo, autore, genere, anno, disponibilita))
        
        conn.commit()

        print(f"\nIl libro {titolo} di {autore}({anno}) è stato aggiunto con successo nel database.")
        
        print("\n --- Elenco aggiornato correttamente.")

        visualizza()
    
    except sqlite3.IntegrityError:
        print(f"\nIl libro {titolo} di {autore}({anno}) è già presente nel database.")
    
    finally:
        conn.close()

def ricerca(id_libro, titolo, autore, genere, anno, disponibilita):
    
    print("\n --- Apertura della sezione RICERCA...")
    
    conn, c = connessione()
    
    elemento = None  #inizializza elemento per evitare problemi di variabili locali

    try:
        
        if id_libro:
            c.execute("SELECT * FROM Libri WHERE ID = ?", (id_libro,))
            elemento = c.fetchone()
            
            if elemento:
                print(f"\nElemento trovato per ID: {elemento}")
                return [elemento]
            
        query = "SELECT * FROM Libri"
        parametri = []
        condizioni = []
            
        if titolo:
            condizioni.append("titolo LIKE ?")
            parametri.append(f"%{titolo}%")

        if autore:
            condizioni.append("autore LIKE ?")
            parametri.append(f"%{autore}%")

        if genere:
            condizioni.append("genere LIKE ?")
            parametri.append(f"%{genere}%")

        if anno:
            condizioni.append("anno = ?")
            parametri.append(anno)

        if disponibilita is not None:
            condizioni.append("disponibilita = ?")
            parametri.append(disponibilita)
        
        if condizioni:
            query += " WHERE " + " AND ".join(condizioni)

        c.execute(query, parametri)

        risultati = c.fetchall() 

        if risultati:

            for libro in risultati:
                print(f"\nLa ricerca effettuata ha generato...\n{libro}")
        
        else:
            print(f"La ricerca non ha generato alcun risultato.")

    except sqlite3.Error as e:
        print(f"Errore durante la ricerca: {e}")

    finally:
        conn.close()
    
    return risultati, elemento

def visualizza(record=None):
    
    conn, c = connessione()
    
    if record is None:
        c.execute("SELECT * FROM Libri")
        record = c.fetchall()
    
    if not record:
        print("\nNessun record trovato.")
        return 
    
    print("\nID | Titolo | Autore | Genere | Anno | Disponibili")
    print("-" * 70)  # Linea divisoria

    for i in record:
        print(i)

    conn.close()

def modifica(id_modifica, titolo, autore, genere, anno, disponibilita):
    
    conn, c = connessione()
    
    print("\n --- Apertura della sezione MODIFICA...")
    
    try:
        c.execute("SELECT * FROM Libri WHERE ID = ?", (id_modifica,))
        elemento_originale = c.fetchone()
        
        print(f"\nL'elemento selezionato corrisponde a:\n{elemento_originale}")
        
        c.execute('''
            UPDATE Libri 
            SET Titolo = ?, Autore = ?, Genere = ?, Anno = ?, Disponibilita = ?
            WHERE ID = ?
        ''', (titolo, autore, genere, anno, disponibilita, id_modifica))
        
        conn.commit()
        
        print(f"\nIl record con ID corrispondente a {id_modifica} è stato modificato con successo.")
        
        c.execute("SELECT * FROM Libri WHERE ID = ?", (id_modifica,))
        elemento_modificato = c.fetchone()
        
        print(f"\nIl nuovo elemento corrisponde a:\n{elemento_modificato}")
    
    except sqlite3.Error as e:
        print(f"Errore durante la modifica del record: {e}")
    
    finally:
        conn.close()

def elimina(id_elimina):
    
    conn, c = connessione()
    
    print("\n --- Apertura della sezione ELIMINA...")
    
    try:
        c.execute("SELECT * FROM Libri WHERE ID = ?", (id_elimina,))
        elemento_elimina = c.fetchone()
        
        print(f"\nL'elemento selezionato corrisponde a:\n{elemento_elimina}")
        
        scelta = input("Vuoi davvero eliminare questo elemento definitivamente? (SI/NO): ").lower().strip()
        
        if scelta == "si" or scelta == "sì":
            c.execute("DELETE FROM Libri WHERE ID = ?", (id_elimina,))
            
            conn.commit()
            
            print(f"\n{elemento_elimina}\nEliminato con successo.")
    
    except sqlite3.Error as e:
        print(f"Errore durante l'eliminazione del record: {e}")

    finally:
        conn.close()

def elimina_more(lista_id):
    
    conn, c = connessione()
    
    print("\n --- Apertura della sezione ELIMINA più elementi...")
    
    try:
        c.execute("SELECT * FROM Libri WHERE ID IN ({})".format(','.join('?' * len(lista_id))), lista_id)
        elementi_selezionati = c.fetchall()
        
        if elementi_selezionati:
            print("\nGli elementi selezionati per l'eliminazione sono:")
            
            for i in elementi_selezionati:
                print(i)
        
        scelta = input("Vuoi davvero eliminare questi elementi definitivamente? (SI/NO): ").lower().strip()
        
        if scelta == "si" or scelta == "sì":
            c.execute("DELETE FROM Libri WHERE ID IN ({})".format(','.join('?' * len(lista_id))), lista_id)
            
            conn.commit()
            
            for i in elementi_selezionati:
                print(f"{i} Eliminato con successo.")
    
    except sqlite3.Error as e:
        print(f"Errore durante l'eliminazione dei record: {e}")
    
    finally:
        conn.close()



