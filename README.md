# 🗞️ Weekly News Digest — Internal Audit & IT Audit (Scheduled)

Rangkuman & analisa **berita satu minggu terakhir** untuk tim Internal Audit
dan IT Audit, mencakup
**7 topik tetap** — dari pelindungan data pribadi sampai bencana alam —
dijalankan otomatis oleh Claude **setiap Senin jam 11.00 WIB**.

Bukan agregator headline. Tiap Senin Claude membaca berita 7 hari terakhir,
memverifikasi tanggal dan angkanya, mencari benang merah antar topik, lalu
menerjemahkannya ke **bahasa kerja tim audit** — proses apa yang tersentuh,
regulasi apa yang bergerak, biaya apa yang naik, apa yang perlu ditanyakan, dan
apa yang bisa dikerjakan minggu ini.

---

## 📌 Tujuh Topik & Sumbernya

| # | Topik | Sumber utama | Pelengkap |
|---|---|---|---|
| 1 | 🔐 PDP (Pelindungan Data Pribadi) | hukumonline.com | web search |
| 2 | 🛡️ Cyber | thehackernews.com | web search |
| 3 | 🤖 Artificial Intelligence | artificialintelligence-news.com | web search |
| 4 | 💼 Regulasi Upah Minimum (UMP/UMK) | — | web search |
| 5 | 🛢️ Harga Minyak Global & Indonesia | opec.org | web search |
| 6 | 🛣️ Perubahan Harga Tol di Indonesia | bpjt.pu.go.id | web search |
| 7 | 🌊 Bencana di Indonesia | bnpb.go.id, bmkg.go.id | web search |

---

## ⚙️ Cara Kerjanya

```
Senin 11.00 WIB  ──▶  Routine membangunkan sesi Claude terjadwal
                         │
                         ├─ 1. Baca prompts/weekly-brief.md (spesifikasi kerja)
                         │      + 2-3 digest terakhir di summary/
                         │
                         ├─ 2. Kumpulkan berita 7 hari terakhir, per topik
                         │      WebSearch dengan allowed_domains sumber utama
                         │      ──▶ lalu web search terbuka sebagai pelengkap
                         │
                         ├─ 3. Verifikasi tanggal & angka lewat query kedua
                         │      yang independen (aturan paling keras)
                         │
                         ├─ 4. Analisa: benang merah antar topik,
                         │      sudut audit umum — apa yang tersentuh,
                         │      apa yang perlu ditanyakan, risiko kalau
                         │      dibiarkan — lalu action board
                         │
                         ├─ 5. Tulis digest lengkap DI CHAT  ──▶ dibaca dari HP 📱
                         │
                         └─ 6. Arsipkan ke repo ini
                                summary/YYYY/MM/YYYY-MM-DD.md
                                + regenerate summary/INDEX.md
```

## 📁 Struktur Repo

| Path | Isi |
|---|---|
| `prompts/weekly-brief.md` | **Otak sistem.** Spesifikasi lengkap cara Claude meneliti & menulis digest. Edit file ini untuk mengubah topik, gaya, atau kedalaman analisa — tidak perlu menyentuh Routine. |
| `templates/weekly-brief.md` | Kerangka Markdown output mingguan. |
| `summary/YYYY/MM/*.md` | Arsip digest mingguan. |
| `summary/INDEX.md` | Daftar isi semua digest (auto-generate). |
| `scripts/build_index.py` | Regenerator `summary/INDEX.md`. |
| `README.md` | Dokumen ini — gambaran flow, aturan sitasi, dan cara menyesuaikan. |

Semua pekerjaan berjalan di branch `claude/scheduled-news-digest-9qqavp`.
Routine tidak pernah membuat pull request.

## 🔗 Aturan Sitasi

Permintaan tetap pemilik repo, dikunci di `prompts/weekly-brief.md`:

