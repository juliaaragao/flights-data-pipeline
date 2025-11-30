import sqlite3
import pandas as pd
from config import CLEANED_DIR, DATABASE_PATH   

def load_data(df: pd.DataFrame) -> None:
    """Loads the transformed flight data into a SQLite database.

    This function:
    - Connects to a SQLite database (creates it if it doesn't exist)
    - Loads the transformed DataFrame into a table named 'flights'
    - If the table already exists, it replaces it

    Args:
        df (pd.DataFrame): The transformed flight data.
    """
    clean_file = CLEANED_DIR / "cleaned_flights_data.csv"
    CLEANED_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(clean_file, index=False)
    print(f"Saved cleaned data to {clean_file}")
    
    print(f"Loading data from {clean_file}")
    df = pd.read_csv(clean_file)

    # Ensure the database directory exists
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

    # Connect to SQLite database (or create it)
    conn = sqlite3.connect(DATABASE_PATH)
    try:
        df.to_sql('flights', conn, if_exists='replace', index=False)
        print(f"Data loaded into database at {DATABASE_PATH} in table 'flights'")
    finally:
        conn.close()
        print("Database connection closed.")

if __name__ == "__main__":
    test_df = pd.read_csv(CLEANED_DIR / "cleaned_flights_data.csv")
    load_data(test_df) 

