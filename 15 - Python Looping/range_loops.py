# ==============================================================================
#          DOKUMENTASI MINI: PYTHON range() FUNCTION (TUKANG BUAT DERET)
# ==============================================================================

# # 1. PENGGUNAAN SATU PARAMETER: range(stop)
# # Artinya: "Bikin deret angka mulai dari 0, nambah 1 terus, dan BERHENTI SEBELUM angka stop"
# # Catatan Penting: Angka stop-nya GAK IKUT DICETAK!

print("=== 1. RANGE DENGAN SATU PARAMETER ===")
for x in range(6):
    print(x)

# # CARA BACA: Bikin angka sebanyak 6 biji dimulai dari 0.
# # Tes Logika: Angka yang keluar adalah 0, 1, 2, 3, 4, 5. Angka 6 TIDAK IKUT!
print("-" * 30)


# # 2. PENGGUNAAN DUA PARAMETER: range(start, stop)
# # Artinya: "Bikin deret angka mulai dari angka 'start', bukan dari 0 lagi"
print("=== 2. RANGE DENGAN START DAN STOP ===")
for x in range(2, 6):
    print(x)

# # CARA BACA: Mulai cetak dari angka 2, berhenti sebelum angka 6.
# # Tes Logika: Angka yang keluar adalah 2, 3, 4, 5. Angka 6 TETEP GAK IKUT!
print("-" * 30)


# # 3. PENGGUNAAN TIGA PARAMETER: range(start, stop, step)
# # Artinya: "Sama kayak nomor 2, tapi lompatan angkanya (increment) ditentukan oleh nilai 'step'"
# # Default step kalau gak ditulis itu nilainya 1.

print("=== 3. RANGE DENGAN STEP (LOMPATAN ANGKA) ===")
for x in range(2, 30, 3):
    print(x)

# # CARA BACA: Mulai dari angka 2, berhenti sebelum 30, setiap putaran angkanya melompat ditambah 3.
# # Tes Logika: Putaran 1 -> 2, Putaran 2 -> 5 (2+3), Putaran 3 -> 8 (5+3), dan seterusnya sampai sebelum angka 30.
