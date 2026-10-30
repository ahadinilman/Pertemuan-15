# Proposal Proyek: Program Rekap dan Analisis Nilai Matematika Kelas

## 1. Judul Proyek
Program Rekap dan Analisis Nilai Matematika Kelas

## 2. Latar Belakang
Guru matematika memerlukan program sederhana yang dapat membaca data nilai, memvalidasi isi, menghitung statistik, menentukan status ketuntasan, dan menyimpan laporan.

## 3. Pengguna dan Tujuan
- Pengguna: Guru matematika.
- Tujuan: Memperoleh statistik kelas dan status ketuntasan secara otomatis berdasarkan data nilai.

## 4. Ruang Lingkup
- Fitur Wajib: Membaca file nilai, memvalidasi nilai 0-100, menghitung rata-rata, minimum, maksimum, menghitung jumlah tuntas/belum tuntas berdasarkan KKM, dan menyimpan laporan ke file teks.
- Batasan Proyek: Program berbasis konsol/terminal Python tanpa antarmuka grafis.

## 5. Kebutuhan (Requirements)
- Kebutuhan Fungsional: Program membaca file, memvalidasi data, menghitung statistik, dan menyimpan laporan.
- Kebutuhan Nonfungsional: Mudah dijalankan dari terminal VS Code dan pesan kesalahan mudah dipahami.

## 6. Input, Proses, dan Output (IPO)
- Input: File teks berisi data nama dan nilai siswa.
- Proses: Membaca file, validasi data, menghitung rata-rata dan statistik kelas, serta klasifikasi ketuntasan.
- Output: Informasi statistik kelas dan file laporan.

## 7. Algoritma dan Pseudocode
MULAI
baca data dari file
jika file tidak ditemukan:
    tampilkan pesan error
    SELESAI
untuk setiap baris data:
    validasi format dan nilai
    simpan data valid
hitung statistik
tentukan status ketuntasan
tampilkan ringkasan
simpan laporan
SELESAI

## 8. Struktur Program dan Modularisasi
- `main.py`: Mengatur alur utama program.
- `src/input_data.py`: Membaca file data.
- `src/analisis.py`: Validasi nilai, hitung statistik, dan status kelulusan.

## 9. Struktur Data
Menggunakan **List** untuk urutan nilai dan **Dictionary** untuk ringkasan statistik.

## 10. Test Case
- TC01 (Normal): Nilai 70, 80, 90 -> Rata-rata 80.
- TC02 (Batas): Nilai 0 -> Diterima sebagai nilai valid.
- TC03 (Batas): Nilai 100 -> Diterima sebagai nilai valid.
- TC04 (Invalid): Nilai 105 -> Ditolak dengan pesan validasi.
- TC05 (Invalid): File tidak ada -> FileNotFoundError ditangani.

## 11. Pembagian Tugas
- Koordinator: Menjaga ruang lingkup dan integrasi.
- Programmer I/O: Mengelola pembacaan file (`input_data.py`).
- Programmer Logika: Mengelola fungsi statistik (`analisis.py`).
- Tester / QA: Menyusun dan menjalankan test case.
- Dokumentasi: Menyusun README.md.

## 12. Jadwal (Milestone)
- Pertemuan 14: Proposal, struktur repositori, pseudocode, dan test case.
- Pertemuan 15: Implementasi, testing, debugging, dan dokumentasi.
- Pertemuan 16: Presentasi dan evaluasi akhir.

## 13. Repositori GitHub
URL: https://github.com/ahadinilman/Pertemuan-14.git