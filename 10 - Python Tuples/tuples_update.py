# # PYTHON UPDATE TUPLES (AKAL-AKALAN MENGUBAH DATA TUPLE)
# ==============================================================================
# # Secara teori, Tuple itu permanen (Immutable) gak bisa diubah/ditambah/dihapus.
# # Trik utamanya: Ubah dulu Tuple jadi List, eksekusi datanya, lalu balikin ke Tuple.
# ==============================================================================

# # 1. Mengubah Nilai / Value di Dalam Tuple
# # Mengubah data spesifik menggunakan nomor index lewat bantuan list().
x = ("apple", "banana", "cherry")
y = list(x)        # 1. Ubah tuple (x) jadi list (y)
y[1] = "kiwi"      # 2. Ganti item index 1 jadi "kiwi"
x = tuple(y)       # 3. Balikin lagi list (y) jadi tuple (x)

print("Hasil Mengubah Nilai Tuple")
print("Data setelah diubah :", x)
print("-" * 50)


# # 2. Menambah Item Ke Dalam Tuple (Cara 1: Pake list.append)
# # Mengubah tuple jadi list terlebih dahulu untuk menambah data baru di ekor.
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)    # 1. Ubah ke list
y.append("orange")     # 2. Tambah data "orange" di akhir
thistuple = tuple(y)   # 3. Balikin ke tuple

print("Hasil Tambah Item (Cara 1 - list.append)")
print("Tuple setelah ditambah:", thistuple)
print("-" * 50)


# # 3. Menambah Item Ke Dalam Tuple (Cara 2: Gabung Tuple + Tuple)
# # Menggabungkan tuple asli dengan tuple baru menggunakan operator (+=).
# # Catatan: Jika cuma menambah 1 item, tetep wajib pakai koma (,) di belakang data.
thistuple = ("apple", "banana", "cherry")
y = ("orange",)        # Bikin tuple baru berisi 1 item (wajib pake koma)
thistuple += y         # Gabungin: thistuple = thistuple + y

print("Hasil Tambah Item (Cara 2 - Gabung Tuple)")
print("Tuple setelah digabung:", thistuple)
print("-" * 50)


# # 4. Menghapus Item Di Dalam Tuple (Menggunakan list.remove)
# # Menghapus item tertentu dengan cara mengubahnya menjadi list terlebih dahulu.
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)    # 1. Ubah ke list
y.remove("apple")      # 2. Hapus data "apple"
thistuple = tuple(y)   # 3. Balikin ke tuple

print("Hasil Menghapus Item")
print("Tuple setelah dihapus:", thistuple)
print("-" * 50)


# # 5. Menghapus Total Seluruh Objek Tuple (Keyword 'del')
# # Menghapus variabel tuple sepenuhnya dari memori komputer.
# # Setelah di-del, variabel tersebut tidak bisa di-print lagi karena objeknya sudah musnah.
thistuple = ("apple", "banana", "cherry")
del thistuple          # Menghapus total objek variabel dari memori

print("Hasil Delete Total Objek Tuple")
print("Note: Jika baris di bawah ini di-uncomment,program akan ERROR karena variabel sudah hilang.")
# print(thistuple)     # Ini akan memicu NameError: name 'thistuple' is not defined
print("-" * 50)