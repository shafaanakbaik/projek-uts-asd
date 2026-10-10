import time
import sys
from contextlib import redirect_stdout
from io import StringIO

sys.dont_write_bytecode = True

from array_data import PengelolaArray
from linked_list import LinkedListKatalog


JUMLAH_DATA = 10_000
array_katalog = PengelolaArray()
array_katalog.daftarKatalog.clear()
ll_katalog = LinkedListKatalog()

start_time = time.perf_counter()
with redirect_stdout(StringIO()):
    for i in range(JUMLAH_DATA):
        array_katalog.tambahKeArray(
            f"PRD{i}", f"Produk {i}", "Skincare", 50_000, 10
        )
time_array_insert = time.perf_counter() - start_time

start_time = time.perf_counter()
for i in range(JUMLAH_DATA):
    ll_katalog.tambahProduk(
        f"PRD{i}", f"Produk {i}", "Skincare", 50_000, 10
    )
time_ll_insert = time.perf_counter() - start_time

kode_dicari = f"PRD{JUMLAH_DATA - 1}"


def cari_array(kode_produk):
    hasil = []
    kata_kunci = kode_produk.lower()
    for produk in array_katalog.daftarKatalog:
        if (
            kata_kunci in produk["namaProduk"].lower()
            or kata_kunci in produk["kodeProduk"].lower()
            or kata_kunci in produk["kategoriProduk"].lower()
        ):
            hasil.append(produk)
    return hasil


def cari_linked_list(kode_produk):
    current = ll_katalog.head
    hasil = []
    kata_kunci = kode_produk.lower()
    while current is not None:
        if (
            kata_kunci in current.namaProduk.lower()
            or kata_kunci in current.kodeProduk.lower()
            or kata_kunci in current.kategoriProduk.lower()
        ):
            hasil.append(current)
        current = current.next
    return hasil


start_time = time.perf_counter()
hasil_array = cari_array(kode_dicari)
time_array_search = time.perf_counter() - start_time

start_time = time.perf_counter()
hasil_ll = cari_linked_list(kode_dicari)
time_ll_search = time.perf_counter() - start_time

if len(array_katalog.daftarKatalog) != JUMLAH_DATA:
    raise RuntimeError("Jumlah data Array tidak sesuai dengan jumlah pengujian.")
if len(hasil_array) != 1 or len(hasil_ll) != 1:
    raise RuntimeError(f"Data {kode_dicari} tidak ditemukan pada kedua struktur.")

jumlah_data_format = f"{JUMLAH_DATA:,}".replace(",", ".")
print(f"=== HASIL PENGUJIAN PERFORMA ({jumlah_data_format} DATA) ===")
print(f"Waktu Insert Array       : {time_array_insert:.6f} detik")
print(f"Waktu Insert Linked List : {time_ll_insert:.6f} detik")
print()
print(f"Waktu Cari Array         : {time_array_search:.6f} detik")
print(f"Waktu Cari Linked List   : {time_ll_search:.6f} detik")
