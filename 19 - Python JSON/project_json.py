import json

# 1. KARDUS FUNGSI: Tugasnya ngambil data mentah PC target (Simulasi)
def dapatkan_data_pc():
    # Ini data internal di dalam game/PC target
    data_mentah = {
        "status": "HACKED",
        "ip_address": "192.168.1.100",
        "username_pc": "Target_Operation_X",
        "os": "Windows 11 Pro",
        "antivirus_active": False
    }
    return data_mentah # Ngirimin data keluar dari kardus

# 2. KARDUS FUNGSI: Tugasnya ngebungkus data jadi file mentah .sav/json biar bisa dikirim lewat internet
def bungkus_paket_kiriman(data_pc):
    # Proses SAVE GAME / EXPORT pake json.dumps
    paket_teks_mentah = json.dumps(data_pc, indent=4)
    return paket_teks_mentah

# ==========================================
# GAMPING ZONE (EKSEKUSI UTAMA)
# ==========================================

print("=== MEMULAI SERANGAN BACKDOOR SIMULATOR ===")

# Langkah A: Ambil data dari PC target
data_korban = dapatkan_data_pc()

# Langkah B: Bungkus jadi JSON teks mentah biar bisa dimaling lewat internet
paket_siap_kirim = bungkus_paket_kiriman(data_korban)

# Langkah C: Tampilkan hasilnya di layar seolah-olah data udah nyampe di laptop lu!
print("\n[+] DATA BERHASIL DICOLONG DAN DI-EXPORT KE JSON:")
print(paket_siap_kirim)

print("\n=== MISI SELESAI, AKUN KORBAN BERHASIL DI-LOG ===")