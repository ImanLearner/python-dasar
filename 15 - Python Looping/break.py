# ==============================================================================
#          DOKUMENTASI MINI: PYTHON break STATEMENT (PENGHENTIAN PAKSA)
# ==============================================================================

# # 1. break PADA while LOOP
# # Artinya: "PAKSA KELUAR DAN BUBARKAN LOOP SEKARANG, WALAUPUN KONDISI UTAMA MASIH TRUE"
# # Analogi: Serangan otomatis nyari password. Pas password bener ketemu, langsung stop biar hemat energi.

print("=== 1. BREAK PADA WHILE LOOP ===")
id_target = 1

while id_target < 9:
    print("Memeriksa ID target nomor: {id_target}")

    if id_target == 3:
        print("ALERT: Target utama ditemukan! Hentikan semua proses secara paksa.")
        break   #Loop langsung di hacnurkan total di sini!
    id_target += 1

# # CARA BACA: Loop harusnya jalan sampai ID 5. Tapi di putaran ke-3, satpam 'if' mendeteksi id_target == 3.
# # Tes Logika: Perintah 'break' dieksekusi. Loop bubar total, angka 4 dan 5 gak sempat diproses.
print("-" * 30)


# # 2. break PADA for LOOP
# # Artinya: "POTONG JALUR PERULANGAN DI TENGAH JALAN SEBELUM SEMUA ITEM DI DALAM LIST HABIS"
# # Analogi: Lu lagi nge-scan daftar nama di database, pas ketemu nama buronan, langsung stop penyisiran.

print("=== 2. BREAK PADA FOR LOOP ===")
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(f"Memeriksa buah: {x}")

    if x == "banana":
        print("Alert: Pisang ditemukan! Stop penyisiran List.")
        break   # Loop langsung bubar, gak bakal lanjut ke buah berikutnya

# # CARA BACA: Untuk setiap buah 'x' di dalam list 'fruits', cek satu-satu.
# # Tes Logika: Putaran 1 'apple' (aman). Putaran 2 'banana', kondisi if terpenuhi, perintah 'break' aktif.
# # Hasil Akhir: Loop berhenti di 'banana'. Buah 'cherry' diabaikan dan gak sempet diperiksa sama sekali!
print("-" * 30)


# # 3. HUKUM PAJAK break TERHADAP else
# # Catatan Sakral: Blok 'else' KAGAK BAKAL JALAN kalau loop dihentikan oleh perintah 'break'!

print("=== 3. EFEK BREAK TERHADAP ELSE ===")
for x in range (5):
    if x == 3:
        print(f"Loop dipotong paksa di angka {x}")
        break 
    print(x)
else:
    # Blok else ini DI ABAIKAN total oleh Python karena di atas ada "break"
    print("Misi Selesai dengan sempurna!")