"""
ATURAN BIKIN NAMA VARIABEL:
1. Harus diawali huruf atau garis bawah / underscore (_)
2. Gak boleh diawali angka!
3. Cuma boleh isi huruf, angka, ama underscore (A-z, 0-9, ama _)
4. Sensitif (case-sensitive). Nama 'Iman', 'iman', ama 'IMAN' itu beda variabel.
="""

# --- Contoh Nama Variabel yang Legal / Boleh Dipake ---
myvar = "Iman"
my_var = "Iman"
_my_var = "Iman"
myVar = "Iman"
MYVAR = "Iman"
myvar2 = "Iman"

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)
print("-" * 30)

# --- Contoh Nama Variabel yang Ilegal / Bakal Error ---
"""
2myvar = "John"   -> Error gara-gara diawali angka
my-var = "John"   -> Error gara-gara pake strip/minus
my var = "John"   -> Error gara-gara pake spasi
"""

# Inget bro, nama variabel itu sensitif sama huruf gede kecil!

# --- Gaya Penulisan Variabel Banyak Kata ---

# 1. Camel Case (Huruf pertama kecil, kata selanjutnya gede)
print("--- Camel Case ---")
myVariableName = "Muhammad"
print(myVariableName)
print("-" * 30)

# 2. Pascal Case (Semua awal kata pake huruf gede)
print("--- Pascal Case ---")
MyVariableName = "Iman"
print(MyVariableName)
print("-" * 30)

# 3. Snake Case (Pake underscore buat misahin kata - Gaya anak Python banget)
print("--- Snake Case ---")
my_variable_name = "Syahputra"
print(my_variable_name)