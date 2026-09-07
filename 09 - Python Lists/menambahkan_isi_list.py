# ==============================================================================
# PYTHON ADD LIST ITEMS (TAMBAH DATA)
# ==============================================================================

# 1. Menambahkan data di paling akhir: .append()
# Otomatis masuk ke urutan paling buntut.
buah = ["apple", "banana", "cherry"]
buah.append("orange")
print("Hasil append :", buah)
print("-" * 30)


# 2. Menambahkan data nyempil (nyelak): .insert()
# Parameter pertama adalah nomor index tujuan, kedua adalah datanya.
# Barang lama di index tersebut otomatis kegeser mundur ke kanan.
items = ["apple", "banana", "cherry"]
items.insert(1, "orange")  # Menyelak di index 1
print("Hasil insert :", items)
print("-" * 30)


# 3. Menggabungkan dua list dari belakang: .extend()
# Membongkar isi list lain dan menempelkannya ke ekor list pertama.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print("Hasil extend :", thislist)
print("-" * 30)


# 4. Memasukkan tipe data iterable lain (Tuple/Set): .extend()
# Tidak harus sesama list, .extend() juga bisa membongkar kurung bulat () tuple.
keranjang = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
keranjang.extend(thistuple)
print("Hasil tuple  :", keranjang)
print("-" * 30)


# 5. EKSPERIMEN: BEDANYA .append() VS .extend() (MASALAH KURUNG HILANG)
# ==============================================================================
# Di sini kita tes masukin kiriman data yang sama ("C", "D") pake dua alat beda.

# A. Pake .append() -> Si Pemalas (Kurung TETEP ADA)
box_append = ["A", "B"]
box_append.append(("C", "D"))  # Dimasukin bulat-bulat sekurungnya
print("Append + Tuple:", box_append)  # Hasil: ['A', 'B', ('C', 'D')]

# B. Pake .extend() -> Si Rajin (Kurung HILANG & LEBUR)
box_extend = ["A", "B"]
box_extend.extend(("C", "D"))  # Dibongkar dulu bungkusnya baru dilebur
print("Extend + Tuple:", box_extend)  # Hasil: ['A', 'B', 'C', 'D']
print("=" * 30)