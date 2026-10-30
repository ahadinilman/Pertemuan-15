import os


def baca_data_nilai(filepath):
  """Membaca data nilai dari file teks eksternal."""
  data_nilai = []
  if not os.path.exists(filepath):
    raise FileNotFoundError(f"File {filepath} tidak ditemukan.")

  with open(filepath, "r", encoding="utf-8") as file:
    for baris in file:
      baris_bersih = baris.strip()
      if baris_bersih:
        try:
          nilai = float(baris_bersih)
          if 0 <= nilai <= 100:
            data_nilai.append(nilai)
        except ValueError:
          pass
  return data_nilai