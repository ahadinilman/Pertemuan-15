# Dokumentasi Test Case Proyek

| ID | Kategori | Input / Kondisi | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC01 | Normal | 70, 80, 90 | Rata-rata terhitung 80.0 | Rata-rata terhitung 80.0 | PASS |
| TC02 | Batas | Nilai 0 | Diterima sebagai nilai valid | Diterima sebagai nilai valid | PASS |
| TC03 | Batas | Nilai 100 | Diterima sebagai nilai valid | Diterima sebagai nilai valid | PASS |
| TC04 | Invalid | Nilai 105 | Ditolak dengan pesan validasi | Diabaikan / Ditolak validasi | PASS |
| TC05 | Invalid | File tidak ada | FileNotFoundError ditangani | Ditangani dengan pesan error | PASS |