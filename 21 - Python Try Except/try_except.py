# ==============================================================================
#      DOKUMENTASI MINI: PYTHON TRY EXCEPT (FITUR ANTI RECT / PERISAI ANTI MATI)
# ==============================================================================

# # Latar Belakang:
# # Biasanya kalau ada error di Python, program lu langsung WIPE OUT (Crash/Mati).
# # Pake 'try except' itu ibarat lu pake item IMMORTALITY di Mobile Legends atau 
# # aegis di Dota. Begitu lu kena hit error, lu gak mati, tapi bisa hidup lagi!

# ==============================================================================
# # 1. STRUKTUR DASAR (TRY & EXCEPT)
# # 🔹 'try'    -> Tempat lu "Open War" atau jalanin aksi yang berisiko error/mati.
# # 🔹 'except' -> "Asuransi Penyelamat". Kalau di 'try' lu mati/error, block ini
# #                bakal jalan biar game/program lu GAK CRASH.
# ==============================================================================
print("--- TEST 1: COBA WAR PAKE PERISAI ANTI MATI ---")
try:
    # Aksi berisiko: Kita panggil variabel 'x' yang BELUM PERNAH DICREATE.
    # Harusnya ini bikin game langsung CRASH/Mati total.
    print(X)
except:
    # Karena ada perisai except, crash-nya ditahan! Malah baris ini yang jalan:
    print("[!] Gagal manggil x, tapi tenang... Hero lu gak mati, program lanjut!")

print("-" * 40)

# ==============================================================================
# # 2. SPECIFIC ERROR HANDLING (COUNTER HERO COUNTER ITEM)
# # Taktik: Lu bisa pasang perisai yang beda-beda tergantung jenis serangannya (jenis error).
# # Contoh: 'NameError' itu khusus buat nangkal error karena salah sebut nama variabel.
# ==============================================================================
print("--- TEST 2: COUNTER JENIS ATTACK TERTENTU ---")
try:
    print(x)
except NameError:
    print("[!] Terjadi NameError: Lu salah/belum bikin nama variabelnya, Cuy!")
except:
    print("[!] Jenis error lain yang kena. Tetep aman!")

print("-" * 40)

# ==============================================================================
# # 3. FITUR TAMBAHAN: ELSE & FINALLY
# # 🔹 'else'    -> Hanya jalan kalau war-nya menang mulus TANPA ADA ERROR.
# # 🔹 'finally' -> Gak peduli lu menang war atau mati dibantai, baris ini AKAN 
# #                 SEALU JALAN di akhir. (Cocok buat beresin/tutup resource).
# ==============================================================================
print("--- TEST 3: FITUR ELSE DAN FINALLY ---")
try:
    print("Aman... Lagi nge-farming buff, gak ada musuh.")
except:
    print("[!] Waduh kena gank!")
else:
    print("[+] GG WP! Farming sukses tanpa kendala (Aksi jika NO ERROR).")
finally:
    print("[*] Game Selesai. Mau menang atau kalah, tetep kembali ke Lobby (FINALLY).")

print("-" * 40)

# ==============================================================================
# # 4. RAISE AN EXCEPTION (BIKIN FITUR BAN/GG OTOMATIS)
# # Taktik: Kalau lu pengen program lu SENGAJA CRASH/MATI pas ada kondisi terlarang 
# #         (misal ada cheat masuk), lu bisa pake kata 'raise'.
# # Analogi: Fitur 'Surrender' atau 'Banned Akun' otomatis.
# ==============================================================================
# Contoh: Duit klub/darah gak boleh minus. Kalau minus, langsung force close game!
darah_hero = -10 

if darah_hero < 0:
    # Sengaja kita bikin error sendiri biar programnya berhenti di sini
    raise Exception("Sorry, darah hero gak boleh minus! Akun lu ke-suspend!")