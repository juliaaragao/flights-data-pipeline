import pandas as pd
from config import FLIGHTS_CSV


def extract_flights() -> pd.DataFrame:
    """
    Extracts flight data from the raw CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the flight data.
    """
    if not FLIGHTS_CSV.exists():
        raise FileNotFoundError(f"The file {FLIGHTS_CSV} does not exist.")
    
    print(f"Extracting data")
    df = pd.read_csv(FLIGHTS_CSV)

    print(f"Data loaded successfully")
    return df

if __name__ == "__main__":  
    # Test the extraction function
    flights_df = extract_flights()
    print(flights_df.head())
