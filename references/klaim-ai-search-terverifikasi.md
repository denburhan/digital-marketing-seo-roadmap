# Klaim AI Search: Terverifikasi dan Tidak Terverifikasi

Diperiksa ke dokumentasi resmi pada 20 November 2026. Dokumentasi berubah, jadi cek ulang sebelum dipakai di materi berbayar atau laporan klien.

## Terverifikasi dari sumber resmi
| Klaim | Sumber | Status |
|---|---|---|
| Tidak ada optimasi teknis khusus untuk AI Overview atau AI Mode, tidak ada schema atau file khusus | Panduan optimasi generative AI, Google Search Central | Terverifikasi |
| Abaikan chunking konten, file teks AI yang tidak perlu (llms.txt), dan mention tidak autentik | Panduan yang sama, bagian mythbusting | Terverifikasi |
| llms.txt tidak berpengaruh positif atau negatif pada peringkat Google | Catatan changelog 15 Juni 2026 | Terverifikasi |
| Konten non-komoditas jadi fokus panduan | Panduan optimasi generative AI | Terverifikasi |
| Query fan-out: model membuat beberapa query terkait secara bersamaan | Panduan yang sama | Terverifikasi |
| Membuat konten terpisah untuk tiap variasi query demi memanipulasi peringkat melanggar kebijakan scaled content abuse | Panduan yang sama | Terverifikasi |
| Kebijakan spam berlaku juga untuk respons generative AI | Changelog 15 Mei 2026 | Terverifikasi |
| Fitur FAQ rich result tidak tampil lagi di hasil Google mulai 7 Mei 2026 | Changelog 8 Mei 2026, pemberitahuan deprecation | Terverifikasi |
| Batas satu sitemap: 50MB tidak terkompresi atau 50.000 URL | Dokumentasi build sitemap | Terverifikasi |
| Ambang Core Web Vitals baik: LCP 2.5 detik, INP 200 ms, CLS 0.1, persentil ke-75 | web.dev/articles/vitals | Terverifikasi |

## Diteruskan dari materi internal tanpa verifikasi ulang di sesi ini
Ditandai agar pembaca tahu tingkat keyakinannya. Cek ulang sebelum dipakai sebagai dasar keputusan.
- Struktur konten (paragraf pendek, heading jelas) sebagai bantuan pemahaman: konsisten dengan panduan umum, tapi bukan "faktor ranking" yang dinyatakan eksplisit.
- Discover: otoritas per topik, prioritas konten lokal, kurangi clickbait. Berasal dari pengumuman Discover Core Update yang tercatat di catatan internal, belum diperiksa ulang di sesi ini.
- SpamBrain menetralkan tautan manipulatif tanpa pemberitahuan. Pernyataan umum Google tentang SpamBrain ada. Gejala "backlink naik di Ahrefs tapi klik stagnan" adalah heuristik dari praktik, bukan pernyataan resmi.

## Klaim yang tidak punya dasar dan jangan dipakai
- Skor "AI Citation Probability" atau prediksi peluang dikutip AI.
- Angka persen kenaikan sitasi atau trafik dari FAQ, pillar page, atau llms.txt tanpa sumber.
- Menyuruh AI menulis statistik contoh sebagai "bukti" di halaman produksi.
- EXIF, IPTC, atau geotag gambar sebagai faktor peringkat.
- Keyword density dan "LSI keyword" sebagai faktor peringkat.
- AggregateRating pada Organization tanpa ulasan nyata.
- Schema SearchAction untuk sitelinks search box (sudah tidak dipakai).

## Aturan pakai
1. Cek klaim berbentuk angka dan prediksi ke sumber resmi sebelum dipakai.
2. Tidak bisa diverifikasi berarti tulis "klaim penulis".
3. Kalau dua materi bertentangan, pilih yang sesuai dokumentasi resmi dan catat pertentangannya.
4. Jangan membawa angka karangan ke deliverable berikutnya karena angka itu ada di materi asal.
