import time
import tracemalloc
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Crea lista casuale
arr = [random.randint(0, 10000) for _ in range(2000)]

# 🔹 Bubble Sort
a = arr.copy()
tracemalloc.start()
start = time.time()
bubble_sort(a)
end = time.time()
current, peak = tracemalloc.get_traced_memory()
print("Bubble Sort:")
print("  Tempo:", round(end - start, 4), "s")
print("  Memoria picco:", peak / 1024, "KB")
tracemalloc.stop()

# 🔹 Quick Sort
a = arr.copy()
tracemalloc.start()
start = time.time()
quick_sort(a)
end = time.time()
current, peak = tracemalloc.get_traced_memory()
print("\nQuick Sort:")
print("  Tempo:", round(end - start, 4), "s")
print("  Memoria picco:", peak / 1024, "KB")
tracemalloc.stop()
