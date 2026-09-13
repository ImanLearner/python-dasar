# ==============================================================================
#      DOKUMENTASI MINI: PYTHON WHILE LOOPS (PERULANGAN BERDASARKAN KONDISI)
# ==============================================================================

# # 1. PENGGUNAAN DASAR: while LOOP DENGAN INCREMENT
# # Artinya: "JALANIN TERUS KODE DI BAWAH SELAMA KONDISINYA MASIH BENAR (TRUE)"
# # Daripada nulis print manual berkali-kali, mending pakai perulangan.
# # Python bakal ngecek kondisinya dulu, kalau true dia jalanin, lalu cek lagi.

i = 1
while i < 6:
    print(i)
    i += 1 # Variabel penambah (increment) biar nilainya naik terus

# # CARA BACA: Selama nilai 'i' kurang dari 6, cetak nilai 'i' lalu tambah 'i' dengan 1.
# # Tes Logika: (i = 1 -> cetak), (i = 2 -> cetak)... pas (i = 6), kondisi (6 < 6) adalah False, loop BERHENTI.
# # Catatan: Ingat untuk naikkan nilai i (increment), kalau tidak komputer lu bakal nge-hang karena Infinite Loop!

print("-" * 30)

# # 2. PENGHENTIAN PAKSA: MENGGUNAKAN PERINTAH break
# # Artinya: "STOP DAN KELUAR DARI LOOP SEKARANG JUGA, WALAUPUN KONDISI UTAMA MASIH TRUE"

i = 1
while i < 6:
    print(i)
    if i == 3:
        break # Loop langsung dihancurkan di sini
    i += 1

# # CARA BACA: Loop berjalan normal dari angka 1. Tapi di setiap putaran, ada satpam 'if i == 3'.
# # Tes Logika: Begitu i bernilai 3, kondisi if terpenuhi, perintah 'break' dieksekusi. Loop bubar total, angka 4 dan 5 gak sempat dicetak.

print("-" * 30)

# # 3. MELEWATI PUTARAN: MENGGUNAKAN PERINTAH continue
# # Artinya: "STOP PUTARAN YANG SEKARANG, JANGAN JALANIN KODE DI BAWAHNYA, LANGSUNG LONCAT KE PUTARAN BERIKUTNYA"

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue # Langsung balik ke atas (while), abaikan perintah print di bawah khusus putaran ini
    print(i)
    
# # CARA BACA: i ditambah 1 dulu di awal putaran. Pas i bernilai 3, perintah 'continue' aktif.
# # Tes Logika: Karena kena 'continue', Python langsung putar balik ke atas buat ngecek angka 4. Perintah print(i) di bawahnya ke-skip, makanya angka 3 GA KECETAK.

print("-" * 30)

# # 4. BLOK AKHIR: MENGGUNAKAN PERINTAH else
# # Artinya: "JALANIN BLOK KODE INI SATU KALI, PAS KONDISI WHILE SUDAH BERUBAH JADI FALSE (SELESAI NORMAL)"

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# # CARA BACA: Setelah looping dari 1 sampai 5 selesai dengan bersih tanpa hambatan, jalankan perintah di dalam else.
# # Catatan Penting: Blok 'else' ini TIDAK AKAN PERNAH JALAN kalau loop di atasnya berhenti karena dipaksa patah oleh perintah 'break'.
