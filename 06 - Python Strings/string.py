# DASAR-DASAR STRING (TEKS) DI PYTHON

# --- 1. Cara Bikin String ---
# Bisa pake kutip satu ('') atau kutip dua (""), hasilnya sama aja.
a = "Hello"
b = 'Hello'

# --- 2. Kutip di Dalam Kutip ---
# Biar gak error, kutip di dalem harus BEDA sama kutip yang ngebungkus di luar.
print("It's alright")          # Luar kutip dua, dalem kutip satu
print("Dia bilang 'Halo'")     # Luar kutip dua, dalem kutip satu
print('Dia bilang "Halo"')     # Luar kutip satu, dalem kutip dua

# --- 3. String Multi-baris (Multiline) ---
# Pake kutip tiga sebanyak 3 biji (bisa ''' atau """). Berfungsi juga ngejaga spasi/Enter kita.
tulisan_panjang = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt."""
print(tulisan_panjang)


# ==========================================
# MANIPULASI & Strings are Arrays
# ==========================================

# --- 4. String adalah Array (Indexing) ---
# Di Python, teks itu kumpulan karakter yang punya nomor urut (indeks mulai dari 0).
# Pake kurung siku [] buat ngambil hurufnya.
teks = "Hello, World!"
print(teks[1])  # Hasilnya: 'e' (karena H=0, e=1, l=2, dst)

# --- 5. Looping String (Ecer Huruf) ---
# Kita bisa belah string per huruf pake perulangan 'for'.
for x in "banana":
    print(x)    # Bakal nyetak huruf b, a, n, a, n, a ke bawah

# --- 6. Cek Panjang String ---
# Pake fungsi len() buat ngitung total huruf/karakter (spasi & simbol ikut dihitung).
sapa = "Hello, World!"
print(len(sapa))  # Hasilnya: 13


# ==========================================
# CEK KATA/CHECK STRING (KEYWORD 'in')
# ==========================================

# --- 7. Cek Apakah Ada (in) ---
# Hasilnya berupa Boolean (True kalau ada, False kalau gak ada).
info = "The best things in life are free!"
print("free" in info)  # Hasilnya: True

# Contoh pake IF (bakal nyetak cuma kalo katanya ada):
if "free" in info:
    print("Mantap, kata 'free' ketemu!")

# --- 8. Cek Apakah GAK Ada (not in) ---
# Kebalikan dari 'in' (True kalau kata itu MEMANG GAK ADA).
print("expensive" not in info)  # Hasilnya: True

# Contoh pake IF:
if "expensive" not in info:
    print("Aman, gak ada kata 'expensive' di sini.")