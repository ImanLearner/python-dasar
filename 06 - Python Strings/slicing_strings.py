# TEKNIK POTONG STRING (SLICING) DI PYTHON
# Rumus Dasar: variabel[mulai : sampai_sebelum]

# Peta Indeks kata "PROGRAMMER":
#  P   R   O   G   R   A   M   M   E   R  <-- Hurufnya
#  0   1   2   3   4   5   6   7   8   9  <-- Ngetung Maju (Dari 0)
# -10 -9  -8  -7  -6  -5  -4  -3  -2  -1  <-- Ngetung Mundur (Gak ada -0)

teks = "PROGRAMMER"

# 1. Slicing Standar (Ambil Tengahnya)
# Ambil dari indeks 1 sampai SEBELUM 4 (indeks 4 gak ikut)
print(teks[1:4])   # Output: ROG

# 2. Potong dari Paling Depan
# Kalau kirinya kosong, otomatis mulai dari indeks 0
print(teks[:3])    # Output: PRO

# 3. Potong sampai Paling Ujung Belakang
# Kalau kanannya kosong, otomatis bablas sampai huruf terakhir
print(teks[4:])    # Output: RAMMER

# 4. Slicing pake Angka Minus (Mundur dari Belakang)
# Ambil dari indeks -4 sampai SEBELUM -1 (indeks -1 gak ikut)
print(teks[-4:-1]) # Output: MME