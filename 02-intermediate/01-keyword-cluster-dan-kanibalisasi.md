# 01. Keyword Cluster dan Kanibalisasi

**Level:** Intermediate | **Waktu baca:** 15 menit | **Prasyarat:** 01-basic/05

## Tujuan
Mengelompokkan ratusan query ke cluster berbasis intent, lalu menemukan dan memperbaiki halaman yang saling bersaing.

## Cluster berbasis intent
Kelompokkan berdasarkan maksud pencarian, bukan kemiripan kata. "Cara pasang parket" dan "jasa pasang parket" mirip secara kata tapi intent-nya beda (edukasi vs transaksi), jadi beda halaman.

Ujian cepat: kalau dua query menampilkan SERP yang hampir sama (jenis halaman dan topiknya), mereka kandidat satu halaman. Kalau SERP-nya berbeda, pisahkan.

## Mendeteksi kanibalisasi
Dari ekspor GSC (query x halaman):
1. Cari query yang menampilkan lebih dari satu URL milikmu.
2. Lihat apakah posisinya berganti-ganti antar URL atau keduanya stagnan di bawah.
3. Putuskan URL pemenang berdasarkan intent dan kekuatan konten.

## Cara memperbaiki
- **Gabung:** isi URL yang lemah dipindahkan ke yang kuat, lalu 301 redirect.
- **Bedakan:** ubah sudut dan intent salah satu halaman supaya tidak tumpang tindih.
- **Canonical:** hanya kalau halaman memang duplikat teknis, bukan solusi untuk konten yang bersaing.
- **Perkuat tautan internal** ke URL pemenang dengan anchor yang konsisten.

## Skrip bantu
Repo ini menyertakan `scripts/cluster_queries.py` yang mengelompokkan query dari CSV berdasarkan kata dasar dan modifier intent. Hasilnya titik awal, bukan keputusan akhir. Selalu cek SERP manual sebelum menggabung halaman.

## Verifikasi hitungan
Kalau kamu menghasilkan tabel ringkasan, hitung ulang dengan kode. Contoh: jumlah query dalam sebuah cluster harus sama dengan jumlah item di kolom daftar query. Tabel yang dihitung tangan sering salah.

## Latihan
1. Ekspor 3 bulan data query x halaman dari GSC.
2. Jalankan skrip cluster. Pilih 3 cluster dan cek SERP-nya manual.
3. Tulis keputusan gabung, bedakan, atau biarkan untuk tiap cluster, dengan alasan.

## Cek pemahaman
- Kenapa canonical bukan obat untuk kanibalisasi konten?
- Apa tanda kamu seharusnya memisahkan dua query ke dua halaman?
