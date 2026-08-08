from pathlib import Path
import pandas as pd

def read_excel_file(file_path: str|Path)-> pd.DataFrame:
    """
    Reading Excel file and returning its contents as a DataFrame object.

    Parameters
    ----------
    file_path:
        Path to the Excel file.

    Returns
    _______
    pd.DataFrame
        Data extracted from the Excel file.

    Raises
    ______
    FileNotFoundError
        If the specified file does not exist.
    ValueError
        If the file is not an Excel workbook.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found in specified path: {path}")

    if path.suffix.lower() not in {".xlsx", ".xls"}:
        raise ValueError(f"Unsupported file type: {path.suffix}")

    return pd.read_excel(path)