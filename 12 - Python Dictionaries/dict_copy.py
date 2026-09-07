# # PYTHON DICTIONARY (MENYALIN / COPY DATA)
# ===================================================================
# # PENTING: Kagak bisa asal copas pake tanda sama dengan (dict2 = dict1)!
# # Karena itu cuma bikin "kaca spion" (referensi). Kalau dict1 diubah, 
# # dict2 bakal ikut berubah otomatis. Ngeri kalau data target lo rusak!
# ===================================================================

# Bikin data master awal (Data Asli)
kamus_asli = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1945
}

# # JALUR ZONK (CONTOH YANG SALAH): cuma pake "="
# # kamus_zonk = kamus_asli
# # Kalau lo ubah "year" di kamus_zonk, "year" di kamus_asli IKUT BERUBAH. Janji jangan gini!


# # 1. Cara Aman Pertama: Pake Method .copy()
# # Ini bakal bikin duplikat fisik yang bener-bener baru dan terpisah di memori.
kamus_salinan_1 = kamus_asli.copy()

print("Hasil Salinan Pake .copy()")
print("Data Duplikat 1 :",kamus_salinan_1)
print("-" * 50)


# # 2. Cara Aman Kedua: Pake Fungsi Bawaan dict()
# # Fungsinya sama persis, ngebuka bungkus baru buat ngedupel data asli lo.
kamus_salinan_2 = dict(kamus_asli)

print("Hasil Salinan Pake Fungsi dict():")
print("Data Duplikat 2 :", kamus_salinan_2)