# # PYTHON FROZENSET (SET VERSI BEKU / ANTI-DIUBAH)
# =========================================================================
# # Karakter Utama Frozenset:
# # 1. Immutable : Gak bisa ditambah atau dihapus isinya setelah dibuat.
# # 2. Unordered : Posisinya tetep acak karena dia adalah turunan dari Set.
# # 3. Fungsi Aman: Cuma bisa pake fungsi yang GAK merubah data (non-mutating).
# =========================================================================

# # 1. Cara Membuat Frozenset & Cek Tipenya
x = frozenset({"apple", "banana", "cherry"})

print("Isi dari frozenset:", x)
print("Tipe datanya adalah:", type(x))
print("-" * 50)


# # 2. Pembuktian Kalau Frozenset Anti-Diubah (Akan Error Jika Dipaksa)
# # x.add("orange")     <-- Kalau ini lu nyalain, Python bakal ERROR ngamuk!
# # x.remove("banana")  <-- Ini juga bakal ERROR, karena datanya udah beku!


# # 3. Fungsi / Method yang Tetep Didukung (Operasi Non-Mutating)
# # Walaupun beku, kita tetep bisa ngebandingin datanya ama set lain
set_biasa = {"google", "microsoft", "apple"}

# A. Mencari data yang kembar (Intersection / &)
hasil_kembar = x.intersection(set_biasa)
print("Hasil irisan (tetep bisa):", hasil_kembar)

# B. Mencari gabungan data (Union / |)
hasil_gabungan = x.union(set_biasa)
print("Hasil gabungan (tetep bisa):", hasil_gabungan)

# C. Mencari selisih (Difference / -)
hasil_selisih = x - set_biasa
print("Hasil selisih minus (tetep bisa):", hasil_selisih)
print("-" * 50)