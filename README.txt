MINILAB BIG DATA - DATA INGESTION

Deskripsi:
Project ini merupakan implementasi ingestion data dari:
- RDBMS (PostgreSQL)
- File CSV/XLSX

Data kemudian disimpan ke object storage MinIO.


PERSIAPAN:
Pastikan sudah terinstall:
- Docker Desktop
- Python 3.x


CARA MENJALANKAN:

1. Jalankan Docker (PostgreSQL & MinIO)
   Jalankan perintah:
   docker-compose up -d

2. Aktifkan Virtual Environment
   python -m venv venv
   venv\Scripts\activate

3. Install Library
   pip install pandas sqlalchemy psycopg2-binary minio openpyxl

4. Jalankan Script Ingestion (DIsini masih menggunakan script yang dipisah untuk tipe data yang berbeda)
   python ingestion/ingest_rdbms.py, python ingestion/ingest_csv.py, python ingestion/ingest_xlsx.py


AKSES MINIO:
Buka browser:
http://localhost:9001

Login:
username: admin
password: admin123


STRUKTUR DATA DI MINIO:
raw/
  rdbms/
  csv/
  xlsx/


SELESAI