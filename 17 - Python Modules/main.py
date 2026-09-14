# File: main.py

# Lu panggil file sebelah pake import
import mymodule
import platform

# Di dalam file utama lu:
# Panggil file di awal, baru variabelnya!
print(mymodule.target_ip)  # Keluar: 192.168.1.5
print(mymodule.version)    # Keluar: v1.0# Cara pakainya: nama_file.nama_fungsi()

print(platform.system())
