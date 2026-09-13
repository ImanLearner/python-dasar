# ==============================================================================
#         DOKUMENTASI MINI: PYTHON continue STATEMENT (LEWATI PUTARAN)
# ==============================================================================

# # 1. continue PADA for LOOP
# # Artinya: "Pas ketemu target, lewati sisa perintah di bawahnya, langsung ambil item berikutnya!"
# # Analogi: Lu lagi absen daftar siswa, pas nama siswa yang izin sakit disebut, lu skip dan langsung panggil nama berikutnya.

print("=== 1. CONTINUE PADA FOR LOOP ===")
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    if x == "banana":
        print("Alert: Pisang dideteksi! Skip buah ini,jangan dicetak!")
        continue  # Python langsung putar balik ke atas loop ambil 'cherry'

    print(f"Buah yang sukses lolos: {x}")

# # CARA BACA: Pas x bernilai "banana", perintah 'continue' aktif. 
# # Baris print(f"Buah yang sukses...") di bawahnya GAK AKAN DIJALANKAN khusus buat banana.
# # Hasil Akhir: "apple" dan "cherry" sukses dicetak, "banana" ilang dari peredaran!
print("-" * 30)


print("=== 2. CONTINUE PADA WHILE LOOP ===")
angka = 0 
while angka < 5:
    angka += 1 # <--- WAJIB DI ATAS! Biar angkanya tetep nambah pas di-skip

    if angka == 3:
        print("Alert: Angka 3 dilewati")
        continue # Langsung melesat naik lagi ke baris 'while angka < 5

    print(f"Angka sekarang: {angka}")

# # Hasil Akhir di Terminal: Angka 1, 2, 4, 5 bakal tercetak. Angka 3 GAK ADA karena di-skip!
print("-" * 30)

# # 3. EFEK continue TERHADAP else
# # Catatan Penting: Berbeda dengan 'break', perintah 'continue' TIDAK MENGGAGALKAN blok 'else'!
# # Kenapa? Karena loop-nya tetep selesai sampai akhir secara alami, cuma ada yang di-skip doang di tengah jalan.

print("=== 3. EFEK CONTINUE TERHADAP ELSE ===")
for x in range(4):
    if x == 2:
        continue # Cuma skip angka 2
    print(x)
else:
    # Blok ini TETEP JALAN dengan gembira karena loop tidak mati paksa!
    print("Misi selesai! Blok else tetap dieksekusi.")