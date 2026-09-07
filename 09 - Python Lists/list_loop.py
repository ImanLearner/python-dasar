# PYTHON LOOP LISTS
# ==============================================================================
# Ada 4 cara utama buat membongkar dan mencetak isi list satu per satu.
# ==============================================================================

thislist = ["apple", "banana", "cherry"]

# 1. Cara Paling Gampang: for x in list
# Membaca langsung "nama barangnya" dari depan sampai belakang.
for x in thislist:
    print("For biasa     :", x)
print("-" * 30)


# 2. Cara Pake Nomor Urut: for i in range(len(list))
# Membaca berdasarkan "nomor index-nya" (0, 1, 2). 
# len(thislist) hasilnya 3, lalu range(3) bakal bikin barisan angka [0, 1, 2].
for i in range(len(thislist)):
    print(f"For index {i}  :", thislist[i])
print("-" * 30)


# 3. Cara Manual: Pake while loop
# Harus bikin variabel hitungan sendiri (i = 0) dan wajib ditambah 1 di bawahnya
# biar perulangannya gak berjalan selamanya (infiniteloop) tanpa henti.
i = 0
while i < len(thislist):
    print("While loop    :", thislist[i])
    i = i + 1
print("-" * 30)


# 4. Cara Jalur Cepat (Shorthand): List Comprehension
# Memadatkan kode 'for loop' biasa menjadi cuma 1 baris di dalam kurung siku.
[print("Comprehension :", x) for x in thislist]
print("-" * 30)