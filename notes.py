#!/usr/bin/env python3
import os
from datetime import datetime

# --- Input nome ---
nome = input("Inserisci il tuo nome: ").strip()

# --- Cartella di lavoro ./notes ---
cartella = "./notes"
os.makedirs(cartella, exist_ok=True)

# --- File relativo all'utente ---
file_path = os.path.join(cartella, f"{nome}.txt")

# --- Append con timestamp ---
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(file_path, "a") as f:
    f.write(f"{timestamp} - Ciao {nome}\n")

# --- Conteggio righe ---
with open(file_path, "r") as f:
    righe = sum(1 for _ in f)
print(f"Il file ha {righe} righe.")

# --- Richiesta numero intero positivo ---
try:
    N = int(input("Inserisci un numero intero positivo N: "))
    if N <= 0:
        raise ValueError
except ValueError:
    print("Errore: devi inserire un numero intero positivo.")
    exit(1)

# --- Stampa numeri pari da 1 a N ---
pari = [str(i) for i in range(2, N+1, 2)]
print(f"Pari 1..{N}:", " ".join(pari))
