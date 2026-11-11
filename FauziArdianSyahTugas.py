print("=== APLIKASI WARKOP BRAYAN ===")

total = 0

while True:
    print("=== MENU MAKANAN ===")
    print("1. Nasi Goreng - Rp25000")
    print("2. Mie Ayam - Rp15000")
    print("3. Ayam Geprek - Rp20000")
    print("4. Sate Ayam - Rp30000")
    print("5. Bakso - Rp18000")
    print("0. Selesai")

    pilihan = int(input("Silahkan dipilih menunya: "))

    if pilihan == 0:
        break

    elif pilihan == 1:
        harga = 25000
        nama = "Nasi Goreng"

    elif pilihan == 2:
        harga = 15000
        nama = "Mie Ayam"

    elif pilihan == 3:
        harga = 20000
        nama = "Ayam Geprek"

    elif pilihan == 4:
        harga = 30000
        nama = "Sate Ayam"

    elif pilihan == 5:
        harga = 18000
        nama = "Bakso"

    else:
        print("Menu tidak tersedia")
        continue

    jumlah = int(input("Berapa porsinya: "))

    subtotal = harga * jumlah
    total += subtotal

    print("Nama makanan:", nama)
    print("Subtotal: Rp", subtotal)

print("=== STRUK PEMBAYARAN ===")
print("Total belanja: Rp", total)

if total > 200000:
    diskon = total * 20 / 100
else:
    diskon = 0

total_bayar = total - diskon

print("Diskon: Rp", diskon)
print("Total bayar: Rp", total_bayar)
print("Terima kasih")


