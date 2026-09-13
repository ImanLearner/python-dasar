# ==============================================================================
#                          DOKUMENTASI PYTHON: ELIF 
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. APA ITU ELIF? (ARTINYA: "KALAU PILIHAN DI ATAS SALAH, COBA CEK YANG INI")
# ------------------------------------------------------------------------------
# Kalau "if" cuma punya 1 pilihan dan "else" cuma cadangan, "elif" ini bikin lo 
# punya banyak pilihan (Plan C, Plan D, dst).
# Python bakal ngecek dari atas ke bawah. Begitu ketemu 1 yang bener (True), 
# pilihan di bawahnya langsung dicuekin (di-skip).

# Contoh pilihan karakter di game Naruto:
nomor_pilihan = 2

if nomor_pilihan == 1:
    print("Lo milih Naruto")
elif nomor_pilihan == 2:
    print("Lo milih Sasuke")  # -> Ini yang bener, kode di bawahnya langsung stop dicek
elif nomor_pilihan == 3:
    print("Lo milih Itachi")
else:
    print("Lo gak milih siapa-siapa")



# ------------------------------------------------------------------------------
# 2. KAPAN HARUS PAKE ELIF? (BIAR RAM LAPTOP GAK BOROS)
# ------------------------------------------------------------------------------
# Pake "elif" jauh lebih hemat RAM dibanding lo nulis "if" pisah-pisah banyak banget.
# Kalau pake "elif", begitu dapet yang bener, Python langsung istirahat.

# Contoh status chakra:
chakra = 90

if chakra >= 90:
    print("Jurus Rasen Shuriken")
elif chakra >= 50:
    print("Jurus Rasengan Biasa")  # -> Ketemu yang bener di sini, pengecekan selesai!
elif chakra >= 20:
    print("Jurus Kage Bunshin")


# ------------------------------------------------------------------------------
# 3. CONTOH SIMULASI UTUH: CEK STATUS HARI (PAKE F-STRING)
# ------------------------------------------------------------------------------
# Ingat, tanda {} di bawah ini wajib karena rumus f-string buat manggil variabel.

nomor_hari = 1

if nomor_hari == 1:
    print(f"Hari ke {nomor_hari} adalah Senin")
elif nomor_hari == 2:
    print(f"Hari ke {nomor_hari} adalah Selasa")
elif nomor_hari == 3:
    print(f"Hari ke {nomor_hari} adalah Rabu")
else:
    print("Nomor hari gak terdaftar")


# ------------------------------------------------------------------------------
# 4. ATURAN PENTING: HANYA PILIHAN "TRUE" PERTAMA YANG JALAN!
# ------------------------------------------------------------------------------
# Walaupun ada dua kondisi yang sama-sama bener, Python cuma mau nyari 
# yang paling atas. Sisanya dianggap angin lalu.

# Contoh level bintang buronan di GTA (pake input biar dinamis, gak kiasan):
bintang_gta = int(input("Masukkan angka bintang GTA lo: "))

if bintang_gta >= 1:
    # Kalau lo ketik angka 5, kondisi ini udah bener (True), karena 5 jelas >= 1.
    # Python langsung stop di sini. Pilihan di bawahnya gak bakal dibaca lagi.
    print("Polisi biasa mulai ngejar lo")
elif bintang_gta >= 3:
    print("Helikopter polisi mulai nembak")
elif bintang_gta == 5:
    print("Tentara bawa tank turun ke jalanan")
else:
    # Jaring pengaman buat angka 0 atau angka minus
    print("Aman, bintang lo 0. Nggak ada polisi yang ngejar.")

# TIPS LOGIKA: Makanya kalau bikin perbandingan angka, taruh angka yang 
# paling besar atau paling spesifik di bagian paling atas!
