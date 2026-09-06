# Indentity Operator

"""
digunakan untuk membandingkan objek, bukan apakah objek tersebut sama, 
    tetapi apakah objek tersebut benar-benar objek yang sama, dengan lokasi memori yang sama:
"""

# Operator `is` mengembalikan nilai `True` jika kedua variabel menunjuk ke objek yang sama:
x = ["apple", "apple"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)
print("-" * 30)

# Operator `is not` mengembalikan `True` jika kedua variabel tidak menunjuk ke objek yang sama:
x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)
print("-" * 30)

# Perbedaan Antara  is and ==
    # is -> Nyocokin KOTAK/FISIK VARIABELNYA (Harus di kotak yang sama)
    # == -> Nyocokin ISI VARIABEL (VALUE) DOANG (Gak peduli beda kotak)

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)
