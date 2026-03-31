import pandas as pd
from minio import Minio
from io import BytesIO

df = pd.read_csv("data/sample.csv")

client = Minio(
    "localhost:9000",
    access_key="minioadmin",
    secret_key="minio123",
    secure=False
)

csv_bytes = df.to_csv(index=False).encode('utf-8')

client.put_object(
    "raw",
    "csv/sample.csv",
    BytesIO(csv_bytes),
    len(csv_bytes)
)

print("Sukses CSV → MinIO")