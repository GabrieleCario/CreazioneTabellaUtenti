import pandas as pd
import sqlite3

file_excel = "utenti.xlsx"
df = pd.read_excel(file_excel)

conn = sqlite3.connect("utenti.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Utenti (
        Nome TEXT,
        Cognome TEXT,
        Email TEXT,
        Telefono TEXT
    )
""")

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO Utenti (Nome, Cognome, Email, Telefono)
        VALUES (?, ?, ?, ?)
    """, (row["Nome"], row["Cognome"], row["Email"], row["Telefono"]))

conn.commit()
conn.close()
print("Tabella SQL creata con successo! I dati corrispondono al file Excel.")
