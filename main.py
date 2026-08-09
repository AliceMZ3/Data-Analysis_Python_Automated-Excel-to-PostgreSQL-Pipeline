from src.ingestion.excel_reader import read_excel_file
from src.validation.sales_validator import validate_sales_data
FILE_PATH = 'data/raw/sales.xlsx'

def main():
    df = read_excel_file(FILE_PATH)

    
    validate_sales_data(df)
    print('Data validation successful.')\
    
main()