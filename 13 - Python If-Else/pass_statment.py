# ==============================================================================
#           DOKUMENTASI MINI: PYTHON PASS STATEMENT (SI PENYELAMAT ERROR)
# ==============================================================================

# 1. PENGGUNAAN: pass DI DALAM IF STATEMENT
# Artinya: "LEWATIN AJA, JANGAN NGAPA-NGAPAIN"
# Python itu gak bolehin ada blok kode (if, elif, else) yang kosong melompong. 
# Kalau belum tahu mau diisi apa, wajib kasih 'pass' biar gak kena IndentationError.
a = 33
b = 200

if b > a:
    pass
# CARA BACA: Jika b lebih besar dari a, lewati aja (nggak usah lakuin tindakan apa-apa).
# Tes Logika: (200 > 33 adalah True). Karena True, program masuk ke 'if' dan ketemu 'pass', jadi lanjut jalan tanpa error!

# ==============================================================================

# 2. FUNGSI UTAMA: pass SEBAGAI PLACEHOLDER (COCOK BUAT SKETSA KODE)
# Gak usah buru-buru mikirin logika lengkap. Sketsa dulu aja strukturnya, isi logikanya belakangan.
age = 16

if age < 18:
    pass # TODO: Tambahin logika buat yang di bawah umur nanti ya!
else:
    print("Access Granted")
# CARA BACA: Jika umur kurang dari 18, lewati dulu. Selain itu, cetak "Access granted".
# Tes Logika: (16 < 18 adalah True). Program bakal masuk ke blok 'if', ketemu 'pass', dan aman gak ada error meskipun belum ada kode eksekusinya.

# ==============================================================================

# 3. BEDA PENTING: pass vs KOMENTAR (#)
# Ingat: Komentar itu dicuekin sama Python. Tapi 'pass' itu dianggap perintah resmi (walau gak ngapa-ngapain).
# Jadi, kalau cuma dikasih komentar di dalam 'if', Python bakal marah dan error!

# CONTOH YANG SALAH (Bakal bikin Error):
# score = 85
# if score > 90:
#     # Ini nilai luar biasa (Kelewatan, gak ada perintah! Bakal IndentationError

# CONTOH YANG BENER (Pakai pass):
score = 85

if score > 90:
    pass # Ini nilai luar biasa
print("Score Processed")


# ==============================================================================

# 4. PENGGUNAAN DI BANYAK PERCABANGAN (if-elif-else)
# Lu bisa taruh 'pass' di cabang mana aja yang emang gak butuh aksi apa-apa.
value = 90

if value < 0:
    print("Negative value")
elif value == 0:
    pass # Kasus angka nol - gak butuh tindakan apa-apa
else:
    print("Positive Value")
# CARA BACA: Kalau negatif cetak teksnya, kalau nol lewati aja, kalau positif cetak teksnya.
# Tes Logika: (50 < 0 -> False), (50 == 0 -> False). Masuk ke 'else', cetak "Positive value".


# ==============================================================================

# 5. BONUS: pass DI KONTEKS LAIN (FUNGSI / FUNCTION)
# Selain di 'if', 'pass' juga sering dipakai pas kita bikin fungsi tapi belum mau nulis isinya.
def calculate_discount(price):
    pass # TODO: Bikin logika diskonnya belakangan

# Fungsinya udah terdaftar dan sah di python,tapi saat ini belum ngapa-ngapain.