# DOKUMENTASI : PYTHON LISTS (KONSEP DASAR)
# ==============================================================================
# Definisi: List itu wadah buat nyimpen BANYAK DATA di dalam SATU VARIABEL.
# Ciri Khas: Pake tanda kurung siku []
# Sifat Utama:
# 1. Ordered    -> Urutannya rapi (Gak bakal berubah, data baru ditaruh di akhir).
# 2. Changeable -> Bisa diedit (Bisa ditambah, diganti, atau dihapus datanya).
# 3. Duplicates -> Boleh kembar (Karena pake sistem nomor urut/indeks).
# ==============================================================================

# 1. CARA BIKIN LIST DASAR & INDEX [0]
# Inget: Komputer ngitung urutan dari angka 0, bukan 1!
buah = ["apple", "banana", "cherry"]
print("1. ISI LIST BUAH      :", buah)
print("-" * 50)


# 2. LIST BOLEH PUNYA DATA KEMBAR (DUPLICATES)
# Meskipun apple ada dua, komputer gak bakal protes karena nomor kotaknya beda.
buah_kembar = ["apple", "banana", "cherry", "apple"]
print("2. LIST DATA KEMBAR   :", buah_kembar)
print("-" * 50)


#  3. CARA NGITUNG JUMLAH BARANG DI LIST: len()
print("3. JUMLAH ITEM (LEN)  :", len(buah)) # Hasil: 3 karena ada 3 barang
print("-" * 50)


#  4. LIST BISA DIISI SEGALA JENIS DATA TYPE (CAMPURAN)
# Boleh string, angka, boolean, bahkan dicampur dalam satu list sekaligus!
list_campuran = ["abc", 34, True, "male"]
print("4. LIST CAMPURAN      :", list_campuran)
print("   Cek Tipe Data      :", type(list_campuran)) # Hasil: <class 'list'>
print("-" * 50)


#  5. CARA ALTERNATIF BIKIN LIST: Pake list() Constructor
# Ciri khasnya pake double tanda kurung bulat biasa list(())
list_baru = list(("apple", "banana", "cherry"))
print("5. LIST CONSTRUCTOR   :", list_baru)
