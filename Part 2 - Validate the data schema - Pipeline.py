import logging
import pandas as pd

# ---------------------------------------------------------
# Configure logging
# ---------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------------------------------------------------
# Load raw CSV with proper exception handling
# ---------------------------------------------------------
def load_raw_csv(file_path: str) -> pd.DataFrame:
    """
    Load the raw CSV file with logging and safe exception handling.
    """
    logging.info(f"Attempting to load CSV file: {file_path}")

    try:
        df = pd.read_csv(file_path)
        logging.info(f"CSV loaded successfully. Shape: {df.shape}")
        return df

    except FileNotFoundError as e:
        logging.error(f"File not found: {file_path}")
        raise e

    except pd.errors.ParserError as e:
        logging.error(f"CSV parsing error: {e}")
        raise e

    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
        raise e

# ---------------------------------------------------------
# Validate data schema
# ---------------------------------------------------------
def validate_schema(df: pd.DataFrame, expected_columns: list) -> None:
    """
    Validate that all expected columns are present in the dataset.
    """
    logging.info("Validating data schema...")

    missing_columns = [col for col in expected_columns if col not in df.columns]

    if missing_columns:
        logging.error(f"Schema validation failed. Missing columns: {missing_columns}")
        raise ValueError(f"Missing columns in dataset: {missing_columns}")

    logging.info("Schema validation successful. All expected columns are present.")

# ---------------------------------------------------------
# Main pipeline entry point
# ---------------------------------------------------------
if __name__ == "__main__":
    logging.info("Starting data pipeline...")

    raw_file = "Metro_Interstate_Traffic_Volume.csv"

    df = load_raw_csv(raw_file)

    expected_columns = [
        "holiday",
        "temp",
        "rain_1h",
        "snow_1h",
        "clouds_all",
        "weather_main",
        "weather_description",
        "date_time",
        "traffic_volume"
    ]

    validate_schema(df, expected_columns)

    logging.info("Pipeline completed successfully.")