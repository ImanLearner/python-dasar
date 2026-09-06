# STRING METHODS PILIHAN

# --- [1. CAPITALIZE] ---
# Fungsi: Mengubah HANYA huruf pertama di paling depan jadi kapital.
teks_satu = "cybersec Indonesia"
print(teks_satu.capitalize())
# Output: Hacker indonesia

# --- [2. TITLE] ---
# Fungsi: Mengubah huruf pertama di SETIAP KATA jadi kapital.
teks_dua = "cybersec indonesia"
print(teks_dua.title())
# Output: Hacker Indonesia

# --- [3. SWAPCASE] ---
# Fungsi: Membalikkan keadaan (huruf kecil jadi gede, huruf gede jadi kecil).
teks_tiga = "HaCkeR"
print(teks_tiga.swapcase())
# Output: hAcKEr

# --- [4. COUNT] ---
# Fungsi: Menghitung berapa kali suatu huruf/kata muncul di dalam teks.
teks_empat = "Cybersec indonesia"
print(teks_empat.count("e"))
# Output: 3  (karena huruf 'e' ada tiga biji)

# --- [5. FIND] ---
# Fungsi: Mencari posisi indeks awal dari kata yang kita cari.
teks_lima = "Cybersec indonesia"
print(teks_lima.find("indonesia"))
# Output: 9 (karena kata "indonesia" dimulai dari indeks ke-9)

# --- [6. STARTSWITH] ---
# Fungsi: Nge-cek apakah teks DIAWALI dengan kata tertentu (Hasil: True/False).
# Sering dipake anak cybersec buat filter log atau protokol web.
url = "https://google.com"
print(url.startswith("https"))
# Output: True

# --- [7. ENDSWITH] ---
# Fungsi: Nge-cek apakah teks DIAKHIRI dengan kata tertentu (Hasil: True/False).
# Sering dipake buat nyaring ekstensi file yang bahaya (.exe, .php, dll).
nama_file = "payload.exe"
print(nama_file.endswith(".txt"))
# Output: False

# --- [8. ISDIGIT] ---
# Fungsi: Nge-cek apakah isi teks adalah ANGKA SEMUA (Hasil: True/False).
# Penting buat validasi input biar gak kena injeksi script hacker.
pin = "12345"
print(pin.isdigit())
# Output: True


# --- [9. ISALNUM] ---
# Fungsi: Nge-cek apakah teks isinya campuran HURUF & ANGKA doang (Hasil: True/False).
# Bakal bernilai False kalau hacker masukin simbol aneh kayak (', ", <, >, /).
username = "root123"
print(username.isalnum())
# Output: True

# --- [10. ZFILL] ---
# Fungsi: Menambahkan angka 0 di depan teks sampai panjangnya sesuai target.
# Berguna banget di cybersec buat ngerapihin format biner atau kode Hex.
nomor = "5"
print(nomor.zfill(3))
# Output: 005 (panjang teks dipaksa jadi 3 karakter)

# --- [11. INDEX] ---
# Fungsi: SAMA PERSIS kayak .find(), yaitu nyari posisi indeks awal suatu kata.
# Bedanya: Kalau katanya GAK KETEMU, .index() bakal bikin program ERROR (Crash), 
# sedangkan .find() lebih aman karena cuma ngasih hasil -1.
teks_enam = "Cybersec indonesia"
print(teks_enam.index("indonesia"))
# Output: 9