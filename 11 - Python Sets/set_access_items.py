# # PYTHON ACCESS SET ITEMS (CARA MENGAKSES DATA SET)
# =========================================================================
# # Karakter Utama Akses Set:
# # 1. No Index/Key : Gak punya nomor index atau key, gak bisa dipanggil pake [0]
# # 2. Loop Access  : Untuk ngeliat semua isinya, kudu diputer pake 'for loop'
# # 3. In Keyword   : Pake kata 'in' buat ngecek apakah suatu item ADA di set
# # 4. Not In       : Pake 'not in' buat ngecek apakah suatu item GAK ADA di set
# =========================================================================

# # 1. Loop Through Items (Muterin Isi Set Pake For Loop)
# # Karena Set gak punya indeks, kita ambil nilainya satu-satu pake loop
thisset = {"apple", "banana", "cherry"}

print("Hasil Loop Set :")
for buah in thisset:
    print(buah)
print("-" * 50)


# # 2. Check if Item Present (Cek Data Pake 'in')
# # Nyari tahu apakah data yang dimaksud ada di dalam Set (Output: True/False)
thisset = {"mangga", "durian", "kelengkeng"}

print("Apakah 'durian' ada di dalam set?")
print("durian" in thisset)
print("-" * 50)


# # 3. Check if Item NOT Present (Cek Data Pake 'not in')
# # Nyari tahu apakah data yang dimaksud EMANG GAK ADA di dalam Set (Output: True/False)
thisset = {"rambutan", "leci", "sirsak"}

print("Apakah 'sirsak' TIDAK ADA di dalam set?")
print("sirsak" not in thisset)