# ==============================================================================
# PYTHON SORT LISTS (MENGURUTKAN DATA)
# ==============================================================================
# Metode sort() digunakan untuk mengurutkan data di dalam list secara langsung.
# Secara default, data akan diurutkan dari yang terkecil ke terbesar (A-Z atau angka kecil ke besar).

# ------------------------------------------------------------------------------
# 1. Mengurutkan secara Ascending (Kecil ke Besar / A-Z)
# ------------------------------------------------------------------------------
# Secara default, jika sort() dipanggil tanpa tambahan apa pun, data otomatis diurutkan dari kecil ke besar.

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print("Ascending Teks  :", thislist)
# Hasil: ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

angka = [100, 50, 65, 82, 23]
angka.sort()
print("Ascending Angka :", angka)
# Hasil: [23, 50, 65, 82, 100]


# ------------------------------------------------------------------------------
# 2. Mengurutkan secara Descending (Besar ke Kecil / Z-A)
# ------------------------------------------------------------------------------
# Untuk membalik urutan dari besar ke kecil, tambahkan perintah reverse = True di dalam kurung sort().

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print("Descending Teks :", thislist)
# Hasil: ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

angka = [100, 50, 65, 82, 23]
angka.sort(reverse = True)
print("Descending Angka:", angka)
# Hasil: [100, 82, 65, 50, 23]


# ------------------------------------------------------------------------------
# 3. Masalah Huruf Kapital (Case Sensitive)
# ------------------------------------------------------------------------------
# Secara bawaan, sort() akan mendahulukan semua kata yang diawali HURUF KAPITAL baru kemudian mengurutkan kata dengan huruf kecil
# Contoh Masalah:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print("Masalah Kapital :", thislist)
# Hasil: ['Kiwi', 'Orange', 'banana', 'cherry'] (Kapital maju duluan)

# Solusi (Case-Insensitive Sort):
# Tambahkan key = str.lower agar Python menyamakan semua huruf menjadi huruf kecil saat diurutkan.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print("Solusi Kapital  :", thislist)
# Hasil: ['banana', 'cherry', 'Kiwi', 'Orange'] (Alfabet beneran rapi)


# ------------------------------------------------------------------------------
# 4. Membalik Urutan Asli List (Tanpa Memperhatikan Alfabet/Nilai)
# ------------------------------------------------------------------------------
# Jika hanya ingin memutar posisi list (yang di belakang pindah ke depan, yang di depan pindah ke belakang) 
# tanpa peduli itu huruf apa atau angka berapa, gunakan fungsi reverse().

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print("Hasil Balik Posisi:", thislist)
# Hasil: ['cherry', 'Kiwi', 'Orange', 'banana']

print("=" * 50)