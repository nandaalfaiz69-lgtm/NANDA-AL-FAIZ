# variabel dan tipe data

nama_mhs = input("Masukkan nama mahasiswa: ")
nalgoritma = int(input("Masukkan nilai nalgoritma: "))
nagama = int(input("Masukkan nilai nagama: "))
nbasisdata = int(input("Masukkan nilai nbasisdata: "))
nlogikainformatika = int(input("Masukkan nilai nlogikainformatika: "))
nbahasaindonesia = int(input("Masukkan nilai nbahasaindonesia: "))
nbahasainggris = int(input("Masukkan nilai nbahasainggris: "))
npancasila = int(input("Masukkan nilai npancasila: "))

print(nama_mhs)
# menghitung nilai rata-rata
rata_rata= (nalgoritma + nagama + nbasisdata + nlogikainformatika + nbahasaindonesia + nbahasainggris + npancasila) / 7
print(" rata_rata ")

# penentuan lulus atau tidak
if rata_rata >= 70 and rata_rata <= 100:
    print("Nilai : A " )
elif rata_rata>= 70 and rata_rata <= 80:
    print("Nilai : B " )
elif rata_rata >= 50 and  rata_rata <= 70:
    print("Nilai : C " )
elif rata_rata >=30 and rata_rata <= 50:
    print("Nilai : D " )
elif rata_rata >=10 and rata_rata <= 30:
    print("Nilai : E " )
else :
    print("Nilai lebih dari 100 atau nilai dibawah 10 " )