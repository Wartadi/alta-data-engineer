# table_formatter.py
from prettytable import PrettyTable
import pandas as pd

def print_table(df: pd.DataFrame) -> None:
    """Mencetak DataFrame dalam format tabel dengan garis putus-putus by Wartadi DE4"""
    # Display up to 5 columns and summarize the rest
    num_columns_to_display = 5
    columns_to_display = df.columns[:num_columns_to_display]
    columns_summary = df.columns[num_columns_to_display:]
    
    df_display = df[columns_to_display].copy()
    
    if not columns_summary.empty:
        # Add a summary column for the remaining columns
        df_display["..."] = df[columns_summary[0]].apply(lambda x: f"Other columns ({len(columns_summary)} more)")

    # Add index to df_display
    df_display.reset_index(inplace=True)
    df_display.rename(columns={'index': 'Row Index'}, inplace=True)
    
    x = PrettyTable()
    x.field_names = df_display.columns.tolist()
    
    # Adjust column alignment and width
    for col in df_display.columns:
        x.align[col] = "l"  # Left-align all columns
        x.max_width[col] = max(df_display[col].astype(str).map(len).max(), len(col))  # Set max width based on data

    for row in df_display.itertuples(index=False):
        x.add_row(row)

    print(x)
