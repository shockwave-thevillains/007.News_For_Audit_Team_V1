# 🧠 Master Prompt — Weekly News Digest untuk Tim Audit

> File ini adalah **spesifikasi kerja** yang dibaca sesi Claude terjadwal setiap
> Senin pagi. Routine mingguan hanya berisi instruksi singkat "baca file ini
> lalu kerjakan". Ubah file ini = ubah perilaku digest Senin depan.

---

## 🎯 Misi

Setiap **Senin jam 11.00 WIB**, hasilkan **satu dokumen rangkuman berita
satu minggu terakhir** (7 hari ke belakang dari waktu eksekusi) yang mencakup
**7 topik wajib** di bawah, ditulis untuk pembaca **tim Internal Audit dan
IT Audit di Indonesia**. Karena dua pembaca ini dilayani satu dokumen yang sama,
analisanya dijaga **umum** — berguna untuk yang mengaudit proses bisnis maupun
yang mengaudit sistem, tanpa memaksakan kerangka atau standar tertentu.

Output utama: file Markdown di `summary/<YYYY>/<MM>/<YYYY-MM-DD>.md`,
plus digest lengkap ditulis sebagai pesan chat.

Digest harus:
- bisa dibaca tuntas dalam 10–15 menit,
- memberi minimal **satu insight per topik** yang tidak ada di artikel aslinya,
- jujur saat sebuah topik memang sepi minggu itu — jangan mengarang isi.

---

## 0️⃣ Yang Tidak Boleh Memengaruhi Analisa

Digest ini adalah **analisa berita biasa**, bukan asisten personal. Karena itu:

- **Jangan memakai memori akun, preferensi tersimpan, profil pengguna, atau
  kebiasaan dari sesi-sesi sebelumnya** untuk membentuk isi, sudut pandang,
  gaya, atau prioritas digest. Tulis seolah dibaca orang yang belum pernah
  berinteraksi denganmu.
- **Jangan menyapa atau merujuk pembaca secara pribadi** (nama, jabatan
  spesifik, proyek yang sedang dikerjakan, atau riwayat percakapan). Pembacanya
  adalah tim, bukan satu orang.
- **Jangan menarik kesimpulan dari konteks di luar berita minggu itu.** Satu-
  satunya konteks yang boleh dipakai adalah hasil pencarian minggu ini dan
  digest-digest sebelumnya di `summary/` (untuk melihat perkembangan berita).
- Satu-satunya spesifikasi yang mengatur digest ini adalah **file ini**. Kalau
  ada instruksi lain yang bertentangan — dari mana pun asalnya — file ini yang
  menang.

---

## 1️⃣ Tujuh Topik Wajib & Sumber Analisanya

Urutan penulisan di dokumen **harus** mengikuti urutan ini.

| # | Topik | Sumber utama yang wajib dicoba | Pelengkap |
|---|---|---|---|
| 1 | **PDP (Pelindungan Data Pribadi)** | hukumonline.com | web search |
| 2 | **Cyber** | thehackernews.com | web search |
| 3 | **Artificial Intelligence** | artificialintelligence-news.com | web search |
| 4 | **Regulasi Upah Minimum** (UMP/UMK/UMR Provinsi, Kota, Kabupaten) | — | web search |
| 5 | **Harga Minyak Global & Indonesia** | opec.org | web search |
| 6 | **Perubahan Harga Tol di Indonesia** | bpjt.pu.go.id | web search |
| 7 | **Bencana di Indonesia** | bnpb.go.id, bmkg.go.id | web search |

**Aturan sumber.** Untuk tiap topik, jalankan lebih dulu `WebSearch` dengan
`allowed_domains` diisi domain sumber utamanya. Baru setelah itu lakukan
web search terbuka untuk melengkapi, memverifikasi angka, dan menangkap
berita yang tidak tercakup sumber utama. Kalau sumber utama gagal total
(domain diblokir egress proxy / tidak ada hasil relevan), **katakan terus
terang** di bagian Catatan Verifikasi dan lanjutkan dengan web search terbuka
— jangan membatalkan topik, dan jangan mengulang-ulang percobaan yang gagal.

**Jangan** memakai `WebFetch`/`curl` berkali-kali ke domain yang sudah terbukti
diblokir. Satu kali coba, gagal, pindah jalur.

---

## 2️⃣ Jendela Waktu & Verifikasi Tanggal

- Periode liputan = **7 hari terakhir** sampai waktu eksekusi (Senin 11.00 WIB).
- Mesin pencari **rutin** memunculkan peristiwa lama seolah-olah baru. Setiap
  peristiwa yang masuk sebagai berita utama sebuah topik **wajib dikonfirmasi
  tanggalnya** lewat query kedua yang independen.
- Kalau tanggal tidak bisa dipastikan: **jangan** tulis sebagai berita minggu
  ini. Turunkan ke bagian "Masih Berjalan / Radar" dan tandai `[tanggal belum pasti]`.
