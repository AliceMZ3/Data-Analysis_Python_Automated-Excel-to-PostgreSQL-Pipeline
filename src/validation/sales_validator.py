import pandas as pd

EXPECTED_COLUMNS ={
    'transaction_id',
    'date',
    'customer',
    'product',
    'category',
    'quantity',
    'unit_price',
    'region',
}

def validate_columns(df: pd.DataFrame)-> None:
    """
    Validate that the DataFrame contains the expected columns.

    Raises
    ------
    ValueError
        If required columns are missing.
    """

    actual_columns = set((df.columns))

    missing_columns = EXPECTED_COLUMNS - actual_columns

    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")

def validate_data_types(df: pd.DataFrame) -> None:
    """
    Validate the data types of columns.
    """

    if not pd.api.types.is_integer_dtype(df["transaction_id"]):
        raise ValueError("transaction_id must contain integers.")

    if not pd.api.types.is_integer_dtype(df["quantity"]):
        raise ValueError("quantity must contain integers.")

    if not pd.api.types.is_numeric_dtype(df["unit_price"]):
        raise ValueError('unit_price must contain numeric values.')

    if not pd.api.types.is_datetime64_any_dtype(df['date']):
        raise ValueError('date must contain valid datetime values.')

def validate_missing_values(df: pd.DataFrame) -> None:
    """
    Ensure required fields do not contain missing values.
    """

    required_columns = [
    'transaction_id',
    'date',
    'customer',
    'product',
    'category',
    'quantity',
    'unit_price',
    'region',
    ]

    missing_values = df[required_columns].isnull().sum()

    #Boolean mask usage lol
    columns_with_missing_values = missing_values[missing_values>0]

    if not columns_with_missing_values.empty:
        raise ValueError(f"Missing values found:\n{columns_with_missing_values.to_string()}")

def validate_duplicates(df: pd.DataFrame)-> None:
    """
    Ensures transaction IDs are unique.
    """

    duplicate_transactions = df[
        df["transaction_id"].duplicated(keep=False)
    ]

    if not duplicate_transactions.empty:
        duplicate_ids = (
            duplicate_transactions["transaction_id"].unique().tolist()
        )

        raise ValueError(
            f'Duplicate transactions IDs were found: {duplicate_ids}'
        )

def validate_rules(df: pd.DataFrame)-> None:
    """
    Business rule validation for sales data
    """

    if (df["quantity"] <= 0).any():
        raise ValueError("Quantity must be greater than zero.")

    if (df['unit_price'] < 0).any():
        raise ValueError('Unit price cannot be negative.')

def validate_sales_data(df: pd.DataFrame) -> None:
    """
    Run all validation checks for the sales dataset.
    """

    validate_columns(df)
    validate_data_types(df)
    validate_missing_values(df)
    validate_duplicates(df)
    validate_rules(df)