1. Semua sumber dikumpulkan di **bagian paling bawah** dokumen (`## 📚 Sumber`).
2. Di badan berita, sumber dirujuk dengan **angka dalam kurung siku** — `[1]`, `[2]`, `[3]`.
3. Link di daftar sumber ditulis sebagai **teks biasa yang tidak bisa diklik**,
   dibungkus backtick supaya dirender sebagai kode:

   ```
   [1] Hukumonline — Judul artikel — `https://www.hukumonline.com/berita/a/xxxx`
   ```

   Format markdown link `[judul](url)` **tidak dipakai** — disengaja.

## 🌐 Catatan Jaringan

Egress proxy lingkungan ini memblokir sebagian domain berita, jadi `WebFetch`
langsung ke situs sumber sering gagal. Jalur **utama** yang dipakai digest adalah
tool `WebSearch` dengan `allowed_domains` diisi domain sumber utama — jalur ini
terbukti tembus. Kalau sebuah sumber tetap gagal, digest wajib menyebutkannya
terus terang di bagian **Catatan Verifikasi**, bukan menyembunyikannya.

Untuk meng-allowlist domain pada environment, lihat
https://code.claude.com/docs/en/claude-code-on-the-web

## ✍️ Menyesuaikan

- **Ganti jam / hari** → ubah cron Routine (disimpan dalam UTC; Senin 11.00 WIB = Senin 04:00 UTC → `0 4 * * 1`).
- **Ganti topik atau sumber** → edit tabel di `prompts/weekly-brief.md` bagian "Tujuh Topik Wajib".
- **Ganti gaya bahasa** → edit bagian "Gaya Bahasa" di prompt yang sama.
- **Ganti struktur dokumen atau isi tiap bagian** → edit bagian "Struktur Dokumen".
- **Ganti cara menulis sudut audit** → edit bagian "Sudut Audit" di dalam "Struktur Dokumen". Di situlah larangan memaksakan kerangka tertentu disimpan.
- **Ganti aturan sitasi** → edit bagian "Aturan Sitasi".
- **Berhenti sementara** → nonaktifkan Routine (`enabled: false`), arsip tetap aman.

Kalau prompt diubah, **ubah juga prompt Routine-nya** kalau perubahannya
menyentuh hal yang ikut disebut di sana (struktur wajib, aturan sitasi, daftar
topik). Prompt Routine sengaja dibuat hanya sebagai ringkasan — kalau keduanya
berbeda, `prompts/weekly-brief.md` yang menang.

## 🧭 Untuk Siapa Ini Dibuat

Pembacanya **tim Internal Audit dan IT Audit** di Indonesia. Keduanya dilayani
oleh satu dokumen yang sama, jadi analisanya sengaja dijaga **umum** — cukup
berguna untuk yang mengaudit proses bisnis, dan cukup berguna untuk yang
mengaudit sistem, tanpa memaksakan kerangka atau standar tertentu.

Maka setiap digest wajib menjawab tiga pertanyaan, bukan cuma "apa yang terjadi":

1. Proses, kontrol, atau kewajiban apa di organisasi yang tersentuh berita ini?
2. Kalau situasinya terjadi di organisasi kita, risikonya di mana?
3. Apa satu langkah konkret yang bisa dikerjakan minggu ini?

Standar atau regulasi disebut **hanya bila memang relevan dan penulis yakin** —
bukan sebagai hiasan di setiap digest. Kalau ragu, sebutkan isunya dan biarkan
pembaca memetakannya sendiri ke kerangka yang dipakai timnya.

Sudut pandangnya adalah **organisasi sendiri**, bukan auditor eksternal yang
menangani klien. Jadi "organisasi kita", bukan "klien".

Satu hal lagi yang dikunci di spesifikasi: digest ini **analisa berita biasa**.
Isi, sudut pandang, dan prioritasnya tidak boleh dibentuk oleh memori akun,
preferensi tersimpan, atau riwayat percakapan siapa pun — ditulis seolah dibaca
orang yang belum pernah berinteraksi dengan Claude.
