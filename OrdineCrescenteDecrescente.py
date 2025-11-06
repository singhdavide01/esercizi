
numeri = []

for i in range(20):
    numero = float(input(f"Inserisci il numero {i+1}: "))
    numeri.append(numero)

for i in range(len(numeri)):
    for j in range(0, len(numeri)-i-1):
        if numeri[j] > numeri[j+1]:
            numeri[j], numeri[j+1] = numeri[j+1], numeri[j]
print("Numeri ordinati in ordine crescente:")
print(numeri)


for i in range(len(numeri)):
    for j in range(0, len(numeri)-i-1):
        if numeri[j] < numeri[j+1]:
            numeri[j], numeri[j+1] = numeri[j+1], numeri[j]
print("Numeri ordinati in ordine decrescente:")
print(numeri)

