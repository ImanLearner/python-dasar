# ==============================================================================
#                      5. NESTED LOOP (LOOP DI DALAM LOOP)
# ==============================================================================#
#  # Artinya: "Setiap satu kali loop luar jalan, loop dalam bakal diselesaikan sampai habis dulu"

adj = ["red", "big"]
fruits = ["apple", "banana"]

for x in adj:
    for y in fruits:
        print(x, y)

# # CARA BACA: 
# # Putaran 1 luar (x = "red") -> loop dalam jalan semua -> cetak "red apple", "red banana"
# # Putaran 2 luar (x = "big") -> loop dalam jalan semua -> cetak "big apple", "big banana"

print("-" * 30)

# # 6. PERNYATAAN pass (UNTUK LOOP KOSONG)
# # Kegunaan: Kalau lu mau bikin struktur loop dulu tapi belom ada isinya, biar gak error.

for x in [0, 1, 2]:

    pass  # Cuma numpang lewat, gak ngelakuin apa-apa dan gak bikin error