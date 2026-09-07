# ==============================================================================
# # PYTHON ACCESS TUPLE ITEMS (MENGAKSES ISI DATA TUPLE)
# ==============================================================================
# # Cara mengambil data di dalam Tuple menggunakan nomor index.
# # Penulisan index tetap menggunakan tanda kurung siku [ ].
# ==============================================================================

# # 1. Akses Menggunakan Index Positif
# # Index dimulai dari angka 0 (item pertama), index 1 (item kedua), dst.
thistuple = ("apple", "banana", "cherry")

print("Hasil Akses Index Positif")
print("Item kedua (index 1):", thistuple[1])
print("-" * 50)


# # 2. Akses Menggunakan Negative Indexing (Index Negatif)
# # Membaca data dimulai dari paling belakang.
# # Index -1 artinya item terakhir, -2 artinya kedua dari terakhir, dst.
thistuple = ("apple", "banana", "cherry")

print("Hasil Akses Index Negatif")
print("Item terakhir (index -1):", thistuple[-1])
print("-" * 50)


# # 3. Mengambil Data dengan Range / Slicing (Index Positif)
# # Mengambil beberapa data sekaligus. Formatnya [start:end].
# # Sifatnya: Index awal (start) DIBAWA, Index akhir (end) TIDAK DIBAWA.
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print("Hasil Range / Slicing Index Positif")
# Mengambil dari index 2 sampai SEBELUM index 5 (yaitu 2, 3, 4)
print("Range [2:5] :", thistuple[2:5])

# Kalau bagian depan dikosongin [:4], artinya mulai dari item paling pertama (index 0)
print("Range [:4]  :", thistuple[:4])

# Kalau bagian belakang dikosongin [2:], artinya mulai dari index 2 sampai paling ujung
print("Range [2:]  :", thistuple[2:])
print("-" * 50)


# # 4. Mengambil Data dengan Range (Index Negatif)
# # Konsepnya sama [start:end], tapi hitungnya maju dari arah belakang.
# # Index awal (-4) DIBAWA, index akhir (-1) TIDAK DIBAWA.
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print("Hasil Range Index Negatif")
# Mengambil dari index -4 sampai SEBELUM index -1
print("Range [-4:-1]:", thistuple[-4:-1])
print("-" * 50)


# # 5. Cek Apakah Data Ada di Dalam Tuple (Keyword 'in')
# # Digunakan untuk memeriksa keberadaan suatu item menggunakan logika 'in'.
thistuple = ("apple", "banana", "cherry")

print("Hasil Cek Ketersediaan Item")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
else:
    print("No, 'Durian' is NOT in the fruits tuple")
print("-" * 50)