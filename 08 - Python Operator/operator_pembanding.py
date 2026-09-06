# PYTHON COMPARISON OPERATORS (OPERATOR PEMBANDING)
# =========================================================================
# Deskripsi: Digunakan untuk membandingkan dua nilai.
# Hasil akhir dari operasi ini SELALU menghasilkan Boolean: True atau False.

# Kita siapkan simulasi variabel gaib (seolah-olah didapat otomatis dari sistem)
x = 10
y = 5

print("Nilai x =", x)
print("Nilai y =", y)
print("-" * 40)


# 1. EQUAL / SAMA DENGAN (==)
# Fungsi: Memeriksa apakah nilai kiri SAMA DENGAN nilai kanan.
# Ingat: Pake tanda sama dengan dua kali (==), kalau cuma satu (=) itu untuk mengisi variabel.
hasil_1 = (x == y)
print("1. Apakah x == y ?", hasil_1)  # Output: False


# 2. NOT EQUAL / TIDAK SAMA DENGAN (!=)
# Fungsi: Memeriksa apakah nilai kiri TIDAK SAMA DENGAN nilai kanan.
hasil_2 = (x != y)
print("2. Apakah x != y ?", hasil_2)  # Output: True


# 3. GREATER THAN / LEBIH BESAR (>)
# Fungsi: Memeriksa apakah nilai kiri LEBIH BESAR dari nilai kanan.
hasil_3 = (x > y)
print("3. Apakah x > y  ?", hasil_3)  # Output: True


# 4. LESS THAN / LEBIH KECIL (<)
# Fungsi: Memeriksa apakah nilai kiri LEBIH KECIL dari nilai kanan.
hasil_4 = (x < y)
print("4. Apakah x < y  ?", hasil_4)  # Output: False


# 5. GREATER THAN OR EQUAL TO / LEBIH BESAR ATAU SAMA DENGAN (>=)
# Fungsi: Memeriksa apakah nilai kiri LEBIH BESAR atau MINIMAL SAMA DENGAN nilai kanan.
hasil_5 = (x >= y)
print("5. Apakah x >= y ?", hasil_5)  # Output: True


# 6. LESS THAN OR EQUAL TO / LEBIH KECIL ATAU SAMA DENGAN (<=)
# Fungsi: Memeriksa apakah nilai kiri LEBIH KECIL atau MAKSIMAL SAMA DENGAN nilai kanan.
hasil_6 = (x <= y)
print("6. Apakah x <= y ?", hasil_6)  # Output: False

# =========================================================================
# CATATAN :
# Operator pembanding inilah yang nanti menjadi motor penggerak utama
# dalam struktur vertikal If-Elif-Else yang rapi dan terstruktur.