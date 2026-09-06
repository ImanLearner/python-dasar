#  KITAB SUCI: MASTER PRECEDENCE ORDER PYTHON (KASTA TERTINGGI KE TERENDAH)
# ==============================================================================
# Aturan: Komputer mengevaluasi kode dari KASTA 1 down to KASTA 5.
# Jika dalam satu kasta levelnya SAMA, perhitungan jalan dari KIRI ke KANAN.
# ==============================================================================

# KASTA 1: RAJA UTAMA
# -> () : Tanda Kurung (Wajib kelar duluan, gak bisa diganggu gugat)

# KASTA 2: MATEMATIKA UTAMA (ARITMATIKA TINGGI)
# -> ** : Pangkat

# KASTA 3: MATEMATIKA BIASA (ARITMATIKA MENENGAH)
# -> * : Perkalian
# -> /  : Pembagian (Hasil selalu desimal/float)
# -> // : Floor Division (Pembagian bulat, angka belakang koma dibuang)
# -> %  : Modulus (Sisa hasil bagi)

# KASTA 4: MATEMATIKA BONTOT (ARITMATIKA RENDAH)
# -> +  : Penjumlahan
# -> -  : Pengurangan

# KASTA 5: CEK KOTAK & DAFTAR (PERBANDINGAN, IDENTITY, MEMBERSHIP)
# (Semua di level ini kastanya SAMA KUAT, dihitung dari Kiri ke Kanan)
# -> == , != , > , >= , < , <=  (Perbandingan isi nilai)
# -> is , is not                (Identity / Cek nomor kotak RAM)
# -> in , not in                (Membership / Cek keanggotaan)

# KASTA 6: SATPAM GERBANG (LOGIKA)
# -> not : Kebalikan (Kasta tertinggi di gerbang logika)
# -> and : Dan
# -> or  : Atau (Kasta paling bontot dari seluruh operator Python)

# ==============================================================================
# CONTOH KASUS GABUNGAN NYATA:
# ==============================================================================
# Alur: Matematika (+) jalan duluan, baru Cek Keanggotaan (in), terakhir Logika (or)
# 1. 2 + 1 = 3
# 2. Apakah 3 ada di dalam list [3, 4]? Jawabannya True.
# 3. True or False? Hasil akhir = True.

eksekusi = 3 in [2 + 1, 4] or False
print("Hasil Uji Kitab Suci :", eksekusi) # Hasil: True