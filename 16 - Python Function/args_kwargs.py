# ==============================================================================
#    DOKUMENTASI MINI: PYTHON *args DAN **kwargs (FUNGSI DINAMIS & FLEKSIBEL)
# ==============================================================================

# # Latar Belakang:
# # Biasanya kalau bikin fungsi, jumlah argumennya harus pas. Kalau kurang/lebih pasti error.
# # Nah, *args dan **kwargs ini solusinya biar fungsi lu bisa nerima argumen sebanyak apa pun
# # tanpa lu tahu jumlah pastinya dari awal (bebas input sebanyak-banyaknya!).

# ==============================================================================
# # 1. *args (ARBITRARY ARGUMENTS) -> DIUBAH JADI TUPLE
# # Aturannya: Pake tanda bintang SATU (*) sebelum nama parameter.
# # Fungsinya: Nampung semua argumen biasa (posisi) yang lu masukin, terus dibungkus jadi TUPLE.
# # Analogi Dota: Kayak lu beli item yang bisa numpuk (stack), bebas mau beli berapa biji.
# ==============================================================================

# Contoh Dasar: Mengakses individual argument lewat indeks
def cetak_anak(*kids):
    # Karena berbentuk tuple, kita bisa akses pake indeks [indeks]
    print("Anak paling bungsu adalah " + kids[2])

cetak_anak("Iman", "Pudol", "Linus")

print("-" * 30)

# Contoh Kombinasi: Parameter Biasa + *args
# Catatan: Parameter biasa WAJIB ditaruh di depan sebelum *args!
def cari_max(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers [0]
    for num in numbers:
        if num > max_num:
           max_rum = num
    return max_rum

print("Net Worth Tertinggi :", cari_max(3, 7, 2, 9, 1))


# ==============================================================================
# # 2. **kwargs (ARBITRARY KEYWORD ARGUMENTS) -> DIUBAH JADI DICTIONARY
# # Aturannya: Pake tanda bintang DUA (**) sebelum nama parameter.
# # Fungsinya: Nampung argumen yang ada KEYWORD-nya (ada nama = nilai), dibungkus jadi DICTIONARY.
# # Analogi Dota: Kayak status hero lu (Strengh = 25, Agility = 30, Intelligence = 15).
# ==============================================================================

# Contoh Dasar: Mengakses value pake Key Dictionary
def cetak_biodata(**kid):
    print("Nama belakangnya adalah " + kid["lname"])

cetak_biodata(fname = "Iman", lname = "Syahputra")

print("-" * 30)

# Contoh Kombinasi: Parameter Biasa + **kwargs
def detail_user(username, **details):
    print("Username", username)
    print("Detail Tambahan :")
    for key, value in details.items():
        print(f" {key}: {value}")

detail_user("Hengker", umur=25, kota="DepoK", hobi="Coding")

print("-" * 30)


# ==============================================================================
# # 3. MELEBUR SEMUANYA (Kombinasi Total)
# # Kalau lu mau pake Parameter Biasa, *args, dan **kwargs SEKALIGUS, urutannya WAJIB:
# # 1. Parameter Biasa -> 2. *args -> 3. **kwargs
# ==============================================================================
def fungsi_dewa(title, *args, **kwargs):
    print("Tittle :", title)
    print("Isi *args (Tuple) :", args)
    print("Isi **kwargs (Dict) :", kwargs)

fungsi_dewa("Data Server", "Korban1", "Korban2", port=90, status="Open")

print("-" * 30)


# ==============================================================================
# # 4. UNPACKING ARGUMENTS (Membongkar List / Dictionary)
# # Selain buat nerima data, tanda * dan ** bisa dipake pas MANGGIL fungsi buat bongkar isi data.
# ==============================================================================

# Unpacking List pake *
def tambah_tiga_angka(a, b, c):
    return a + b + c

angka_list = [1, 2, 3]
# Tanda * bakal ngebongkar list [1,2,3] jadi 1, 2, 3 terpisah
hasil_list = tambah_tiga_angka(*angka_list) 
print("Hasil Unpack List:", hasil_list) 
# Unpacking Dictionary pake **
def sapa_orang(fname, lname):
    print("Halo", fname, lname)

data_orang = {"fname": "Emil", "lname": "Refsnes"}
# Tanda ** bakal ngebongkar dict jadi fname="Emil", lname="Refsnes"
sapa_orang(**data_orang)