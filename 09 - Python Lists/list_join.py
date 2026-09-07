# =====================================================================
# PYTHON JOIN LIST (GABUNGIN DATA)
# =====================================================================

# # 1. Menggabungkan menggunakan operator tambah: +
# Cara paling gampang. Membuat list baru (list3) tanpa merusak list asli (list1 & list2).
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2

print("Hasil Join (+)")
print("List 1 asli:", list1)
print("List 2 asli:", list2)
print("List 3 baru:", list3) # Hasil: ['a', 'b', 'c', 1, 2, 3]
print("-" * 50)


# # 2. Menggabungkan menggunakan perulangan: for loop & .append()
# Mengambil isi list2 satu per satu, lalu dimasukkan ke dalam list1.
# Cara ini merusak/mengubah data asli dari list1.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print("Hasil Join (for loop)")
print("List 1 (Berubah) :", list1) # Hasil: ['a', 'b', 'c', 1, 2, 3]
print("List 2 (Tetap)   :", list2)
print("-" * 50)


# # 3. Menggabungkan menggunakan method: .extend()
# Cara paling cepat untuk membongkar isi list2 dan langsung ditempel ke ekor list1.
# Sama seperti cara nomor 2, cara ini juga mengubah data asli dari list1.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)

print("Hasil Join (.extend())")
print("List 1 (Berubah) :", list1) # Hasil: ['a', 'b', 'c', 1, 2, 3]
print("List 2 (Tetap)   :", list2)
print("-" * 50)