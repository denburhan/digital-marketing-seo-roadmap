# 05. Otomasi dan Pengukuran

**Level:** Expert | **Waktu baca:** 18 menit | **Prasyarat:** 02-intermediate/07

## Tujuan
Mengotomasi pengumpulan data dan pemeriksaan rutin supaya keputusan berbasis data konsisten.

## Yang layak diotomasi
- Ekspor harian atau mingguan dari Search Console API ke penyimpanan sendiri.
- Pemeriksaan status HTTP halaman penting dan sitemap.
- Pemeriksaan robots.txt dan noindex tidak sengaja setelah deployment.
- Laporan mingguan ringkas.

## Yang jangan diotomasi tanpa kendali manusia
- Publikasi konten massal tanpa review.
- Perubahan pada iklan aktif.
- Penghapusan atau redirect massal.

## Praktik aman
- Simpan kredensial di variabel lingkungan atau secret manager. Jangan menaruhnya di repo atau dokumen.
- Jalankan skrip dalam mode baca dulu (dry run).
- Catat hasil dan galat.
- Verifikasi hitungan dengan kode, bukan estimasi manual.

## Contoh di repo
- `scripts/cluster_queries.py`: pengelompokan query dari CSV.
- `scripts/check_urls.py`: cek status HTTP, redirect, dan tag noindex dari daftar URL.

## Latihan
1. Jalankan `check_urls.py` pada 20 URL penting dan simpan hasilnya.
2. Rancang jadwal otomatis mingguan untuk skrip itu.

## Cek pemahaman
- Kenapa dry run penting sebelum otomasi menyentuh produksi?
- Apa yang tidak boleh masuk ke repo kode?
