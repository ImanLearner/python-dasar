# ==============================================================================
#                 DOKUMENTASI PYTHON: ELSE (GERBANG TERAKHIR / MUTLAK)
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. APA ITU ELSE? (ARTINYA: "NANGKEP APA PUN YANG GAGAL DI ATAS")
# ------------------------------------------------------------------------------
# `else` itu tugasnya jadi jaring pengaman paling bawah. Dia baru jalan kalau
# kondisi `if` (dan semua `elif`) hasilnya SALAH (False).
# Hukum Sakral: `else` GAK BOLEH dikasih syarat matematika lagi. Langsung titik dua!

# Contoh perbandingan angka
a = 500
b = 200

if a > b:
    print("a lebih besar dari b")
elif a == b:
    print("a dan b nilainya sama")
else:
    # Karena dua kondisi di atas False (200 gak < 33, dan gak sama), langsung jatuh ke sini!
    print("b lebih besar dari a")


# ------------------------------------------------------------------------------
# 2. BISA JALAN TANPA ELIF (CUMA 2 PILIHAN NASIB)
# ------------------------------------------------------------------------------
# Lo gak wajib pasang `elif` terus-terusan, bro. Kalau pilihannya cuma hidup atau mati,
# menang atau kalah, lo cukup pake kombinasi `if` dan `else` doang.

# Contoh ngetes angka Ganjil atau Genap:
angka = 9

if angka % 2 == 0:
    print("Angka ini adalah Genap")
else:
    # Kalau gak genap, ya PASTI ganjil. Gak ada pilihan ketiga wkwk.
    print("Angka ini adalah Ganjil")

# ------------------------------------------------------------------------------
# 3. STRUKTUR LENGKAP: IF - ELIF - ELSE (RANTAI KEPUTUSAN KOMPLIT)
# ------------------------------------------------------------------------------
# Ini versi industri paling estetik yang lo suka. Rapi, aman dari layar kosong, 
# dan super hemat RAM komputer lo.

# Contoh klasifikasi suhu cuaca:
suhu = 25

if suhu > 30:
    print("Di luar panas banget,bro!")
elif suhu > 20:
    print("Di luar anget kuku,santai")   # -> Angka 22 lolos di sini. Selesai!
elif suhu > 10 :
    print("Di luar agak adaem/dingin")
else:
    print("Di luar beku parah, pake jaket!")


# ------------------------------------------------------------------------------
# 4. ELSE SEBAGAI TAMENG AMAN (ERROR HANDLING & VALIDASI INPUT)
# ------------------------------------------------------------------------------
# Ini fungsi vital di dunia hacker/cybersec yang lo omongin tadi. 
# Buat nahan biar sistem gak eror atau kosong melompong pas user typo.

# Contoh validasi nama pas login (pake f-string {}):
nama_user = "Iman"

if len(nama_user) > 0:
    # Kalau user beneran ngetik nama (panjang huruf lebih dari 0)
    print(f"Selamat datang kembali, {nama_user}")
else:
    # JALUR TAMENG: Kalau user gak ngetik apa-apa langsung enter (kosong)
    print("Eror: Nama gak boleh kosong melompong, bro!")