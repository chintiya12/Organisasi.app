# Aplikasi Organisasi Mahasiswa 
Aplikasi ini merupakan sistem informasi sederhana berbasis terminal (CLI) yang digunakan untuk melihat daftar, informasi, dan melakukan pendaftaran ke organisasi mahasiswa.

## 1. Pendahuluan
### 1.1 Tujuan
### 1.2 Lingkup
### 1.3 Definisi dan Istilah

---

## 2. Deskripsi Umum
Aplikasi ini dikembangkan untuk mempermudah mahasiswa dalam mencari informasi tentang organisasi kampus dan mendaftar ke organisasi pilihan mereka. Sistem ini mengelola data organisasi dan pendaftar secara lokal dalam memori selama aplikasi berjalan.

### 2.1 Fungsi Utama Sistem
Aplikasi CLI untuk pengelolaan informasi dan pendaftaran organisasi kampus oleh mahasiswa.

### 2.2 Lingkungan Pengembangan
- Python 3.x
- Platform: Linux, macOS, Windows
- Text editor: VSCode

### 2.3 Asumsi & Ketergantungan
- Data tidak disimpan ke database, hanya disimpan sementara di memori
- Input pengguna dilakukan secara manual melalui terminal

### 2.4 Perspektif Pengguna
Pengguna utama adalah mahasiswa yang ingin menjelajahi organisasi kampus, mempelajari detailnya, dan mendaftar. Aplikasi ini juga dapat digunakan oleh pengelola organisasi untuk melihat daftar pendaftar.

---

## 3. Kebutuhan Fungsional
| ID | Deskripsi |
|----|-----------|
| F1 | Menampilkan daftar organisasi yang tersedia |
| F2 | Menampilkan deskripsi dan kontak organisasi berdasarkan input nama |
| F3 | Menerima input nama mahasiswa dan nama organisasi untuk proses pendaftaran |
| F4 | Menampilkan daftar semua mahasiswa yang telah mendaftar |
| F5 | Menangani perintah keluar dari aplikasi |

---

## 4. Kebutuhan Non-Fungsional

| ID | Deskripsi |
|----|-----------|
| NF1 | Program berjalan menggunakan Python tanpa library eksternal |
| NF2 | Aplikasi memiliki struktur modular agar mudah dipelihara |
| NF3 | User interface berbasis teks dengan navigasi sederhana |
| NF4 | Validasi input dilakukan untuk menghindari crash dan kesalahan pendaftaran |
| NF5 | Data pendaftar tidak disimpan permanen (tidak menggunakan file/database) |

---

## 5. Antarmuka Sistem

### 5.1 Tampilan Awal Menu
===== Aplikasi Organisasi Mahasiswa =====
1. Lihat daftar organisasi
2. Lihat informasi organisasi
3. Daftar ke organisasi
4. Lihat data pendaftar
5. Keluar## Pendahuluan

### Tujuan
Dokumen ini menyediakan spesifikasi kebutuhan perangkat lunak untuk Aplikasi Organisasi Mahasiswa, sebuah sistem berbasis konsol yang dirancang untuk membantu mahasiswa mengelola informasi organisasi kampus, mendaftar ke organisasi, dan melihat data pendaftar. Dokumentasi ini ditujukan untuk pengembang, pengguna, dan pemangku kepentingan lainnya.

### Ruang Lingkup
Aplikasi ini memungkinkan pengguna untuk:
- Melihat daftar organisasi mahasiswa yang tersedia.
- Mengakses informasi detail tentang setiap organisasi, termasuk deskripsi dan kontak.
- Mendaftar ke organisasi yang dipilih.
- Melihat daftar pendaftar yang telah mendaftar ke berbagai organisasi.
Aplikasi ini berjalan pada lingkungan Python dan menggunakan antarmuka berbasis teks (CLI).

### Definisi dan Akronim
- **Ormawa**: Organisasi Mahasiswa, seperti BEM dan MPM.
- **UKM**: Unit Kegiatan Mahasiswa, seperti Seni Tari atau Bulu Tangkis.
- **CLI**: Command Line Interface, antarmuka berbasis teks untuk interaksi pengguna.

## Deskripsi Umum

### Latar Belakang
Aplikasi ini dikembangkan untuk mempermudah mahasiswa dalam mencari informasi tentang organisasi kampus dan mendaftar ke organisasi pilihan mereka. Sistem ini mengelola data organisasi dan pendaftar secara lokal dalam memori selama aplikasi berjalan.

