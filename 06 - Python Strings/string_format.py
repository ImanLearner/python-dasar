# CARA MODERN GABUNGIN TEKS & ANGKA (F-STRINGS)

# Aturan main: Kasih huruf 'f' di depan kutip, 
# terus pake kurung kurawal {} buat nampung variabel/angka.

umur = 20

# --- 1. Cara Jadul (Bikin Error) ---
# teks_error = "Umur gue " + umur  # <-- Ini bakal error total!

# --- 2. Solusi Pake F-String (Simpel & Aman) ---
teks_aman = f"Umur gue {umur} tahun"
print(teks_aman)  # Output: Umur gue 20 tahun


# =========================================================
# MODIFIER (PENGATUR FORMAT) & OPERASI MATEMATIKA
# =========================================================

# --- 3. Mengatur Desimal (:.2f) ---
# Kunci cybersec/finance: Biar angka desimal rapi di belakang koma (titik).
# Titik dua (:) artinya perintah format, (.2f) artinya mau 2 angka di belakang desimal.
harga = 59
print(f"Harganya adalah {harga:.2f} dollar")
# Output: Harganya adalah 59.00 dollar


# --- 4. Langsung Ngitung Matematika di Dalem {} ---
# Lu bisa langsung naruh rumus matematika di dalem kurung kurawal.
print(f"Total belanjaan: {20 * 5} ribu")
# Output: Total belanjaan: 100 ribu


# =========================================================
# KASUS DUNIA CYBERSECURITY (BONUS LAGI JIR!)
# =========================================================
# F-string sering banget dipake buat nge-print status serangan/scanning.

ip = "10.0.0.1"
port = 80
status = "OPEN"

print(f"[+] Hasil Scan: IP {ip} pada Port {port} statusnya adalah {status}!")
# Output: [+] Hasil Scan: IP 10.0.0.1 pada Port 80 statusnya adalah OPEN!