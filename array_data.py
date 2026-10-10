class PengelolaArray:
    def __init__(self):
        self.daftarKatalog = [
            {"kodeProduk": "MK01", "namaProduk": "Matte Lipstick Ruby", "kategoriProduk": "Makeup", "hargaProduk": 150000, "stokProduk": 25},
            {"kodeProduk": "MK02", "namaProduk": "Liquid Foundation Ivory", "kategoriProduk": "Makeup", "hargaProduk": 220000, "stokProduk": 15},
            {"kodeProduk": "MK03", "namaProduk": "Waterproof Mascara Black", "kategoriProduk": "Makeup", "hargaProduk": 120000, "stokProduk": 30},
            {"kodeProduk": "MK04", "namaProduk": "Eyebrow Pencil Dark Brown", "kategoriProduk": "Makeup", "hargaProduk": 85000, "stokProduk": 40},
            {"kodeProduk": "MK05", "namaProduk": "Blush On Peach Glow", "kategoriProduk": "Makeup", "hargaProduk": 110000, "stokProduk": 20},
            {"kodeProduk": "MK06", "namaProduk": "Loose Powder Translucent", "kategoriProduk": "Makeup", "hargaProduk": 95000, "stokProduk": 25},
            {"kodeProduk": "MK07", "namaProduk": "Eyeliner Pen Waterproof", "kategoriProduk": "Makeup", "hargaProduk": 105000, "stokProduk": 35},
            {"kodeProduk": "MK08", "namaProduk": "Eyeshadow Palette Nude", "kategoriProduk": "Makeup", "hargaProduk": 180000, "stokProduk": 18},
            {"kodeProduk": "MK09", "namaProduk": "Highlighter Glow Beam", "kategoriProduk": "Makeup", "hargaProduk": 130000, "stokProduk": 22},
            {"kodeProduk": "MK10", "namaProduk": "Tinted Lip Balm Cherry", "kategoriProduk": "Makeup", "hargaProduk": 75000, "stokProduk": 45},

            {"kodeProduk": "SK01", "namaProduk": "Hydrating Toner 150ml", "kategoriProduk": "Skincare", "hargaProduk": 180000, "stokProduk": 18},
            {"kodeProduk": "SK02", "namaProduk": "Brightening Serum 30ml", "kategoriProduk": "Skincare", "hargaProduk": 250000, "stokProduk": 12},
            {"kodeProduk": "SK03", "namaProduk": "Acne Spot Gel 15g", "kategoriProduk": "Skincare", "hargaProduk": 95000, "stokProduk": 35},
            {"kodeProduk": "SK04", "namaProduk": "Sunscreen SPF 50 PA+", "kategoriProduk": "Skincare", "hargaProduk": 135000, "stokProduk": 28},
            {"kodeProduk": "SK05", "namaProduk": "Gentle Facial Wash", "kategoriProduk": "Skincare", "hargaProduk": 90000, "stokProduk": 50},
            {"kodeProduk": "SK06", "namaProduk": "Exfoliating Toner AHA/BHA", "kategoriProduk": "Skincare", "hargaProduk": 195000, "stokProduk": 15},
            {"kodeProduk": "SK07", "namaProduk": "Sheet Mask Aloe Vera", "kategoriProduk": "Skincare", "hargaProduk": 20000, "stokProduk": 60},
            {"kodeProduk": "SK08", "namaProduk": "Clay Mask Green Tea", "kategoriProduk": "Skincare", "hargaProduk": 115000, "stokProduk": 25},
            {"kodeProduk": "SK09", "namaProduk": "Eye Cream Anti Aging", "kategoriProduk": "Skincare", "hargaProduk": 210000, "stokProduk": 10},
            {"kodeProduk": "SK10", "namaProduk": "Sleeping Mask Water Bomb", "kategoriProduk": "Skincare", "hargaProduk": 165000, "stokProduk": 20},

            {"kodeProduk": "BK01", "namaProduk": "Body Lotion Vanilla Musk", "kategoriProduk": "Bodycare", "hargaProduk": 125000, "stokProduk": 22},
            {"kodeProduk": "BK02", "namaProduk": "Exfoliating Body Scrub", "kategoriProduk": "Bodycare", "hargaProduk": 140000, "stokProduk": 15},
            {"kodeProduk": "BK03", "namaProduk": "Nourishing Shower Gel", "kategoriProduk": "Bodycare", "hargaProduk": 105000, "stokProduk": 30},
            {"kodeProduk": "BK04", "namaProduk": "Hand Cream Shea Butter", "kategoriProduk": "Bodycare", "hargaProduk": 65000, "stokProduk": 45},
            {"kodeProduk": "BK05", "namaProduk": "Relaxing Massage Oil", "kategoriProduk": "Bodycare", "hargaProduk": 175000, "stokProduk": 10},
            {"kodeProduk": "BK06", "namaProduk": "Whitening Body Serum", "kategoriProduk": "Bodycare", "hargaProduk": 155000, "stokProduk": 25},
            {"kodeProduk": "BK07", "namaProduk": "Underarm Scrub Cream", "kategoriProduk": "Bodycare", "hargaProduk": 85000, "stokProduk": 30},
            {"kodeProduk": "BK08", "namaProduk": "Foot Care Cream Mint", "kategoriProduk": "Bodycare", "hargaProduk": 55000, "stokProduk": 40},
            {"kodeProduk": "BK09", "namaProduk": "Deodorant Spray Fresh", "kategoriProduk": "Bodycare", "hargaProduk": 45000, "stokProduk": 50},
            {"kodeProduk": "BK10", "namaProduk": "Body Mist Rose Water", "kategoriProduk": "Bodycare", "hargaProduk": 95000, "stokProduk": 35},

            {"kodeProduk": "HK01", "namaProduk": "Keratin Smooth Shampoo", "kategoriProduk": "Haircare", "hargaProduk": 160000, "stokProduk": 25},
            {"kodeProduk": "HK02", "namaProduk": "Deep Repair Hair Mask", "kategoriProduk": "Haircare", "hargaProduk": 190000, "stokProduk": 14},
            {"kodeProduk": "HK03", "namaProduk": "Argan Hair Serum 50ml", "kategoriProduk": "Haircare", "hargaProduk": 210000, "stokProduk": 19},
            {"kodeProduk": "HK04", "namaProduk": "Scalp Tonic Anti Dandruff", "kategoriProduk": "Haircare", "hargaProduk": 145000, "stokProduk": 22},
            {"kodeProduk": "HK05", "namaProduk": "Hair Vitamin Spray", "kategoriProduk": "Haircare", "hargaProduk": 75000, "stokProduk": 38},
            {"kodeProduk": "HK06", "namaProduk": "Volumizing Conditioner", "kategoriProduk": "Haircare", "hargaProduk": 150000, "stokProduk": 20},
            {"kodeProduk": "HK07", "namaProduk": "Hair Scalp Scrub", "kategoriProduk": "Haircare", "hargaProduk": 125000, "stokProduk": 18},
            {"kodeProduk": "HK08", "namaProduk": "Heat Protectant Spray", "kategoriProduk": "Haircare", "hargaProduk": 135000, "stokProduk": 25},
            {"kodeProduk": "HK09", "namaProduk": "Dry Shampoo Refresh", "kategoriProduk": "Haircare", "hargaProduk": 110000, "stokProduk": 30},
            {"kodeProduk": "HK10", "namaProduk": "Hair Growth Tonic", "kategoriProduk": "Haircare", "hargaProduk": 225000, "stokProduk": 12}
        ]

    def tampilkanArray(self):
        print("\n--- DAFTAR KATALOG PRODUK (MENGGUNAKAN ARRAY/LIST) ---")
        print(f"{'No':<3} | {'Kode':<8} | {'Nama Produk':<30} | {'Kategori':<12} | {'Harga':<10} | {'Stok':<5}")
        print("-" * 79)
        for indeks, produk in enumerate(self.daftarKatalog, start=1):
            print(f"{indeks:<3} | {produk['kodeProduk']:<8} | {produk['namaProduk']:<30} | {produk['kategoriProduk']:<12} | Rp{produk['hargaProduk']:<8} | {produk['stokProduk']:<5}")
        print("-" * 79)

    def tambahKeArray(self, kodeProduk, namaProduk, kategoriProduk, hargaProduk, stokProduk):
        produkBaru = {
            "kodeProduk": kodeProduk,
            "namaProduk": namaProduk,
            "kategoriProduk": kategoriProduk,
            "hargaProduk": hargaProduk,
            "stokProduk": stokProduk
        }
        self.daftarKatalog.append(produkBaru)
        print(f"Informasi: Produk '{namaProduk}' berhasil ditambahkan ke Array.")

    def ubahArray(self, kodeProdukCari, namaBaru, kategoriBaru, hargaBaru, stokBaru):
        for produk in self.daftarKatalog:
            if produk["kodeProduk"] == kodeProdukCari:
                produk["namaProduk"] = namaBaru
                produk["kategoriProduk"] = kategoriBaru
                produk["hargaProduk"] = hargaBaru
                produk["stokProduk"] = stokBaru
                print(f"Informasi: Data produk {kodeProdukCari} dalam Array berhasil diperbarui.")
                return True
        print(f"Peringatan: Produk dengan kode {kodeProdukCari} tidak ditemukan di Array.")
        return False

    def hapusArray(self, kodeProdukCari):
        for produk in self.daftarKatalog:
            if produk["kodeProduk"] == kodeProdukCari:
                self.daftarKatalog.remove(produk)
                print(f"Informasi: Produk {kodeProdukCari} berhasil dihapus dari Array.")
                return True
        print(f"Peringatan: Produk dengan kode {kodeProdukCari} tidak ditemukan di Array.")
        return False