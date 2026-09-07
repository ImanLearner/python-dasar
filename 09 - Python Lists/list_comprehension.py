# PYTHON LIST COMPREHENSION (JALAN PINTAS BIKIN LIST)
# ==============================================================================
# List Comprehension itu cara gaul & singkat di Python buat bikin LIST BARU 
# berdasarkan isi dari list yang udah ada, cuma dalam SATU BARIS KODE.

# ------------------------------------------------------------------------------
# RUMUS SAKRALNYA:
# newlist = [ EKSPRESI  for  ITEM  in  ITERABLE  if  KONDISI ]
#
# Keterangan:
# 1. EKSPRESI : Mau diapain data akhirnya? (Contoh: diubah kapital, diganti teks, dll).
# 2. ITEM     : Variabel sementara buat nampung data pas di-loop (biasanya pake 'x').
# 3. ITERABLE : Sumber datanya (bisa List lama, Tuple, range(), dll).
# 4. KONDISI  : (Opsional/Sifatnya Filter) Cuma data yang lolos syarat yang bakal masuk.
# ------------------------------------------------------------------------------

# JALUR LAMA (Tanpa List Comprehension) -> Panjang & Butuh banyak baris
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
jalur_lama = []
for x in fruits:
    if "a" in x:
        jalur_lama.append(x)
print("Jalur Lama        :", jalur_lama)
print("-" * 50)


# JALUR CEPAT (Pakai List Comprehension) -> Cuma 1 Baris, Hasil Sama Persis!
# Arti kodenya: "Ambil x, dari setiap x yang ada di fruits, KALO ada huruf 'a'-nya"
jalur_cepat = [x for x in fruits if "a" in x]
print("List Comprehension:", jalur_cepat)
print("=" * 50)

# ==============================================================================
# VARIASI CONTOH & MANIPULASI DATA (SILAKAN COBA DI RUN)
# ==============================================================================

# 1. MODEL FILTER (Menyaring Data)
# Contoh: Ambil semua buah KECUALI "apple"
bukan_apel = [x for x in fruits if x != "apple"]
print("Tanpa Apel        :", bukan_apel)


# 2. TANPA IF (Ambil Semua Tanpa Disaring)
# Contoh: Copy semua isi buah ke list baru
copy_fruits = [x for x in fruits]
print("Copy Semua Buah   :", copy_fruits)


# 3. PAKE range() (Bikin Angka Otomatis)
# Contoh: Bikin list angka dari 0 sampai 9
angka_0_9 = [x for x in range(10)]
print("Angka 0 s/d 9     :", angka_0_9)


# 4. GABUNGAN range() DAN FILTER IF
# Contoh: Ambil angka yang di bawah 5 aja
angka_bawah_5 = [x for x in range(10) if x < 5]
print("Angka di bawah 5  :", angka_bawah_5)


# 5. MANIPULASI EKSPRESI (Ubah Data Sebelum Dimasukin)
# Contoh: Semua nama buah otomatis diubah jadi HURUF KAPITAL (.upper())
buah_kapital = [x.upper() for x in fruits]
print("Buah Kapital      :", buah_kapital)


# 6. MENGGANTI TOTAL OUTPUT
# Contoh: Ubah semua isi list jadi teks 'hello' sebanyak jumlah buah
tukar_hello = ['hello' for x in fruits]
print("Tukar Jadi Hello  :", tukar_hello)


# 7. LEVEL TRICKY: PAKE IF-ELSE DI DEPAN (Bukan Buat Filter, Tapi Buat Tukar Isi)
# Aturan: Kalau mau pake ELSE, posisi IF-ELSE-nya harus dipindah ke DEPAN 'for'.
# Arti kodenya: "Ambil x jika x bukan banana, TAPI KALO banana ganti jadi orange"
tukar_pisang = [x if x != "banana" else "orange" for x in fruits]
print("Tukar Pisang      :", tukar_pisang)
print("=" * 50)