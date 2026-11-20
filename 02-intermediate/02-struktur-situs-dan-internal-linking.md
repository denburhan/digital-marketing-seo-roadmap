# 02. Struktur Situs dan Internal Linking

**Level:** Intermediate | **Waktu baca:** 15 menit | **Prasyarat:** 01-basic/06

## Tujuan
Merancang struktur yang memudahkan pengguna dan crawler memahami hubungan antar halaman.

## Pola pilar dan pendukung
- **Halaman pilar:** membahas topik luas secara komprehensif.
- **Halaman pendukung:** membahas sub-topik spesifik, menaut ke pilar.
- Pilar menaut balik ke pendukung yang paling relevan.

Ini pola organisasi, bukan rumus ranking. Manfaatnya nyata untuk navigasi dan kejelasan topik.

## Prinsip internal link
1. Tautan harus berupa elemen `<a href>` yang bisa di-crawl.
2. Anchor text menjelaskan tujuan, bukan "klik di sini".
3. Taruh tautan di dalam konten utama di tempat yang relevan, bukan hanya di footer.
4. Hindari halaman yatim (tanpa tautan masuk).
5. Jaga kedalaman klik: halaman penting idealnya dicapai dalam sedikit klik dari beranda.

## Audit cepat
- Crawl situs dengan crawler (Screaming Frog versi gratis cukup untuk situs kecil).
- Daftar halaman dengan tautan masuk internal nol.
- Daftar halaman penting yang kedalaman kliknya tinggi.
- Daftar anchor generik.

## Breadcrumb dan navigasi
Breadcrumb membantu pengguna tahu posisi. Struktur data breadcrumb bisa dipasang sesuai dokumentasi Google, tapi tampilannya tidak dijamin.

## Latihan
1. Gambar peta pilar dan pendukung untuk satu topik.
2. Temukan 5 halaman yatim di situsmu dan beri tautan masuk yang masuk akal.

## Cek pemahaman
- Kenapa anchor "klik di sini" kurang membantu?
- Apa risiko menaruh semua tautan penting hanya di footer?
