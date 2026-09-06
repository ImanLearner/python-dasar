# =========================================================
# LENGKAP 9 ESCAPE CHARACTERS (VERSI SUPER SIMPEL)
# =========================================================

# 1. \' (Single Quote) -> Nyisipin kutip satu di dalem kutip satu
print('It\'s alright')        # Output: It's alright

# 2. \\ (Backslash) -> Nyetak tanda backslash (\) murni
print("C:\\Windows")          # Output: C:\Windows

# 3. \n (New Line) -> Perintah "Enter" (Turun baris)
print("Halo\nBandung")        # Output: Halo (di bawahnya) Bandung

# 4. \r (Carriage Return) -> Kursor balik ke awal (Teks belakang nimpa depan)
print("Maling\rPolisi")       # Output: Polisi (Kata "Maling" ketimpa)

# 5. \t (Tab) -> Ngasih jarak spasi lebar otomatis
print("Nama:\tBudi")          # Output: Nama:   Budi

# 6. \b (Backspace) -> Ngapus 1 karakter di kirinya
print("Hacker \b")            # Output: Hacker (Spasi sebelum \b kehapus)

# 7. \f (Form Feed) -> Perintah ganti halaman (Zaman printer jadul)
print("Hal1\fHal2")           # Output: Hal1♀Hal2 (Di terminal muncul simbol)

# 8. \ooo (Octal value) -> Nerjemahin angka Oktal (basis 8) jadi huruf
print("\141")                 # Output: a (141 adalah kode oktal huruf 'a')

# 9. \xhh (Hex value) -> Nerjemahin angka Hexadecimal (basis 16) jadi huruf
print("\x41")                 # Output: A (41 adalah kode hex huruf 'A')