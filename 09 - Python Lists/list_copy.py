# =====================================================================
# PYTHON COPY LIST (SALIN DATA)
# =====================================================================

# # 1. Masalah copy menggunakan sama dengan: =
# Tidak menyalin data asli, melainkan hanya membuat jalan pintas (referensi).
# Jika data asli diubah, data salinan otomatis ikut berubah.
buah = ["apple", "banana", "cherry"]
buah_copy_gagal = buah
buah.append("durian") # Mencoba ubah data asli

print("Hasil Asli (=)  :", buah)
print("Hasil Gagal Copy:", buah_copy_gagal)
print("-" * 50)


# # 2. Menyalin menggunakan method: .copy()
# Membuat duplikat total yang baru dan mandiri di memory.
# Jika data asli diubah, data salinan tetap aman dan tidak ikut berubah.
items = ["apple", "banana", "cherry"]
items_copy = items.copy()
items.append("grape") # Mencoba ubah data asli

print("Hasil Asli (.copy()) :", items)
print("Hasil Sukses Copy 1  :", items_copy)
print("-" * 50)


# # 3. Menyalin menggunakan function: list()
# Memasukkan isi data asli ke dalam wadah list baru yang terpisah.
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
thislist.append("mango") # Mencoba ubah data asli

print("Hasil Asli (list()) :", thislist)
print("Hasil Sukses Copy 2 :", mylist)
print("-" * 50)


# # 4. Menyalin menggunakan Slice Operator: [:]
# Mengambil potongan data dari awal sampai akhir untuk ditaruh di list baru.
keranjang = ["apple", "banana", "cherry"]
keranjang_copy = keranjang[:]
keranjang.append("orange") # Mencoba ubah data asli

print("Hasil Asli ([:])    :", keranjang)
print("Hasil Sukses Copy 3 :", keranjang_copy)
print("-" * 50)