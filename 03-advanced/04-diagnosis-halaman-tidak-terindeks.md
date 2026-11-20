# 04. Diagnosis Halaman Tidak Terindeks

**Level:** Advanced | **Waktu baca:** 18 menit | **Prasyarat:** 01-basic/03

## Tujuan
Menemukan penyebab sebuah halaman atau seluruh situs tidak muncul di indeks.

## Urutan diagnosis
1. **Cek URL Inspection.** Apakah URL dikenal Google? Terakhir di-crawl kapan? Status indeks?
2. **Cek yang menghalangi:** `noindex` (meta atau header), robots.txt, canonical menunjuk ke URL lain, redirect, status bukan 200, login wall.
3. **Cek penemuan:** apakah URL ada di sitemap dan punya tautan internal?
4. **Cek kualitas:** halaman tipis, duplikat, atau mirip massal dengan halaman lain.
5. **Cek kebijakan spam:** apakah situs memuat pola yang dilarang (scaled content abuse, link spam, cloaking, dan lainnya)?

## Status GSC yang sering membingungkan
- **Ditemukan, saat ini belum diindeks:** Google tahu URL-nya tapi belum meng-crawl. Penyebab umum: situs baru, kapasitas server, atau Google menilai prioritasnya rendah.
- **Di-crawl, saat ini belum diindeks:** Google sudah membaca tapi memutuskan belum memasukkan. Periksa kualitas dan keunikan.
- **Duplikat, Google memilih kanonik berbeda:** Google tidak setuju dengan canonical-mu. Samakan sinyal: konten, tautan internal, sitemap, canonical.

## Yang tidak membantu
- Mengirim URL berulang-ulang. Meminta indexing tidak menjamin pengindeksan.
- Menambah sitemap berisi ribuan URL tipis.
- Menganggap masalah "pasti penalti". Mayoritas kasus adalah kualitas, teknis, atau prioritas crawl.

## Manual action
Cek laporan Manual Actions di GSC. Kalau ada, ikuti instruksi di sana dan ajukan peninjauan setelah memperbaiki masalah.

## Latihan
Ambil 10 URL yang tidak terindeks. Klasifikasikan penyebabnya ke salah satu dari lima langkah diagnosis. Tulis perbaikan dan ukur ulang dalam beberapa minggu.

## Cek pemahaman
- Apa beda "Ditemukan" dan "Di-crawl" yang belum diindeks?
- Kenapa mengirim ulang URL berkali-kali tidak efektif?
