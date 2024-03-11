import random
import sys
import time
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.000000001)
mengetik('HALLO SELAMAT DATANG DI TOKO KAMI.')
jenis1 = ""
jenis2 = ""
print("  ===TOKO APA AJA===")
nama = input("Nama Pembeli: ")
tgl = input("tanggal pembelian: ")
print("Nama Konsumen: ", nama)
print("Tanggal Pembelian: ", tgl)
print("")
print("Produk Pakaian")
 
 
def pilihan(i):
 
    switcher = {
        1: '----Kemeja = Rp.135.000----',
        2: '----Kaos = Rp.65.000----',
        3: '----Jaket = Rp.200.000----',
        4: '----Baju Muslim = Rp.167.000----',
    }
    return switcher.get(i, "Masukkan Pilihan Yang Benar!")
 
 
print("1. Kemeja")
print("2. Kaos")
print("3. Jaket")
print("4. Baju Muslim")
nomor = int(input("Masukkan Pilihan: "))
c = pilihan(nomor)
print(c)
jumlah1 = int(input("Banyak unit yang dibeli: "))
if nomor == "1":
    a = jumlah1*135000
    print("Sub-Total= Rp. ", a)
    jenis1 = ("Kemeja")
elif nomor == 2:
    a = jumlah1*65000
    print("Sub-Total= Rp. ", a)
    jenis1 = ("Kaos")
elif nomor == 3:
    a = jumlah1*200000
    print("Sub-Total= Rp. ", a)
    jenis1 = ("Jaket")
elif nomor == 4:
    a = jumlah1*167000
    print("Sub-Total= Rp. ", a)
    jenis1 = ("Baju Muslim")
 
 
def pilihan(i):
 
    switcher = {
        1: '----celana panjang = Rp.150.000----',
        2: '----Celana Pendek = Rp.85.000----',
        3: '----Jeans = Rp.325.000----',
        4: '----Sarung = Rp.100.000----',
    }
    return switcher.get(i, "Masukkan Pilihan Yang Benar!")
 
 
print("\nProduk Celana")
print("1. Celana Panjang")
print("2. Celana Pendek")
print("3. Jeans")
print("4. Sarung")
nomor = int(input("Masukkan Pilihan: "))
c = pilihan(nomor)
print(c)
jumlah2 = int(input("Banyak unit yang dibeli: "))
if nomor == 1:
    b = jumlah2*150000
    print("Sub-Total= Rp. ", b)
    jenis2 = ("Celana Panjang")
elif nomor == 2:
    b = jumlah2*85000
    print("Sub-Total= Rp. ", b)
    jenis2 = ("Celana Pendek")
elif nomor == 3:
    b = jumlah2*325000
    print("Sub-Total= Rp. ", b)
    jenis2 = ("Jeans")
elif nomor == 4:
    b = jumlah2*100000
    print("Sub-Total= Rp. ", b)
    jenis2 = ("Sarung")
print("total Belanja= Rp.", a+b)
uang = int(input("\nUang Tunai: Rp."))
akhir = int(uang-(a+b))
print("|================================|")
print("|========== S T R U K ===========|")
print("|================================|")
print("|== Nama :", nama,)
print("|== Tanggal :", tgl,)
print("|== Beli :", jumlah1, jenis1,)
print("|==       ", jumlah2, jenis2,)
print("|== Tagihan :Rp.", a+b,)
print("|== Bayar :Rp.", uang,)
print("|== Kembalian :Rp.", akhir,)
print("|==========TERIMAKASIH===========|")
print("|=telah berbelanja di toko kami= |")
print("|================================|")