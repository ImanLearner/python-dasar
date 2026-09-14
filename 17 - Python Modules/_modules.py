# =============================================================================
# #                    DOKUMENTASI MINI: PYTHON MODULES
# =============================================================================


# =============================================================================
# # 1. APA ITU MODULE?
# # Artinya: Module adalah file Python (.py) yang berisi kumpulan kode.
# # Isinya bisa berupa function, variable, dictionary, list, class, dll.
# # Gunanya: Supaya kode lebih rapi dan bisa dipakai ulang di file lain.
# =============================================================================

print("=== 1. APA ITU MODULE ===")

# Misalnya kita punya file bernama:
# mymodule.py

def greeting(name):
    print("Hello, " + name)

# Cara pakai module:
# import mymodule
#
# mymodule.greeting("Jonathan")


print("-" * 30)



# =============================================================================
# # 2. MEMBUAT MODULE
# # Cara membuat module sangat mudah.
# # Cukup simpan kode Python ke dalam file berekstensi .py
# # Nama file itulah yang menjadi nama module.
# =============================================================================

print("=== 2. MEMBUAT MODULE ===")

# File:
# mymodule.py

def greeting(name):
    print("Hello, " + name)

# Tidak ada output karena file ini hanya berisi kode.

print("-" * 30)



# =============================================================================
# # 3. MENGGUNAKAN MODULE (IMPORT MODULE)
# # Gunakan keyword 'import'
# # Setelah itu panggil:
# # nama_module.nama_function()
# =============================================================================

print("=== 3. IMPORT MODULE ===")

# import mymodule
#
# mymodule.greeting("Jonathan")

# Output:
#
# Hello, Jonathan

print("-" * 30)



# =============================================================================
# # 4. MODULE BISA MENYIMPAN VARIABLE
# # Module tidak hanya berisi function.
# # Bisa juga menyimpan:
# # - Variable
# # - List
# # - Tuple
# # - Dictionary
# # - Object
# =============================================================================

print("=== 4. VARIABLE DI MODULE ===")

# File:
# mymodule.py

person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}

# Cara mengambil datanya:
#
# import mymodule
#
# umur = mymodule.person1["age"]
# print(umur)

# Output:
#
# 36

print("-" * 30)



# =============================================================================
# # 5. NAMA MODULE
# # Nama file bebas.
# # Yang penting:
# # - Berekstensi .py
# # - Sebaiknya menggunakan huruf kecil
# # - Tidak memakai spasi
# =============================================================================

print("=== 5. NAMA MODULE ===")

# Contoh nama module:

# mymodule.py
# database.py
# kalkulator.py
# belajar_python.py

print("-" * 30)



# =============================================================================
# # 6. MEMBERI ALIAS MODULE (AS)
# # Keyword:
# # as
# #
# # Gunanya supaya nama module lebih pendek.
# =============================================================================

print("=== 6. ALIAS MODULE ===")

# import mymodule as mx
#
# print(mx.person1["age"])

# Output:
#
# 36

print("-" * 30)



# =============================================================================
# # 7. BUILT-IN MODULE
# # Python sudah menyediakan banyak module bawaan.
# # Tinggal import tanpa install.
# =============================================================================

print("=== 7. BUILT-IN MODULE ===")

# import platform
#
# sistem = platform.system()
# print(sistem)

# Contoh output:
#
# Windows
#
# Linux
#
# Darwin (MacOS)

print("-" * 30)



# =============================================================================
# # 8. FUNCTION dir()
# # Gunanya untuk melihat isi dari sebuah module.
# # Bisa melihat:
# # - Function
# # - Variable
# # - Class
# # - Attribute
# =============================================================================

print("=== 8. FUNCTION dir() ===")

# import platform

# print(dir(platform))

# Output:
#
# ['architecture',
#  'machine',
#  'processor',
#  'python_version',
#  'release',
#  'system',
#  ...]

print("-" * 30)



# =============================================================================
# # 9. IMPORT SEBAGIAN ISI MODULE
# # Gunakan keyword:
# # from ... import ...
# #
# # Jadi kita tidak perlu menulis:
# # nama_module.nama_variable
# =============================================================================

print("=== 9. FROM IMPORT ===")

# File:
# mymodule.py

def greeting(name):
    print("Hello, " + name)

person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}

# Cara pakai:
#
# from mymodule import person1
#
# print(person1["age"])

# Output:
#
# 36

print("-" * 30)



# =============================================================================
# # CATATAN PENTING
#
# import module
#
# --> Mengambil seluruh isi module.
#
# from module import sesuatu
#
# --> Mengambil bagian tertentu saja.
#
# import module as alias
#
# --> Memberi nama lain pada module.
#
# dir(module)
#
# --> Melihat semua isi yang ada di dalam module.
#
# Module bisa berisi:
# - Function
# - Variable
# - List
# - Tuple
# - Dictionary
# - Class
# - Object
# =============================================================================