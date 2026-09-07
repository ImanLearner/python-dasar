# # PYTHON TUPLES (MENYIMPAN DATA PERMANEN)
# ==============================================================================
# # Karakteristik: Ordered (Berurutan) & Unchangeable (Gak bisa diubah/gembok mati)
# # Pake tanda kurung biasa ( )
# ==============================================================================

# # 1. Bikin Tuple Standar & Menggunakan Fungsi len()
# # Menampilkan isi data dan menghitung total item di dalam Tuple.
thistuple = ("apple", "banana", "cherry")

print("Hasil Tuple Standar")
print("Isi Tuple       :", thistuple)
print("Jumlah data len :", len(thistuple))
print("-" * 50)


# # 2. Membuat Tuple dengan 1 Item (Jebakan Batman)
# # Wajib hukumnya pake tanda koma (,) di akhir data biar dibaca sebagai Tuple.
# # Kalau gak pake koma, Python bakal ngira itu String biasa (str).
tuple_asli = ("apple",)
bukan_tuple = ("apple")

print("Hasil Cek Tipe Data 1 Item")
print("Pake koma (Tuple)     :", type(tuple_asli))
print("Gak pake koma (String):", type(bukan_tuple))
print("-" * 50)


# # 3. Variasi Tipe Data di Dalam Tuple
# # Tuple bebas menampung tipe data apa saja, bahkan dicampur dalam satu tempat.
tuple1 = ("apple", "banana", "cherry")   # Isi String
tuple2 = (1, 5, 7, 9, 3)                 # Isi Integer
tuple3 = (True, False, False)            # Isi Boolean
tuple_campur = ("abc", 34, True, 40, "male") # Data Campuran

print("Hasil Tuple Campuran")
print("Data campuran :", tuple_campur)
print("Tipe objek    :", type(tuple_campur))
print("-" * 50)


# # 4. Membuat Tuple Menggunakan Constructor tuple()
# # Cara alternatif bikin Tuple pake fungsi bawaan. Perhatikan kurungnya dobel (( )).
thistuple_constructor = tuple(("apple", "banana", "cherry"))

print("Hasil Tuple Constructor")
print("Isi dari constructor :", thistuple_constructor)
print("-" * 50)