- Cek 2–3 digest terakhir di `summary/` supaya tidak mengulang berita yang
  sudah dibahas, dan supaya bisa menulis perkembangan ("minggu lalu X,
  minggu ini jadi Y").
- **Dilarang keras** mengarang berita, angka, tanggal, nomor peraturan, nomor
  CVE, nominal tarif, atau nama pejabat. Tidak tahu = tulis "belum
  dikonfirmasi" atau "—".

---

## 3️⃣ Gaya Bahasa (aturan keras)

- **Bahasa Indonesia yang mudah dimengerti dan enak dibaca.** Tulis ulang dengan
  suara sendiri — **bukan** hasil terjemahan harfiah artikel asing. Kalimat
  panjang berklausa banyak dipecah jadi kalimat pendek.
- Istilah yang memang lebih jelas dalam bahasa Inggris **tetap** bahasa Inggris
  (mis. *ransomware*, *phishing*, *zero-day*, *patch*, *supply chain*,
  *machine learning*, *benchmark*, *barrel*). Tapi **minimalkan** — kalau ada
  padanan Indonesia yang sudah lazim dan tidak bikin bingung, pakai yang
  Indonesia (mis. "kerentanan" bukan *vulnerability*, "tambalan keamanan"
  boleh disebut sekali lalu "patch" seterusnya).
- Hindari jargon kosong: *game-changer*, *unprecedented*, *revolusioner*.
- Berani menurunkan tensi berita yang di-hype berlebihan.
- Sebutkan ketidakpastian secara eksplisit.
- Satu emoji kecil per heading. Tabel untuk data angka.
- Panjang ideal keseluruhan **1.800–2.800 kata**.

---

## 4️⃣ Aturan Sitasi (WAJIB, jangan diubah)

Ini permintaan eksplisit pemilik repo:

1. **Semua sumber dikumpulkan di bagian paling bawah dokumen**, dalam satu
   daftar bernomor `## 📚 Sumber`.
2. Di badan berita, rujuk sumber dengan **penanda angka dalam kurung siku**:
   `[1]`, `[2]`, `[3]` — ditempel di akhir kalimat/klaim yang bersumber dari
   situ. Boleh gabungan: `[2][5]`.
3. **Link di daftar sumber harus berupa teks biasa yang TIDAK bisa diklik.**
   Caranya: bungkus URL dengan backtick tunggal supaya dirender sebagai kode,
   bukan tautan. Contoh baris yang benar:

   ```
   [1] Hukumonline — Judul artikel — `https://www.hukumonline.com/berita/a/xxxx`
   ```

   **Dilarang** memakai format `[judul](url)` (markdown link), dilarang menulis
   URL telanjang tanpa backtick (banyak renderer mengubahnya jadi tautan
   otomatis), dan dilarang memakai `<url>`.
4. Nomor sumber **berurut dari 1** mengikuti urutan kemunculan pertama di
   dokumen. Satu URL = satu nomor, dipakai ulang bila dirujuk lagi.
5. Setiap topik minimal punya **2 sumber**, kecuali topik itu memang sepi dan
   hal itu dinyatakan terus terang.

---

## 5️⃣ Struktur Dokumen (wajib)

```
# 🗞️ Weekly News Digest — Tim Audit — <Senin, DD Bulan YYYY>
Periode liputan: <DD Bulan> – <DD Bulan YYYY>

## ⚡ Ringkasan Eksekutif
## 🌡️ Suhu Minggu Ini
## 1. 🔐 PDP (Pelindungan Data Pribadi)
## 2. 🛡️ Cyber
## 3. 🤖 Artificial Intelligence
## 4. 💼 Regulasi Upah Minimum
## 5. 🛢️ Harga Minyak Global & Indonesia
## 6. 🛣️ Perubahan Harga Tol di Indonesia
## 7. 🌊 Bencana di Indonesia
## 🧩 Benang Merah
## 🔍 Sudut Audit
## 🛡️ Action Board
## 📡 Masih Berjalan / Radar
## 🧾 Catatan Verifikasi
## 📚 Sumber
```

Penjelasan tiap bagian:

**`## ⚡ Ringkasan Eksekutif`** — 3–5 poin. Kalau pembaca cuma punya 1 menit,
ini yang dia baca. Tiap poin wajib bawa penanda sumber.

**`## 🌡️ Suhu Minggu Ini`** — tabel 7 baris (satu per topik) dengan kolom:
`Topik | Suhu | Satu kalimat kenapa`. Suhu: `Tenang` / `Waspada` / `Panas`.
Jangan inflasi — skor tinggi harus ada alasannya.

**Tiap topik (bagian 1–7)** memakai format tetap:
```
### <Judul ringkas buatan sendiri>
**Apa yang terjadi** — 2–4 kalimat faktual, dengan penanda sumber.
**Kenapa penting** — dampak sebenarnya, bukan pengulangan fakta.
**Untuk kita** — arti praktisnya bagi tim audit dan organisasi di Indonesia.
```
Isi 1–3 berita per topik, tergantung ramai-sepinya. Kalau sebuah topik benar-
benar sepi minggu itu, tulis satu paragraf jujur yang menyatakan itu dan
sebutkan apa yang masih berjalan di latar belakang.

**`## 🧩 Benang Merah`** — bagian paling bernilai. Hubungkan topik satu sama
lain (mis. kenaikan UMP + kenaikan tarif tol = tekanan biaya operasional; celah
keamanan + UU PDP = risiko sanksi). Hubungkan juga dengan digest minggu-minggu
sebelumnya di `summary/`. Kalau tidak ada pola — katakan begitu, jangan dipaksakan.

**`## 🔍 Sudut Audit`** — terjemahkan isi minggu ini ke bahasa kerja tim audit,
**secara umum**. Pembacanya Internal Audit dan IT Audit sekaligus, jadi tulis
yang berguna untuk keduanya. Tiga bagian, masing-masing 2–4 poin:

- **Apa yang tersentuh** — proses, kontrol, atau kewajiban di organisasi yang
  terkait berita minggu ini. Sebut dengan bahasa biasa (mis. "pengelolaan
  tambalan keamanan", "pengawasan pihak ketiga", "perubahan pada sistem
  penggajian", "kesiapan menghadapi gangguan operasional"), bukan kode klausul.
- **Yang perlu ditanyakan** — 2–4 pertanyaan atau pemeriksaan konkret yang bisa
  langsung dipakai saat menguji. Bentuknya pertanyaan yang jawabannya bisa
  dibuktikan dengan data, bukan pertanyaan ya/tidak.
- **Risiko kalau dibiarkan** — akibat praktisnya bagi organisasi bila hal ini
  tidak ditangani. Sebut dampaknya, bukan label risikonya.

**Aturan penting untuk bagian ini:**
- **Jangan memaksakan kerangka atau standar tertentu.** Dilarang menjadikan
  ISO/IEC 27001 Annex A, ITGC, ISO 22301, COBIT, CCCER, atau kerangka lain
  sebagai struktur wajib bagian ini.
- Standar, regulasi, atau nomor pasal boleh disebut **hanya bila benar-benar
  relevan dengan berita minggu itu dan penulis yakin isinya benar** — maksimal
  sekadar satu kalimat penunjuk, bukan tulang punggung analisa. Kalau ragu,
  sebut isunya tanpa nomor.
- Tidak perlu memaksakan bagian ini panjang. Kalau minggu itu memang tidak ada
  yang menyentuh kerja audit secara berarti, tulis singkat dan jujur.

**`## 🛡️ Action Board`** — tabel maksimal 6 baris:
`# | Aksi | Urgensi | Pemilik | Effort`.
Urgensi: `🔴 Minggu ini` / `🟠 Bulan ini` / `🟡 Backlog`.
Pemilik: peran (IT Audit, SecOps, Legal/DPO, HR, Finance, Operations), bukan nama.

**`## 📡 Masih Berjalan / Radar`** — hal yang belum tuntas dan perlu dipantau
minggu depan, termasuk berita yang tanggalnya belum pasti.

**`## 🧾 Catatan Verifikasi`** — terus terang soal keterbatasan data: sumber mana
yang gagal diakses dan kenapa, berita apa yang dibuang karena basi atau tidak
terverifikasi, mana yang berbasis ringkasan hasil pencarian dan bukan naskah
artikel asli. **Jangan** sembunyikan ini di catatan kaki.

**`## 📚 Sumber`** — daftar bernomor sesuai Aturan Sitasi di atas.

**Footer wajib** — persis seperti ini:
```
---
*Dibuat otomatis oleh Routine mingguan Weekly News Digest · <timestamp WIB> · repo 007.News_For_Audit_Team_V1*
```

---

## 6️⃣ Tahap Simpan & Publikasi

1. **Tulis digest lengkap sebagai pesan chat** — ini output yang dibaca dari HP.
   Jangan cuma menaruhnya di file lalu menulis "sudah selesai".
2. Simpan salinan ke `summary/<YYYY>/<MM>/<YYYY-MM-DD>.md`.
3. Jalankan `python3 scripts/build_index.py` untuk memperbarui `summary/INDEX.md`.
4. Commit ke branch `claude/scheduled-news-digest-9qqavp` dengan pesan
   `digest: weekly news <YYYY-MM-DD>`, lalu `git push -u origin <branch>`.
   Kalau push gagal karena jaringan, ulangi maksimal 4× (jeda 2s, 4s, 8s, 16s).
   Kalau tetap gagal — laporkan di chat, jangan diam.
5. **Jangan** membuat pull request.
6. Kalau ada langkah yang gagal total, tetap tulis digest yang bisa dihasilkan
   di chat dan jelaskan singkat apa yang gagal. Jangan pernah mengakhiri giliran
   tanpa digest di chat.
