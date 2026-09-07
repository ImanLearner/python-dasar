# # PYTHON DICTIONARY: REMOVE ITEMS (PENGHAPUSAN DATA)
# ===================================================================
# # Di Python, ada beberapa taktik buat ngebuang data di Dictionary.
# # Pilih cara sesuai kebutuhan perang lo di lapangan!
# ===================================================================

# 1. Menggunakan `.pop("nama_judul")`
# -> Menghapus data spesifik berdasarkan judul yang lo pilih.
mobil1 = {"brand": "Ford", "model": "Mustang", "year": 1964}
mobil1.pop("model") # Ngapus judul 'model' beserta isinya
print("1. Hasil Pake .pop()     :", mobil1)


# 2. Menggunakan `.popitem()`
# -> Otomatis ngapus data yang PALING TERAKHIR dimasukin ke kamus.
# -> Gak usah sebut nama judul di dalem kurungnya.
mobil2 = {"brand": "Ford", "model": "Mustang", "year": 1964}
mobil2.popitem() # Otomatis ngapus 'year' karena ada di paling ujung
print("2. Hasil Pake .popitem() :", mobil2)


# 3. Menggunakan Kata Kunci `del` (Delete)
# -> Pake cara manual buat ngapus judul spesifik. 
# -> Hasilnya mirip banget kayak .pop(), cuma beda gaya nulis doang.
mobil3 = {"brand": "Ford", "model": "Mustang", "year": 1964}
del mobil3["model"] # Ngapus judul 'model'
print("3. Hasil Pake del manual :", mobil3)

# 4. Menggunakan `.clear()`
# -> Ngosongin isi kamus sampai bersih total tanpa sisa.
# -> Laci lemarinya tetep ada, tapi isinya jadi zonk / kosong.
mobil4 = {"brand": "Ford", "model": "Mustang", "Tahun": 1995}
mobil4.clear() #Isinya dikuras habis
print("4. Hasil Pake .clear():     ", mobil4) # Hasil {}
print("-" * 50)

# ===================================================================
# # PERINGATAN KELAS BERBAHAYA (del TOTAL)
# ===================================================================
# Kalau lo ngetik `del nama_variabel` TANPA kurung siku judulnya,
# lo bakal ngehapus SELURUH VARIABLE itu dari memori komputer.
# Efeknya: Variabel itu dianggap GAK PERNAH ADA. Kalau di-print bakal CRASH!

mobil_bom = {"brand": "Ford", "model": "Mustang", "year": 1964}
del mobil_bom # Variabel mobil_bom dihancurkan total

# print(mobil_bom) 
# ⚠️ JANGAN DI-RUN BARIS DI ATAS! Bakal error: "NameError: name 'mobil_bom' is not defined"
