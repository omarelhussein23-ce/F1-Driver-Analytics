import pandas as pd
import requests

url = "https://api.openf1.org/v1/sessions"

params = {
    "year": 2023,
    "country_name": "Singapore",
    "session_name": "Race"
}

response = requests.get(url, params=params, timeout=30)

response.raise_for_status()

data = response.json()

df = pd.DataFrame(data)

if df.empty:
    print("No race session found!")
else:
    print("\n===== 2023 SINGAPORE GRAND PRIX =====")

    print(
        df[["session_key", "session_name", "date_start"]]
        .to_string(index=False)
    )

    race_session_key = df["session_key"].iloc[0]

    print(f"\nRace session key: {race_session_key}")
