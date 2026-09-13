# ==============================================================================
#            DOKUMENTASI MINI: SHORTHAND IF (MODE SATU BARIS)
# ==============================================================================

# 1. MODE IF DOANG (Cuma naikin baris bawah ke atas)
a = 5
b = 2

if a > b: print("a lebih besar dari b")
# CARA BACA: Jika a lebih besar dari b, langsung cetak teksnya.


# 2. MODE IF ELSE (Posisinya dibalik kayak bahasa Inggris)
a = 2
b = 330

print("A") if a > b else print("B")
# CARA BACA: Cetak "A" jika a lebih besar dari b, kalau kagak cetak "B".


# 3. MODE ISI VARIABEL (Paling taktis buat ngisi data instan)
x = 15
y = 20

max_value = x if x > y else y
# CARA BACA: Isi 'max_value' dengan x jika x lebih besar dari y, kalau kagak isi dengan y.

print("Nilai maksimum:", max_value)


# 4. MODE TIGA PILIHAN (Diputus-putus bacanya dari kiri)
a = 330
b = 330

print("A") if a > b else print("=") if a == b else print("B")
# CARA BACA: 
# - Cetak "A" jika a lebih besar dari b,
# - Kalau kagak, cetak "=" jika a sama dengan b,
# - Kalau masih kagak juga, baru cetak "B".