class NodeProduk:
    def __init__(self, kodeProduk, namaProduk, kategoriProduk, hargaProduk, stokProduk):
        self.kodeProduk = kodeProduk
        self.namaProduk = namaProduk
        self.kategoriProduk = kategoriProduk
        self.hargaProduk = hargaProduk
        self.stokProduk = stokProduk
        self.next = None