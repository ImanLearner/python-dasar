# ==============================================================================
#                 DOKUMENTASI PYTHON: IF STATEMENT & CONDITIONS
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. OPERATOR PERBANDINGAN (MATEMATIKA LOGIKA)
# ------------------------------------------------------------------------------
# Pake operator ini buat ngecek kondisi (Hasilnya pasti True atau False)

# a == b   -> SAMA DENGAN
# a != b   -> TIDAK SAMA DENGAN
# a < b    -> KURANG DARI
# a <= b   -> KURANG DARI ATAU SAMA DENGAN
# a > b    -> LEBIH DARI
# a >= b   -> LEBIH DARI ATAU SAMA DENGAN

# ------------------------------------------------------------------------------
# 2. CARA KERJA IF STATEMENT (CONTOH DASAR)
# ------------------------------------------------------------------------------
# Jika kondisi bernilai True, kode di dalemnya bakal dieksekusi.
# Jika False, kodenya dilewati (di-skip).

a = 33
b = 200
if b > a:
    print("LOG: b lebih besar dari a. kondisi terpenuhi")

# Contoh nyatanya buat ngecek angka positif:
number = 15
if number > 0:
    print("LOG: Angka ini positif")

# ------------------------------------------------------------------------------
# 3. HUKUM SAKRAL: INDENTASI (TAB / SPASI)
# ------------------------------------------------------------------------------
# Python GAK PAKE kurung kurawal {} kayak Dart/Java buat nandain isi blok kode.
# Python pake INDENTASI (menjorok ke dalem pake 1x TAB atau 4x SPASI).

# CONTOH EROR (Jangan dicolok komentarnya nanti programnya meledak):
# if b > a:
# print("Ini bakal IndentationError karena gak masuk ke dalem!")

# CATATAN: Jumlah spasi/tab di dalem satu blok harus sama rata semuanya.


# ------------------------------------------------------------------------------
# 4. BANYAK PERINTAH DI DALAM SATU IF BLOCK
# ------------------------------------------------------------------------------
# Lo bisa naruh banyak baris kode di dalem if, asalkan tingkat menjoroknya (Tab) sama.

age = 20
if age >= 18:
    print("1. Anda sudah dewasa")
    print("2. Anda sudah bisa bikin KTP")
    print("3. Hak legal penuh sudah aktif.")

# ------------------------------------------------------------------------------
# 5. MENGECEK VARIABEL BOOLEAN LANGSUNG
# ------------------------------------------------------------------------------
# Variabel yang isinya True/False bisa langsung ditaruh di "if" tanpa operator ==

is_logged_in = True

if is_logged_in:
    print("LOG: Akses Diterima,Selamat datang kembali, atmin!")

# ------------------------------------------------------------------------------ 
# 6. SIFAT GAIB PYTHON: "TRUTHY" & "FALSY" VALUES
# ------------------------------------------------------------------------------
# Di Python, lo bisa masukin data selain Boolean ke dalem 'if'.
# Ada data yang otomatis dianggap FALSE, ada yang otomatis dianggap TRUE.

# A. Data yang dianggap FALSE (Falsy):
# - Angka Nol (0)
# - String Kosong ("")
# - None (Kosong/Null)
# - List/Data koleksi yang kosong ([])

# B. Data yang dianggap TRUE (Truthy):
# - Angka positif atau negatif (5, -3)
# - String yang ada isinya (Bahkan string "False" dianggap TRUE karena gak kosong!)

# Contoh pembuktian Truthy/Falsy:
nama_hacker = "ImanPlay" # String ada isinya (Truthy)

if nama_hacker:
    print(f"LOG: String gak kosong, User aktif: {nama_hacker}")

pintu_rahasia = 0 # Angka 0 (Falsy)

if pintu_rahasia:
    # Bagian ini HANYA JALAN kalau laser NYALA (True)
    print("LOG: Laser nyala! Penyusup ketahuan, alarm bunyi!")
else:
    # Bagian ini OTOMATIS JALAN kalau laser MATI (False)
    print("LOG: Laser mati! Aman, mari kita menyelinap masuk! Muehehe.")

