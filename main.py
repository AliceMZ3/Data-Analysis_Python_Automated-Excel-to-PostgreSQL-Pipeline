from src.ingestion.excel_reader import read_excel_file

FILE_PATH = 'data/raw/sales.xlsx'

def main():
    df = read_excel_file(FILE_PATH)

    
    print("\nFirst five rows:")
    print(df.head())

    print('\nDataset dimentions/shape')
    print(f"Rows: {df.shape[0]}")
    print(f'Columns: {df.shape[1]}')

    print('\nColumn names:')
    print(df.columns.to_list())

    print('\nData types:')
    print(df.dtypes)

    print('\nMissing values:')
    print(df.isnull().sum())

    print('\nDuplicate rows:')
    print(df.duplicated().sum())
main()