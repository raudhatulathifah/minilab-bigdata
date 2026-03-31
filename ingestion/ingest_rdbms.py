import pandas as pd
from sqlalchemy import create_engine
from minio import Minio
from io import BytesIO

# koneksi postgres
engine = create_engine("postgresql://admin:admin123@127.0.0.1:5433/bigdata")

df = pd.read_sql("SELECT * FROM pelanggan", engine)

# koneksi minio
client = Minio(
    "localhost:9000",
    access_key="minioadmin",
    secret_key="minio123",
    secure=False
)

csv_bytes = df.to_csv(index=False).encode('utf-8')

client.put_object(
    "raw",
    "rdbms/pelanggan.csv",
    BytesIO(csv_bytes),
    len(csv_bytes)
)

print("Sukses RDBMS → MinIO")