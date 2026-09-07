# # PYTHON TUPLE METHODS (FITUR BAWAAN TUPLE)
# ==============================================================================
# # Karena Tuple bersifat 'Immutable' (gembok mati), dia gak punya method buat 
# # nambah atau hapus data kayak List. Tuple CUMA PUNYA 2 method bawaan ini:
# ==============================================================================

my_tuple = ("apple", "banana", "cherry", "banana", "apple", "banana")

# # 1. Method .count()
# # Fungsi: Menghitung berapa kali suatu data muncul/disebut di dalam Tuple.
jumlah_banana = my_tuple.count("banana")

print("Hasil Method .count()")
print("Data 'banana' muncul sebanyak :", jumlah_banana, "kali")
print("-" * 50)


# # 2. Method .index()
# # Fungsi: Mencari posisi nomor index pertama dari data yang kita tentukan.
# # Catatan: Kalau datanya ada kembar (kayak 'banana'), yang diambil adalah index YANG PERTAMA KETEMU.
posisi_cherry = my_tuple.index("cherry")
posisi_banana = my_tuple.index("banana")

print("Hasil Method .index()")
print("Data 'cherry' ada di posisi index ke- :", posisi_cherry)
print("Data 'banana' pertama kali ketemu di index ke- :", posisi_banana)
print("-" * 50)