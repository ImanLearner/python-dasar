# --- 1. Cara Standar Cetak Variabel ---
# Fungsi print() emang tugas utamanya buat ngeluarin isi kotak/variabel.
x = "Python is awesome"
print(x)
print("-" * 30)


# --- 2. Nyetak Banyak Variabel Pake Koma (,) ---
# Otomatis dapet spasi gratis di antara kata. Gak usah repot nambahin spasi di dalem teks.
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)  # Hasil: Python is awesome
print("-" * 30)


# --- 3. Nyetak Banyak Variabel Pake Tanda Plus (+) ---
# Fungsinya nempelin teks (kayak dilem). Gak dapet spasi gratis!
# Makanya lo kudu ngasih spasi manual di dalem tanda kutipnya biar gak dempet.
x = "Python "  # Ada spasi di ujung
y = "is "      # Ada spasi di ujung
z = "awesome"
print(x + y + z)  # Hasil: Python is awesome
print("-" * 30)


# --- 4. Tanda (+) Ketemu Angka (Matematika) ---
# Kalau isinya angka murni, tanda (+) berubah fungsi jadi pertambahan matematika biasa.
x = 5
y = 10
print(x + y)  # Hasilnya otomatis jadi 15
print("-" * 30)


# --- 5. ZONA ERROR: Angka Ditambah Teks ---
# Alasan error: Tanda (+) gak bisa gabungin dua jenis data beda alam.
# Solusi bener: Kalau mau gabungin angka ama teks, WAJIB pake koma ( , ).
"""
x = 5
y = "John"
print(x + y)  # Jangan dilepas kutip tiganya biar program gak mogok
"""


# --- 6. Solusi Paling Aman: Pake Koma (,) ---
# Cara paling bener kalau mau gabungin variabel beda jenis (angka ama teks) ya pake koma.
x = 5
y = "Iman"
print(x, y)  # Aman jaya, hasilnya: 5 Iman