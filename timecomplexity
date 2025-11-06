import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Generate a random array of integers
arr = [random.randint(0, 1000) for _ in range(1000)]

# Timing Bubble Sort
start_time = time.time()
bubble_sort(arr.copy())
bubble_time = time.time() - start_time

# Timing Quick Sort
start_time = time.time()
quicksort(arr.copy())
quick_time = time.time() - start_time

print(f"Bubble Sort Time: {bubble_time} seconds")
print(f"Quick Sort Time: {quick_time} seconds")
