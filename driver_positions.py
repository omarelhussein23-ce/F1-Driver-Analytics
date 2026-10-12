import pandas as pd
import requests

drivers_url = "https://api.openf1.org/v1/drivers?session_key=9158"
positions_url = "https://api.openf1.org/v1/position?session_key=9158"

drivers_response = requests.get(drivers_url, timeout=30)
drivers_response.raise_for_status()

drivers_data = drivers_response.json()
drivers_df = pd.DataFrame(drivers_data)

positions_response = requests.get(positions_url, timeout=30)
positions_response.raise_for_status()

positions_data = positions_response.json()
positions_df = pd.DataFrame(positions_data)

combined_df = pd.merge(
    drivers_df,
    positions_df,
    on="driver_number",
    how="inner"
)

print("\n===== F1 DRIVER POSITIONS =====")

print(
    combined_df[
        ["full_name", "team_name", "position", "date"]
    ].head(10).to_string(index=False)
)

print("\n===== COMBINED DATASET SIZE =====")
print(combined_df.shape)

print("\n===== UNIQUE DRIVERS =====")
print(combined_df["driver_number"].nunique())
