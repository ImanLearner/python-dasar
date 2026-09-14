# ==============================================================================
#          DOKUMENTASI MINI: PYTHON JSON (TUKAR MENUKAR DATA INTERNET)
# ==============================================================================

# # Latar Belakang:
# # JSON (JavaScript Object Notation) itu format teks standar buat ngirim data di internet.
# # Python punya modul bawaan namanya 'json'. Jadi wajib ketik 'import json' di paling atas!

import json

# ==============================================================================
# # 1. PARSE JSON (CONVERT DARI JSON STRING KE DICTIONARY PYTHON)
# # Taktik: Pake perintah 'json.loads()' -> (load string).
# # Analogi: Kayak lu dapet kiriman paket berupa teks mentah dari luar, terus lu bongkar 
# #          biar jadi data Python (Dictionary) yang bisa diakses kuncinya.
# ==============================================================================

# Data JSON (Bentuknya string biasa, dibungkus kutip satu di luar)
data_json = '{"name": "Iman", "age": 23, "city": "Depok"}'

# Bongkar string JSON jadi Dictionary Python
data_python = json.loads(data_json)

print("--- HASH DARI JSON KE PYTHON ---")
print("Tipe Data setelah di-load", type(data_python))
print("Akses Umur :", data_python["age"])

print("-" * 30)

# ==============================================================================
# # 2. CONVERT PYTHON KE JSON STRING
# # Taktik: Pake perintah 'json.dumps()' -> (dump string).
# # Analogi: Lu punya data Dict di Python, terus lu bungkus jadi Teks Mentah (JSON) 
# #          biar bisa dikirim dengan aman lewat jaringan internet ke komputer lain.
# ==============================================================================

# Data awal bentuk Dictionary Python
akun_korban = {
    "username": "Imansyah",
    "level": 99,
    "is_active": True
}

# Bungkus jadi JSON String
json_string = json.dumps(akun_korban)

print("--- HASH DARI PYTHON KE JSON ---")
print("Tipe Data setelah di-dumps:", type(json_string))
print("Hasil Teks JSON:", json_string)

print("-" * 30)

# ==============================================================================
# # 3. TABEL KONVERSI OTOMATIS PYTHON KE JSON
# # Pas lu pake json.dumps(), Python bakal otomatis ngubah tipe data ke versi JSON:
# # Python      -->   JSON Equivalent
# # dict        -->   Object {}
# # list, tuple -->   Array []
# # str         -->   String ""
# # int, float  -->   Number
# # True, False -->   true, false (huruf kecil)
# # None        -->   null
# ==============================================================================

# Contoh nge-dump data campuran kasta lengkap
data_campuran = {
    "name": "Iman",
    "kuliah": True,         # Bakal jadi true
    "pets": None,           # Bakal jadi null
    "sister": ("Putri"),    # Bakal jadi Array []
    "cars": [
        {"model": "BMW 230", "mpg":27.5}
    ]
}

# ==============================================================================
# # 4. FORMATTING & ORDERING RESULT (TRIK BIAR RAPI)
# # Secara default, hasil json.dumps() itu satu baris panjang dan pusing dibaca.
# # Kita bisa pake parameter tambahan biar rapi di terminal:
# # indent=4       -> Ngasih spasi menjorok (tab) biar enak dibaca.
# # sort_keys=True -> Ngurutin nama kunci (Key) sesuai abjad (A-Z).
# ==============================================================================
print("--- HASIL JSON YANG RAPI & BERURUTAN (A-Z) ---")
json_rapi = json.dumps(data_campuran, indent=4, sort_keys=False)
print(json_rapi)

# Catatan Tambahan (Kustom Separator):
# Lu juga bisa ganti tanda pemisah default pake parameter 'separators':
# Contoh: json.dumps(x, indent=4, separators=(". ", " = "))