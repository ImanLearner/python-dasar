# DOKUMENTASI : CARA MENGUBAH ISI LIST (CHANGE ITEMS)
# ==============================================================================
# Sifat List itu "Changeable", artinya isinya bisa diotak-atik setelah dibuat.
# ==============================================================================

# 1. GANTI SATU DATA PAKE INDEX
buah = ["apple", "banana", "cherry"]
buah[1] = "blackcurrant"  # Menimpa index 1 (banana) menjadi blackcurrant
print("1. Ganti Satu Data (Index 1) :", buah)
print("-" * 50)


# 2. GANTI BANYAK DATA SEKALIGUS PAKE RANGE [mulai:sampai]
# Inget hukum lama: index belakang (3) gak ikut dihitung! Jadi yang diganti cuma index 1 dan 2.
menu = ["apple", "banana", "cherry", "orange"]
menu[1:3] = ["blackcurrant", "watermelon"]
print("2. Ganti Banyak Data [1:3]    :", menu)
print("-" * 50)


# 3. TRICK: MASUKIN DATA LEBIH BANYAK DARIPADA YANG DIGANTI
# Kita cuma numpang di lapak index 1:2 (cuma banana), tapi kita jejelin 2 buah baru.
# Efeknya: Panjang list bakal otomatis melar/bertambah!
keranjang = ["apple", "banana", "cherry"]
keranjang[1:2] = ["blackcurrant", "watermelon"]
print("3. Dimelarin (Jejel 2 Data)   :", keranjang)
print("-" * 50)


# 4. TRICK: MASUKIN DATA LEBIH DIKIT DARIPADA YANG DIGANTI
# Kita pilih index 1:3 (banana & cherry), tapi cuma kita ganti pake 1 buah doang.
# Efeknya: List-nya otomatis mengkerut/makin pendek!
stok = ["apple", "banana", "cherry"]
stok[1:3] = ["watermelon"]
print("4. Diangkerutin (Sisa 1 Data) :", stok)


