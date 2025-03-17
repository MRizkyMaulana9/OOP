# Kelas Dasar Produk
class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok
    
    def tampilkanInfo(self):
        print(f"Nama: {self.nama}")
        print(f"Harga: Rp {self.harga}")
        print(f"Stok: {self.stok} unit")

# Kelas Buku (Turunan dari Produk)
class Buku(Produk):
    def __init__(self, nama, harga, stok, penulis, penerbit):
        super().__init__(nama, harga, stok)
        self.penulis = penulis
        self.penerbit = penerbit
    
    def tampilkanInfo(self):
        super().tampilkanInfo()
        print(f"Penulis: {self.penulis}")
        print(f"Penerbit: {self.penerbit}")

# Kelas Elektronik (Turunan dari Produk)
class Elektronik(Produk):
    def __init__(self, nama, harga, stok, merek, garansi):
        super().__init__(nama, harga, stok)
        self.merek = merek
        self.garansi = garansi
    
    def tampilkanInfo(self):
        super().tampilkanInfo()
        print(f"Merek: {self.merek}")
        print(f"Garansi: {self.garansi} tahun")

# Kelas Pakaian (Turunan dari Produk)
class Pakaian(Produk):
    def __init__(self, nama, harga, stok, ukuran, warna):
        super().__init__(nama, harga, stok)
        self.ukuran = ukuran
        self.warna = warna
    
    def tampilkanInfo(self):
        super().tampilkanInfo()
        print(f"Ukuran: {self.ukuran}")
        print(f"Warna: {self.warna}")

# Kelas Inventaris
class Inventaris:
    def __init__(self):
        self.produk_list = []
    
    def tambahProduk(self, produk):
        self.produk_list.append(produk)
        print(f"{produk.nama} berhasil ditambahkan ke inventaris.")
    
    def hapusProduk(self, nama):
        for produk in self.produk_list:
            if produk.nama.lower() == nama.lower():
                self.produk_list.remove(produk)
                print(f"{nama} berhasil dihapus dari inventaris.")
                return
        print(f"Produk {nama} tidak ditemukan.")
    
    def cariProduk(self, nama):
        for produk in self.produk_list:
            if produk.nama.lower() == nama.lower():
                produk.tampilkanInfo()
                return
        print(f"Produk {nama} tidak ditemukan.")
    
    def tampilkanSemuaProduk(self):
        if not self.produk_list:
            print("Inventaris kosong.")
            return
        print("\nDaftar Produk di Inventaris:")
        for produk in self.produk_list:
            produk.tampilkanInfo()
            print("-")

# Antarmuka Pengguna
inventaris = Inventaris()
while True:
    print("\n=== Sistem Manajemen Inventaris ===")
    print("1. Tambah Produk")
    print("2. Hapus Produk")
    print("3. Cari Produk")
    print("4. Tampilkan Semua Produk")
    print("5. Keluar")
    
    pilihan = input("Pilih menu: ")
    
    if pilihan == "1":
        jenis = input("Jenis produk (Buku/Elektronik/Pakaian): ").lower()
        nama = input("Nama Produk: ")
        harga = int(input("Harga: "))
        stok = int(input("Stok: "))
        
        if jenis == "buku":
            penulis = input("Penulis: ")
            penerbit = input("Penerbit: ")
            produk = Buku(nama, harga, stok, penulis, penerbit)
        elif jenis == "elektronik":
            merek = input("Merek: ")
            garansi = int(input("Garansi (tahun): "))
            produk = Elektronik(nama, harga, stok, merek, garansi)
        elif jenis == "pakaian":
            ukuran = input("Ukuran: ")
            warna = input("Warna: ")
            produk = Pakaian(nama, harga, stok, ukuran, warna)
        else:
            print("Jenis produk tidak valid.")
            continue
        
        inventaris.tambahProduk(produk)
    
    elif pilihan == "2":
        nama = input("Nama produk yang akan dihapus: ")
        inventaris.hapusProduk(nama)
    
    elif pilihan == "3":
        nama = input("Nama produk yang dicari: ")
        inventaris.cariProduk(nama)
    
    elif pilihan == "4":
        inventaris.tampilkanSemuaProduk()
    
    elif pilihan == "5":
        print("Keluar dari sistem.")
        break
    
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
