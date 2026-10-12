import pandas as pd
import requests

url = "https://api.openf1.org/v1/position?session_key=9158"

response = requests.get(url, timeout=30)

response.raise_for_status()

data = response.json()

positions_df = pd.DataFrame(data)

print("\n===== FIRST 5 POSITION RECORDS =====")
print(positions_df.head())

print("\n===== AVAILABLE COLUMNS =====")
print(positions_df.columns)

print("\n===== DATASET SIZE =====")
print(positions_df.shape)
