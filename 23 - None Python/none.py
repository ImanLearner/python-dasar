# ==============================================================================
#      DOKUMENTASI PYTHON NONE: MATERI SLOT GAIB / KOTAK KOSONG
# ==============================================================================

# Latar Belakang:
# None itu konstanta spesial di Python yang artinya tidak ada nilainya.
# Tipe datanya disebut NoneType. Cuma dia satu-satunya penghuni tipe data ini.

# ==============================================================================
# 1. CARA DEKLARASI & CEK TIPE DATA NONE
# Taktik: Dipake buat nandain kalau variabel itu belum di-set nilainya.
# ==============================================================================
print("--- TEST 1: CEK SLOT KOSONG ---")
slot_weapon = None

print(slot_weapon)           # Hasil: None
print(type(slot_weapon))     # Hasil: <class 'NoneType'>   

print("-" * 50)

# ==============================================================================
# 2. HUKUM ADAT MEMBANDINGKAN NONE (PAKE 'is' ATAU 'is not')
# Aturan Sakral: Kalau mau ngecek None, jangan pake ==, tapi pake is!
# is      = Apakah beneran kosong?
# is not  = Apakah ada isinya (tidak kosong)?
# ==============================================================================
print("--- TEST 2: SCANNING STATUS INVENTORY ---")
drop_rate_item = None

# Gaya 1: Pake 'is'
if drop_rate_item is None:
    print("STATUS: Bos belum dilawan, item belum drop (Masih None)")
else:
    print("STATUS: Item berhasil didapatkan!")

# Gaya 2: Pake 'is not' (Kebalikan dari di atas)
if drop_rate_item is not None:
    print("STATUS: Mantap, data ready!")
else:
    print("STATUS: Data masih kosong melompong. Man!")  

print("-" * 50)

# ==============================================================================
# 3. BOOSTER LOGIKA (NONE = FALSE)
# Sifat asli: Di dalam hukum logika if, None itu otomatis dianggap FALSE.
# ==============================================================================
print("--- TEST 3: CEK TRUTHINESS ---")
print(f"Apakah None itu True atau False? Jawabannya: {bool(None)}") # Hasil: False

print("-" * 50)

# ==============================================================================
# 4. FUNCTION GAIB YANG LUPA KASIH RETURN
# Sikon Nyata: Kalau lu bikin fungsi/macro tapi lupa ngasih kata kunci return,
#              Python bakal otomatis ngasih hadiah berupa None!
# ==============================================================================
print("--- TEST 4: JURUS TANPA RETURN WKWKWK ---")

def jurus_pukulan_saitama():
    damage = 99999
    # Di sini kita cuma ngitung, lupa ngasih 'return damage' ke luar

hasil_jurus = jurus_pukulan_saitama()
print(f"Hasil output jurusnya: {hasil_jurus}")
# Hasil: None (Karena di dalem fungsi gak ada perintah nge-BALIKIN data!)
