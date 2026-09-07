# # CHEAT SHEET: PYTHON SET METHODS (TABEL LENGKAP W3SCHOOLS)
# ===================================================================
# # Referensi dari gambar "image_d00106.png" & "image_d00106.png" (kelanjutannya).
# # Set = Tipe data unik. Gak ada index, dan ANTI DATA KEMBAR/DUPLIKAT!
# ===================================================================

# Data awal buat demo matematika himpunan
grup_A = {1, 2, 3, 4}
grup_B = {3, 4, 5, 6}

print("=== CONTEKAN JURUS INSTAN SET ===")

# # 1. `.add(item)` -> Nambahin anggota baru ke dalam Set
set_user = {"iman", "play"}
set_user.add("cyber") # Kalau lo add "iman" lagi, bakal diabaikan karena udah ada
print("1. Hasil .add()      :", set_user)


# # 2. `.discard(item)` & `.remove(item)` -> Ngapus anggota spesifik
# # Bedanya: .remove() bakal bikin program crash kalau anggotanya gak ada.
# # Sedangkan .discard() lebih aman (Anti-Crash), kalau gak ada ya dicuekin.
set_user.discard("ngasal") # Gak ada di set, tapi aman gak error!


# # 3. `.difference()` (Shortcut: `-`) -> Mencari data yang CUMA ada di grup kiri
# # Kasus: Anggota grup_A yang kagak ada di grup_B
print("3. Hasil .difference():", grup_A.difference(grup_B)) # Hasil: {1, 2}
# Note: Kalau `.difference_update()`, dia langsung ngubah isi asli grup_A jadi {1, 2}


# # 4. `.intersection()` (Shortcut: `&`) -> Irisan / Mencari data yang SAMA-SAMA ADA
# # Kasus: Anggota yang ada di grup_A DAN juga ada di grup_B
print("4. Hasil .intersection():", grup_A.intersection(grup_B)) # Hasil: {3, 4}
# Note: Kalau `.intersection_update()` (Shortcut: `&=`), dia langsung maksa ngerubah grup asli.


# # 5. `.symmetric_difference()` (Shortcut: `^`) -> Mencari data yang UNIK di masing-masing grup
# # Kebalikan dari irisan: Data yang cuma ada di A ditambah data yang cuma ada di B.
print("5. Hasil .symmetric_d():", grup_A.symmetric_difference(grup_B)) # Hasil: {1, 2, 5, 6}


# # 6. `.union()` (Shortcut: `|`) -> Gabungan total semua anggota grup
# # Otomatis angka yang kembar (3 dan 4) cuma ditulis satu kali.
print("6. Hasil .union()       :", grup_A.union(grup_B)) # Hasil: {1, 2, 3, 4, 5, 6}


# # 7. `.update()` (Shortcut: `|=`) -> Masukin rombongan data baru sekaligus
grup_A.update({7, 8}) # grup_A sekarang ketambahan 7 dan 8
print("7. Hasil .update()      :", grup_A)


# # 8. `.isdisjoint()` -> Ngecek "Ada gak data yang sama?"
# # Menghasilkan True kalau kedua grup bener-bener musuhan (gak ada satu pun angka yang sama).
print("8. Hasil .isdisjoint()  :", grup_A.isdisjoint(grup_B)) # Hasil: False (karena ada yang sama)


# # 9. `.issubset()` (Shortcut: `<=`) -> Ngecek "Apakah grup gua ada di dalem grup dia?"
kecil = {1, 2}
print("9. Hasil .issubset()    :", kecil.issubset(grup_A)) # Hasil: True


# # 10. `.issuperset()` (Shortcut: `>=`) -> Kebalikan subset. Ngecek "Apakah gua wadah gedenya dia?"
print("10. Hasil .issuperset() :", grup_A.issuperset(kecil)) # Hasil: True


# # 11. `.pop()` & `.clear()` & `.copy()`
# # .clear() buat nguras habis set jadi set() kosong.
# # .copy() buat duplikat set ke variabel baru.
# # .pop() di Set itu BAR-BAR, dia bakal ngapus satu data SECARA ACAK/RANDOM karena Set gak punya index!
data_acak = grup_B.pop() 
print("11. Hasil .pop() acak   :", grup_B, f"| Anggota yg kebuang: {data_acak}")

print("-" * 65)