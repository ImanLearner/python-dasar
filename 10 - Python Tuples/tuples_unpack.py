# # PYTHON UNPACK TUPLES (MEMBONGKAR ISI TUPLE KE VARIABEL)
# ==============================================================================
# # Packing   = Memasukkan banyak data ke dalam satu wadah Tuple.
# # Unpacking = Membongkar isi Tuple dan membagikannya ke beberapa variabel baru.
# ==============================================================================

# # 1. Unpacking Standar (Jumlah Variabel PAS)
# # Jumlah variabel di sebelah kiri HARUS SAMA dengan jumlah isi data di dalam Tuple.
fruits = ("apple", "banana", "cherry")

# Membongkar isi tuple ke dalam 3 variabel baru
(green, yellow, red) = fruits

print("Hasil Unpacking Standar")
print("green  :", green)   # Mengambil index 0 ("apple")
print("yellow :", yellow)  # Mengambil index 1 ("banana")
print("red    :", red)     # Mengambil index 2 ("cherry")
print("-" * 50)


# # 2. Menggunakan Asterisk (*) di Akhir Variabel
# # Jika jumlah variabel LEBIH SEDIKIT dari jumlah data, pasang tanda bintang (*) 
# # pada variabel terakhir. Sisa datanya otomatis ditampung dalam bentuk LIST.
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# green dapet data pertama, yellow dapet data kedua, sisanya diborong sama *red
(green, yellow, *red) = fruits

print("Hasil Unpacking dengan Asterisk (*) di Akhir")
print("green  :", green)
print("yellow :", yellow)
print("red    :", red)     # Output berupa LIST: ['cherry', 'strawberry', 'raspberry']
print("-" * 50)


# # 3. Menggunakan Asterisk (*) di Tengah Variabel
# # Bintang (*) juga bisa dipasang di variabel tengah. Python akan membagikan data 
# # untuk variabel ujung-ujung dulu, baru sisanya dimasukkan ke variabel berbintang.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# green dapet data pertama ("apple"), red dapet data terakhir ("cherry")
# *tropic memborong semua sisa data yang ada di tengah-tengah
(green, *tropic, red) = fruits

print("Hasil Unpacking dengan Asterisk (*) di Tengah")
print("green  :", green)
print("tropic :", tropic)   # Output berupa LIST data tengah: ['mango', 'papaya', 'pineapple']
print("red    :", red)
print("-" * 50)