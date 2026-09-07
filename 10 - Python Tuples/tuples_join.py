# # PYTHON JOIN TUPLES (MENGGABUNGKAN DAN MENGALIKAN TUPLE)
# ==============================================================================
# # Walaupun Tuple gembok mati, kita bisa menggabungkan atau melipatgandakan 
# # isinya untuk membuat sebuah Tuple baru tanpa merusak Tuple yang asli.
# ==============================================================================

# # 1. Menggabungkan Dua Tuple (Menggunakan Operator +)
# # Menyambungkan isi tuple pertama dengan tuple kedua menjadi satu wadah baru.
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2

print("Hasil Gabung Dua Tuple (+)")
print("Tuple 3 Baru :", tuple3)  # Hasil: ('a', 'b', 'c', 1, 2, 3)
print("-" * 50)


# # 2. Melipatgandakan Isi Tuple (Menggunakan Operator *)
# # Menggandakan seluruh isi di dalam Tuple sebanyak jumlah yang kita tentukan.
fruits = ("apple", "banana", "cherry")

mytuple = fruits * 2

print("Hasil Kali Isi Tuple (*)")
print("Tuple Gandar :", mytuple) # Hasil: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
print("-" * 50)