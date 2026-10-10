======================================================================
               README - PROJECT UTS ALGORITMA & STRUKTUR DATA
======================================================================

1. IDENTITAS MAHASISWA
   - Nama  : Shafa Fadilah Wibisono
   - NPM   : G1F026001
   - Kelas : Sistem Informasi A

2. JUDUL PROJECT
   - Implementasi Struktur Data Array dan Linked List pada Sistem Katalog Produk Kecantikan

3. DESKRIPSI SINGKAT PROJECT
   Program ini dikembangkan untuk memenuhi Ujian Tengah Semester (UTS) mata kuliah Algoritma dan Struktur Data. Aplikasi berbasis teks ini dirancang untuk mengelola katalog produk kecantikan (Makeup, Skincare, Bodycare, Haircare) dengan menerapkan dua struktur data utama, yaitu Array/List Python dan Linked List manual menggunakan Node.

4. BAHASA PEMROGRAMAN
   - Python

5. STRUKTUR DIREKTORI DAN BERKAS
   project_uts/
   ├── main.py              -> Berisi logika antarmuka menu utama dan alur program
   ├── array_data.py        -> Modul pengelolaan data menggunakan Array/List
   ├── linked_list.py       -> Modul implementasi Linked List
   ├── node.py              -> Modul definisi struktur class Node
   ├── data/
   │   └── data.csv         -> Berkas penyimpanan data eksternal/arsip pendukung
   └── README.txt           -> Berkas informasi dan petunjuk penggunaan

6. CARA MENJALANKAN PROGRAM
   - Buka aplikasi VS Code dan buka folder project_uts.
   - Buka terminal baru (Terminal > New Terminal).
   - Ketik perintah: python main.py

7. PENJELASAN SINGKAT STRUKTUR DATA
   - Array/List: Struktur data linier dengan indeks berurutan. Unggul dalam akses data langsung (*random access*).
   - Linked List: Struktur data dinamis berbasis Node yang saling terhubung melalui referensi (*pointer*), sangat efisien untuk operasi penyisipan dan penghapusan data.