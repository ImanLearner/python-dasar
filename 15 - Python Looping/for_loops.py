# ==============================================================================
#       DOKUMENTASI MINI: PYTHON FOR LOOPS (PERULANGAN BERDASARKAN URUTAN)
# ==============================================================================

# # 1. PENGGUNAAN DASAR: LIST DAN STRING
# # Artinya: "AMBIL SETIAP ITEM DI DALAM LIST/STRING SATU PER SATU DARI AWAL SAMPAI HABIS"
# # Bedanya sama while: Gak perlu bikin variabel indeks (i = 1) atau increment (i += 1) secara manual.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# # CARA BACA: Untuk setiap 'x' (item) yang ada di dalam list 'fruits', cetak 'x'.
# # Tes Logika: Putaran 1 -> x = "apple", Putaran 2 -> x = "banana", Putaran 3 -> x = "cherry". Habis, loop selesai.

print("-" * 30)

# # Looping bisa juga ngebongkar huruf di dalam teks (String):
for x in "banana":
    print(x)

print("-" * 30)


# # 2. PENGHENTIAN PAKSA & SKIPPING: break DAN continue
# # Aturannya SAMA: break buat bubar total, continue buat skip satu item.

# Contoh break (Potong di tengah jalan):
for x in fruits:
    if x == "banana":
        break   # Begitu ketemu banana, loop langsung hancur
    print(x)

print("-" * 30)

# Contoh continue (Lewati item tertentu):
for x in fruits:
    if x == "banana":
        continue    # Skip banana, langsung loncat ambil item berikutnya
    print(x)

print("-" * 30)


