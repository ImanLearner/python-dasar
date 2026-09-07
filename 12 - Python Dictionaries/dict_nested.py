# # PYTHON NESTED DICTIONARY (KAMUS DI DALAM KAMUS)
# ===================================================================
# # Karakteristik: Satu Dictionary besar nampung beberapa Dictionary kecil.
# # Konsep ini mirip banget sama struktur data akun game atau database web!
# ===================================================================

# # 1. Cara Pertama: Langsung Gabungin dari Awal
# # Bikin satu wadah besar yang isinya langsung dijabarkan anak-anaknya.
keluarga_saya = {
    "anak1" : {
        "nama" : "Emil",
        "tahun" : 2003
    },
    "anak2" : {
        "nama" : "Tobias",
        "tahun": 2007
    },
    "anak3" : {
        "nama" : "Linus",
        "tahun" : 2012
    }
}

print("Hasil Cara Pertama (Langsung) :", keluarga_saya)
print("-" * 50)


# # 2. Cara Kedua: Bikin Terpisah Baru Digabung (Jalur Rapi)
# # Bikin satu-satu dulu kamus kecilnya, baru dimasatin ke satu kamus besar.
child1 = {"nama" : "Emil", "Tahun" : 2003}
child2 = {"nama" : "Tobias", "Tahun" : 2007}
child3 = {"nama" : "Linus", "Tahun" : 2012}

# Dimasukin ke variabel baru
keluarga_baru = {
    "anak1" : child1,
    "anak2" : child2,
    "anak3" : child3
}

print("Hasil Cara Kedua (Terpisah)  :", keluarga_baru)
print("-" * 50)


# # 3. Cara Akses Data (Double Indexing / Kurung Siku Dobel)
# # Aturannya: Panggil Kamus Luar dulu, baru disusul panggil Kamus Dalam.
print("=== CARA AKSES NESTED DICT ===")
print("Nama Anak Kedua :", keluarga_saya["anak2"]["nama"]) # Hasil: Tobias
print("-" * 50)


# # 4. LOOPING NESTED DICT (LOOP DI DALAM LOOP)
# # Variabel sengaja diganti biar gak klise (pake 'slot' dan 'data_anak')
# # Loop pertama ngebuka pintu luar, Loop kedua ngebongkar isi dalemnya!
print("=== HASIL LOOPING NESTED DICT ===")

for slot, data_anak in keluarga_saya.items():
    print("Kategori :", slot) # Nyetak 'anak1', 'anak2', dst.
    
# Loop kedua buat ngebongkar isi dari 'data_anak'
    for info in data_anak:
        # info = judulnya (nama), data_anak[info] = isinya (Emil)
        print(info + ":", data_anak[info])
