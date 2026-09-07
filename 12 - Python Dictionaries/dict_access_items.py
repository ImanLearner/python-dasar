# DOKUMENTASI LATIHAN: ACCESS DICTIONARY ITEMS (CARA AMBIL DATA DARI KAMUS)
# =========================================================================

# Kita pakai data simulasi mobil biar sama kayak dokumentasi W3Schools
mobil = {
    "brand": "Supra",
    "model": "Sport",
    "year": 2003
}

# 1. Mengakses Nilai Menggunakan Kurung Siku [ ]
# -------------------------------------------------------------------------
# Cara paling dasar. Panggil nama Label (Key) untuk tahu isinya.
x = mobil["model"]
print("1. Hasil Akses Kurung Siku :", x)


# 2. Mengakses Nilai Menggunakan Method .get()
# -------------------------------------------------------------------------
# Hasilnya sama, tapi ini cara yang direkomendasikan karena lebih aman dari eror crash.
y = mobil.get("model")
print("2. Hasil Akses Method .get() :", y)


# 3. Mengambil Semua Nama Label Menggunakan .keys() + Efek "Live View"
# -------------------------------------------------------------------------
# .keys() mengembalikan daftar semua label (Key) di dalam dictionary.
# Sifatnya adalah "View", artinya kalau isi kamus berubah, variabel list ini ikut update otomatis!
daftar_kunci = mobil.keys()
print("\n3. Daftar Kunci SEBELUM ditambah warna :", daftar_kunci)

# Coba kita tambah data baru ke kamus mobil
mobil["color"] = "white"
print("Daftar Kunci SESUDAH ditambah warna :", daftar_kunci)


# 4. Mengambil Semua Isi Data Menggunakan .values() + Efek "Live View"
# -------------------------------------------------------------------------
# .values() mengembalikan daftar semua isi/nilai (Value) tanpa nama labelnya.
daftar_isi = mobil.values()
print("\n4. Daftar ISI SEBELUM tahun diganti :", daftar_isi)

# Coba kita ganti tahunnya dari 1964 jadi 2020
mobil["year"] = 2020
print(" Daftar Ise SESUDAH tahun diganti :", daftar_isi)

# 5. Mengambil Pasangan Lengkap Menggunakan .items()
# -------------------------------------------------------------------------
# .items() mengembalikan semua data dalam bentuk pasangan (Key, Value) 
# yang dibungkus di dalam Tuple dan List. Berguna banget buat looping nanti.
pasangan_data = mobil.items()
print("\n5. Bentuk Pasangan Lengkap (.items()) :", pasangan_data)

# 6. Mengecek Apakah Label (Key) Ada di Kamus Menggunakan Keyword 'in'
# -------------------------------------------------------------------------
# Penting banget buat validasi logika di backend/security sebelum eksekusi data.
print("\n6. Hasil Pengecekan Key 'model':")
if "model" in mobil:
    print("   Aman bro! Label 'model' emang ada di dalam kamus mobil ini.")