# Program Penilaian Mahasiswa

# Input nilai mahasiswa
tugas = float(input("Nilai tugas: "))
uts = float(input("Nilai UTS: "))
uas = float(input("Nilai UAS: "))
kehadiran = float(input("Kehadiran: "))

# Hitung nilai akhir
nilai_akhir = (0.20 * tugas) + (0.30 * uts) + (0.50 * uas)

# Menentukan status kelulusan dan predikat
lulus = nilai_akhir >= 75 and kehadiran >= 80
if nilai_akhir >= 85 and kehadiran >= 90 and nilai_akhir % 2 == 0:
    status = "LULUS DENGAN PREDIKAT"
elif nilai_akhir >= 75 and kehadiran >= 80:
    status = "LULUS"
else:
    status = "BELUM LULUS"

# menampilkan hasil
print("Nilai Akhir: ", nilai_akhir)
print("Status: ", status)