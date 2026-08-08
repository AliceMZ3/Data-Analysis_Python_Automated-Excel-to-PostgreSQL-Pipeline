
import pandas as pd

FILE_PATH = 'data/raw/sales.xlsx'

def main():
    df = pd.read_excel(FILE_PATH)

    print(df)

    print('\n Dataset info:')
    df.info()

    print('\nStat summary:')
    print(df.describe())

main()