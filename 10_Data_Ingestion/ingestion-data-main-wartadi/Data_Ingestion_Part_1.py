import pandas as pd
from prettytable import PrettyTable

# 1. Memuat dataset dengan low_memory=False untuk menangani peringatan tipe campuran
df = pd.read_csv("/Users/wartadi/Desktop/alta/ingestion-data-main/dataset/yellow_tripdata_2020-07.csv", low_memory=False)

# Menampilkan beberapa baris pertama dari data yang dimuat
def print_table_with_index(df: pd.DataFrame, num_display_columns: int = 5) -> None:
    """Mencetak DataFrame dalam format tabel dengan nomor index baris dan batas kolom."""
    
    # Menentukan kolom yang ditampilkan
    displayed_columns = df.columns[:num_display_columns]
    
    # Membuat objek PrettyTable
    x = PrettyTable()
    x.field_names = ["Index"] + displayed_columns.tolist()
    
    # Menentukan lebar kolom
    max_widths = {col: max(df[col].astype(str).map(len).max(), len(col)) for col in displayed_columns}
    max_widths["Index"] = len("Index")
    
    # Menambahkan baris ke tabel
    for idx, row in df.iterrows():
        displayed_row = [idx] + [str(row[col]) for col in displayed_columns]
        x.add_row(displayed_row)
    
    # Menampilkan tabel
    print(x)
    print("="*50)

print("="*50)
print("1. DataFrame setelah memuat dataset:")
print_table_with_index(df.head())
print("\n")

# 2. Mengganti nama kolom menjadi snake_case
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Menampilkan nama-nama kolom setelah diganti menjadi snake_case
print("="*50)
print("2. Nama kolom setelah diganti menjadi snake_case:")
print(df.columns.tolist())
print("="*50, "\n")

# 3. Memilih kolom-kolom yang relevan dan 10 baris teratas dengan jumlah penumpang tertinggi
selected_columns = [
    'vendorid', 'passenger_count', 'trip_distance', 'payment_type',
    'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount',
    'improvement_surcharge', 'total_amount', 'congestion_surcharge'
]
df_selected = df[selected_columns]

# Memilih 10 baris teratas dengan jumlah penumpang tertinggi
top_10_passenger_count = df_selected.nlargest(10, 'passenger_count')

# Fungsi untuk mencetak DataFrame dengan format tabel mirip contoh
def print_table_with_summary(df: pd.DataFrame, num_display_columns: int = 9) -> None:
    """Mencetak DataFrame dalam format tabel mirip contoh dengan pemisah kolom dan ringkasan kolom."""
    
    # Menentukan kolom yang ditampilkan dan yang tidak ditampilkan
    displayed_columns = df.columns[:num_display_columns]
    hidden_columns = df.columns[num_display_columns:]
    
    # Membuat objek PrettyTable
    x = PrettyTable()
    x.field_names = ["Index"] + displayed_columns.tolist() + ["Other columns"]
    
    # Menentukan lebar kolom
    max_widths = {col: max(df[col].astype(str).map(len).max(), len(col)) for col in displayed_columns}
    max_widths["Other columns"] = 20
    max_widths["Index"] = len("Index")
    
    # Menambahkan baris ke tabel
    for idx, row in df.iterrows():
        # Menampilkan data kolom yang ditampilkan
        displayed_row = [idx] + [str(row[col]) for col in displayed_columns]
        # Menyertakan ringkasan untuk kolom yang tidak ditampilkan
        hidden_summary = f"Other columns ({len(hidden_columns)} more)"
        x.add_row(displayed_row + [hidden_summary])
    
    # Menampilkan tabel
    print("\n" + "="*50)
    print(x)
    print("="*50)
    print(f"Menampilkan {num_display_columns} kolom dari {len(df.columns)} kolom total.")
    print(f"Kolom yang tidak ditampilkan ({len(hidden_columns)} kolom):")
    print(", ".join(hidden_columns))
    print("="*50)

print("="*50)
print("3. 10 baris teratas dengan jumlah penumpang tertinggi:")
print_table_with_summary(top_10_passenger_count)
print("\n")

# 4. Mengubah tipe data dan menampilkan DataFrame setelah casting
print("="*50)
print("4. Nilai NaN sebelum mengubah tipe data:")
print(df_selected.isna().sum())
print("="*50, "\n")

# Menggunakan .loc untuk mengisi nilai NaN dan mengubah tipe
df_selected.loc[:, 'vendorid'] = df_selected['vendorid'].fillna(0).astype(int)
df_selected.loc[:, 'passenger_count'] = df_selected['passenger_count'].fillna(0).astype(int)
float_columns = [
    'trip_distance', 'fare_amount', 'extra', 'mta_tax', 'tip_amount',
    'tolls_amount', 'improvement_surcharge', 'total_amount', 'congestion_surcharge'
]
for col in float_columns:
    df_selected.loc[:, col] = df_selected[col].fillna(0.0).astype(float)

# Menampilkan DataFrame setelah mengubah tipe data
print("="*50)
print("4. DataFrame setelah mengubah tipe data:")
print_table_with_summary(df_selected.head())
print("\n")