# MATERI: PYTHON LOGICAL OPERATORS (OPERATOR LOGIKA)
# =========================================================================
# Deskripsi: Digunakan untuk menggabungkan beberapa kondisi pembanding.
# Terdiri dari 3 jenis utama: and, or, dan not.

x = 5

# --- [ 1. OPERATOR AND ] ---
# Aturan: Menghasilkan True HANYA JIKA semua kondisi bernilai BENAR.
# Jika ada satu saja yang salah, hasil akhirnya langsung False.
kondisi_and = (x > 3 and x < 10)
# Penjelasan: Apakah 5 > 3? (True) DAN Apakah 5 < 10? (True). Karena dua-duanya True:
print("1. Hasil operasi AND =", kondisi_and)  # Output: True

 
# --- [ 2. OPERATOR OR ] ---
# Aturan: Menghasilkan True jika MINIMAL ADA SATU kondisi yang bernilai BENAR.
# Hanya akan bernilai False jika semua kondisi salah total.
kondisi_or = (x < 4 or x == 5)
# Penjelasan: Apakah 5 < 4? (False) ATAU Apakah 5 == 5? (True). Karena ada satu yang True:
print("2. Hasil operasi OR  =", kondisi_or)   # Output: True


# --- [ 3. OPERATOR NOT ] ---
# Aturan: Membalikkan hasil logika. Yang True diubah jadi False, yang False jadi True.
kondisi_not = not(x > 3 and x < 10)
# Penjelasan: Hasil di dalam kurung adalah True (dari contoh nomor 1).
# Karena di depannya ada kata 'not', maka hasilnya dibalik total:
print("3. Hasil operasi NOT =", kondisi_not)  # Output: False


# =========================================================================
# Itu adalah cara Python untuk menulis: Operator Logika
# =========================================================================