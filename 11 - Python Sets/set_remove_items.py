# # PYTHON REMOVE SET ITEMS (CARA NGEHAPUS DATA SET)
# =========================================================================
# # Karakter Utama Hapus Data Set:
# # 1. remove()  : Hapus data spesifik. Kalau barangnya GAK ADA -> Bakal ERROR!
# # 2. discard() : Hapus data spesifik. Kalau barangnya GAK ADA -> AMAN (Gak Error).
# # 3. pop()     : Hapus data SECARA ACAK, karena Set gak punya indeks.
# # 4. clear()   : Mengosongkan isi Set sampai bersih total (Set-nya masih ada).
# # 5. del       : Menghapus total variabel Set dari memori (Set-nya lenyap).
# =========================================================================

# # 1. Menggunakan remove()
# # Menghapus item secara spesifik, tapi harus yakin datanya ada
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")

print("Hasil remove() 'banana':")
print(thisset)
# # Catatan Taktis: Kalau lu coba thisset.remove("sirsak"), kodingan lu bakal ERROR MERAH!
print("-" * 50)


# # 2. Menggunakan discard()
# # Menghapus item secara spesifik, jauh lebih aman buat codingan industri
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")

print("Hasil discard() 'banana': ")
print(thisset)

# # Pembuktian Aman: Kita coba hapus "sirsak" yang emang gak ada di set
thisset.discard("sirsak")
print("Hasil discard() data ghaib (Aman gak error):")
print(thisset)
print("-" * 50)


# # 3. Menggunakan pop()
# # Menghapus item secara acak. Lu gak bakal tahu buah mana yang bakal ketendang!
thisset = {"mangga", "durian", "leci"}
x = thisset.pop()   #Buah yang kehapus bakal ditambung di variabel x

print("Buah yang gak beruntung kehapus acak oleh pop():")
print("Sisa isi set sekarang:")
print(thisset)
print("-" * 50)


# # 4. Menggunakan clear()
# # Membuat set jadi kosong melongpong (tersisa kurung set() kosong)
thisset = {"sirsak", "kelengkeng", "nangka"}
thisset.clear()

print("Hasil setelah clear() (Set Kosong):")
print(thisset)
print("-" * 50)


# # 5. Menggunakan keyword del
# # Menghapus total variabel dari memori sistem
thisset = {"alpukat", "manggis", "kiwi"}
del thisset

print("Hasil setelah del:")
# # print(thisset) <-- Ini kalau lu nyalain bakal ERROR, karena variabel 'thisset' udah gak eksis lagi di dunia!
print("Variabel 'thisset sukses lenyap dari memori !")