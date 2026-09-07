# # PYTHON LOOP SETS (CARA NGEBONGKAR ISI SET)
# =========================================================================
# # Konsep Penting Loop Set:
# # 1. Set itu Unindexed, jadi gak bisa panggil `thisset[0]`.
# # 2. Cara satu-satunya buat ngakses datanya adalah dengan cara "diiterasi" 
# #    (diputerin satu per satu) pake `for loop`.
# # 3. Ingat: Karena sifatnya Unordered, urutan cetaknya bakal ACAK tiap kali di-run!
# =========================================================================

# # Contoh Dasar Loop Set
thisset = {"durian", "mangga", "kelengkeng"}

print("Mulai membongkar isi Set:")

for x in thisset:
    # # Variabel 'x' bakal mewakili tiap data yang lagi diambil dalam satu putaran
    print("Data yang ditemukan :", x)

print("-" * 50)

# # Skenario Industri: 
# # Misal lu punya Set isi IP Firewall yang mencurigakan
blocked_ips = {"192.168.1.5", "10.0.0.1", "172.16.0.25"}

print("Daftar IP yang sedang diblokir :")
for ip in blocked_ips:
    print("Mengamankan Trafik dari :", ip)

