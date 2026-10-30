import os
from src.analisis import ringkasan_statistik 
from src.input_data import baca_data_nilai


def main():
  print("=== PROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA ===")
  base_dir = os.path.dirname(os.path.abspath(__file__))
  path_file = os.path.join(base_dir, "Data", "contoh_data.txt")

  try:
    nilai_siswa = baca_data_nilai(path_file)
    hasil = ringkasan_statistik(nilai_siswa)

    print(f"\nBerhasil memproses {hasil['jumlah']} data siswa.")
    print(f"Rata-rata Kelas : {hasil['rata_rata']:.2f}")
    print(f"Nilai Minimum   : {hasil['minimum']}")
    print(f"Nilai Maksimum  : {hasil['maksimum']}")
    print(f"Jumlah Tuntas   : {hasil['lulus']} siswa")

  except FileNotFoundError as e:
    print(f"Kesalahan: {e}")
  except Exception as e:
    print(f"Terjadi kesalahan tak terduga: {e}")


if __name__ == "__main__":
  main()