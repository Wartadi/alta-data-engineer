import pandas as pd
from fastparquet import ParquetFile
from sqlalchemy import create_engine, text
from sqlalchemy.types import BigInteger, Float, Boolean, DateTime
import os

# Soal 1 dan 2: Jalankan parquet file
file_path = os.path.abspath('./dataset/yellow_tripdata_2023-01.parquet')
df = pd.read_parquet(file_path)

# Investigasi data dalam Data Frame
print("DataFrame head data:")
print(df.head())

print("\nDataFrame schema:")
print(df.info())

# Soal 3: Bersihkan data trip kuning
# Casting pandas
df["passenger_count"] = df["passenger_count"].astype("Int8")
df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])

# Atur nilai NUll
df["passenger_count"].fillna(0, inplace=True)
df["store_and_fwd_flag"] = df["store_and_fwd_flag"].replace(["N", "Y"], [False, True]).astype("boolean")
df["store_and_fwd_flag"].fillna(False, inplace=True)

print("\nCleaned DataFrame:")
print(df.head())
print(df.info())

# Soal 4: Define the data type schema
df_schema = {
    "VendorID": BigInteger,
    "tpep_pickup_datetime": DateTime,
    "tpep_dropoff_datetime": DateTime,
    "passenger_count": BigInteger,
    "trip_distance": Float,
    "RatecodeID": BigInteger,
    "store_and_fwd_flag": Boolean,
    "PULocationID": BigInteger,
    "DOLocationID": BigInteger,
    "payment_type": BigInteger,
    "fare_amount": Float,
    "extra": Float,
    "mta_tax": Float,
    "tip_amount": Float,
    "tolls_amount": Float,
    "improvement_surcharge": Float,
    "total_amount": Float,
    "congestion_surcharge": Float,
    "airport_fee": Float
}

# Soal 5: Ingest the Yellow Trip dataset to PostgreSQL
def create_connection():
    user = "postgres"
    password = "admin"
    host = "localhost"
    database = "mydb"
    port = 5437  
    conn_string = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(conn_string)
    return engine

def to_postgres(df, table_name, schema):
    engine = create_connection()
    try:
        df.to_sql(name=table_name, con=engine, if_exists="replace", index=False, schema="public", dtype=schema, method=None, chunksize=5000)
        print("Data ingestion successful.")
    except Exception as e:
        print("Data ingestion error:", e)

to_postgres(df, "yellow_tripdata", df_schema)

# Soal 6: Count how many rows are ingested
def count_rows(table_name):
    engine = create_connection()
    query = text(f"SELECT COUNT(1) FROM {table_name}")
    with engine.connect() as connection:
        result = connection.execute(query)
        count = result.fetchone()[0]
        print(f"Number of rows in {table_name}: {count}")

count_rows("yellow_tripdata")
