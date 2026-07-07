# Laporan Responsi Praktikum Sistem Terdistribusi dan Terdesentralisasi

**Nama:** Ardian Kurniawan  
**Repository:** [13ardiankurniawan/prak-dis-dec](https://github.com/13ardiankurniawan/prak-dis-dec)  

---

## 🛠️ CPMK 1: Setup YugabyteDB via Docker & Pengisian Data

Langkah awal adalah menjalankan database YugabyteDB menggunakan Docker, masuk ke shell interaktif, dan melakukan inisialisasi tabel data.

### 1. Menjalankan Container YugabyteDB
```bash
docker run -d --name yugabyte-node1 -p 7000:7000 -p 9000:9000 -p 5433:5433 -p 9042:9042 yugabytedb/yugabyte:latest bin/yugabyted start --daemon=false



docker exec -it yugabyte-node1 bin/ysqlsh -h 172.17.0.2

-- Membuat Tabel 1: mahasiswa
CREATE TABLE mahasiswa (
    id SERIAL PRIMARY KEY,
    nama VARCHAR(100),
    jurusan VARCHAR(50)
);

-- Mengisi data ke Tabel mahasiswa
INSERT INTO mahasiswa (nama, jurusan) VALUES 
('Alice', 'Informatika'), 
('Bob', 'Sistem Informasi'), 
('Charlie', 'Teknik Elektro'), 
('David', 'Informatika'), 
('Emma', 'Sistem Informasi');

-- Membuat Tabel 2: mata_kuliah
CREATE TABLE mata_kuliah (
    id SERIAL PRIMARY KEY,
    nama_mk VARCHAR(100),
    sks INT
);

-- Mengisi data ke Tabel mata_kuliah
INSERT INTO mata_kuliah (nama_mk, sks) VALUES 
('Sistem Terdistribusi', 3), 
('Basis Data', 4), 
('Pemrograman Web', 3), 
('Kecerdasan Buatan', 3), 
('Jaringan Komputer', 3);

graph TD
    A[User Mengirim Transaksi] --> B[Transaksi Masuk ke Mempool]
    B --> C[RANDAO Memilih 1 Validator sebagai Block Proposer]
    C --> D[Proposer Membuat & Menyiapkan Blok Baru]
    D --> E[Komite Validator Melakukan Atestasi/Validasi]
    E -- Blok Valid --> F[Blok Ditambahkan ke Rantai Utama]
    E -- Blok Palsu/Curang --> G[Validator Terkena Slashing / Saldo Dipotong]
    F --> H[Transaksi Mencapai Tahap Finalisasi Selesai 1 Epoch]
