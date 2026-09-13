# ==============================================================================
# #               DOKUMENTASI MINI: DASAR PYTHON FUNCTIONS
# ==============================================================================

# # 1. CARA BIKIN & MANGGIL FUNCTION (CREATING & CALLING)
# # Artinya: Function itu blok kode yang baru akan jalan kalau dipanggil namanya.
# # Gunanya jelas: Buat menghindari nulis kode yang sama berulang-ulang.

print("=== 1. CARA BIKIN & MANGGIL FUNCTION ===")

# Cara bikin: Pake keyword 'def', nama fungsi, kurung (), dan tanda titik dua
def my_function():
    # Kode di dalam sini WAJIB masuk spasi (indentasi)
    print("Hello from a function")

# Cara manggil: Tulis namanya diikuti kurung ()
my_function()

# Kelebihan: Bisa dipanggil berkali-kali sesuka hati
my_function()
my_function()

# # CARA BACA: Saat 'my_function()' dipanggil, Python akan mengeksekusi kode print di dalamnya.
print("-" * 30)


# # 2. ATURAN PENAMAAN FUNGSI (FUNCTION NAMES)
# # Aturannya persis sama kayak bikin variabel:
# # - Wajib diawali huruf atau garis bawah (_)
# # - Hanya boleh berisi huruf, angka, dan underscore
# # - Sensitif huruf (myFunction dan myfunction dianggap dua hal berbeda)

print("=== 2. ATURAN NAMA FUNGSI (VALID) ===")

def calculate_sum():
    pass

def _private_function():
    pass

def myFunction2():
    pass

print("Semua contoh nama fungsi di atas lolos validasi aturan Python.")
print("-" * 30)


# # 3. MENGATASI REPETISI KODE (WHY USE FUNCTIONS?)
# # Contoh Kasus: Konversi suhu Fahrenheit ke Celsius. 
# # Daripada nulis rumus yang sama berkali-kali untuk tiap variabel suhu, mending bungkus jadi satu fungsi.

print("=== 3. MENGATASI KODE YANG BERULANG ===")

# Cukup tulis rumusnya sekali di dalam fungsi
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# Tinggal panggil berkali-kali pake data yang beda
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

# # CARA BACA: Kode jadi jauh lebih bersih dan ringkas dibanding harus nulis rumus manual di setiap variabel.
print("-" * 30)


# # 4. KATA KUNCI return (RETURN VALUES)
# # Artinya: Mengirimkan data hasil proses di dalam fungsi keluar ke si pemanggil.
# # Efek penting: Begitu menyentuh 'return', fungsi akan langsung BERHENTI beroperasi saat itu juga.

print("=== 4. CARA KERJA RETURN VALUE ===")

def get_greeting():
    return "Hello from a function"

# Cara A: Hasil return ditampung dulu ke variabel, baru di-print
message = get_greeting()
print(message)

# Cara B: Hasil return langsung ditembak ke dalam print
print(get_greeting())

# # CATATAN: Jika sebuah fungsi tidak memakai kata kunci 'return', maka secara default dia akan mengembalikan nilai 'None'.
print("-" * 30)


# # 5. KEYWORD pass SEBAGAI PLACEHOLDER
# # Artinya: Python melarang keras ada fungsi yang kosong tanpa kode di dalamnya.
# # Solusi: Pake kata 'pass' agar struktur fungsi aman dan tidak bikin program eror/crash saat dikembangkan.

print("=== 5. FUNGSI KOSONG DENGAN STATEMENT pass ===")

def fungsi_kosong_buat_nanti():
    pass

print("Fungsi kosong berhasil dilewati dengan aman tanpa memicu eror merah.")
print("-" * 30)