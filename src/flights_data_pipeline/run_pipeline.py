from extract import extract_flights
from transform import transform_data
from load import load_data

def run_pipeline():
    print(" 🚀 STARTING ETL PIPELINE\n")

    # Extract
    print(" 📥 STEP 1 — Extracting raw data...")
    df_raw = extract_flights()
    print(f"✔ Extracted {df_raw.shape[0]} rows.")

    # Transform
    print(" 🔧 STEP 2 — Transforming data...")
    df_clean = transform_data()
    print(f"✔ Cleaned dataset: {df_clean.shape[0]} rows × {df_clean.shape[1]} columns.")

    # Load
    print(" 💾 STEP 3 — Loading data into SQLite...")
    load_data(df_clean)
    print("✔ Loaded into database successfully.")

    print(" 🎉 ETL PIPELINE FINISHED SUCCESSFULLY")

if __name__ == "__main__":
    run_pipeline()