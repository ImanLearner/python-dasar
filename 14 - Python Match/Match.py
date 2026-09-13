# ==============================================================================
#             DOKUMENTASI MINI: PYTHON MATCH STATEMENT (SI MULTI-SELEKSI)
# ==============================================================================

# 1. PENGGUNAAN DASAR: match CASE
# Artinya: "COCOKKIN NILAI VARIABEL SAMA PILIHAN YANG ADA"
# Daripada capek nulis if-elif-elif-elif kebanyakan, mending pakai match. 
# Python bakal ngecek nilainya sekali, terus langsung lompat ke case yang cocok.

day = 7
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

# CARA BACA: Cocokkan nilai dari variabel 'day'. Kalau day nilainya 4, jalanin perintah di bawah 'case 4'.
# Tes Logika: (day = 4). Python scan dari atas, ketemu 'case 4:', langsung cetak "Thursday".

print("-" * 30)

# 2. DEFAULT VALUE: GUNAKAN GARIS BAWAH (_)
# Artinya: "KALAU GAK ADA YANG COCOK, MASUK SINI"

day = 4 
match day:
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _:
        print("Looking Forward to the weekend")

# CARA BACA: Cek apakah day itu 6? Bukan. Apakah 7? Bukan. Ya udah, masuk ke pilihan terakhir (_).
# Tes Logika: (4 tidak sama dengan 6 atau 7). Karena gak ada yang cocok, masuk ke 'case _' dan cetak "Looking forward to the Weekend".

print("-" * 30)

# 3. GABUNGIN NILAI: PAKAI TANDA PIPA (|)
# Artinya: "OPERATOR OR (ATAU) VERSI RINGKAS"
day = 4

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6 | 7:
        print("I love weekends!")
# CARA BACA: Kalau day nilainya 1, 2, 3, 4, ATAU 5, cetak "Today is a weekday".
# Tes Logika: Karena day adalah 4, dan 4 ada di rombongan case pertama, maka jebol! Cetak "Today is a weekday".

print("-" * 30)

# 4. LEVEL LANJUTAN: SELEKSI TAMBAHAN PAKAI IF GUARDS
# Artinya: "DAH COCOK, TAPI DI-SELEKSI LAGI PAKAI SYARAT EXTRA"
month = 5
day = 4

match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in September")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in Oktober")
    case _:
        print("No Match")
# CARA BACA: Cek apakah day antara 1-5 DAN bulannya 4? Kalau bukan, cek apakah day 1-5 DAN bulannya 5?
# Tes Logika: Day lolos (4), dan month == 5 itu BENER. Jebol! Cetak "A weekday in May".

