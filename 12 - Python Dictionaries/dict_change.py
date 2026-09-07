# # PYTHON DICTIONARY: CHANGE ITEMS (MENGUBAH ISI)
# ===================================================================
# # Di Python, buat ngubah isi data ada 2 cara resmi dari W3Schools.
# # Dua-duanya sama-sama nembak "Judul" buat ganti "Isi"-nya!
# ===================================================================

# Data awal mobil sport
mobil_gua = {
    "Brand": "Supra",
    "Model": "Super",
    "year": 1990
}

print("=== DATA AWAL MOBIL ===")
print(mobil_gua)
print("-" * 50)

# # CARA 1: Tembak Langsung Pake Kurung Siku ['judul']
# # Cara paling simpel kalau cuma mau ngubah SATU data doang.
# # Rumus: nama_dict["judul"] = isi_baru
mobil_gua["year"] = 2000

print("1. Hasil ubah pake cara manual:")
print(mobil_gua) # Tahunnya berubah menjadi 2000
print("-" * 50)


# # CARA 2: Pake Method `.update()`
# # Cara elegan kalau mau ngubah data pake format dictionary lagi.
# # Aturan wajib: Isi di dalem kurung .update() HARUS dibungkus kurung kurawal {} lagi.
mobil_gua.update({"year": 2020})

print("2. Hasil ubah pake .update():")
print(mobil_gua)    # Tahunnya ditimpa lagi jadi 2020
print("-" * 50)

# Tampilannya otomatis berbaris rapi ke bawah
for judul, isi in mobil_gua.items():
    print(judul + ":", isi)
