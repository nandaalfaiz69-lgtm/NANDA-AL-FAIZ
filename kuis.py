# mulai program nilai target mahasiswa 
# program remedial ujian matematika

target_mahasiswa = { 
      "andi" : 70,
      "budi" : 75,
      "citra" : 80,
}
print("=== Program Remedial Ujian Matematika ===")
nama = input("Masukkan nama mahasiswa: ").strip()

# Cari target nilai sesuai nama mahasiswa

if nama.lower() in target_mahasiswa:
    target = target_mahasiswa[nama.lower()]
else:
    print("Nama tidak ada di data. Masukkan target secara manual.")
    target = int(input("Masukkan target nilai: "))

print(f"Target nilai {nama}: {target}")

percobaan = 0
lulus = False

while percobaan < 3 and not lulus:
    percobaan += 1
    nilai = int(input(f"Nilai {percobaan}: "))

    if nilai >= target:
        lulus = True
    else:
        print(f"Nilai belum mencapai target ({nilai} < {target}).")

print()
if lulus:
    print(f"{nama} berhasil lulus setelah {percobaan} kali percobaan!")
else:
    print(f"{nama} tidak lulus setelah {percobaan} kali percobaan!")