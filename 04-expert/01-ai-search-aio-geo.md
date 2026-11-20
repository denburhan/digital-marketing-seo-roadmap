# 01. AI Search, AEO, dan GEO

**Level:** Expert | **Waktu baca:** 20 menit | **Prasyarat:** 03-advanced

## Tujuan
Memahami apa yang benar dan tidak benar tentang optimasi untuk AI Overview, AI Mode, dan mesin jawaban lain.

## Yang terverifikasi (pernyataan resmi Google)
- **Tidak ada optimasi teknis khusus** untuk muncul di AI Overview atau AI Mode. Tidak ada schema khusus dan tidak ada file llms.txt yang disyaratkan. Syaratnya: halaman bisa diindeks dan memenuhi Search Essentials.
- **llms.txt tidak dipakai Google** untuk ranking. Membuatnya tidak merugikan, tapi jangan berharap dampak di Google.
- **Tidak ada formula penulisan khusus "AI-friendly".** Menulis untuk manusia sudah cukup.
- **Memecah konten jadi banyak halaman kecil demi AI (chunking berlebihan) tidak perlu.**
- **Structured data membantu pemahaman**, bukan jalur VIP.

Sumber ringkasan: `references/klaim-ai-search-terverifikasi.md` di repo ini, yang menyalin hasil verifikasi dari panduan resmi Google.

## Tambahan dari panduan optimasi generative AI Google (diperiksa 20 November 2026)
- Panduan resmi menyarankan mengabaikan taktik "chunking" konten, file teks AI yang tidak perlu (seperti llms.txt), dan mention yang tidak autentik.
- Membuat konten terpisah untuk setiap variasi query atau fan-out query terutama demi memanipulasi peringkat atau jawaban AI melanggar kebijakan scaled content abuse.
- Search Console memiliki Generative AI performance report. Cek di Search Console situsmu apakah laporan itu sudah tersedia untuk propertimu, lalu pakai sebagai sumber data utama sebelum uji manual.

## Pola yang dipahami (heuristik yang masuk akal)
- AI Overview dibangun di atas sistem ranking inti: ranking terjadi lebih dulu, lalu jawaban dirangkai. SEO tidak mati. Indikator keberhasilan bergeser ke dua: posisi dan apakah kamu dikutip sebagai sumber.
- **Query fan-out:** pertanyaan besar dipecah jadi sub-pertanyaan. Halaman kuat menjawab pertanyaan inti dan mengantisipasi sub-pertanyaannya.
- **Struktur yang jelas membantu:** heading rapi, paragraf pendek, satu ide per paragraf, jawaban inti di awal.
- **Konten non-komoditas lebih tahan:** data orisinal, pengalaman langsung, studi kasus nyata.

## Yang harus dicurigai
- Skor "AI Citation Probability" atau sejenisnya: tidak ada alat yang bisa memprediksi itu.
- Angka persen tanpa sumber di materi GEO (misalnya "sitasi naik sekian persen"): perlakukan sebagai klaim penulis.
- Saran menulis statistik contoh untuk menaikkan otoritas: menghasilkan data palsu. Jangan.
- Membeli mention atau sitasi: sentimen web dibaca dan mention spam difilter.

## Soal FAQ schema
Per dokumentasi Google yang diperiksa 20 November 2026, fitur FAQ rich result tidak lagi tampil di hasil pencarian Google (pembaruan dokumentasi menyebut berlaku mulai 7 Mei 2026). Menulis FAQ untuk pembaca tetap berguna, tapi jangan menjanjikan tampilan rich result. Catatan: materi lama sering masih menyebut pembatasan 2023 dan klaim kenaikan trafik tanpa sumber. Periksa dokumentasi terkini sebelum memakainya.

## Mengukur
- Lacak query dan halaman lewat GSC.
- Catat sendiri apakah halamanmu muncul sebagai sumber di jawaban AI untuk set query tetap (uji manual, catat tanggal dan hasil apa adanya). Ini sampel kecil, bukan statistik pasar.

## Latihan
1. Pilih 10 query bernilai. Uji manual tiap bulan, catat apakah situsmu dikutip.
2. Tulis satu halaman yang menjawab pertanyaan inti dan 3 sub-pertanyaan, dengan satu bukti orisinal.

## Cek pemahaman
- Kenapa membuat llms.txt tidak menambah peringkat di Google?
- Apa arti query fan-out bagi struktur halamanmu?
