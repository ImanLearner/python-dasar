# # PYTHON DICTIONARY (MENAMBAH & UPDATE DATA)
# ===================================================================
# # Karakteristik Dictionary: Key-Value Pair, Unordered, & Changeable
# # Pake tanda kurung kurawal { } dan dipisah tanda titik dua (:)
# ===================================================================

# # 1. Bikin Dictionary Standar (Basis Data Target Modus)
# # Menyiapkan data awal sebelum kita manipulasi kodenya

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print("Hasil Awal Sebelum Ditambah")
print("Data Kamus AAwal :", thisdict)
print("-" * 50)

# # 2. Menambah Item Baru Pake Cara Indexing (Cara Paling Simpel)
# # Tinggal sebut nama key baru di dalem kurung siku [ ], lalu isi nilainya
# # Konsep ini mirip pas lo nampung data hasil pancingan input korban!
thisdict["color"] = "white"

print("Hasil Tambah Item Pake Indexing")
print("Data Setelah Ditambah :", thisdict)
print("-" * 50)

# # 3. Menambah / Update Item Pake Method update()
# # Aturannya: Argumen di dalam update() WAJIB berbentuk pasangan key:value lagi {}
# # JALUR MODUS: Kalau Key BELUM ADA -> Bakal otomatis ditambahin (kaya "status_target" di bawah)
# # JALUR MODUS: Kalau Key SUDAH ADA  -> Nilai lamanya bakal otomatis ditimpa/di-update!

# Contoh A: Menambah item baru karena key belum ada
thisdict.update({"Status_target": "Kena Lock"})

# Contoh B: Mengupdate data lama (Tahun 1964 diganti jadi 2026)
thisdict.update({"year": 2026})

print("Hasil Setelah Pake Method update()")
print("Data Kamus Terbaru    :", thisdict)
print("-" * 50)