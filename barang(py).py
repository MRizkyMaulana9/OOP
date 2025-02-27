class Barang:
    def __init__(self, nama, kode, harga, stok):
        self.nama = nama
        self.kode = kode
        self.harga = harga
        self.stok = stok

    def tampilkanInfoBarang(self):
        print(f"Nama: {self.nama}, Kode: {self.kode}, Harga: {self.harga}, Stok: {self.stok}")

    def updateStok(self, jumlah):
        self.stok += jumlah

class Pemasok:
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat

    def tampilkanInfoPemasok(self):
        print(f"Nama: {self.nama}, Alamat: {self.alamat}")

class Penjualan:
    def __init__(self, tanggal, barang, jumlah):
        self.tanggal = tanggal
        self.barang = barang
        self.jumlah = jumlah

    def hitungTotalPenjualan(self):
        return self.barang.harga * self.jumlah

# Contoh penggunaan
barang1 = Barang("Sabun Mandi", "S001", 5000, 100)
pemasok1 = Pemasok("PT. Sejahtera", "Jakarta")
penjualan1 = Penjualan("2024-07-27", barang1, 5)

barang1.tampilkanInfoBarang()
pemasok1.tampilkanInfoPemasok()
print(f"Total Penjualan: {penjualan1.hitungTotalPenjualan()}")
barang1.updateStok(-5)
barang1.tampilkanInfoBarang()