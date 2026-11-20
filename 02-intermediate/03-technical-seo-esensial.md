# 03. Technical SEO Esensial

**Level:** Intermediate | **Waktu baca:** 20 menit | **Prasyarat:** 01-basic/03

## Tujuan
Memastikan fondasi teknis tidak menghalangi crawl, indexing, dan pengalaman pengguna.

## Daftar periksa inti
1. **HTTPS** di seluruh situs, tanpa mixed content.
2. **Satu versi URL.** Pilih www atau non-www, dengan atau tanpa trailing slash, lalu 301 sisanya.
3. **Status kode benar.** Halaman hidup 200, pindah permanen 301, hilang 404 atau 410. Hindari soft 404 (halaman kosong tapi 200).
4. **robots.txt** tidak memblokir CSS, JS, dan konten penting.
5. **Sitemap** hanya berisi URL kanonik yang bisa diindeks dan statusnya 200.
6. **Canonical** konsisten, menunjuk ke versi utama.
7. **Mobile friendly.** Konten dan tautan sama dengan versi desktop.
8. **Data terstruktur** valid, sesuai isi halaman.
9. **Halaman error** kustom yang membantu pengguna.

## Core Web Vitals
Ambang "baik" menurut web.dev: LCP 2.5 detik atau kurang, INP 200 milidetik atau kurang, CLS 0.1 atau kurang, dinilai pada persentil ke-75 data lapangan.
- **LCP:** biasanya dipengaruhi gambar atau teks terbesar di layar pertama. Kompres, gunakan format modern, jangan lazy-load gambar utama.
- **INP:** responsivitas. Kurangi JavaScript berat di main thread.
- **CLS:** pergeseran layout. Tentukan dimensi gambar dan iklan.

## JavaScript SEO
Kalau konten dirender di sisi klien, pastikan konten penting muncul di HTML hasil render dan bisa dilihat lewat URL Inspection. Rendering di server atau statis lebih aman untuk konten yang ingin diindeks.

## Redirect
- 301 untuk perpindahan permanen. Hindari rantai redirect.
- Saat migrasi, buat pemetaan URL lama ke baru satu per satu dan uji sebelum peluncuran.

## Latihan
1. Audit satu situs dengan daftar di atas. Beri status lulus atau gagal.
2. Ambil 3 halaman, ukur Core Web Vitals dari data lapangan, dan catat sumber datanya.

## Cek pemahaman
- Apa beda soft 404 dan 404 sungguhan?
- Kenapa sitemap tidak boleh berisi URL yang diredirect atau noindex?
