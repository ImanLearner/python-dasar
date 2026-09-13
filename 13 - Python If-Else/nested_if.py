# PYTHON NESTED IF (IF BERANAK)
# ==============================================================================

# 1. NESTED IF DASAR (Satu anak di dalam induk)
# Aturan Main: Pintu DALAM cuma bakal dicek kalau pintu LUAR udah jebol (True).
x = 25
if x > 10:
    print(" Di atas sepuluh")

    # Ini anaknya (Nested If), posisinya makin menjorok ke dalam
    if x > 20:
        print("dan juga di atas 20")
    else:
        print("di bawah 20")

    print("-" * 30)

# CARA BACA: 
# - Cek pintu luar: Apakah 41 > 10? Iya (True). Masuk ke dalam.
# - Cek pintu dalam: Apakah 41 > 20? Iya (True). Cetak "dan juga di atas 20!".


# ------------------------------------------------------------------------------
# 2. CONTOH KASUS SIMULASI NYATA (Bikin SIM)
# ------------------------------------------------------------------------------
umur = 20
punya_sim = False

if umur >= 17:
    # Anak pertama: Cek kelengkapan surat
    if punya_sim:
        print("Aman Bro, silahkan lanjut berkendara")
    else:
        print("Kena tilang lo, belum punya sim")

else:
    # Kalau umur di bawah 17, langsung mental ke sini tanpa ngecek SIM
    print("Bocil dilarang bawa motor!")

print("-" * 30)

# ------------------------------------------------------------------------------
# 3. KAPAN NESTED IF BISA DIGANTI PAKE OPERATOR 'and'?
# ------------------------------------------------------------------------------
# Kalau syaratnya sederhana dan sama-sama penting, mending digabung pake 'and'
# biar kodingannya gak terlalu menjorok ke dalam (makin clean).

suhu = 25
cerah = True

# Versi 1: Pake Nested If (Agak panjang)
if suhu > 20:
    if cerah:
        print("Mantap, gas pantai!")

# Versi 2: Pake 'and' (Hasilnya 100% SAMA, tapi lebih ringkas)
if suhu > 20 and cerah:
    print("Mantap, gas pantai!")

print("-" * 30)


# ------------------------------------------------------------------------------
# 4. KASUS LOGIN AKUN (Tiga Tingkat Anak - Batas Maksimal Biar Gak Mumet)
# ------------------------------------------------------------------------------

username = "Iman"
password = "Python123"
akun_aktif = True 

if username:
    if password:
        if akun_aktif:
            print("Login Sukses! Selamat Mabar")
        else:
            print("Akun lo kena ban/nonaktif,bro")
    else:
        print("Password-nya isi dulu woy!")
else:
    print("Username-nya mana?")

print("-" * 30)

# Perhitungan nilai dengan logika bertingkat:
score = 95
extra_credit = 1

if score >= 90:
  if extra_credit > 0:
    print("A+ grade")
  else:
    print("A grade")
elif score >= 80:
  print("B grade")
else:
  print("C grade or below")