# # CHEAT SHEET: PYTHON DICTIONARY METHODS (TABEL LENGKAP W3SCHOOLS)
# ===================================================================
# # Referensi dari gambar "image_cffce6.png". 
# # Ini kamus jalan pintas terlengkap buat manipulasi Dictionary.
# ===================================================================

# Data dummy buat bahan eksperimen
mobil_gua = {"brand": "Ford", "model": "Mustang", "year": 1964}

print("=== CONTEKAN JURUS INSTAN DICTIONARY ===")

# # 1. `.clear()` -> Kuras habis isi kamus jadi zonk {}
# mobil_gua.clear()


# # 2. `.copy()` -> Kloning/gandain kamus (Jalur Aman biar data asli gak rusak)
# salinan_mobil = mobil_gua.copy()


# # 3. `.fromkeys(kumpulan_judul, nilai_bawaan)` -> Bikin kamus baru dari nol secara massal
# # Berguna banget kalau lo punya daftar judul, tapi isinya mau disamain semua dulu di awal.
judul_baru = ('spek1', 'spek2', 'spek3')
kamus_baru = dict.fromkeys(judul_baru, "Belum Diisi")
print("3. Hasil .fromkeys() :", kamus_baru) 
# Hasil: {'spek1': 'Belum Diisi', 'spek2': 'Belum Diisi', ...}


# # 4. `.get("judul", nilai_cadangan)` -> Ambil isi data dengan aman (Anti-Crash!)
# # Kalau judulnya gak ada, program gak akan error, melainkan keluar nilai cadangannya.
print("4. Hasil .get()      :", mobil_gua.get("brand", "Gak Ada"))


# # 5. `.items()` -> Ngambil sepasang 'Judul' dan 'Isi' sekaligus
# # Ini yang lo pake di loop pertama tadi buat mecah data ke bawah!
print("5. Hasil .items()    :", mobil_gua.items())


# # 6. `.keys()` -> Ngambil rombongan 'Judul'-nya doang (Key)
print("6. Hasil .keys()     :", mobil_gua.keys()) # Hasil: ['brand', 'model', 'year']


# # 7. `.values()` -> Ngambil rombongan 'Isi'-nya doang (Value)
print("7. Hasil .values()   :", mobil_gua.values()) # Hasil: ['Ford', 'Mustang', 1964]


# # 8. `.pop("judul")` -> Hapus data target yang lo pilih
# mobil_gua.pop("model")


# # 9. `.popitem()` -> Hapus data otomatis yang ada di paling buntut/ujung akhir
# mobil_gua.popitem()


# # 10. `.update({"judul": "isi_baru"})` -> Nimpa data lama ATAU nambahin data baru sekaligus
# mobil_gua.update({"year": 2026})


# # 11. `.setdefault("judul", isi_cadangan)` -> Jurus "Isi Otomatis Kalau Kosong"
# # Fungsinya: Mirip kayak .get(), tapi bedanya, kalau judul yang lo cari itu "GAK ADA",
# # si Python bakal langsung AUTOMATIS MEMASUKKAN judul dan isi cadangan itu ke kamus lo!
warna = mobil_gua.setdefault("color", "Hitam")
print("11a. Hasil .setdefault:", warna)
print("11b. Kondisi Kamus Kini:", mobil_gua) # Judul 'color': 'Hitam' otomatis nambah di dalam!

print("-" * 65)