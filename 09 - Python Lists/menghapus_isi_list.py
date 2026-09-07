# CARA MENGHAPUS ISI LIST (REMOVE ITEMS)
# ==============================================================================
# Ada 4 cara utama buat ngusir data dari List di Python.
# ==============================================================================

# 1. NGUSIR PAKE NAMA BARANGNYA: .remove()
# PENTING: Kalau ada nama barang yang KEMBAR, yang dihapus cuma yang PERTAMA KETEMU!
buah = ["apple", "banana", "cherry", "banana"]
buah.remove("banana")
print("Hasil remove :", buah)
print("-" * 30)


# 2. NGUSIR PAKE NOMOR INDEX: .pop()
# Kelebihan: Data yang dihapus bisa lu 'simpen' atau lu ambil kalau mau.
# TRICK: Kalau tanda kurungnya KOSONG .pop(), otomatis yang diusir adalah data PALING AKHIR!
items = ["apple", "banana", "cherry"]
items.pop(1)
print("Hasil pop index 1   :", items)

items.pop()
print("Hasil pop kosong    :", items)
print("-" * 30)


# 3. HAPUS SADIS PAKE KATA KUNCI: del
# Kegunaan 1: Bisa hapus pake index spesifik kayak .pop()
stok = ["apple", "banana", "cherry"]
del stok[0]
print("Hasil del index 0   :", stok)
# Kegunaan 2: Bisa hapus TOTAL satu variabel list sampai lenyap dari RAM komputer!
# del stok -> Kalau baris ini lu nyalain, variabel 'stok' bakal ilang permanen dan bikin error kalau di-print.
print("-" * 50)


# 4. DIKOSONGIN TAPI RUMAHNYA TETEP ADA: .clear()
# Efek: Keranjangnya gak dihancurin, cuma isinya dikuras abis sampai kosong melompong [].
keranjang = ["apple", "banana", "cherry"]
keranjang.clear()
print("Hasil clear         :", keranjang)
print("-" * 50)
