# Ada 3 jenis utama: int, float, dan complex
x = 1    # int (bilangan bulat)
y = 2.8  # float (bilangan desimal)
z = 1j   # complex (bilangan kompleks)

print(type(x))
print(type(y))
print(type(z))

# --- INTEGER (int) ---
# Bilangan bulat, bisa positif/negatif, panjangnya bebas gak terbatas
angka_1 = 1
angka_2 = 35656222554887711
angka_3 = -3255522

print(type(angka_1))

# --- FLOAT (float) ---
# Bilangan desimal (pake titik, bukan koma)
desimal_1 = 1.10
desimal_2 = 1.0
desimal_3 = -35.59

print(type(desimal_1))

# Float juga bisa pake format ilmiah (e / E) artinya "pangkat 10"
ilmiah_1 = 35e3    # sama dengan 35 * 10^3 = 35000.0
ilmiah_2 = 12E4    # sama dengan 12 * 10^4 = 120000.0
ilmiah_3 = -87.7e1 # sama dengan -87.7 * 10^1 = -877.0

print(type(ilmiah_1))

# --- COMPLEX ---
# Angka yang ada bagian imajiner, ditandai pake huruf "j"
kompleks_1 = 3+5j
kompleks_2 = 5j
kompleks_3 = -5j

print(type(kompleks_1))

# ------------------------------------------------
# 2. KONVERSI TIPE DATA (TYPE CONVERSION)

# Kita bisa ubah tipe data pake fungsi int(), float(), atau complex()
p = 1    # int
q = 2.8  # float
r = 1j   # complex

# Ubah dari int ke float
f = float(p)  # Hasilnya jadi 1.0

# Ubah dari float ke int (angkanya bakal dipotong, bukan dibulatin)
i = int(q)    # Hasilnya jadi 2 (bukan 3)

# Ubah dari int ke complex
c = complex(p) # Hasilnya jadi (1+0j)

print(f, type(f))
print(i, type(i))
print(c, type(c))


# Random Number
    # Impor modul random, dan tampilkan angka acak dari 1 hingga 9 (Karna dihitung dari 0)
import random

print(random.randrange(1, 10)) 