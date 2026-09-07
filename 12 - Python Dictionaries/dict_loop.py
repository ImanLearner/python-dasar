# # PYTHON DICTIONARY (LOOPING / PERULANGAN DATA)
# ===================================================================
# # Karakteristik For Loop di Dict: Secara default cuma ngambil KEY.
# # Tapi ada method khusus (.values(), .keys(), .items()) buat custom!
# ===================================================================

# Bikin data awal terget simulasi dulu
target_dict = {
    "username": "iman_play",
    "Status": "Target Terkunci",
    "level_akun": "Whales" 
}

# # 1. Loop Standar (Otomatis Cuma Ngambil KEY Doang)
# # Kalau lo langsung tembak nama dictionary-nya, Python cuma bakal ngeluarin judul datanya (Key).
print("Hasil Loop Stander (Ambil Key):")
for x in target_dict:
    print(x)
print("-" * 50)


# # 2. Ambil VALUE Pake Cara Manual / Indexing
# # Kita tetep loop key-nya, tapi pas di-print kita panggil pake format target_dict[x]
print("Hasil Ambil Value Pake .values():")
for x in target_dict.values():
    print(x)
print("-" * 50)


# # 4. Ambil KEY Secara Eksplisit Pake Method .keys()
# # Hasilnya sama kayak nomor 1, tapi cara ini mempertegas di kodingan kalau lo emang mau nyari KEY-nya
print("Hasil Ambil Key Pake .keys():")
for x in target_dict.keys():
    print(x)
print("-" * 50)

# # 5. DUET MAUT: Ambil KEY & VALUE Sekaligus Pake .items()
# # WAJIB HUKUMNYA pake 2 variabel (misal x dan y) biar gak eror. 
# # Variabel pertama (x) bakal otomatis dapet Key, variabel kedua (y) dapet Value.
print("Hasil Duet Maut (Key & Value Barengan) Pake .items():")
for x, y in target_dict.items():
    print("Kunci :", x, "| Isinya :", y)
print("-" * 50)