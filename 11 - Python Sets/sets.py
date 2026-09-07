# # PYTHON SETS (KUMPULAN DATA UNIK & ACAK)
# ==============================================================================
# # Karakter Utama Set: 
# # 1. Unordered  : Gak punya urutan (posisinya bakal acak-acakan terus).
# # 2. Unindexed  : Gak punya nomor index, jadi GAK BISA dipanggil pake [0] atau [1].
# # 3. Unchangeable: Item di dalemnya gak bisa diubah/diedit, tapi BISA ditambah/dihapus.
# # 4. No Duplicate: KAGAK BOLEH ada data kembar. Kalau ada yang kembar, otomatis dibuang.
# ==============================================================================

# # 1. Membuat Set Dasar & Karakter Acak (Unordered)
# # Coba lu running kode ini berkali-kali, posisi outputnya bakal berubah-ubah terus!
thisset = {"apple", "banana", "cherry"}

print("Hasil Set Dasar (Posisi Acak):")
print(thisset)
print("-" * 50)


# # 2. Sifat Anti-Duplicate (Data Kembar Diabaikan)
# # Python otomatis bakal ngebuang kata 'apple' yang kedua karena dianggap duplikat.
duplicate_set = {"apple", "banana", "cherry", "apple"}

print("Hasil Set Anti-Duplicate:")
print(duplicate_set)  # Output cuma bakal nampilin 3 buah unik
print("-" * 50)


# # 3. Jebakan Batman: Angka 1/0 vs True/False
# # Di dalam Set, nilai True dianggap sama dengan 1, dan False dianggap sama dengan 0.
# # Siapa yang ditulis duluan, dia yang dipertahankan. Yang belakangan dibuang!
boolean_set_1 = {"apple", "banana", True, 1, 2}      # True ditulis duluan, maka 1 dibuang
boolean_set_2 = {"apple", "banana", False, 0, "test"} # False ditulis duluan, maka 0 dibuang

print("Hasil Jebakan Boolean vs Angka:")
print("Set 1 (True vs 1) :", boolean_set_1)
print("Set 2 (False vs 0):", boolean_set_2)
print("-" * 50)


# # 4. Fungsi Universal len() & Berbagai Tipe Data
# # len() di sini bertugas menghitung total item unik yang ada di dalam Set.
mix_set = {"abc", 34, True, 40, "male"}

print("Informasi Set Campuran:")
print("Total item unik    :", len(mix_set))
print("Tipe data resmi    :", type(mix_set))  # Output: <class 'set'>
print("-" * 50)


# # 5. Membuat Set Menggunakan Constructor: set()
# # Cara alternatif bikin set dari tipe data lain (harus pake double kurung).
constructor_set = set(("apple", "banana", "cherry"))

print("Hasil Set Constructor:")
print(constructor_set)
print("-" * 50)