# ==============================================================================
#      DOKUMENTASI F-STRING PART 2: METODE FORMAT() (SKIN JADUL / LEGACY ITEM)
# ==============================================================================

# # Latar Belakang:
# # Sebelum ada F-String, Python pake fungsi `.format()` di akhir string.
# # Bedanya: Di depan tanda kutip GAK USAH pake huruf 'f'. 
# # Tapi variabelnya dioper di paling belakang lewat `.format(variabel)`.

# ==============================================================================
# # 1. CARA PAKAI DASAR & MULTI-ITEM (BERDASARKAN ANTRIAN/URUTAN)
# # 🔹 Taktik: Jumlah `{ }` di dalam teks harus sama kayak jumlah item di dalam `.format()`.
# # 🔹 Sistem bakal nyocokin otomatis sesuai urutan antrian dari kiri ke kanan.
# ==============================================================================
print("--- TEST 1: ANTRIAN ITEM OTOMATIS ---")
quantity = 3 
itemno = 567
price = 49

# Format desimal `:.2f` tetep bisa dipake di dalam kurung kurawal
myoder = "I want {} pieces of item number {} for {:.2f} dollars"

# Python bakal masukin: quantity ke {}, itemno ke {}, price ke {:.2f}
print(myoder.format(quantity, itemno, price))

print("-" * 50)

# ==============================================================================
# # 2. INDEX NUMBERS (SETTING SLOT INVENTORY PAKE ANGKA)
# # Taktik: Biar gak ketuker, lu bisa kasih nomor index di dalam `{}` dimulai dari 0.
# # 🔹 {0} = Item pertama di .format()
# # 🔹 {1} = Item kedua di .format(), dst.
# # Kegunaan: Lu bisa manggil item yang sama berkali-kali tanpa perlu nulis ulang!
# ==============================================================================
print("--- TEST 2: FORMAT PAKE INDEX (SLOT) ---")
# Slot 0 = age (36), Slot 1 = name ("John")
age = 23
name = "Iman"

# Kita panggil Slot 1 dulu baru Slot 0
txt = "His name is {1}. {1} is {0} years old"
print(txt.format(age, name))

print("-" * 50)

# ==============================================================================
# # 3. NAMED INDEXES (LOCK KEY / PANGGIL PAKE NAMA VARIABLE)
# # Taktik: Daripada pusing ngingetin urutan angka (0, 1, 2), lu bisa kasih nama custom 
# #         di dalam `{}`. Pas di `.format()`, lu tinggal sebutin namanya kayak key-value.
# # Analogi: Mirip panggil nama akun/nickname di dalam game!
# ==============================================================================
print("--- TEST 3: PANGGIL PAKE NAMA CUSTOM ---")

# Di dalam teks kita pasang variabel custom: {carname} dan {model}
myorder_costum = "i Have {carname}, it is a {model}."

# Pas manggil, kita sebutin namanya secara spesifik
print(myorder_costum.format(carname = "Ford", model = "Mustang"))