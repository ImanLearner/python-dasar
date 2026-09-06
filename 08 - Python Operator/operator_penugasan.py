# PYTHON ASSIGNMENT OPERATORS
# ==========================================
# Deskripsi: Operator buat ngisi atau ngubah nilai variabel.

# 1. DASAR SAMA DENGAN (=)
# Fungsi: Memasukkan nilai dari kanan ke variabel di kiri.
x = 5
print("1. Nilai awal x =", x)  # Output: 5


# 2. ADD AND ASSIGN (+=)
# Konsep: x += 3 itu SAMA AJA KAYAK x = x + 3
# Penjelasan: Nilai x yang lama (5) ditambahin 3, terus disimpen lagi ke x.
x += 3
print("2. x += 3 hasilnya =", x)  # Output: 8


# 3. SUBTRACT AND ASSIGN (-=)
# Konsep: x -= 3 itu SAMA AJA KAYAK x = x - 3
# Penjelasan: Nilai x sekarang (8) dikurangin 3.
x -= 3
print("3. x -= 3 hasilnya =", x)  # Output: 5


# 4. MULTIPLY AND ASSIGN (*=)
# Konsep: x *= 3 itu SAMA AJA KAYAK x = x * 3
# Penjelasan: Nilai x sekarang (5) dikali 3.
x *= 3
print("4. x *= 3 hasilnya =", x)  # Output: 15


# 5. DIVIDE AND ASSIGN (/=)
# Konsep: x /= 3 itu SAMA AJA KAYAK x = x / 3
# Penjelasan: Nilai x sekarang (15) dibagi 3 (inget, hasilnya otomatis jadi Float!).
x /= 3
print("5. x /= 3 hasilnya =", x)  # Output: 5.0


# 6. MODULUS AND ASSIGN (%=)
# Konsep: x %= 3 itu SAMA AJA KAYAK x = x % 3
# Penjelasan: Nilai x sekarang (5.0) dicari sisa baginya dengan 3 (pake logika martabak lu tadi!).
x %= 3
print("6. x %= 3 hasilnya =", x)  # Output: 2.0


# 7. FLOOR DIVIDE AND ASSIGN (//=)
# Reset nilai x dulu biar gampang dihitung
x = 10
# Konsep: x //= 3 itu SAMA AJA KAYAK x = x // 3
# Penjelasan: Memotong koma hasil pembagian.
x //= 3
print("7. x //= 3 hasilnya =", x)  # Output: 3


# 8. EXPONENTIATION AND ASSIGN (**=)
# Konsep: x **= 3 itu SAMA AJA KAYAK x = x ** 3
# Penjelasan: Nilai x sekarang (3) dipangkatin 3 (3 * 3 * 3).
x **= 3
print("8. x **= 3 hasilnya =", x)  # Output: 27

# =========================================================================
