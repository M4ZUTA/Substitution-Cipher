# Monoalphabetic Cipher Analyzer

Aplikasi Python untuk mempelajari **monoalphabetic substitution cipher** melalui analisis frekuensi dan percobaan pemetaan huruf. Proyek menyediakan antarmuka web interaktif berbasis Streamlit serta dua program command-line (CLI).

> Cipher substitution sederhana tidak aman untuk melindungi informasi. Proyek ini ditujukan untuk pembelajaran dan eksperimen, bukan untuk keamanan data.

## Fitur

- Tempel ciphertext ke antarmuka web dan lihat jumlah huruf serta jumlah huruf unik.
- Bandingkan frekuensi huruf ciphertext dengan frekuensi umum bahasa Inggris melalui grafik.
- Uji pemetaan huruf cipher ke huruf plaintext dan lihat preview dekripsi secara langsung.
- Pertahankan spasi dan tanda baca pada preview. Huruf yang belum dipetakan dibedakan dari huruf yang sudah dipetakan.
- Analisis frekuensi huruf, pasangan huruf, tripel, pasangan berulang, dan kelompok empat huruf lewat program CLI.
- Dekripsi file menggunakan substitution key tetap lewat program CLI.

## Tech stack

| Teknologi | Kegunaan |
| --- | --- |
| Python | Bahasa pemrograman |
| Streamlit | Antarmuka web interaktif |
| Pandas | Menyiapkan data untuk grafik |
| Plotly Express | Membuat grafik perbandingan frekuensi |

Dependensi Python tercantum di [`requirements.txt`](./requirements.txt). Tidak diperlukan layanan database atau backend terpisah.

## Persiapan dan menjalankan UI

Pastikan Python tersedia, lalu jalankan perintah berikut dari direktori proyek.

### Linux atau macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Streamlit akan menampilkan alamat aplikasi di terminal, biasanya <http://localhost:8501>. Buka alamat tersebut di browser. Untuk menghentikan aplikasi, tekan `Ctrl+C` di terminal.

## Alur penggunaan UI

1. **Masukkan ciphertext** dengan menempel atau mengetik pesan di kolom Ciphertext.
2. **Amati ringkasan dan grafik frekuensi.** Huruf A–Z dihitung tanpa membedakan kapitalisasi; spasi dan tanda baca tidak ikut dihitung. Grafik membandingkan distribusi pesan dengan frekuensi tipikal bahasa Inggris.
3. **Coba pemetaan substitusi.** Isi kolom di bagian Decryption Workbench: label di sebelah kiri adalah huruf cipher, dan nilai yang diisi adalah huruf plaintext penggantinya. Contoh: jika `X` diduga mewakili `E`, isi `E` pada baris `X`.
4. **Baca live decryption preview.** Perubahan pemetaan langsung memperbarui preview. Huruf yang sudah dipetakan ditandai hijau, sedangkan huruf yang belum dipetakan ditampilkan sebagai huruf kecil berwarna berbeda.
5. **Perbaiki atau mulai ulang pemetaan.** Tombol Reset mappings mengosongkan seluruh pemetaan. UI memberi peringatan jika nilai pemetaan bukan satu huruf A–Z atau jika beberapa huruf cipher dipetakan ke huruf plaintext yang sama.

Pemetaan disimpan di sesi Streamlit selama sesi browser berlangsung. Aplikasi tidak otomatis memecahkan cipher: pengguna menyimpulkan pemetaan dari pola dan memperbaruinya sendiri. Preview UI juga tidak otomatis disimpan sebagai file.

## Program command-line

Semua perintah berikut dijalankan dari direktori proyek.

### Analisis frekuensi

```bash
python Cryptanalysis.py
```

Program membaca `Aleem S.txt` dan menampilkan analisis di terminal. Fungsi analisisnya berada di [`Cryptanalysis.py`](./Cryptanalysis.py).

### Dekripsi dengan kunci tetap

```bash
python main.py
```

Program membaca `Aleem S.txt`, menerapkan substitution key yang sudah ditentukan di kode, mencetak hasil ke terminal, dan menulis hasil ke `plain_text.txt`. Menjalankan perintah ini akan mengganti isi `plain_text.txt` yang sudah ada.

UI Streamlit dan program CLI adalah alur yang terpisah: UI menerima ciphertext yang ditempel langsung dan menyediakan pemetaan interaktif, sedangkan CLI membaca file input bernama tetap.

## Struktur proyek

```text
.
├── app.py              # UI Streamlit: grafik frekuensi dan workbench pemetaan
├── Cryptanalysis.py    # Fungsi analisis frekuensi dan program CLI analisis
├── main.py             # Program CLI dekripsi dengan key tetap
├── Aleem S.txt         # Ciphertext contoh/default untuk program CLI
├── plain_text.txt      # Hasil dekripsi CLI; dibuat atau ditimpa saat main.py dijalankan
├── requirements.txt    # Dependensi Python untuk UI
├── PRD.md              # Ringkasan kebutuhan produk UI
└── README.md           # Dokumentasi proyek
```

Folder virtual environment seperti `.venv/` dibuat secara lokal saat instalasi dan bukan bagian dari source code aplikasi.

## Batasan dan catatan

- Grafik perbandingan menggunakan frekuensi tipikal bahasa Inggris. Hasilnya kurang sesuai untuk ciphertext dari bahasa lain.
- Frekuensi adalah petunjuk untuk analisis, bukan jaminan bahwa suatu huruf pasti mewakili huruf tertentu.
- UI melakukan substitusi manual dan belum menyediakan solver otomatis, impor file dari browser, atau ekspor hasil dekripsi.
- CLI `main.py` menggunakan kunci tetap yang didefinisikan di dalam kode; kunci itu mungkin tidak cocok untuk ciphertext lain.
- Perbandingan frekuensi tunggal maupun kelompok huruf dipengaruhi panjang dan isi teks sampel.

## Lisensi

Belum ada file lisensi di repository ini. Jangan menganggap kode atau materi proyek memiliki lisensi penggunaan ulang tertentu sebelum lisensi ditambahkan.
