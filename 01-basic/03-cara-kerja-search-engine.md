# 03. Cara Kerja Mesin Pencari

**Level:** Basic | **Waktu baca:** 12 menit | **Prasyarat:** modul 01

## Tujuan
Memahami tiga tahap inti (crawling, indexing, serving) agar kamu tahu di mana sebuah masalah SEO terjadi.

## Tiga tahap
1. **Crawling.** Program (Googlebot) menemukan dan mengunduh halaman lewat tautan dan sitemap.
2. **Indexing.** Isi halaman dianalisis lalu disimpan di indeks. Tidak semua halaman yang di-crawl masuk indeks.
3. **Serving.** Saat ada pencarian, sistem memilih dan mengurutkan halaman dari indeks.

Diagnosis dasar mengikuti urutan itu: halaman tidak ditemukan (masalah crawl), ditemukan tapi tidak diindeks (masalah indexing atau kualitas), terindeks tapi tidak muncul tinggi (masalah relevansi, otoritas, atau kompetisi).

## Hal yang menghalangi
- `robots.txt` yang memblokir crawling. Perhatikan: robots.txt mengatur crawling, bukan jaminan sebuah URL tidak muncul di indeks. Untuk menjaga halaman tetap keluar dari hasil pencarian, pakai `noindex` (dan biarkan halaman bisa di-crawl agar tag itu terbaca).
- `noindex` yang tidak sengaja terpasang, misalnya sisa dari masa pengembangan.
- Halaman yatim tanpa satu pun tautan internal.
- Konten tipis atau duplikat.
- Server lambat atau sering error.

## Mobile-first indexing
Google terutama memakai versi mobile sebuah halaman untuk indexing dan ranking. Konten yang hanya ada di desktop berisiko tidak terbaca. Pastikan versi mobile memuat konten dan tautan yang sama pentingnya.

## Sitemap
Sitemap membantu penemuan URL, bukan jaminan peringkat. Batas satu file sitemap: 50 MB tidak terkompresi atau 50.000 URL (sumber: dokumentasi Google Search Central tentang membangun sitemap). Kalau lebih, pecah jadi beberapa file dan daftarkan lewat sitemap index.

## Latihan
1. Buka `situsmu.com/robots.txt` dan baca isinya. Apa saja yang diblokir?
2. Di Google Search Console, jalankan URL Inspection pada satu halaman. Catat status crawl dan indeksnya.

## Cek pemahaman
- Kenapa robots.txt bukan cara yang tepat untuk menghapus halaman dari hasil pencarian?
- Di tahap mana masalahmu kalau halaman "ditemukan tapi saat ini tidak diindeks"?

## Sumber resmi
Google Search Central: How Search works, dan dokumentasi sitemap.
