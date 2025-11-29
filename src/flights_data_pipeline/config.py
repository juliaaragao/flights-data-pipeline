from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parents[2]
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
CLEANED_DIR = DATA_DIR / "cleaned"
SAMPLES_DIR = DATA_DIR / "sample"


DATABASE_DIR = BASE_DIR / "database"
DATABASE_PATH = DATABASE_DIR / "flights_data.db"

#Print paths for verification
print(f"Base Directory: {BASE_DIR}")
print(f"Data Directory: {DATA_DIR}")
print(f"Raw Data Directory: {RAW_DIR}")
print(f"Cleaned Data Directory: {CLEANED_DIR}")
print(f"Sample Data Directory: {SAMPLES_DIR}")
print(f"Database Directory: {DATABASE_DIR}")
print(f"Database Path: {DATABASE_PATH}")
