# ==============================================================================
#      DOKUMENTASI MINI: PYTHON MATH FUNCTIONS (OPERASI MATEMATIKA)
# ==============================================================================

# # 1. FUNGSI BAWAAN (BUILT-IN): LANGSUNG PAKE TANPA IMPORT
# # Artinya: Fungsi-fungsi dasar matematika yang udah ada dari lahir di Python.

# # min() dan max() 
# # Nyari nilai paling kecil (lowest) atau paling gede (highest).
# # Analogi Dota: Kayak ngecek Net Worth paling miskin (min) dan paling kaya (max)
x = min (5, 10, 25)
y = max (5, 10, 25) 

print("Paling kecil :", x)
print("Paling besar :", y)

print("-" * 30)

# #  abs() (Absolute Value)
# # Mengubah angka minus (negatif) otomatis jadi positif.
x = abs(-7.25)

print("Nilai mutlak :", x)

print("-" * 30)


# # pow(x, y) (Power)
# # Nyari hasil pangkat (x pangkat y). Nilai pow(4, 3) sama aja kayak 4 * 4 * 4.
# # Analogi Cybersec: Buat ngitung total kombinasi password pas brute force!
z = pow(4, 3)

print("Hasil pangkat:", z) # Hasil: 64

print("-" * 30)

# ==============================================================================
# # 2. PENGGUNAAN MODUL MATEMATIKA (import math)
# # Aturannya: Wajib ketik 'import math' di baris paling atas sebelum fungsi dipake.
# ==============================================================================
import math

# # math.sqrt() (Square Root)
# # Nyari nilai akar kuadrat dari sebuah angka. Hasilnya otomatis tipe data float.
x = math.sqrt(64)

print("Akar kuadrat :", x)

print("-" * 30)

# # math.ceil() dan math.floor()
# # Analogi Dota: Kayak pembulatan status mekanik game.
# # math.ceil()  -> Dibuletin ke ATAS ke bilangan bulat terdekat.
# # math.floor() -> Dibuletin ke BAWAH (komanya langsung dibuang).
x = math.ceil(1.4)
y = math.floor(1.4)

print("Bulet ke atas :", x)
print("Bulet ke bawah :", y)

print("-" * 30)

# # math.pi
# # Manggil nilai konstanta PI (3.14...) yang presisi bawaan matematika
x = math.pi

print("Nilai PI:", x) 