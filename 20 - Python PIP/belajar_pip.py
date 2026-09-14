# ==============================================================================
#          DOKUMENTASI MINI: PYTHON PIP (MARKETPLACE UTK ITEM SAKTI)
# ==============================================================================

# # Latar Belakang:
# # PIP itu singkatan dari "Preferred Installer Program". 
# # Fungsinya buat download 'Package' atau 'Module' (Library/Kode buatan orang lain).
# # Analogi: PIP itu STEAM. Package/Module itu GAME yang ada di dalam Steam.
# #          Lu tinggal ketik perintah, PIP yang bakal download dan instalin.

# ==============================================================================
# # 1. CEK VERSION (FITUR CEK APAKAH STEAM SUDAH TERINSTAL)
# # Taktik: Ketik perintah ini DI TERMINAL (Bukan di dalam file Python/VS Code!).
# # Perintah: pip --version
# # Note: Kalau Python lu versi 3.4 ke atas, ini udah otomatis ada, gak usah download.
# ==============================================================================

# ==============================================================================
# # 2. INSTALL PACKAGE (DOWNLOAD GAME BARU DARI STEAM)
# # Taktik: Buka terminal, terus ketik perintah 'pip install nama_package'.
# # Contoh di dokumentasi lu: pip install camelcase
# # (Camelcase itu package buat bikin huruf pertama di tiap kata jadi KAPITAL).
# ==============================================================================

# Contoh cara pake "Game/Item" yang udah lu download lewat PIP:
import camelcase  # Panggil library yang udah di-download tadi

c = camelcase.CamelCase()
txt = "hello world"

print("--- DEMO UTILS DARI PIP (CAMELCASE) ---")
print(c.hump(txt))  # Hasil: "Hello World" (Huruf depan otomatis gede)
print("-" * 30)

# ==============================================================================
# # 3. LIST PACKAGES (CEK LIBRARY UTK KEBUTUHAN CYBERSEC)
# # Kenapa PIP penting banget buat Cybersec? Karena tools hacking kayak:
# # 🔹 'requests' (buat spam/brute force HTTP request web target)
# # 🔹 'scapy' (buat ngintip/sniffing paket data wifi orang lain)
# # Itu semua harus lu download dulu pake PIP sebelum bisa lu pake kodenya!
# ==============================================================================

# ==============================================================================
# # 4. MANAJEMEN ITEM INVENTORY (PERINTAH TERMINAL UTK PIP)
# # Ingat! Ketik ini langsung di CMD / Terminal VS Code lu:
# #
# # 🔹 Cek semua game/library yang terinstal: 
# #    pip list
# #    (Bakal keluar list inventory item lu beserta level/versi-nya).
# #
# # 🔹 Hapus game/library yang udah gak kepake (Buang item dari Inventory):
# #    pip uninstall camelcase
# #    (Nanti tinggal ketik 'y' buat konfirmasi hapus).
# ==============================================================================