# ==============================================================================
#      DOKUMENTASI F-STRING PART 1: AUTO-PRESET CHAT & MODIFIER COMMAND
# ==============================================================================

# # Latar Belakang:
# # Dulu sebelum Python 3.6, kalau mau gabungin teks sama variabel itu ribet kudu 
# # pake fungsi .format() atau tanda tambah (+). Sekarang udah ada F-String, 
# # ibarat fitur "Quick Chat Preset" di game, tinggal pencet langsung rapi!

# ==============================================================================
# # 1. CARA PAKAI DASAR (PLACEHOLDER `{ }`)
# # 🔹 Aturan Sakral: Wajib taruh huruf 'f' (kecil atau gede) di depan tanda kutip!
# # 🔹 Tanda `{ }` itu namanya Placeholder, fungsinya buat manggil item/variabel.
# ==============================================================================
print("--- TEST 1: PRESET CHAT DASAR ---")
harga_skin = 59
# Tinggal mas"ukin variabelnya ke dalam kurung kurawal
info_item = f"Harga skin ini adalah {harga_skin} Diamond"
print(info_item)

print("-" * 50)

# ==============================================================================
# # 2. PEMAKAIAN MODIFIER TIPE FORMAT (`:`)
# # Taktik: Di dalam `{ }`, lu bisa nambahin tanda titik dua `:` diikuti kode format
# # 🔹 `:.2f` = Paksa angka desimal cuma tampil 2 angka di belakang koma (Fixed Point).
# # 🔹 `:,`   = Otomatis ngasih tanda koma sebagai pemisah ribuan biar gak pusing bacanya.
# ==============================================================================
print("--- TEST 2: CUSTOM SKIN ANGKA (MODIFIER) ---")
# Contoh 2 angka desimal pake variabel
harga_dolar = 59
print(f"Harga game: {harga_dolar:.2f} USD")

# Lu juga bisa langsung format angkanya secara instan TANPA BIKIN VARIABEL dulu:
print(f"Harga bundle: {95:.2f} USD") # Hasil: 95.00

# Contoh pemisah ribuan (Thousand Separator) biar kayak duit ATM/Bank
gold_jarahan = 59000
print(f"Total gold di tas lu: {gold_jarahan:,} Gold")

print("-" * 50)

# ==============================================================================
# # 3. EKSEKUSI MATEMATIKA & LOGIKA IF-ELSE LANGSUNG DI TEMPAT
# # Taktik: Lu gak perlu bikin variabel baru buat ngitung matematika atau cek rumus.
# #         Langsung hantam di dalam `{ }` aja, Man!
# ==============================================================================
print("--- TEST 3: HITUNG RUMUS & LOGIKA DI DALAM CHAT ---")
# A. Math Operations langsung pake angka
print(f"Total Damage Combo (20 * 59): {20 * 59}")

# B. Math Operations gabungan sama variabel (Hitung Pajak/Diskon)
harga_asli = 59
pajak = 0.25 
print(f"Harga setelah kena pajak server: {harga_asli + (harga_asli * pajak)}")

# C. If...Else Statement langsung di dalam string (Ternary Operator)
harga_item_shop = 49
# Nyari status: Kalau di atas 50 Mahal, kalau di bawah 50 Murah
status_item = f"Skin ini termasuk item yang: {'Mahal' if harga_item_shop > 50 else 'murah'}"
print(status_item) 

print("-" * 50)

# ==============================================================================
# # 4. RUNNING FUNGSI (METHOD/FUNCTION BENTUKAN SENDIRI)
# # Taktik: Lu bisa manggil fungsi bawaan Python (kayak `.upper()` buat kapitalin huruf)
# #         atau panggil fungsi *macro* buatan lu sendiri di dalam `{ }`.
# ==============================================================================
print("--- TEST 4: PANGGIL FUNGSI MACRO ---")
# A. Pake fungsi bawaan Python (Bikin huruf jadi GEDE SEMUA)
nama_fruit = "apples"
print(f"i love {nama_fruit.upper()}")

# B. Pake fungsi buatan sendiri (Contoh: Konversi Jarak Ketinggian Pesawat)
def konversi_kaki_ke_meter(kaki):
    return kaki * 0.3048

jarak_kaki = 30000
# Fungsi langsung dipanggil dan dihitung otomatis di dalam chat
print(f"Pesawat tempur musuh terbang di ketinggian: {konversi_kaki_ke_meter(jarak_kaki)} meter.")