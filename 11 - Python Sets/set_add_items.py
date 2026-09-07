# # PYTHON ADD SET ITEMS (CARA NAMBAHIN DATA KE SET)
# =========================================================================
# # Karakter Utama Tambah Data Set:
# # 1. Cannot Change but Can Add : Item lama gak bisa diedit, tapi bisa ditambah baru
# # 2. add() Method               : Dipake kalau cuma mau nambahin 1 DATA aja
# # 3. update() Method            : Dipake buat nambahin DATA BORONGAN dari Set lain
# # 4. Any Iterable Update        : update() bisa nampung List, Tuple, dll (Gak harus Set)
# =========================================================================

# # 1. Add Items (Nambahin Satu Data Pake .add())
# # Kita masukin satu buah/data baru ke dalam Set yang sudah ada
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print("Hasil setelah add() 1 Items :")
print(thisset)
print("-" * 50)


# # 2. Add Sets (Nambahin Data Borongan Sesama Set Pake .update())
# # Menggabungkan semua data dari Set 'tropical' ke dalam 'thisset'
thisset = {"mangga", "durian", "cherry"}
tropical = {"kelengkeng", "leci", "sirsak"}

thisset.update(tropical)

print("Hasil Setelah update () Sesama Set:")
print(thisset)
print("-" * 50)


# # 3. Add Any Iterable (update() Bebas Pake Tipe Data Apapun)
# # Kerennya .update(), dia bisa ngosongin isi dari tipe data List/Tuple ke dalam Set
thisset = {"rambutan", "alpukat", "Nangka"}
mylist = ["jambu", "pisang"]

thisset.update(mylist)
print("Hasil Setelah update () Pake List :")
print(thisset)