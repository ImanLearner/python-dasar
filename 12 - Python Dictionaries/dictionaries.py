# # PYTHON DICTIONARIES (KAMUS DATA SAKTI / KEY-VALUE PAIRS)
# =========================================================================
# # Aturan Main Dictionary:
# # 1. Menggunakan Kurung Kurawal { } dan formatnya -> "Key": "Value".
# # 2. Ordered   : Punya urutan tetap sejak Python 3.7 (urutan gak bakal berubah).
# # 3. Changeable: Isinya bebas lu ubah, tambah, atau hapus setelah dibuat.
# # 4. No Duplicates untuk KEY: NAMA LABEL (KEY) GAK BOLEH KEMBAR! 
# #    Kalau lu maksa bikin Key yang sama, nilai yang lama bakal DITIMPA ama yang baru.
# =========================================================================

# # 1. Cara Membuat & Print Dictionary Dasar
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print("Isi Dictionary Lengkap:", thisdict)
print("Tipe Datanya :", type(thisdict))
print("-" * 50)

# # 2. Cara Mengakses Isi Data (Panggil Pake Nama KEY/Label-nya)
# # Lu gak bisa manggil pake angka [0]. Wajib sebut nama labelnya di dalem kotak!
print("Merk Mobilnya :", thisdict["brand"])
print("Tahun Pembuatan :", thisdict["year"])
print("-" * 50)

# # 3. Hukum Duplikat KEY (Nilai Baru Bakal Menimpa Nilai Lama)
mobil_baru = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print("Hasil Duplikat Key (Tahun Berubah) :", mobil_baru)
print("-" * 50)

# # 4. Cek Jumlah Data (len()) & Isinya Bebas Tipe Data Apa Saja (Bisa List)
server_profile = {
    "ip_address": "192.168.1.1",
    "is_active": True,
    "total_attack": 5,
    "allowed_users": ["admin", "moderator", "root"] # <-- Isinya boleh list
}

print("Profil Server :", server_profile)
print("Jumlah Kategori Data di Server :", len(server_profile))
print("-" * 50)


# # 5. Cara Alternatif: Pake Constructor dict()
# # Bikin dictionary tanpa kurung kurawal, melainkan pake fungsi dict() langsung
user_Data = dict(name="Iman", age=36, country="Depok")
print("Hasil Pembuatan pake dict() :", user_Data)