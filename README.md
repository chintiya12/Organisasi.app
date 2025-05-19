# Aplikasi Organisasi Mahasiswa 
Aplikasi ini merupakan sistem informasi sederhana berbasis terminal (CLI) yang digunakan untuk melihat daftar, informasi, dan melakukan pendaftaran ke organisasi mahasiswa.

## 1. Pendahuluan
### 1.1 Tujuan
### 1.2 Lingkup
### 1.3 Definisi dan Istilah

---

## 2. Deskripsi Umum

### 2.1 Fungsi Utama Sistem
Aplikasi CLI untuk pengelolaan informasi dan pendaftaran organisasi kampus oleh mahasiswa.

### 2.2 Lingkungan Pengembangan
- Python 3.x
- Platform: Linux, macOS, Windows
- Text editor: VSCode

### 2.3 Asumsi & Ketergantungan
- Data tidak disimpan ke database, hanya disimpan sementara di memori
- Input pengguna dilakukan secara manual melalui terminal

### 2.4 Karakteristik Pengguna
Pengguna sistem adalah 

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
5. Keluar

## 5.2 Input Pengguna
1. Input angka 1–5 untuk navigasi
2. Input nama organisasi harus sesuai dengan daftar yang tersedia
3. Input nama mahasiswa bersifat bebas (non-kosong)


## Fitur Aplikasi

- Menampilkan daftar organisasi mahasiswa
- Melihat informasi detail setiap organisasi
- Melakukan pendaftaran ke organisasi yang dipilih
- Melihat daftar seluruh pendaftar

## Daftar Organisasi

Aplikasi ini mencakup total 27 organisasi, terdiri dari berbagai jenis:

### Ormawa
- BEM (Badan Eksekutif Mahasiswa)
- MPM (Majelis Permusyawaratan Mahasiswa)

### Keagamaan
- USWAH
- Hindu Dharma
- KMK (Keluarga Mahasiswa Katolik)
- PMK AGAPE

### Seni dan Budaya
- Seni Tari 
- Paduan Suara Mahasiswa Gita Advayatva
- Teater Hijau 51
- Band
- ASPIRASI
- Master of Ceremony (MC)
- Unit Fotografi dan Videografi (UFO)

### Olahraga dan Bela Diri
- Bulu Tangkis
- Bola Voli
- Basket 
- Tarung Derajat
- Catur
- JU JIT-SU
- Pencak Silat
- Taekwondo
- Sepakbola

### Kepemimpinan dan Lainnya
- Conference
- KSR PMI 
- AIESEC
- Content Creator Club (C3)
- E-Sport
- MAPALA
- Resimen Mahasiswa
