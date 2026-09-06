# KONVERSI TIPE DATA (TYPE CASTING)
    # Proses maksa suatu nilai biar berubah ke tipe data yang kita mau.

# Kita pakai fungsi bawaan Python: int(), float(), dan str().

# --- 1. Fungsi int() ---
# Tugas: Mengubah data jadi Bilangan Bulat.
# - Kalau dari float: Buntut desimalnya bakal langsung dipangkas (dibuang).
# - Kalau dari string: Isinya HARUS berupa angka bulat (gak boleh ada huruf/titik).
x = int(1)      # Tetep 1
y = int(2.8)    # Jadi 2 (desimalnya dibuang)
z = int("3")    # Jadi 3 (string berubah jadi angka)

print(x, y, z)


# --- 2. Fungsi float() ---
# Tugas: Mengubah data jadi Bilangan Desimal.
# - Kalau dari int: Bakal ditumpukin buntut `.0` di belakangnya.
# - Kalau dari string: Isinya harus berupa angka (bisa bulat atau desimal).
a = float(1)      # Jadi 1.0
b = float(2.8)    # Tetep 2.8
c = float("3")    # Jadi 3.0
d = float("4.2")  # Jadi 4.2

print(a, b, c, d)


# --- 3. Fungsi str() ---
# Tugas: Mengubah data jenis apapun jadi Teks (String).
# - Semua data (int, float, dll) bisa diubah jadi string tanpa error.
p = str("s1")   # Tetep "s1"
q = str(2)      # Jadi "2" (angka 2 yang dianggap sebagai teks)
r = str(3.0)    # Jadi "3.0" (angka desimal yang dianggap sebagai teks)

print(p, q, r)