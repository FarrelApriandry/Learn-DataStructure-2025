# -*- coding: utf-8 -*-
"""2430506056_StrukturData_Array.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Q7skS34haL4n9SFI3ib1BEQM1Dpd7qdM
"""

numbers = [10, 20, 30, 40, 50]
print("List:", numbers)

numbers = [10, 20, 30, 40, 50]
print("First element:", numbers[0])
print("Last element:", numbers[-1])

numbers.append(60)  # Adds 60 to the end of the list
print("After append:", numbers)

numbers.insert(2, 25)  # Inserts 25 at index 2
print("After insert:", numbers)

numbers.remove(25)  # Removes the first occurrence of 25
print("After remove:", numbers)

numbers.pop(2)  # Removes the element at index 2
print("After pop:", numbers)

for num in numbers:
    print("Number:", num)

import numpy as np

# Creating a 2D array
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array:")
print(matrix)

# Accessing elements in a 2D array
print("Element at row 1, column 2:", matrix[1][2])  # Output: 6

NPM = [2430506055, 2430506056, 2430506057, 2430506058, 2430506059]

print("NPM =", NPM)

NPM[1] = 243050605620

print("NPM =", NPM)

fakultas = ["FKIP", "TEKNIK", "FISIPOL", "FE", "FAPERTA"]

for range in fakultas:
  print("Fakultas: ", range)

harga_barang = [10000, 30000, 50000, 75000, 85000]

print("Total harga barang:", sum(harga_barang))

matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

for baris in matriks:
  print(baris)

print("Element at fourth collumn and second row is: ", matriks[3][1])

matriks.append(["09", "04", "20", "06"])

for baris in matriks:
  print(baris)

matriks[4].pop(2)

for baris in matriks:
  print(baris)

matriks[4][2] = "14"

for baris in matriks:
  print(baris)

print("============================")
print("Welcome to the grocery store")
print("============================")
print("\n")

item = [
    "Trash Bag",
    "Chocolate",
    "Soft Drink"
]

for i in item:
  print(i)

print("\n")
print("=====================")
print("First Update Grocery Items")
print("=====================")
print("\n")

item.append("Ice Cream")

for i in item:
  print(i)

item.remove("Trash Bag")

print("\n")
print("=====================")
print("Second Update Grocery Items")
print("=====================")
print("\n")

for i in item:
  print(i)

size = 10

treasure_map = ["_" for _ in range(size)]

print(f"Selamat datang di Treasure Hunt! Peta memiliki {size} lokasi (0 hingga {size-1}).")

treasure_index = int(input(f"Masukkan lokasi harta karun (0-{size-1}) :"))
while treasure_index < 0 or treasure_index >= size:
    print("Lokasi tidak valid. Silakan coba lagi.")
    treasure_index = int(input(f"Masukkan lokasi harta karun (0-{size-1}) :"))

treasure_map[treasure_index] = "X"

def play_treasure_hunt():
  print("\nHarta Karun telah disembunyikan! Sekarang giliran pemain menebak.")
  print("Cobalah untuk menemukan harta karun dengan menebak indeks yang benar.")

  while True:
    print("\nPeta saat ini: ", ["_" for _ in range(size)])

    try:
      guess = int(input(f"Masukkan indeks tebakanmu (0-{size-1}): "))
    except ValueError:
      print("Masukkan angka yang valid!")
      continue
    if guess < 0 or guess >= size:
      print("Indeks tidak valid, pilih anatara 0 hingga", size-1)
      continue
    if treasure_map[guess] == "X":
      print("Selamat! Kamu menemukan harta karun di lokasi:", guess)
      break
    else:
      print("Tidak ada harta di lokasi ini. Coba lagi!")

  print("Terima kasih sudah bermain!")

play_treasure_hunt()

def play_treasure_hunt(size, treasure_map):
    print("\nHarta Karun telah disembunyikan! Sekarang giliran pemain menebak.")
    while True:
        print("\nPeta saat ini:", ["_"] * size)
        guess = int(input(f"Masukkan indeks tebakanmu (0-{size-1}): "))
        if guess < 0 or guess >= size:
            print("Indeks tidak valid, pilih antara 0 hingga", size-1)
            continue
        if treasure_map[guess] == "X":
            print("Selamat! Kamu menemukan harta karun di lokasi:", guess)
            break
        else:
            print("Tidak ada harta di lokasi ini. Coba lagi!")
    print("Terima kasih sudah bermain!")

size = int(input("Masukkan ukuran peta yang diinginkan (minimal 2): "))
while size < 2:
    print("Ukuran peta harus minimal 2.")
    size = int(input("Masukkan ukuran peta yang diinginkan (minimal 2): "))

treasure_map = ["_"] * size
print(f"Selamat datang di Treasure Hunt! Peta memiliki {size} lokasi (0 hingga {size-1}).")

treasure_index = int(input(f"Masukkan lokasi harta karun (0-{size-1}): "))
while treasure_index < 0 or treasure_index >= size:
    print("Lokasi tidak valid. Silakan coba lagi.")
    treasure_index = int(input(f"Masukkan lokasi harta karun (0-{size-1}): "))

treasure_map[treasure_index] = "X"

play_treasure_hunt(size, treasure_map)

import random

def play_treasure_hunt(size, treasure_map):
    print("\nHarta Karun telah disembunyikan! Sekarang giliran pemain menebak.")
    while True:
        print("\nPeta saat ini:", ["_"] * size)
        guess = int(input(f"Masukkan indeks tebakanmu (1-{size}): ")) - 1
        if guess < 0 or guess >= size:
            print("Indeks tidak valid, pilih antara 1 hingga", size)
            continue
        if treasure_map[guess] == "X":
            print("Selamat! Kamu menemukan harta karun di lokasi:", guess + 1)
            break
        else:
            print("Tidak ada harta di lokasi ini. Coba lagi!")
    print("Terima kasih sudah bermain!")

size = int(input("Masukkan ukuran peta yang diinginkan (minimal 2): "))
while size < 2:
    print("Ukuran peta harus minimal 2.")
    size = int(input("Masukkan ukuran peta yang diinginkan (minimal 2): "))

treasure_map = ["_"] * size
print(f"Selamat datang di Treasure Hunt! Peta memiliki {size} lokasi (1 hingga {size}).")

treasure_index = random.randint(0, size - 1)
print(f"Harta karun telah disembunyikan secara otomatis!")
8
treasure_map[treasure_index] = "X"

play_treasure_hunt(size, treasure_map)