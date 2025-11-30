import pandas as pd
from extract import extract_flights
from config import CLEANED_DIR


def transform_data() -> pd.DataFrame:
    """Transforms the raw flight data.

    This function:
    - Loads raw flight data using the extract_data function.
    - Creates a FLIGHT_DATE column from YEAR, MONTH and DAY
    - Creates a binary delay flag: IS_DELAYED_15 (arrival delay >= 15 minutes)
    - Drops columns that are not needed for the delay analysis
    - Removes duplicate rows if any exist
    - Saves the cleaned dataset into the CLEANED_DIR folder

    Returns:
        pd.DataFrame: The transformed flight data.
    """
    df = extract_flights()
    print(f"Initial shape: {df.shape[0]} rows × {df.shape[1]} columns")

    # Create FLIGHT_DATE column
    df['FLIGHT_DATE'] = pd.to_datetime(df[['YEAR', 'MONTH', 'DAY']])
    print("Created FLIGHT_DATE column")

    # Create IS_DELAYED_15 column
    df["IS_DELAYED_15"] = df["ARRIVAL_DELAY"] >= 15 
    df["IS_DELAYED_15"] = df["IS_DELAYED_15"].fillna(False)
    print("Created IS_DELAYED_15 column")

    # Drop unnecessary columns
    columns_to_drop =   [
        "TAIL_NUMBER",
        "FLIGHT_NUMBER",
        "SCHEDULED_DEPARTURE",
        "DEPARTURE_TIME",
        "TAXI_OUT",
        "WHEELS_OFF",
        "SCHEDULED_TIME",
        "ELAPSED_TIME",
        "AIR_TIME",
        "WHEELS_ON",
        "TAXI_IN",
        "SCHEDULED_ARRIVAL",
        "ARRIVAL_TIME",
        "CANCELLED",
        "CANCELLATION_REASON",
        "DIVERTED",
        "YEAR", 
        "MONTH", 
        "DAY"
    ]
    existing_cols = [c for c in columns_to_drop if c in df.columns]
    df.drop(columns=existing_cols, inplace=True)
    print(f"Dropped columns: {existing_cols}")

    #If duplicates exist, drop them
    initial_rows = df.shape[0]
    df.drop_duplicates(inplace=True)
    final_rows = df.shape[0]
    if final_rows < initial_rows:
        print(f"Dropped {initial_rows - final_rows} duplicate rows")
    else:
        print("No duplicate rows found")

    # Save cleaned data
    CLEANED_DIR.mkdir(parents=True, exist_ok=True)
    cleaned_file_path = CLEANED_DIR / 'cleaned_flights_data.csv'
    df.to_csv(cleaned_file_path, index=False)
    print(f"Cleaned data saved to {cleaned_file_path}")
    print(f"Transformed shape: {df.shape[0]} rows × {df.shape[1]} columns") 

    return df


if __name__ == "__main__":  
    # Test the transformation function
    transformed_df = transform_data()
    print(transformed_df.head())