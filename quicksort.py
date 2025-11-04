arr = [10, 7, 8, 9, 1, 5]

# Usiamo una "pila" per gestire le parti dell'array da ordinare (simuliamo la ricorsione)
stack = [(0, len(arr) - 1)]

while stack:
    start, end = stack.pop()

    if start < end:
        # Partition manuale
        pivot = arr[end]
        i = start - 1

        for j in range(start, end):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        # Mettiamo il pivot nella posizione giusta
        i += 1
        arr[i], arr[end] = arr[end], arr[i]
        pivot_index = i

        # Aggiungiamo le due parti da ordinare nella pila
        stack.append((start, pivot_index - 1))
        stack.append((pivot_index + 1, end))

print("Lista ordinata:", arr)
