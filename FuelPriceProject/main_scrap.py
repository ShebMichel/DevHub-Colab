import os
import time
import pandas as pd
import requests
from tqdm import tqdm

# URL pattern for the CSVs
BASE_URL = "https://warsydprdstafuelwatch.blob.core.windows.net/historical-reports/FuelWatchRetail-{month:02d}-{year}.csv"

# Directory to store downloaded files
DOWNLOAD_DIR = "fuel_data"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Date range
START_YEAR, START_MONTH = 2001, 1
END_YEAR, END_MONTH = 2025, 2

# Generate date list
date_range = [(year, month) for year in range(START_YEAR, END_YEAR + 1)
              for month in range(1, 13) if not (year == END_YEAR and month > END_MONTH)]

def is_connected():
    """Check if the internet is available."""
    try:
        requests.get("https://www.google.com", timeout=5)  # Test with Google
        return True
    except requests.ConnectionError:
        return False

# Download CSV files
for year, month in tqdm(date_range, desc="Downloading CSVs"):
    url = BASE_URL.format(year=year, month=month)
    file_path = os.path.join(DOWNLOAD_DIR, f"FuelWatchRetail-{month:02d}-{year}.csv")

    if os.path.exists(file_path):  # Skip if already downloaded
        continue

    while True:  # Keep trying until successful
        if is_connected():
            try:
                response = requests.get(url, stream=True, timeout=10)
                if response.status_code == 200:
                    with open(file_path, "wb") as f:
                        f.write(response.content)
                    break  # Success, move to next file
                else:
                    print(f"Failed to download {url} (Status: {response.status_code})")
                    break  # Skip to next file if it's unavailable
            except requests.exceptions.RequestException as e:
                print(f"Error downloading {url}: {e}, retrying...")
        else:
            print("No internet connection. Pausing downloads...")
            while not is_connected():  # Wait until connection is restored
                time.sleep(5)  # Check every 5 seconds
            print("Internet restored. Resuming downloads...")

# Merge CSV files
all_data = []
for year, month in date_range:
    file_path = os.path.join(DOWNLOAD_DIR, f"FuelWatchRetail-{month:02d}-{year}.csv")
    if os.path.exists(file_path):
        try:
            df = pd.read_csv(file_path)
            df["Year"] = year
            df["Month"] = month
            all_data.append(df)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

# Save merged CSV
if all_data:
    merged_df = pd.concat(all_data, ignore_index=True)
    merged_csv_path = "fuel_prices_2001_2025.csv"
    merged_df.to_csv(merged_csv_path, index=False)
    print(f"Merged CSV saved as '{merged_csv_path}'")
else:
    print("No data files found to merge.")

