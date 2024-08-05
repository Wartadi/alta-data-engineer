import pandas as pd
from fastparquet import ParquetFile
from sqlalchemy import create_engine, text
from sqlalchemy.types import BigInteger, DateTime, Boolean, Float, Integer
from sqlalchemy.exc import SQLAlchemyError
from prettytable import PrettyTable

class Extraction:
    def __init__(self) -> None:
        self.path: str
        self.dataframe = pd.DataFrame()

    def local_file(self, path: str) -> pd.DataFrame:
        """Membaca file Parquet dan memproses DataFrame by Wartadi DE4"""
        self.path = path
        self.__read_parquetfile()

        # Mengatur tampilan agar semua kolom ditampilkan
        pd.set_option('display.max_columns', None)
        
        # Menampilkan nama-nama kolom
        print("\n=== Task 1: Nama-nama kolom dalam DataFrame by Wartadi DE4 ===")
        print(self.dataframe.columns.tolist())
        
        # Menampilkan DataFrame sebelum dibersihkan dan di-cast
        print("\n=== Task 2: DataFrame dari file Parquet sebelum dibersihkan dan di-cast by Wartadi DE4 ===")
        self.print_table(self.dataframe.head(10))
        
        # Membersihkan dataset
        self.clean_data()
        
        # Menampilkan DataFrame setelah dibersihkan
        print("\n=== Task 3: DataFrame setelah dibersihkan by Wartadi DE4 ===")
        self.print_table(self.dataframe.head(10))
        
        # Menentukan skema tipe data dan meng-cast kolom
        self.cast_data()
        
        # Menampilkan informasi schema DataFrame setelah casting
        print("\n=== Task 4: Informasi Schema DataFrame setelah di-cast by Wartadi DE4 ===")
        print(self.dataframe.info())
        
        # Menampilkan DataFrame setelah di-cast
        print("\n=== Task 5: DataFrame setelah di-cast by Wartadi DE4 ===")
        self.print_table(self.dataframe.head(10))
        
        print("\n Jawabannya ada di postgreSQL, terpisah kami hehehe")
        
        return self.dataframe
    
    def __read_parquetfile(self) -> None:
        """Membaca file Parquet menjadi DataFrame by Wartadi DE4"""
        parquetfile = ParquetFile(self.path)
        self.dataframe = parquetfile.to_pandas()

    def clean_data(self) -> None:
        """Membersihkan DataFrame dari nilai NaN, duplikat, dan data invalid by Wartadi DE4"""
        self.dataframe.dropna(inplace=True)
        self.dataframe.drop_duplicates(inplace=True)
        self.dataframe = self.dataframe[self.dataframe["trip_distance"] >= 0]

    def cast_data(self) -> None:
        """Meng-cast kolom DataFrame ke tipe data yang sesuai by Wartadi DE4"""
        self.dataframe["passenger_count"] = self.dataframe["passenger_count"].astype("Int8")
        self.dataframe["store_and_fwd_flag"] = self.dataframe["store_and_fwd_flag"].map({"N": False, "Y": True}).astype("boolean")
        self.dataframe["tpep_pickup_datetime"] = pd.to_datetime(self.dataframe["tpep_pickup_datetime"])
        self.dataframe["tpep_dropoff_datetime"] = pd.to_datetime(self.dataframe["tpep_dropoff_datetime"])

    def print_table(self, df: pd.DataFrame) -> None:
        """Mencetak DataFrame dalam format tabel dengan garis putus-putus by Wartadi DE4"""
        # Display up to 5 columns and summarize the rest
        num_columns_to_display = 5
        columns_to_display = df.columns[:num_columns_to_display]
        columns_summary = df.columns[num_columns_to_display:]
        
        df_display = df[columns_to_display]
        
        if columns_summary.size > 0:
            # Add a summary column for the remaining columns
            df_display["..."] = df[columns_summary[0]].apply(lambda x: f"Other columns ({len(columns_summary)} more)")

        x = PrettyTable()
        x.field_names = df_display.columns.tolist()
        
        # Adjust column alignment and width
        for col in df_display.columns:
            x.align[col] = "l"  # Left-align all columns
            x.max_width[col] = max(df_display[col].astype(str).map(len).max(), len(col))  # Set max width based on data

        for row in df_display.itertuples(index=False):
            x.add_row(row)

        print(x)

class Load:
    def __init__(self) -> None:
        self.engine = None
    
    def __create_connection(self) -> None:
        """Membuat koneksi ke database PostgreSQL by Wartadi DE4"""
        user = "postgres"
        password = "admin"
        host = "localhost"
        database = "mydb"
        port = 5434
        conn_string = f"postgresql://{user}:{password}@{host}:{port}/{database}"
        self.engine = create_engine(conn_string) 

    def to_postgres(self, db_name: str, data: pd.DataFrame) -> None:
        """Mengimpor DataFrame ke dalam database PostgreSQL by Wartadi DE4"""
        self.__create_connection()
        df_schema = {
            "VendorID": BigInteger,
            "tpep_pickup_datetime": DateTime,
            "tpep_dropoff_datetime": DateTime,
            "passenger_count": BigInteger,
            "trip_distance": Float,
            "RatecodeID": Float,
            "store_and_fwd_flag": Boolean,
            "PULocationID": Integer,
            "DOLocationID": Integer,
            "payment_type": Integer,
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
        try:
            data.to_sql(name=db_name, con=self.engine, if_exists="replace", index=False, schema="public", dtype=df_schema, method=None, chunksize=5000)
            
            # Menghitung dan menampilkan jumlah baris yang di-ingest
            with self.engine.connect() as connection:
                result = connection.execute(text(f"SELECT COUNT(*) FROM public.{db_name}"))
                row_count = result.scalar()
                print(f"\n=== Task 6: Jumlah baris yang di-ingest by Wartadi DE4 ===")
                print(f"Jumlah baris yang di-ingest: {row_count}")
        except SQLAlchemyError as err:
            print(f"error >> {err}")

def main():
    extract = Extraction()
    file_path = "/Users/wartadi/Desktop/alta/ingestion-data-main/dataset/yellow_tripdata_2023-01.parquet"
    df_result = extract.local_file(file_path)
    
    load = Load()
    db_name = "data_parquet_by_wartadi"
    load.to_postgres(db_name, df_result)

if __name__ == "__main__":
    main()
