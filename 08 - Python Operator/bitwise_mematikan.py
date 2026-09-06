# BITWISE OPERATORS (OPERATOR ANGKA BINER)
# ==============================================================================
# Rumus Dasar: Komputer itu cuma tahu angka biner. 
# Angka 1 dianggap TRUE, Angka 0 dianggap FALSE.
#
# Kita pakai dua angka contoh ini buat eksperimen:
# Angka 5  di memori komputer bentuk binernya adalah: 0101
# Angka 3 di memori komputer bentuk binernya adalah: 0011
# ==============================================================================

x = 5  # Biner: 0101
y = 3  # Biner: 0011

# ------------------------------------------------------------------------------
# 1. OPERATOR & (AND) -> Nyari yang DUA-DUANYA ANGKANYA 1
# ------------------------------------------------------------------------------
# Cara komputer ngitung vertikal:
# 0101  (angka 5)
# 0011  (angka 3)
# ---- & (Dua-duanya harus 1 biar jadi 1)
# 0001  (Biner 0001 itu adalah angka 1 di matematika)
print("Hasil x & y :", x & y)  # Hasil di terminal: 1


# ------------------------------------------------------------------------------
# 2. OPERATOR | (OR) -> ASALKAN ADA ANGKA 1, LANGSUNG JADI 1
# ------------------------------------------------------------------------------
# Cara komputer ngitung vertikal:
# 0101  (angka 5)
# 0011  (angka 3)
# ---- | (Asal ada angka 1, gas jadi 1)
# 0111  (Biner 0111 itu adalah angka 7 di matematika)
print("Hasil x | y :", x | y)  # Hasil di terminal: 7


# ------------------------------------------------------------------------------
# 3. OPERATOR ^ (XOR) -> HARUS BEDA BARU JADI 1 (Kalau kembar malah jadi 0)
# ------------------------------------------------------------------------------
# Cara komputer ngitung vertikal:
# 0101  (angka 5)
# 0011  (angka 3)
# ---- ^ (1 ketemu 1 jadi 0, 1 ketemu 0 jadi 1)
# 0110  (Biner 0110 itu adalah angka 6 di matematika)
print("Hasil x ^ y :", x ^ y)  # Hasil di terminal: 6


# ------------------------------------------------------------------------------
# 4. OPERATOR ~ (NOT) -> TUKANG MEMBANTAH / MEMBALIKKAN ANGKA
# ------------------------------------------------------------------------------
# Rumus cepat matematika Python: ~x itu rumusnya adalah -(x + 1)
# Jadi kalau x = 5, hasilnya pasti -(5 + 1) = -6
print("Hasil ~x    :", ~x)  # Hasil di terminal: -6


# ------------------------------------------------------------------------------
# 5. OPERATOR << (Left Shift) -> GESER BIT KE KIRI (Angka makin GEDE)
# ------------------------------------------------------------------------------
# x << 2 artinya biner angka 5 (0101) digeser ke kiri sebanyak 2 kali.
# Kosongnya diisi angka 0 di buntut, biner berubah jadi: 010100 (Angka 20)
print("Hasil x << 2:", x << 2)  # Hasil di terminal: 20


# ------------------------------------------------------------------------------
# 6. OPERATOR >> (Right Shift) -> GESER BIT KE KANAN (Angka makin KECIL)
# ------------------------------------------------------------------------------
# x >> 2 artinya biner angka 5 (0101) digeser ke kanan sebanyak 2 kali.
# Buntut paling kanan dibuang/jatuh, biner berubah jadi: 0001 (Angka 1)
print("Hasil x >> 2:", x >> 2)  # Hasil di terminal: 1