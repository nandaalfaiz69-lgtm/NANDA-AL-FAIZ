# =====================================
# Aplikasi Kasir Restoran
# =====================================

def rupiah(angka):
    return "Rp" + f"{angka:,}".replace(",", ".")


# Mulai program
print("=" * 42)
print("        RESTORAN SANTAPAN NUSANTARA")
print("=" * 42)

total = 0
pesanan = {}  # format: {nama: [harga, jumlah]}

# Tampilkan menu dan proses pemesanan (berulang sampai pilih 0)
while True:
    print("\n               DAFTAR MENU               ")
    print("=" * 42)
    print("Menu Makanan:")
    print("=" * 42)
    print("1. Nasi Goreng  - Rp25.000")
    print("2. Mie Ayam     - Rp15.000")
    print("3. Ayam Geprek  - Rp20.000")
    print("4. Sate Ayam    - Rp30.000")
    print("5. Bakso        - Rp18.000")
    print("6. Ayam Penyet  - Rp20.000")
    print("7. Ayam Kremes  - Rp20.000")
    print("8. Sate Ayam    - Rp25.000")
    print("9. Sate Kambing - Rp30.000")
    print("10. Sate Sapi   - Rp35.000")
    print("=" * 42)
    print("Menu Minuman:")
    print("=" * 42)
    print("11. Es Teh       - Rp5.000")
    print("12. Es Jeruk     - Rp7.000")
    print("13. Air Mineral  - Rp5.000")
    print("14. Lemon Tea    - Rp10.000")
    print("15. cappuccino    - Rp15.000")
    print("16. milkshake     - Rp20.000")
    print("17. es kopi susu  - Rp15.000")
    print("18. Strawberry Squash - Rp15.000")
    print("19. kopi hitam      - Rp10.000")
    print("20. teh tarik       - Rp10.000")
    print("0. Selesai Memilih")

    pilihan = input("Pilih menu (0-20): ")

    if pilihan == "0":
        break
    elif pilihan == "1":
        nama, harga = "Nasi Goreng", 25000
    elif pilihan == "2":
        nama, harga = "Mie Ayam", 15000
    elif pilihan == "3":
        nama, harga = "Ayam Geprek", 20000
    elif pilihan == "4":
        nama, harga = "Sate Ayam", 30000
    elif pilihan == "5":
        nama, harga = "Bakso", 18000
    elif pilihan == "6":
        nama, harga = "Ayam Penyet", 20000
    elif pilihan == "7":
        nama, harga = "Ayam Kremes", 20000
    elif pilihan == "8":
        nama, harga = "Sate Ayam", 25000
    elif pilihan == "9":
        nama, harga = "Sate Kambing", 30000
    elif pilihan == "10":
        nama, harga = "Sate Sapi", 35000
    elif pilihan == "11":
        nama, harga = "Es Teh", 5000
    elif pilihan == "12":
        nama, harga = "Es Jeruk", 7000
    elif pilihan == "13":
        nama, harga = "Air Mineral", 5000
    elif pilihan == "14":
        nama, harga = "Lemon Tea", 10000
    elif pilihan == "15":
        nama, harga = "Cappuccino", 15000
    elif pilihan == "16":
        nama, harga = "Milkshake", 20000
    elif pilihan == "17":
        nama, harga = "Es Kopi Susu", 15000
    elif pilihan == "18":
        nama, harga = "Strawberry Squash", 15000
    elif pilihan == "19":
        nama, harga = "Kopi Hitam", 10000
    elif pilihan == "20":
        nama, harga = "Teh Tarik", 10000
    else:
        print("Pilihan tidak valid, coba lagi.")
        continue

    jumlah_input = input(f"Jumlah {nama}: ")
    if not jumlah_input.isdigit() or int(jumlah_input) <= 0:
        print("Jumlah tidak valid, coba lagi.")
        continue

    jumlah = int(jumlah_input)
    subtotal = harga * jumlah
    total += subtotal

    # simpan ke daftar pesanan (gabung jika menu yang sama dipilih lagi)
    if nama in pesanan:
        pesanan[nama][1] += jumlah
    else:
        pesanan[nama] = [harga, jumlah]

    print(f"Ditambahkan: {nama} x{jumlah} = {rupiah(subtotal)}")

# Jika belum ada pesanan
if total == 0:
    print("\nTidak ada pesanan. Terima kasih!")
else:
    # 5. Hitung diskon
    if total > 200000:
        persen = 20
    else:
        persen = 0
    potongan = total * persen // 100
    total_bayar = total - potongan

    jumlah_semua = 0
    for data in pesanan.values():
        jumlah_semua += data[1]

    # Tampilkan struk pembayaran
    print("\n" + "=" * 42)
    print("          STRUK PEMBAYARAN")
    print("=" * 42)
    print(f"{'Nama Barang':<16}{'Harga':>9}{'Qty':>5}{'Subtotal':>12}")
    print("-" * 42)
    for nama, data in pesanan.items():
        harga, qty = data
        print(f"{nama:<16}{rupiah(harga):>9}{qty:>5}{rupiah(harga * qty):>12}")
    print("-" * 42)
    print(f"{'Jumlah Semua Barang':<26}: {jumlah_semua} item")
    print(f"{'Total Belanja':<26}: {rupiah(total)}")
    print(f"{'Diskon':<26}: {persen}%")
    print(f"{'Potongan':<26}: {rupiah(potongan)}")
    print("-" * 42)
    print(f"{'TOTAL BAYAR':<26}: {rupiah(total_bayar)}")
    print("=" * 42)
    print("            Terima Kasih")
