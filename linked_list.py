from node import NodeProduk

class LinkedListKatalog:
    def __init__(self):
        self.head = None

    def tambahProduk(self, kodeProduk, namaProduk, kategoriProduk, hargaProduk, stokProduk):
        nodeBaru = NodeProduk(kodeProduk, namaProduk, kategoriProduk, hargaProduk, stokProduk)
        if self.head is None:
            self.head = nodeBaru
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = nodeBaru

    def tampilkanProduk(self):
        if self.head is None:
            print("\n[Linked List] Informasi: Katalog produk saat ini kosong.")
            return
        
        print("\n--- DAFTAR KATALOG PRODUK KECANTIKAN (LINKED LIST) ---")
        print(f"{'Kode':<8} | {'Nama Produk':<30} | {'Kategori':<12} | {'Harga':<10} | {'Stok':<5}")
        print("-" * 75)
        current = self.head
        while current is not None:
            print(f"{current.kodeProduk:<8} | {current.namaProduk:<30} | {current.kategoriProduk:<12} | Rp{current.hargaProduk:<8} | {current.stokProduk:<5}")
            current = current.next
        print("-" * 75)

    def cariProduk(self, kataKunci):
        current = self.head
        ditemukan = False
        kataKunci = kataKunci.lower()
        
        print(f"\n--- HASIL PENCARIAN TERKAIT: '{kataKunci}' ---")
        print(f"{'Kode':<8} | {'Nama Produk':<30} | {'Kategori':<12} | {'Harga':<10} | {'Stok':<5}")
        print("-" * 75)
        
        while current is not None:
            if kataKunci in current.namaProduk.lower() or kataKunci in current.kodeProduk.lower() or kataKunci in current.kategoriProduk.lower():
                print(f"{current.kodeProduk:<8} | {current.namaProduk:<30} | {current.kategoriProduk:<12} | Rp{current.hargaProduk:<8} | {current.stokProduk:<5}")
                ditemukan = True
            current = current.next
            
        print("-" * 75)
        if not ditemukan:
            print("Informasi: Tidak ada produk yang cocok dengan kata kunci tersebut.")

    def ubahData(self, kodeProdukCari, namaBaru, kategoriBaru, hargaBaru, stokBaru):
        current = self.head
        while current is not None:
            if current.kodeProduk == kodeProdukCari:
                current.namaProduk = namaBaru
                current.kategoriProduk = kategoriBaru
                current.hargaProduk = hargaBaru
                current.stokProduk = stokBaru
                print(f"Informasi: Data produk dengan kode {kodeProdukCari} berhasil diperbarui.")
                return True
            current = current.next
        print(f"Peringatan: Produk dengan kode {kodeProdukCari} tidak ditemukan.")
        return False

    def hapusData(self, kodeProdukCari):
        current = self.head
        
        if current is None:
            print("Peringatan: Katalog kosong, tidak ada data yang dapat dihapus.")
            return

        if current.kodeProduk == kodeProdukCari:
            self.head = current.next
            print(f"Informasi: Produk dengan kode {kodeProdukCari} berhasil dihapus.")
            return

        prev = None
        while current is not None and current.kodeProduk != kodeProdukCari:
            prev = current
            current = current.next

        if current is None:
            print(f"Peringatan: Produk dengan kode {kodeProdukCari} tidak ditemukan.")
            return

        prev.next = current.next
        print(f"Informasi: Produk dengan kode {kodeProdukCari} berhasil dihapus.")