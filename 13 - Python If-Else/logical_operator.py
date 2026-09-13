# ==============================================================================
#           DOKUMENTASI MINI: PYTHON LOGICAL OPERATORS (PENYAMBUNG SYARAT)
# ==============================================================================

# 1. OPERATOR: and (ARTINYA: "DUA-DUANYA WAJIB TRUE")
# Syarat kiri DAN syarat kanan HARUS BENER. Kalau ada satu aja yang salah, langsung gagal.
a = 200 
b = 33
c = 500

if a > b and c > a:
    print("Dua-duanya beneran True!")
# CARA BACA: Jika a lebih besar dari b DAN c lebih besar dari a, cetak teksnya.
# Tes Logika: (200 > 33 adalah True) DAN (500 > 200 adalah True). Karena dua-duanya True, jebol!


# 2. OPERATOR: or (ARTINYA: "SALAH SATU TRUE UDAH CUKUP")
# Gak usah serakah, mau syarat kiri atau kanan yang bener, yang penting ada satu yang True, langsung lolos.
a = 200
b = 33
c = 500

if a > b or a > c:
    print("Minimal ada satu syarat yang True!")
# CARA BACA: Jika a lebih besar dari b ATAU a lebih besar dari c, cetak teksnya.
# Tes Logika: (200 > 33 adalah True) ATAU (200 > 500 adalah False). Karena udah ada satu yang True, tetep lolos!

# 3. OPERATOR: not (ARTINYA: "MEMBALIKKAN KENYATAAN")
# Mengubah yang tadinya True jadi False, atau yang tadinya False jadi True. Nyebelin tapi penting.
a = 33
b = 200

if not a > b:
    print("a TIDAK lebih besar dari b")
# CARA BACA: Jika TIDAK BENAR bahwa a lebih besar dari b, cetak teksnya.
# Tes Logika: Aslinya 33 > 200 itu False (Salah). Tapi karena didepannya dikasih 'not', dibalik jadi True! Jalur jebol!


# ==============================================================================
#            CONTOH KASUS NYATA DI INDUSTRI (YANG PAKE MENJOROK KE BAWAH)
# ==============================================================================

# KASUS 1: Cek Batasan Angka (Range Checking)
score = 85

if score >= 0 and score <= 100:
    print("Nilai valid, bro!")
else:
    print("Nilai ngaco!")
# CARA BACA: Nilai harus di atas atau sama dengan 0 DAN sekaligus di bawah atau sama dengan 100.


# KASUS 2: Login Akun Game / Aplikasi
username = "Tobias"
password = "secret123"
is_verified = True

if username and password and is_verified:
    print("Login berhasil, selamat mabar!")
else:   
    print("Login gagal! Cek akun lo lagi.")
# CARA BACA: Username harus diisi DAN password harus diisi DAN akun harus sudah terverifikasi.