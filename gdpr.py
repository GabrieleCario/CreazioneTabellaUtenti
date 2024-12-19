import pandas as pd
import random

df_nomi = pd.read_csv("nomi.csv")

lista_nomi = df_nomi["Nome"].tolist()
lista_cognomi = df_nomi["Cognome"].tolist()

utenti = []
for _ in range(10):
    nome = random.choice(lista_nomi)
    cognome = random.choice(lista_cognomi)
    email = nome.lower() + "." + cognome.lower() + "@example.com"
    telefono = "+39 " + str(random.randint(300, 399)) + " " + str(random.randint(1000000, 9999999))
    utenti.append({
        "Nome": nome,
        "Cognome": cognome,
        "Email": email,
        "Telefono": telefono
    })

df = pd.DataFrame(utenti)
df.to_excel("utenti.xlsx", index=False)
print("File Excel creato con successo")

