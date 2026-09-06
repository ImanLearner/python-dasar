#  PYTHON TERNARY OPERATOR 
# ==========================================
# Deskripsi: Jalan pintas menulis If-Else dan If-Elif-Else hanya dalam 1 baris.

num = 6

# -------------------------------------------------------------------------
# 1. TERNARY STANDAR (Pengganti If-Else)
# -------------------------------------------------------------------------

# CARA BIASA (4 Baris)
# if num >= 5:
#     status = "Boleh Masuk"
# else:
#     status = "Pulang Tidur"

# CARA TERNARY (Cuma 1 Baris!)
# Rumus Baca: [Hasil jika Benar] if [Syaratnya] else [Hasil jika Salah]
status = "Boleh Masuk" if num >= 5 else "Pulang Tidur"
print("1. Hasil Ternary Standar =", status)
# Output: Boleh Masuk

# -------------------------------------------------------------------------
# 2. NESTED TERNARY (Pengganti If-Elif-Else)
# -------------------------------------------------------------------------

# CARA BIASA (Menggunakan If-Elif-Else)
# if num == 5:
#     x = "Fri"
# elif num == 6:
#     x = "Sat"
# elif num == 7:
#     x = "Sun"
# else:
#     x = "weekday"

# CARA TERNARY (Nested / Bersarang)
# Cara baca: Evaluasi dilakukan berantai dari kiri ke kanan.
x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"
print("2. Hasil Nested Ternary =", x)
# Output: Sat


# -------------------------------------------------------------------------
# CARA MEMBACA LOGIKA NESTED TERNARY:
# -------------------------------------------------------------------------
# - Ambil "Fri" jika num sama dengan 5.
# - Kalau bukan, ambil "Sat" jika num sama dengan 6.
# - Kalau bukan, ambil "Sun" jika num sama dengan 7.
# - Kalau semuanya salah, hasil otomatis menjadi "weekday".