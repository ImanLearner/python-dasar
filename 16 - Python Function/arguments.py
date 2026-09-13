# ==============================================================================
# LATIHAN: PYTHON FUNCTION ARGUMENTS & PARAMETERS
# ==============================================================================

# # 1. DASAR FUNCTION (PARAMETER VS ARGUMENT)
# # Artinya: Mengirim data mentah dari luar untuk dipakai di dalam mesin fungsi.
# # Gunanya: Biar fungsi bisa menghasilkan output yang dinamis tergantung data input.

print("=== 1. DASAR FUNCTION (PARAMETER VS ARGUMENT) ===")

# Cara bikin: Tulis nama variabel/slot kosong di dalam kurung def
def sapa_user(name):
    # Parameter 'name' dipakai di dalam fungsi
    print("Hello", name)

# Cara manggil: Masukkan nilai asli (Argument) ke dalam kurung
sapa_user("Iman")

# # CARA BACA: Saat sapa_user("Iman") dipanggil, string "Iman" akan mengisi slot 'name' lalu dicetak.
print("-" * 30)

# # 2. DEFAULT PARAMETER (DATA CADANGAN)
# # Artinya: Memasang nilai bawaan pada parameter menggunakan tanda sama dengan (=).
# # Gunanya: Menghindari error jika user lupa atau sengaja tidak mengirimkan data.

print("=== 2. DEFAULT PARAMETER (DATA CADANGAN) ===")

# Cara bikin: Kasih nilai langsung di parameter contoh (name = "friend")

def sapa_default(name = "friend"):
    print("Hello", name)

# Cara manggil: bisa di kasih data,bisa juga dikosongkan
sapa_default("Iman")    # Pakai data yang dikirim
sapa_default()          # Kosong, otomatis pakai data cadangan"friend"

# # CARA BACA: Jika kurung kosong, Python otomatis mengambil data cadangan yang sudah disiapkan.
print("-" * 30)

# # 3. GAYA PANGGILAN (POSITIONAL VS KEYWORD)
# # Artinya: Dua metode berbeda untuk memasukkan data ke dalam banyak parameter.
# # Gunanya: Memberikan fleksibilitas, mau urutan ketat atau sebut nama slot bebas.

print("=== 3. GAYA PANGGILAN (POSITIONAL VS KEYWORD) ===")

def data_hewan(animal, name):
    print(f"Jenis Hewan, {animal} | Nama Hewan : {name}")

# Gaya Positional: Dimasukin langsung, wajib berurutan sesuai slotnya
data_hewan("Cat", "Boogy")

# Gaya Keyword: Menyebutkan nama slotnya (key = value), urutan bebas dibolak-balik
data_hewan(name = "Boogy", animal = "Cat")

# # CARA BACA: Positional harus urut agar tidak tertukar, sedangkan Keyword bebas karena tujuannya jelas.
print("-" * 30)

# # 4. ATURAN KETAT: POSITION-ONLY (Pake tanda /)
# # Artinya: Membatasi parameter agar HANYA BISA menerima gaya urutan langsung.
# # Gunanya: Memaksa kode ditulis ringkas dan mencegah penggunaan gaya keyword.

print("=== 4. ATURAN KETAT: POSITION-ONLY (Pake tanda /) ===")

# Cara bikin: Tambahkan tanda ', /' setelah nama parameter
def hanya_posisi(nama, /):
    print("Hallo", nama)

# Cara manggil: Wajib langsung nilainya, tidak boleh nulis (nama = "Linus")
hanya_posisi("Linus")

# # CARA BACA: Semua parameter di sebelah kiri tanda '/' dipaksa mati-matian jadi positional-only.
print("-" * 30)

# # 5. ATURAN KETAT: KEYWORD-ONLY (Pake tanda *)
# # Artinya: Membatasi parameter agar HANYA BISA menerima gaya sebut nama slot.
# # Gunanya: Menjaga kejelasan data yang dikirim agar tidak tertukar di fungsi yang kompleks.

print("=== 5. ATURAN KETAT: KEYWORD-ONLY (Pake tanda *) ===")

# Cara bikin: Tambahkan tanda '*, ' di awal sebelum nama parameter
def hanya_keyword(*, nama):
    print("Hallo", nama)

# Cara manggil: Wajib sebut nama slotnya, jika langsung nilainya akan ERROR
hanya_keyword(nama = "Muhammad Iman")

# # CARA BACA: Semua parameter di sebelah kanan tanda '*' dipaksa wajib disebut nama slotnya.
print("-" * 30)

# # 6. GABUNGAN ATURAN KETAT ( / dan * )
# # Artinya: Menggabungkan pembatas positional-only dan keyword-only dalam satu fungsi.
# # Gunanya: Kontrol penuh tingkat tinggi terhadap cara penulisan argumen di industri besar.

print("=== 6. GABUNGAN ATURAN KETAT ( / dan * ) ===")

# Parameter sebelum / adalah positional, parameter setelah * adalah keyword
def hitung_total(a, b, /, *, c, d):
    return a + b + c + d

# Cara manggil: Ikuti aturan pembatas masing-masing slot
hasil = hitung_total(5, 10, c = 15, d = 20)
print("Hasil Total Hitungan:", hasil)

# # CARA BACA: Angka 5 dan 10 masuk ke a dan b secara urut, sedangkan c dan d wajib ditulis kuncinya.
print("-" * 30)