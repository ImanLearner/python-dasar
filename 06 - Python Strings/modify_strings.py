
# MANIPULASI STRING (MODIFY STRINGS) - KATA KUNCI: PAKE ()

# --- 1. upper() ---
# Tugas: Maksain semua huruf jadi HURUF BESAR (KAPITAL)
a = "Hello, World!"
print(a.upper())  # Output: "HELLO, WORLD!"

# --- 2. lower() ---
# Tugas: Maksain semua huruf jadi huruf kecil semua
b = "Hello, World!"
print(b.lower())  # Output: "hello, world!"

# --- 3. strip() ---
# Tugas: Tukang cukur spasi gaib di pangkas paling depan & paling belakang teks doang
# (Spasi yang di tengah kata GAK AKAN ikut dihapus)
c = "   Hello, World!   "
print(c.strip())  # Output: "Hello, World!"

# --- 4. replace() ---
# Tugas: Cari kata/huruf lama, terus diganti ama yang baru
# Rumus: .replace("yang_mau_diganti", "penggantinya")
d = "Hello, World!"
print(d.replace("H", "J"))  # Output: "Jello, World!"

# --- 5. split() ---
# Tugas: Belah teks jadi potongan-potongan (List) berdasarkan tanda pemisah tertentu
e = "Hello, World!"
print(e.split(","))  # Output: ['Hello', ' World!'] (dibelah pas nemu tanda koma)

# --- 6. join() ---
# Tugas: Kebalikan dari split. Tugasnya merakit kembali potongan kata (List) 
# menjadi satu teks utuh (String), pake lem/perekat yang kita mau.
# Rumus: "lem_perekat".join(list_yang_mau_digabung)
f = ['Hello', 'World!']
print(",".join(f))  # Output: "Hello,World!" (digabung kembali pake lem koma)