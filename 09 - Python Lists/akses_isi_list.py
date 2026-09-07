# DOKUMENTASI : CARA AKSES ISI LIST (ACCESS ITEMS)
# ==============================================================================
# Rumus Utama: Index selalu dimulai dari angka 0!
# ==============================================================================

buah = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# Index:    0          1         2         3        4        5        6
# Minus:   -7         -6        -5        -4       -3       -2       -1

# 1. AKSES PAKE INDEX POSITIF (DARI DEPAN)
print("1. Index [1] (Barang ke-2) :", buah[1])   # Hasil: banana
print("-" * 50)


# 2. AKSES PAKE INDEX NEGATIF (DARI BELAKANG)
# Cocok banget kalau lu males ngitung panjang list tapi mau nyomot data terakhir!
print("2. Index [-1] (Paling Akhir):", buah[-1])  # Hasil: mango
print("-" * 50)


# 3. RANGE INDEX PAKE TITIK DUA [mulai:sampai]
# HUKUM MUTLAK: Angka belakang JANGAN DIHITUNG (Stop sebelum index tersebut)!
# buah[2:5] -> Ambil index 2, 3, 4 (index 5 dibuang)
print("3. Range [2:5]             :", buah[2:5]) # Hasil: ['cherry', 'orange', 'kiwi']
print("-" * 50)


# 4. RANGE POTONG KOMPAS (KIRI / KANAN KOSONG)
# Jika kiri kosong [:4] -> Otomatis mulai dari index paling awal sampai sebelum 4
print("4. Dari Awal Berhenti di 4 :", buah[:4])  # Hasil: ['apple', 'banana', 'cherry', 'orange']

# Jika kanan kosong [2:] -> Otomatis ambil dari index 2 sampai ludes ke paling ujung
print("   Dari Index 2 Sampai Habis:", buah[2:])  # Hasil: ['cherry', 'orange', 'kiwi', 'melon', 'mango']
print("-" * 50)


# 5. RANGE INDEX MINUS (DARI BELAKANG)
# buah[-4:-1] -> Ambil dari index -4 sampai sebelum -1 (index -1 nya mango dibuang)
print("5. Range Minus [-4:-1]     :", buah[-4:-1]) # Hasil: ['orange', 'kiwi', 'melon']


#  6. CEK APAKAH BARANG ADA DI LIST (Pake 'in' yang kita pelajarin tadi!)
print("6. Cek Keanggotaan:")
if "apple" in buah:
    print("   Yes, 'apple' beneran ada di dalem list buah!")