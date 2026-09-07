# # PYTHON JOIN SETS (CARA NGEGABUNGIN & NGEBANDINGIN SET)
# =========================================================================
# # RANGKUMAN LOGIKA OPERASI SET:
# # 1. GABUNGAN (Union / | )       : Ambil SEMUA data dari kedua pihak.
# # 2. IRISAN (Intersection / & )  : Cuma ambil data yang KEMBAR/DUPLIKAT doang.
# # 3. SELISIH (Difference / - )   : Ambil data di Set ke-1 yang GAK ADA di Set ke-2.
# # 4. BEDA SIMETRIS (Symmetric / ^): Ambil semua data, KECUALI yang kembar.
# =========================================================================

# # --- 1. UNION (GABUNGAN SEMUA DATA) ---
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

# Cara 1: Pake .union() -> hasil berupa Set baru (Bisa digabung List/Tuple juga)
set3 = set1.union(set2)
print("Hasil .union() :", set3)

# Cara 2: Pake simbol pipa | -> Hasil sama, tapi wajib sesama Set
set_simbol = set1 | set2
print("Hasil operator | :", set_simbol)
print("-" * 50)


# # --- 2. INTERSECTION (CUMA AMBIL YANG KEMBAR) ---
set_a = {"apple", "banana", "cherry"}
set_b = {"google", "microsoft", "apple"}

# Cara 1: Pake .intersection() -> Bikin Set baru isi data yang sama aja
set_c = set_a.intersection(set_b)
print("Hasil .Intersection() (Cuma yang kembar): ", set_c)

# Cara 2: Pake simbol dan &
set_dan = set_a & set_b
print("Hasil operator & :",set_dan)

# Cara 3: Pake .intersection_update() -> Langsung ngerubah variabel set_a asli
set_a.intersection_update(set_b)
print("Hasil setelah intersection_update() (set_a berubah) :", set_a)
print("-" * 50)


# # --- 3. DIFFERENCE (SELISIH / YANG GAK ADA DI SEBELAH) ---
set_x = {"apple", "google", "cherry"}
set_y = {"google", "micrososft", "apple"}

# Cara 1: Pake .difference() -> Cari apa yang ada di set_x tapi GAK ADA di set_y
set_z = set_x.difference(set_y)
print("Hasil .difference() (Yang gak ada di sebelah) :", set_z)

# Cara 2: Pake simbol minus -
set_minus = set_x - set_y
print("Hasil operator - :" ,set_minus)
print("-" * 50)


# # --- 4. SYMMETRIC DIFFERENCE (BUANG YANG KEMBAR) ---
set_m = {"apple", "banana", "cherry"}
set_n = {"google", "microsoft", "apple"}

# Cara 1: Pake .symmetric_difference() -> Gabungin semua, tapi "apple" dibuang karena kembar
set_o = set_m.symmetric_difference(set_n)
print("Hasil .symetric_difference() (Anti-kembar) :" ,set_o)

# Cara 2: Pake simbol pangkat ^
set_pangkat = set_m ^ set_n
print("Hasil Operator ^ :", set_pangkat)