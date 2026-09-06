# GABUNGIN TEKS (STRING CONCATENATION)
# Gunakan operator (+) buat nempelin string satu dengan string lainnya.
a = "Hello"
b = "World"

# --- 1. Gabungin Langsung Tanpa Spasi ---
# Kalau langsung digabung, teksnya bakal nempel dempet.
c = a + b
print(c)  # Output: HelloWorld


# --- 2. Gabungin Pake Spasi Manual ---
# Biar rapi ada jaraknya, kita selipin string kosong yang isinya spasi (" ") di tengahnya.
d = a + " " + b
print(d)  # Output: Hello World


# =========================================================
# KASUS DUNIA CYBERSECURITY (BONUS BUAT LU!)
# =========================================================
# Contoh penerapan gabungin string pas lu bikin script automasi log/IP.

ip_depan = "192.168"
ip_belakang = "1.50"

# Gabungin blok IP pake titik (".") manual
ip_address = ip_depan + "." + ip_belakang
print("Target IP ditemukan: " + ip_address)
# Output: Target IP ditemukan: 192.168.1.50