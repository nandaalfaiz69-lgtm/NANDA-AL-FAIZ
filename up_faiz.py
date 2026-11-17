# program aplikasi pemesanan tiket bioskop

Harga_tiket = {
    "reguler": 35000,
    "vip": 50000,
    "premium": 75000,
}
Batas_diskon = 3      
Persen_diskon = 10


def format_rupiah(angka):
    return "Rp{:,.0f}".format(angka).replace(",", ".")


print("=== APLIKASI PEMESANAN TIKET BIOSKOP ===")

lanjut = "y"
while lanjut.lower() == "y":
    
    nama = input("\nMasukkan nama pelanggan : ").strip()

    
    print("Pilihan tiket: Reguler / VIP / Premium")
    jenis = input("Pilih jenis tiket       : ").strip().lower()

    while jenis not in Harga_tiket:
        print("Jenis tiket tidak valid, coba lagi.")
        jenis = input("Pilih jenis tiket       : ").strip().lower()

    jumlah = 0
    while jumlah <= 0:
        try:
            jumlah = int(input("Jumlah tiket            : "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0.")
        except ValueError:
            print("Masukkan angka yang valid.")

    
    if jenis == "reguler":
        harga = 35000
    elif jenis == "vip":
        harga = 50000
    else:
        harga = 75000

    total = harga * jumlah

    
    if jumlah > Batas_diskon:
        diskon = total * Persen_diskon / 100
    else:
        diskon = 0

    total_bayar = total - diskon

    
    print("\n----------- STRUK PEMESANAN -----------")
    print("Nama pelanggan :", nama)
    print("Jenis tiket    :", jenis.capitalize() if jenis != "vip" else "VIP")
    print("Jumlah tiket   :", jumlah)
    print("Harga satuan   :", format_rupiah(harga))
    print("Subtotal       :", format_rupiah(total))
    if diskon > 0:
        print("Diskon 10%     : -" + format_rupiah(diskon))
    else:
        print("Diskon         : -")
    print("Total bayar    :", format_rupiah(total_bayar))
    print("---------------------------------------")
    print("Terima kasih telah memesan tiket di bioskop kami!")

    
    lanjut = input("\nLayani pelanggan lain? (y/t): ")

print("\nTerima kasih! ")