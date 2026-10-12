import pandas as pd
import requests

url = "https://api.openf1.org/v1/drivers?session_key=9158"

response = requests.get(url, timeout=15)

response.raise_for_status()

data = response.json()

df = pd.DataFrame(data)

print(df[["full_name", "driver_number", "team_name"]])
print(f"\nTotal drivers: {len(df)}")