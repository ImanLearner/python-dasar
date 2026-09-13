# ==============================================================================
#          DOKUMENTASI MINI: PYTHON SCOPE (WILAYAH KEKUASAAN VARIABEL)
# ==============================================================================

# # Latar Belakang:
# # Scope itu adalah aturan tempat/wilayah di mana sebuah variabel bisa diakses.
# # Gak semua variabel bisa dipanggil di sembarang tempat. Ada kasta dan wilayahnya!

# ==============================================================================
# # 1. LOCAL SCOPE (JAGO KANDANG)
# # Artinya: Variabel yang lu bikin di DALAM sebuah fungsi cuma hidup di dalam fungsi itu.
# # Lu panggil di luar fungsi? Pasti crash/error!
# ==============================================================================
def fungsi_lokal():
    x = 300  # Ini variabel Lokal
    print("Di dalam fungsi:", x) # Aman

fungsi_lokal()
# print(x) # KELUARIN DARI KOMENTAR KALAU MAU LIHAT ERROR: NameError (x gak kenal di luar)

print("-" * 30)

# # Fungsi di Dalam Fungsi (Nested Function)
# # Fungsi yang ada di dalem bisa ngintip/pake variabel milik fungsi luarnya (Enclosing).
def fungsi_luar():
    x = 300
    def fungsi_dalam():
        print("Fungsi dalem ngintip x luar:", x) # Bisa diakses!
    fungsi_dalam()

fungsi_luar()

print("-" * 30)


# ==============================================================================
# # 2. GLOBAL SCOPE (RAJA MAP / BEBAS KELUYURAN)
# # Artinya: Variabel yang dibikin di luar fungsi (di body utama kodingan).
# # Bisa diakses sama siapa aja, mau dari dalam fungsi atau luar fungsi.
# ==============================================================================
y = 500 # Ini variabel Global

def cek_global():
    print("Fungsi ngakses global y:", y) # Bisa banget

cek_global()
print("Luar fungsi ngakses global y:", y)

print("-" * 30)


# ==============================================================================
# # 3. NAMING VARIABLES (NAMA SAMA, BEDA KASTA)
# # Kalau nama variabel di luar (global) dan di dalam (lokal) itu SAMA, 
# # Python bakal menganggap mereka itu DUA VARABEL YANG BERBEDA. Gak saling ganggu!
# ==============================================================================
z = 999 # Global z

def cetak_z():
    z = 111 # Lokal z (Cuma berlaku di dalam kandang ini)
    print("z Lokal:", z) # Hasil: 111

cetak_z()
print("z Global:", z) # Hasil: 999 (Tetep aman gak berubah)

print("-" * 30)


# ==============================================================================
# # 4. KEYWORD 'global' (JEBOL DINDING LOKAL)
# # Dipake kalau lu lagi di DALAM fungsi (lokal), tapi mau:
# # 1. Bikin variabel baru yang sifatnya global, ATAU
# # 2. Mau ngerubah/ngedit isi variabel global yang ada di luar.
# ==============================================================================
# Contoh 1: Bikin variabel global dari dalem fungsi
def buat_global():
    global var_gaib
    var_gaib = 777

buat_global()
print("Manggil var_gaib di luar:", var_gaib) # Hasil: 777 (Gak error lagi!)

# Contoh 2: Ngerubah total isi variabel global dari dalem
gold_tim = 3000

def beli_item():
    global gold_tim
    gold_tim = 1200 # Ngerubah variabel global di atas!

beli_item()
print("Sisa Gold Tim sekarang:", gold_tim) # Hasil: 1200

print("-" * 30)


# ==============================================================================
# # 5. KEYWORD 'nonlocal' (KHUSUS FUNGSI BERSARANG)
# # Dipake di dalam fungsi bertingkat (nested). Biar fungsi yang paling dalem
# # bisa ngerubah isi variabel milik fungsi luarnya (bukan global).
# ==============================================================================
def myfunc1():
    nama = "Jane"
    def myfunc2():
        nonlocal nama # Nunjuk ke 'nama' milik myfunc1
        nama = "hello"
    myfunc2()
    return nama

print("Hasil nonlocal:", myfunc1()) # Hasil: hello

print("-" * 30)


# ==============================================================================
# # 6. HUKUM PENCARIAN PYTHON (LEGB RULE)
# # Pas lu manggil variabel, Python bakal nyari dengan urutan kasta ini:
# # L (Local)    -> Nyari di dalem fungsi dulu. Gak ada? Naik ke...
# # E (Enclosing)-> Nyari di fungsi luarnya (kalau bersarang). Gak ada? Naik ke...
# # G (Global)   -> Nyari di level paling atas kodingan. Gak ada? Pilihan terakhir...
# # B (Built-in) -> Nyari di sistem bawaan Python (kayak fungsi print, len, dll).
# ==============================================================================
kasta = "Ini Global"

def outer():
    kasta = "Ini Enclosing"
    def inner():
        kasta = "Ini Local"
        print("Inner (L):", kasta)
    inner()
    print("Outer (E):", kasta)

outer()
print("Global (G):", kasta)