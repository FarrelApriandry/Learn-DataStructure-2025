# -*- coding: utf-8 -*-
"""2430506056_StrukDat_Searching.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LX33faue0jcljdbo16-nZ9klwaTilRGS
"""

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return index if found
    return -1  # Return -1 if not found

# Example usage
arr = [10, 23, 45, 70, 11, 15]
target = int(input("Input: "))
result = linear_search(arr, target)

print(f"Target found at index {result}" if result != -1 else "Target not found")

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Element found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Return -1 if not found

# Example usage
arr = [5, 10, 15, 20, 25, 30, 35]  # Must be sorted
target = int(input("Input: "))
result = binary_search(arr, target)

print(f"Target found at index {result}" if result != -1 else "Target not found")

import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))  # Define the jump step
    prev = 0

    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1  # Target not found

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i  # Return index if found

    return -1  # Return -1 if not found

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  # Must be sorted
target = int(input("Input: "))
result = jump_search(arr, target)

print(f"Target found at index {result}" if result != -1 else "Target not found")

"""# **Langkah Praktikum**

## **1. Implementasi Linear Search**
"""

def linear_search(arr, target):
  for i in range (len(arr)):
    if arr[i] == target:
      return i
  return -1

arr = [12, 45, 78, 23, 56, 89, 34, 67, 90, 11]
target = int(input("Enter last 3 digit of your id: "))

result = linear_search(arr, target)

if result != -1:
  print(f"Element found at index {result}")
else :
  print("Doesn't found same element")

"""## **2. Implementasi Binary Search**"""

def binary_search(arr, target):
  low = 0
  high = len(arr) - 1

  while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return -1

arr = ["1010", "1202", "1405", "1707", "2508", "3009", "0311", "2412", "0904"]
arr_int = sorted([int(x) for x in arr])

print(arr_int)
target = int(input("Enter your birthday date (DDMM): "))

result = binary_search(arr_int, target)

if result != -1:
  print(f"Element found at index {result}")
else :
  print("Doesn't found same element")

"""## **3. Implementasi Jump Search**"""

import math

def jump_search(arr, target):
  n = len(arr)
  step = int(math.sqrt(n))
  prev = 0

  while arr[min(step, n) - 1] < target:
    prev = step
    step += int(math.sqrt(n))
    if prev >= n:
      return -1

  for i in range(prev, min(step, n)):
    if arr[i] == target:
      return i
  return -1

arr = ["Aldi", "Luthfi", "Faiz", "Rama", "Sabil", "Hakkan", "Yasa", "Assep", "Anip", "Biyu", "Rel"]
target = input("Enter your name: ")

result = jump_search(arr, target)

if result != -1:
  print(f"Element found at index {result}")
else :
  print("Doesn't found same element")

"""# **Latihan/Tugas**

## **1. Implementasi Linear Search, Binary Search, dan Jump Search pada sebuah array random**
"""

import random
import math

def linear_search(arr, target):
    comparisons = 0
    for i, num in enumerate(arr):
        comparisons += 1
        if num == target:
            return i, comparisons
    return -1, comparisons

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev, comparisons = 0, 0

    while prev < n and arr[min(step, n) - 1] < target:
        comparisons += 1
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1, comparisons

    for i in range(prev, min(step, n)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons

    return -1, comparisons

# Generate 100 unique random numbers and sort them
arr = sorted(random.sample(range(1, 1001), 100))

# Select a random target
target = random.choice(arr)

# Perform searches and count comparisons
ls_index, ls_comparisons = linear_search(arr, target)
bs_index, bs_comparisons = binary_search(arr, target)
js_index, js_comparisons = jump_search(arr, target)

# Print results
print(f"Target: {target}")
print(f"Linear Search: Index {ls_index}, Comparisons {ls_comparisons}")
print(f"Binary Search: Index {bs_index}, Comparisons {bs_comparisons}")
print(f"Jump Search: Index {js_index}, Comparisons {js_comparisons}")

"""## **2. Implementasi code task 1, menggunakan library tabulate**"""

import random
import math
from tabulate import tabulate

def linear_search(arr, target):
    comparisons = 0
    for i, num in enumerate(arr):
        comparisons += 1
        if num == target:
            return i, comparisons
    return -1, comparisons

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev, comparisons = 0, 0

    while prev < n and arr[min(step, n) - 1] < target:
        comparisons += 1
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1, comparisons

    for i in range(prev, min(step, n)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons

    return -1, comparisons

# Generate 100 unique random numbers and sort them
arr = sorted(random.sample(range(1, 1001), 100))

# Select a random target
target = random.choice(arr)

# Perform searches and count comparisons
ls_index, ls_comparisons = linear_search(arr, target)
bs_index, bs_comparisons = binary_search(arr, target)
js_index, js_comparisons = jump_search(arr, target)

# Create table
headers = ["Algorithm", "Index Found", "Comparisons"]
data = [
    ["Linear Search", ls_index, ls_comparisons],
    ["Binary Search", bs_index, bs_comparisons],
    ["Jump Search", js_index, js_comparisons]
]

# Print results
print("\nSearch Results:")
print(tabulate(data, headers=headers, tablefmt="fancy_grid"))