### Perspektif Pengguna
Pengguna utama adalah mahasiswa yang ingin menjelajahi organisasi kampus, mempelajari detailnya, dan mendaftar. Aplikasi ini juga dapat digunakan oleh pengelola organisasi untuk melihat daftar pendaftar.

### Asumsi dan Ketergantungan
- Pengguna memiliki pengetahuan dasar tentang penggunaan aplikasi berbasis konsol.
- Python 3.x terinstal di sistem pengguna.
- Tidak ada ketergantungan eksternal (library) di luar modul standar Python.

## Kebutuhan Fungsional

### Fitur Aplikasi
Aplikasi ini memiliki fitur berikut:
- **Menampilkan daftar organisasi mahasiswa**: Menampilkan semua organisasi yang tersedia dalam format bernomor.
- **Melihat informasi detail setiap organisasi**: Menampilkan deskripsi dan kontak organisasi berdasarkan nama yang dimasukkan pengguna.
- **Melakukan pendaftaran ke organisasi yang dipilih**: Memungkinkan pengguna mendaftar dengan memasukkan nama mereka dan nama organisasi.
- **Melihat daftar seluruh pendaftar**: Menampilkan daftar pendaftar beserta organisasi yang mereka daftar.

### Daftar Organisasi
Aplikasi ini mencakup total 27 organisasi, terdiri dari berbagai jenis:

#### Ormawa
- **BEM (Badan Eksekutif Mahasiswa)**: Menjalankan program kerja dan menyuarakan aspirasi mahasiswa.
- **MPM (Majelis Permusyawaratan Mahasiswa)**: Mengawasi dan menetapkan kebijakan kampus.

#### Keagamaan
- **USWAH**: Kegiatan keislaman seperti pengajian dan kajian Islam.
- **Hindu Dharma**: Kegiatan keagamaan Hindu dan diskusi kitab suci.
- **KMK (Keluarga Mahasiswa Katolik)**: Pembinaan iman Katolik melalui misa dan pelayanan sosial.
- **PMK AGAPE**: Persekutuan Mahasiswa Kristen untuk ibadah dan kegiatan rohani.

#### Seni dan Budaya
- **Seni Tari**: Menyalurkan minat seni tari tradisional dan modern.
- **Paduan Suara Mahasiswa Gita Advayatva**: Pelatihan vokal dan tampil di acara resmi.
- **Teater Hijau 51**: Kreativitas seni pertunjukan melalui drama dan akting.
- **Band**: Pengembangan bakat musik dan tampil di event kampus.
- **ASPIRASI**: Penyaluran aspirasi dan diskusi isu sosial.
- **Master of Ceremony (MC)**: Pelatihan public speaking dan pembawa acara.
- **Unit Fotografi dan Videografi (UFO)**: Keterampilan dokumentasi visual dan sinematografi.

#### Olahraga dan Bela Diri
- **Bulu Tangkis**: Latihan dan kejuaraan antar mahasiswa.
- **Bola Voli**: Pengembangan keterampilan voli dan turnamen.
- **Basket**: Latihan fisik dan turnamen antar kampus.
- **Tarung Derajat**: Bela diri khas Indonesia untuk fisik dan disiplin.
- **Catur**: Mengasah strategi dan logika melalui kompetisi.
- **JU JIT-SU**: Bela diri untuk pertahanan diri dan ketangkasan.
- **Pencak Silat**: Bela diri tradisional Indonesia.
- **Taekwondo**: Bela diri Korea dengan teknik tendangan.
- **Sepakbola**: Latihan dan liga antar fakultas/universitas.

#### Kepemimpinan dan Lainnya
- **Conference**: Forum ilmiah dan pertukaran pemikiran.
- **KSR PMI**: Pelatihan pertolongan pertama dan kegiatan kemanusiaan.
- **AIESEC**: Kepemimpinan dan program magang global.
- **Content Creator Club (C3)**: Pembuatan konten digital seperti video dan podcast.
- **E-Sport**: Game kompetitif dan turnamen daring.
- **MAPALA**: Pendakian dan pelestarian lingkungan.
- **Resimen Mahasiswa**: Kedisiplinan dan kepemimpinan semi-militer.

