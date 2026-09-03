# 1. GLOBAL VARIABLE
# ==================================================
# Variabel dibuat di luar function.
# Bisa dipakai di mana saja, termasuk di dalam function.

x_global = "awesome"

def myfunc1():
    print("Python is " + x_global)

myfunc1()

print("-" * 30)


# ==================================================
# 2. GLOBAL VS LOKAL
# ==================================================
# Kalau ada variabel di dalam function,
# variabel itu hanya hidup di function tersebut.
# Variabel luar tidak akan berubah.

x_global = "awesome"

def myfunc2():
    x_lokal = "fantastic"

    print("Python is " + x_lokal)

myfunc2()

# Tetap memakai variabel global
print("Python is " + x_global)

print("-" * 30)


# ==================================================
# 3. KEYWORD GLOBAL
# ==================================================
# Keyword global dipakai untuk membuat
# atau mengubah variabel global dari dalam function.


# --- A. Membuat variabel global dari dalam function ---

def myfunc3():
    global y_baru
    y_baru = "fantastic"

myfunc3()

print("Python is " + y_baru)

print("-" * 30)


# --- B. Mengubah variabel global dari dalam function ---

x_target = "awesome"

def myfunc4():
    global x_target
    x_target = "fantastic"

myfunc4()

print("Python is " + x_target)