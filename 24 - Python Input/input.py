# ==============================================================================
#      DOKUMENTASI PYTHON USER INPUT: MATERI GERBANG INTERAKSI USER
# ==============================================================================

# Latar Belakang:
# input() adalah fungsi bawaan Python buat minta data langsung dari ketikan user.
# Aturan Sakral: Semua data yang masuk lewat input() OTOMATIS dianggap STRING (teks),
# meskipun user mengetik angka 10 atau 100.

# ==============================================================================
# 1. DASAR USER INPUT
# Taktik: Naruh teks petunjuk langsung di dalam kurung input() biar rapi satu baris.
# ==============================================================================
print("--- TEST 1: INPUT TEKS BIASA ---")
nama_agent = input("Masukkan nama code/alias lu: ")
print(f"Selamat datang di server, Ageng {nama_agent}!")

print("-" * 50)

# ==============================================================================
# 2. MASALAH ANGKA PADA INPUT (WAJIB CASTING/CONVERT)
# Sikon: Karena input() menghasilkan string, kita gak bisa langsung pakai matematika.
# Kita harus bungkus pake float() atau int() dulu biar berubah jadi angka asli.
# ==============================================================================
print("--- TEST 2: INPUT ANGKA DENGAN CONVERT ---")
target_port_str = input("Masukkan port target untuk di-scan: ")

# Mengubah dari string ke integer (angka bulat)
port_target = int(target_port_str)

print(f"Mulai scanning pada port: {port_target}")
# Sekarang variabel port_target sudah aman dipakai buat hitung-hitungan logika

print("-" * 50)

# ==============================================================================
# 3. VALIDASI INPUT PAKE TIM MEDIS (TRY-EXCEPT + WHILE LOOP)
# Penting: User itu sering ngaco. Diminta masukin angka malah masukin huruf.
# Biar program kita gak crash eror merah, kita kunci pake looping dan try-except!
# ==============================================================================
print("--- TEST 3: VALIDASI ANTI-CRASH ---")

status_grinding = True

while status_grinding == True:
    input_user = input("Masukkan target IP dengan angka (contoh: 192): ")

    try:
        # Coba ubah ketikan user menjadi angka desimal/float
        angka_valid = float(input_user)

        # Kalau berhasil dan gak eror, kita matikan looping-nya
        status_grinding = False
        print(f"Sukses! Data IP {angka_valid} diterima oleh sistem")
    
    except:
        # Kalau user ngaco (misal ngetik 'admin'), baris float() di atas pasti eror.
        # Daripada program crash, tim medis except langsung mengambil alih:
        print("Eror! Input lu bukan angka. Tolong ulangi lagi, Man.")

print("Proses validasi selesai. Server aman!")