### Alur Fungsional
1. **Menampilkan Menu**: Pengguna melihat menu utama dengan 5 pilihan.
2. **Lihat Daftar Organisasi**: Menampilkan daftar 27 organisasi.
3. **Lihat Informasi Organisasi**: Pengguna memasukkan nama organisasi, dan sistem menampilkan deskripsi dan kontak.
4. **Daftar ke Organisasi**: Pengguna memasukkan nama dan organisasi, sistem memvalidasi, dan menyimpan data pendaftar.
5. **Lihat Daftar Pendaftar**: Menampilkan semua pendaftar atau pesan jika belum ada.
6. **Keluar**: Menghentikan aplikasi.

## Kebutuhan Non-Fungsional

### Kinerja
- Aplikasi harus merespons input pengguna dalam waktu kurang dari 1 detik.
- Sistem dapat menangani hingga 100 pendaftar tanpa penurunan kinerja.

### Keandalan
- Aplikasi harus bebas dari crash selama penggunaan normal.
- Input pengguna divalidasi untuk mencegah kesalahan (misalnya, organisasi tidak ditemukan).

### Keamanan
- Tidak ada data sensitif yang disimpan secara permanen (data pendaftar hanya disimpan di memori selama aplikasi berjalan).
- Input pengguna dibersihkan untuk mencegah error (meskipun tidak ada risiko injeksi karena tidak ada database).

### Usability
- Antarmuka teks jelas dan mudah dipahami oleh pengguna non-teknis.
- Pesan error informatif (misalnya, "Organisasi tidak ditemukan").

## Antarmuka Sistem

### Antarmuka Pengguna
- **Tipe**: Command Line Interface (CLI).
- **Input**: Pengguna memasukkan pilihan menu (1-5) dan data seperti nama atau nama organisasi melalui keyboard.
- **Output**: Teks yang ditampilkan di konsol, termasuk menu, daftar organisasi, informasi organisasi, daftar pendaftar, dan pesan konfirmasi/error.

### Antarmuka Perangkat Keras
- Tidak ada kebutuhan khusus selain perangkat dengan terminal/konsol yang mendukung Python.

### Antarmuka Perangkat Lunak
- Ditulis dalam Python 3.x.
- Tidak memerlukan library eksternal.

## Installation Guide

1. **Prasyarat**:
   - Instal Python 3.x dari [python.org](https://www.python.org).
   - Pastikan perintah `python --version` menunjukkan versi 3.x.

2. **Langkah Instalasi**:
   - Unduh atau salin file proyek: `main.py`, `menu.py`, `organisasi.py`, dan `pendaftaran.py`.
   - Simpan semua file dalam satu direktori.

3. **Menjalankan Aplikasi**:
   - Buka terminal di direktori proyek.
   - Jalankan perintah:
     ```bash
     python main.py
     ```
   - Aplikasi akan menampilkan menu utama.

## Operating Procedures

1. **Memulai Aplikasi**:
   - Jalankan `python main.py` di terminal.
   - Menu utama akan ditampilkan dengan 5 opsi.

2. **Navigasi Menu**:
   - Masukkan angka 1-5 untuk memilih opsi.
   - Ikuti petunjuk di layar untuk memasukkan data (misalnya, nama organisasi atau nama pendaftar).

3. **Contoh Penggunaan**:
   - Pilih `1` untuk melihat daftar organisasi.
   - Pilih `2`, lalu masukkan "BEM" untuk melihat informasi BEM.
   - Pilih `3`, masukkan nama Anda dan organisasi (misalnya, "USWAH"), untuk mendaftar.
   - Pilih `4` untuk melihat daftar pendaftar.
   - Pilih `5` untuk keluar.

## Error Messages and Troubleshooting

### Pesan Error Umum
- **"Pilihan tidak valid."**:
  - **Penyebab**: Pengguna memasukkan angka selain 1-5 di menu utama.
  - **Solusi**: Masukkan angka antara 1 dan 5.
- **"Organisasi tidak ditemukan."**:
  - **Penyebab**: Nama organisasi yang dimasukkan tidak ada di daftar.
  - **Solusi**: Periksa ejaan atau pilih organisasi dari daftar (gunakan opsi 1 untuk melihat daftar).
- **"Belum ada pendaftar."**:
  - **Penyebab**: Tidak ada data pendaftar yang tersimpan.
  - **Solusi**: Daftar ke organisasi terlebih dahulu menggunakan opsi 3.
