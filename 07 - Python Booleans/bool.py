# Boolean Values
        #Python mendapatkan salah satu dari dua jawaban, Benar atau Salah.

print(10 > 5)
print(10 == 10)
print(10 < 9)
print("-" * 30)

# 2. Logika Boolean di dalam Percabangan (if-else) 
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")  # Ini yang jalan, karena 33 > 200 itu False

print("-" * 30)

# Beberapa data bernilai True
    # Semua teks (string) itu pasti True, KECUALI teks kosong ("") yang kagak ada isinya sama sekali.
    # Semua angka itu pasti True, KECUALI angka nol (0) yang artinya amsyong/kosong.
    # Semua wadah data (kayak list, tuple, set, atau dictionary) itu pasti True, KECUALI wadah kosong yang gak ada isiannya blas.

print(bool("abc")) #True                                 # print(bool("")) = false
print(bool(123))   #True                                 # print(bool(0))  = false
print(bool(["apple", "cherry", "banana"]))          


print("-" * 30)

# Beberapa data bernilai salah
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

print("-" * 30)

# Functions can Return a Boolean
    # membuat fungsi yang mengembalikan nilai Boolean:
def myFunction() :
  return True

print(myFunction())

print("-" * 30)


# menjalankan kode berdasarkan jawaban Boolean dari suatu fungsi:
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

print("-" * 30)

