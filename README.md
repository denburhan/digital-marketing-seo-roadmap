# Digital Marketing dan SEO: Dari Basic sampai Expert

Kurikulum belajar digital marketing dengan fokus SEO, berbahasa Indonesia. Disusun bertingkat: Basic, Intermediate, Advanced, Expert. Tiap modul punya tujuan, penjelasan, latihan, dan cek pemahaman.

## Prinsip repo ini
1. **Tidak ada angka karangan.** Tidak ada statistik contoh, persentase prediksi, atau studi kasus fiktif. Kalau butuh contoh angka, pakai data nyata dari situsmu sendiri atau tulis N/A.
2. **Klaim dilabeli.** Klaim taktik dicek ke dokumentasi resmi (Google Search Central, web.dev). Yang tidak bisa diverifikasi ditandai "klaim penulis". Lihat `references/klaim-ai-search-terverifikasi.md`.
3. **Estimasi tool pihak ketiga bukan data Google.** Volume, DR, difficulty adalah perkiraan. Jangan dicampur dengan data Search Console tanpa label sumber.
4. **Ukur, jangan klaim.** Pantau lewat GSC dan analitik.
5. **Satu rekomendasi tegas** di akhir setiap analisis, beralasan angka.
6. **Tanggal pemeriksaan dicantumkan.** Dokumentasi Google berubah. Cek ulang sebelum dijadikan dasar keputusan.

## Peta belajar

### 01-basic (sekitar 4 minggu)
1. Apa itu digital marketing
2. Funnel dan customer journey
3. Cara kerja mesin pencari
4. Istilah SEO dasar
5. Riset keyword dasar
6. On-page SEO dasar
7. Tools gratis: GSC, GA4, PageSpeed
8. Rencana belajar 30 hari

### 02-intermediate (sekitar 6 minggu)
1. Keyword cluster dan kanibalisasi
2. Struktur situs dan internal linking
3. Technical SEO esensial
4. Content strategy dan konten berguna
5. Local SEO
6. Link building dasar
7. Analitik lanjutan GSC dan GA4
8. Iklan berbayar dan integrasi SEO
9. Rencana belajar

### 03-advanced (sekitar 8 minggu)
1. Entity SEO dan brand
2. E-E-A-T dan trust
3. Audit halaman
4. Diagnosis halaman tidak terindeks
5. Kebijakan spam dan risiko
6. Programmatic SEO yang sehat
7. Rencana belajar

### 04-expert (sekitar 12 minggu)
1. AI Search, AEO, dan GEO
2. Topical authority
3. Google Discover dan gambar
4. Strategi dan pengambilan keputusan
5. Otomasi dan pengukuran
6. Rencana belajar

## Isi lain
- `templates/`: keyword map (CSV), template audit halaman, laporan keputusan.
- `scripts/`: skrip Python tanpa dependensi eksternal (`cluster_queries.py`, `check_urls.py`).
- `references/`: sumber resmi, glosarium, daftar klaim terverifikasi.

## Cara pakai
1. Mulai dari `01-basic/01-apa-itu-digital-marketing.md`, urut sampai rencana belajar di tiap level.
2. Kerjakan latihan di situs nyata (milikmu atau yang kamu punya izinnya).
3. Jangan lompat level sebelum kriteria lulus level sebelumnya terpenuhi.

## Etika
- Jangan menyentuh akun iklan atau situs produksi milik orang lain tanpa izin.
- Jangan memakai skrip di repo ini untuk crawling agresif.
- Jangan memasukkan kredensial, token, atau data klien ke repo.

## Lisensi
Konten: CC BY 4.0. Kode di `scripts/`: MIT. Lihat `LICENSE`.
