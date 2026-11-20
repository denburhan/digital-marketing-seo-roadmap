---
name: seo-playbook-id
description: "Use for SEO work in Indonesian: keyword and intent research, page audit, indexing diagnosis, AI Search claims. Verifies claims, never invents numbers."
version: 1.0.0
license: MIT (kode) dan CC BY 4.0 (teks)
---

# SEO Playbook (Bahasa Indonesia)

Panduan kerja SEO untuk agen AI atau manusia: riset keyword dan intent, audit halaman, diagnosis halaman tidak terindeks, dan menilai klaim AI Search. Kurikulum lengkapnya ada di repo induk (folder `01-basic` sampai `04-expert`). Skill ini adalah ringkasan prosedur yang bisa langsung dipakai.

## Kapan dipakai
- Diminta riset keyword, cluster, intent, atau memetakan keyword ke URL.
- Diminta audit satu halaman atau menilai apakah halaman siap bersaing.
- Halaman atau situs tidak terindeks, atau impresi turun tajam.
- Ditanya soal AI Overview, AI Mode, AEO, GEO, llms.txt, FAQ schema.
- Ada materi SEO dari luar (kursus, blog, deck) yang perlu dinilai sebelum dipakai.

Tidak untuk: gaya penulisan, desain, atau eksekusi massal di CMS.

## Aturan selalu aktif
1. **Jangan mengarang angka.** Tidak ada statistik contoh, volume, CPC, posisi, atau prediksi persentase tanpa data. Data tidak ada: tulis N/A.
2. **Labeli tingkat keyakinan.** Tiap angka bukan hasil ukur sendiri diberi sumber. Yang tidak bisa diverifikasi ditandai "klaim penulis". Prediksi ditulis sebagai estimasi, bukan janji.
3. **Beda data Google dan tool pihak ketiga.** Search Console dan analitik milikmu adalah data. Volume, DR, difficulty dari tool lain adalah estimasi. Jangan campur dalam satu tabel tanpa label sumber.
4. **Verifikasi klaim taktik** ke dokumentasi resmi (Google Search Central, web.dev) sebelum dipakai. Dokumentasi berubah, jadi cantumkan tanggal pemeriksaan.
5. **Ukur, jangan klaim.** Pantau lewat Search Console, bukan tangkapan layar atau perkiraan.
6. **Akhiri dengan satu rekomendasi tegas** yang beralasan angka, bukan daftar opsi netral.
7. **Jangan tulis pengalaman atau studi kasus karangan.** Kalau butuh contoh, labeli "contoh skenario".
8. **Jangan sentuh iklan aktif atau situs produksi secara destruktif** (hapus, redirect massal, noindex) tanpa konfirmasi pemilik.
9. **Jangan bocorkan kredensial.** Token dan API key tidak masuk dokumen, repo, atau log.

## Prosedur A: Riset keyword dan intent
1. Kumpulkan seed dari layanan, kompetitor, autocomplete, dan query nyata di Search Console.
2. Satu halaman satu primary keyword. Tambah beberapa secondary yang searah intent.
3. Kelompokkan berdasarkan intent dan pola SERP, bukan kemiripan kata. Kalau SERP tidak diperiksa, tulis "kemungkinan", jangan menyatakan pasti.
4. Klasifikasikan tahap funnel (TOFU, MOFU, BOFU) dan jenis intent. Pakai `scripts/cluster_queries.py` untuk draf awal, lalu koreksi manual.
5. Petakan ke URL: cluster, target URL, intent, status (ada, perlu dibuat, perlu revisi). Template: `templates/keyword-intent-map.csv`.
6. Cek kanibalisasi: beberapa URL bergantian muncul untuk query sama di Search Console. Solusi: gabung dengan 301, bedakan intent, atau canonical.
7. Prioritaskan: nilai bisnis dulu, lalu halaman posisi 5 sampai 15 yang butuh dorongan.

## Prosedur B: Audit halaman
Lima lapis: intent, konten, struktur, teknis, kepercayaan dan konversi. Tiap lapis diberi status lulus, perlu perbaikan, atau gagal beserta alasan satu kalimat. Tiap temuan wajib punya alat ukur (fetch halaman, PageSpeed atau data lapangan, data Search Console). Temuan tanpa bukti tidak masuk laporan. Jangan membuat skor karangan. Template: `templates/audit-halaman.md`.

## Prosedur C: Halaman tidak terindeks
Urutan diagnosis, jangan melompat:
1. URL Inspection: dikenal, terakhir di-crawl, status indeks.
2. Penghalang: noindex (meta atau header), robots.txt, canonical ke URL lain, redirect, status bukan 200, login wall. Bantuan: `scripts/check_urls.py`.
3. Penemuan: ada di sitemap dan punya tautan internal?
4. Kualitas: tipis, duplikat, atau mirip massal.
5. Kebijakan spam dan Manual Actions di Search Console.
Mengirim ulang URL berkali-kali tidak menjamin pengindeksan.

## Prosedur D: Menilai klaim AI Search
- Per panduan resmi Google yang diperiksa 20 November 2026: tidak ada optimasi teknis khusus untuk AI Overview atau AI Mode, dan taktik seperti chunking, file llms.txt, serta mention tidak autentik bisa diabaikan.
- FAQ rich result tidak tampil lagi di Google sejak 7 Mei 2026 (menurut catatan dokumentasi Google).
- Skor "AI Citation Probability" dan angka persen kenaikan sitasi tanpa sumber: tandai klaim penulis.
- Tabel lengkap dan status verifikasi: `references/klaim-ai-search-terverifikasi.md`. Cek ulang ke sumber di `references/sumber-resmi.md` sebelum dipakai untuk keputusan.

## Format jawaban
1. Situasi (angka dan sumbernya).
2. Diagnosis (hipotesis, bukti, tingkat keyakinan).
3. Opsi (maksimal tiga, dengan trade-off).
4. Satu rekomendasi tegas dan alasannya.
5. Cara mengukur dan kapan ditinjau.
Bahasa Indonesia, tanpa em dash atau en dash.

## Pitfall umum
- Mengukur panjang artikel dengan hitungan mentah. Entity HTML seperti `&#8211;` membuat hitungan meleset. Unescape dulu.
- Taktik usang yang masih beredar: keyword density, LSI keyword sebagai faktor ranking, schema SearchAction untuk sitelinks search box, EXIF gambar sebagai faktor ranking, AggregateRating tanpa ulasan nyata.
- Dua URL untuk intent yang sama: satukan dengan 301 ke pemenang berdasarkan data Search Console, bukan menambah halaman hub baru.
- Materi SEO yang bertentangan satu sama lain: pilih versi yang cocok dengan dokumentasi resmi dan sebut pertentangannya.

## File pendukung
- `references/klaim-ai-search-terverifikasi.md`
- `references/sumber-resmi.md`
- `references/glosarium.md`
- `templates/audit-halaman.md`, `templates/keyword-intent-map.csv`, `templates/laporan-keputusan.md`
- `scripts/cluster_queries.py` (opsi --lang id, en, both), `scripts/check_urls.py` (Python 3, tanpa dependensi)
