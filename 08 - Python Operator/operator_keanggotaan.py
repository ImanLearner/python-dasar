# Python Membership Operators
# ==============================================================================
# 1. CONTOH PADA LIST (Kumpulan Data)
fruits = ["apple", "banana", "cherry"]

# Cek apakah "banana" ada di dalam list fruits
print('Apakah "banana" in fruits?      :', "banana" in fruits)        # Hasil: True

# Cek apakah "pineapple" TIDAK ADA di dalam list fruits
print('Apakah "pineapple" not in fruits:', "pineapple" not in fruits)  # Hasil: True
print("-" * 50)

# 2. CONTOH PADA STRINGS (Teks)
text = "Hello World"

# Cek huruf besar "H" (Ada)
print('Apakah "H" in text?             :', "H" in text)              # Hasil: True

# Penting : Python sensitif huruf besar-kecil! "hello" kecil GAK SAMA dengan "Hello" besar.
print('Apakah "hello" in text?         :', "hello" in text)          # Hasil: False

# Cek apakah huruf "z" beneran gak ada di dalam text
print('Apakah "z" not in text?         :', "z" not in text)          # Hasil: True