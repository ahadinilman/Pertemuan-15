BATAS_LULUS = 60


def validasi_nilai(nilai):
  """Memeriksa apakah nilai berada pada rentang 0 sampai 100."""
  try:
    val = float(nilai)
    return 0 <= val <= 100
  except ValueError:
    return False


def hitung_rata_rata(data):
  """Mengembalikan rata-rata dari list numerik.

  Mengembalikan 0 jika data kosong.
  """
  if not data:
    return 0
  return sum(data) / len(data)


def status_lulus(nilai, batas=BATAS_LULUS):
  """Menentukan apakah nilai memenuhi batas KKM."""
  return nilai >= batas


def ringkasan_statistik(data):
  """Menghasilkan dictionary berisi ringkasan statistik kelas."""
  if not data:
    return {
        "jumlah": 0,
        "rata_rata": 0,
        "minimum": None,
        "maksimum": None,
        "lulus": 0,
    }

  lulus_count = sum(1 for n in data if status_lulus(n))
  return {
      "jumlah": len(data),
      "rata_rata": hitung_rata_rata(data),
      "minimum": min(data),
      "maksimum": max(data),
      "lulus": lulus_count,
  }