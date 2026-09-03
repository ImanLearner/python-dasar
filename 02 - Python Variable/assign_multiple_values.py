# --- 1. Banyak Variabel, Banyak Isi (Satu Baris Langsung Beres) ---
# Konsepnya: Kotak di kiri urutannya harus sama ama isinya yang di kanan.
a, b, c = "Durian", "Mangga", "Anggur"

print(a)
print(b)
print(c)
print("-" * 30)
# Inget bro: Jumlah kotak (kiri) ama jumlah isi (kanan) musti sama, biar gak error!


# --- 2. Satu Isi Buat Banyak Variabel (Satu untuk Semua) ---
# Konsepnya: Banyak kotak, tapi isinya sama semua/berbagi isi pake tanda (=).
x = y = z = "Orange"

print(x)
print(y)
print(z)
print("-" * 30)


# --- 3. Bongkar Paket / Bongkar List (Unpack a Collection) ---
# Konsepnya: Isinya dibungkus dulu dalem satu paket (List), trus dibongkar ke masing-masing kotak.
fruits = ["apple", "banana", "cherry"]  # Ini paketnya
x, y, z = fruits                        # Dibongkar urut dari depan

print(x)
print(y)
print(z)