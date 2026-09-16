# ==============================================================================
#      DOKUMENTASI F-STRING PART 3: THE CYBERSEC & GENERAL CHEAT SHEET
# ==============================================================================

# Note: List modifier penting yang sering kepake di lapangan, sisanya abaikan aja!

# 1. MODIFIER PERSEN [ :% ] -> Otomatis kali 100 dan kasih tanda %
win_rate = 0.756
print(f"Statistik Akun: {win_rate:.1%}") 
# Hasil: 75.6% (Rapih langsung dibuletin 1 angka belakang koma)

print("-" * 50)

# 2. MODIFIER BINER [ :b ] -> Mengubah angka jadi bahasa komputer (0 dan 1)
# Sikon Cybersec: Sering dipake pas belajar enkripsi data / bitwise operation.
angka_rahasia = 10
print(f"Angka 10 kalau diubah ke Biner: {angka_rahasia:b}") 
# Hasil: 1010

print("-" * 50)

# 3. MODIFIER HEXADECIMAL [ :x atau :X ] -> Mengubah angka ke Hex (Basis 16)
# Sikon Cybersec: Pake ini buat ngebaca alokasi memori atau kode hash malware.
kode_sistem = 255
print(f"Kode Hex (Kecil): {kode_sistem:x}") # Hasil: ff
print(f"Kode Hex (Gede) : {kode_sistem:X}") # Hasil: FF

print("-" * 50)

# 4. MODIFIER RATA TENGAH [ :^ ] -> Biar teks presisi di tengah space kosong
# Taktik: {teks:^jumlah_karakter}
nama_menu = "LOBBY UTAMA"
print(f"==={nama_menu:^20}===")
# Hasil: ===    LOBBY UTAMA     === (Otomatis seimbang kiri-kanan!)