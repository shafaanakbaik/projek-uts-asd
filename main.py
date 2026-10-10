import sys

sys.dont_write_bytecode = True

from array_data import PengelolaArray
from linked_list import LinkedListKatalog

def jalankanProgram():
    pengelolaArray = PengelolaArray()
    linkedListKatalog = LinkedListKatalog()

    for item in pengelolaArray.daftarKatalog:
        linkedListKatalog.tambahProduk(
            item["kodeProduk"], 
            item["namaProduk"], 
            item["kategoriProduk"], 
            item["hargaProduk"], 
            item["stokProduk"]
        )

    while True:
        print("\n==============================================")
        print("       APLIKASI KATALOG PRODUK KECANTIKAN")
        print("==============================================")
        print("1. Tampilkan Katalog (Array)")
        print("2. Tampilkan Katalog (Linked List)")
        print("3. Cari Produk")
        print("4. Tambah Produk Baru")
        print("5. Ubah Data Produk")
        print("6. Hapus Produk")
        print("7. Keluar Program")
        
        pilihanMenu = input("Silakan masukkan pilihan menu (1-7): ")

        if pilihanMenu == "1":
            pengelolaArray.tampilkanArray()

        elif pilihanMenu == "2":
            linkedListKatalog.tampilkanProduk()

        elif pilihanMenu == "3":
            print("\n--- CARI PRODUK ---")
            kataKunci = input("Masukkan nama atau kode produk yang dicari: ")
            linkedListKatalog.cariProduk(kataKunci)

        elif pilihanMenu == "4":
            print("\n--- TAMBAH PRODUK BARU ---")
            kode = input("Masukkan Kode Produk: ")
            nama = input("Masukkan Nama Produk: ")
            kategori = input("Masukkan Kategori: ")
            try:
                harga = int(input("Masukkan Harga Produk: "))
                stok = int(input("Masukkan Stok Produk: "))
            except ValueError:
                print("Kesalahan: Harga dan Stok harus berupa angka.")
                continue

            pengelolaArray.tambahKeArray(kode, nama, kategori, harga, stok)
            linkedListKatalog.tambahProduk(kode, nama, kategori, harga, stok)

        elif pilihanMenu == "5":
            print("\n--- UBAH DATA PRODUK ---")
            print("Tips: Jika belum tahu kode produk, gunakan Menu 3 (Cari Produk) terlebih dahulu.")
            kodeCari = input("Masukkan Kode Produk yang ingin diubah: ")
            namaBaru = input("Nama Produk baru: ")
            kategoriBaru = input("Kategori baru: ")
            try:
                hargaBaru = int(input("Harga baru: "))
                stokBaru = int(input("Stok baru: "))
            except ValueError:
                print("Kesalahan: Harga dan Stok harus berupa angka.")
                continue

            pengelolaArray.ubahArray(kodeCari, namaBaru, kategoriBaru, hargaBaru, stokBaru)
            linkedListKatalog.ubahData(kodeCari, namaBaru, kategoriBaru, hargaBaru, stokBaru)

        elif pilihanMenu == "6":
            print("\n--- HAPUS PRODUK ---")
            print("Tips: Jika belum tahu kode produk, gunakan Menu 3 (Cari Produk) terlebih dahulu.")
            kodeCari = input("Masukkan Kode Produk yang ingin dihapus: ")
            
            pengelolaArray.hapusArray(kodeCari)
            linkedListKatalog.hapusData(kodeCari)

        elif pilihanMenu == "7":
            print("\nTerima kasih telah menggunakan aplikasi katalog produk kecantikan.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka antara 1 sampai 7.")

if __name__ == "__main__":
    jalankanProgram()