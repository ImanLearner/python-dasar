# # PYTHON LOOP TUPLES (PERULANGAN PADA DATA TUPLE)
# ==============================================================================
# # Cara menampilkan atau memproses seluruh isi Tuple satu per satu.
# # Bisa menggunakan 'for loop' (langsung datanya / lewat index) atau 'while loop'.
# ==============================================================================

# # 1. Perulangan Langsung Menggunakan 'for' Loop (Loop Through Items)
# # Cara paling simpel. Variabel 'x' akan otomatis mengambil nilai item satu per satu.
thistuple = ("apple", "banana", "cherry")

print("Hasil For Loop (Langsung Item)")
for x in thistuple:
    print(x)
print("-" * 50)


# # 2. Perulangan Menggunakan Index / Nomor Urut (range & len)
# # Menggunakan fungsi len() untuk hitung total data, dan range() buat bikin urutan index.
# # Sangat berguna kalau lu butuh tahu posisi nomor index dari tiap item saat looping.
thistuple = ("apple", "banana", "cherry")

print("Hasil For Loop (Lewat Index Numbers)")
# len(thistuple) adalah 3, maka range(3) akan memicu index 0, 1, 2
for i in range(len(thistuple)):
    print(f"Index ke-{i} : {thistuple[i]}") 
print("-" * 50)


# # 3. Perulangan Menggunakan 'while' Loop
# # Menggunakan kondisi batas nilai. Memerlukan variabel hitung manual (i = 0).
# # Wajib menaikkan nilai i (i = i + 1) di akhir perulangan agar tidak terjadi Infinite Loop!
thistuple = ("apple", "banana", "cherry")
i = 0

print("Hasil While Loop")
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1  # Menaikkan counter agar looping berjalan maju
print("-" * 50)