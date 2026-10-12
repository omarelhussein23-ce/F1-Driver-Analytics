import pandas as pd

drivers = {
    "Driver": ["Max Verstappen", "Charles Leclerc", "Lando Norris", "Lewis Hamilton"],
    "Team": ["Red Bull", "Ferrari", "McLaren", "Ferrari"],
    "Points": [250, 220, 240, 180],
    "Wins": [5, 3, 4, 1],
    "Podiums": [8, 6, 7, 4]
}

df = pd.DataFrame(drivers)


def compare_drivers(data, driver1, driver2):
    first_driver = data[
        data["Driver"].str.lower() == driver1.lower()
        ]

    second_driver = data[
        data["Driver"].str.lower() == driver2.lower()
        ]

    if first_driver.empty or second_driver.empty:
        print("\nOne or both drivers were not found!")
        print("Available drivers:")
        for name in data["Driver"]:
            print(f"- {name}")
        return

    first = first_driver.iloc[0]
    second = second_driver.iloc[0]

    points1 = first["Points"]
    points2 = second["Points"]

    wins1 = first["Wins"]
    wins2 = second["Wins"]

    podiums1 = first["Podiums"]
    podiums2 = second["Podiums"]

    difference = abs(points1 - points2)

    print("\n===== F1 DRIVER COMPARISON =====")
    print(f"\n{first['Driver']} vs {second['Driver']}")

    print(f"Points: {points1} vs {points2}")
    print(f"Wins: {wins1} vs {wins2}")
    print(f"Podiums: {podiums1} vs {podiums2}")

    print(f"\nPoints difference: {difference}")

    if points1 > points2:
        print(f"Driver with more points: {first['Driver']}")
    elif points2 > points1:
        print(f"Driver with more points: {second['Driver']}")
    else:
        print("Both drivers have equal points!")


def show_leaderboard(data):
    sort_by = input(
        "\nSort by (Points/Wins/Podiums): "
    ).strip().lower()

    valid_options = ["points", "wins", "podiums"]

    if sort_by not in valid_options:
        print("Invalid option! Choose Points, Wins, or Podiums.")
        return

    column = sort_by.capitalize()

    leaderboard = data.sort_values(
        by=column,
        ascending=False
    )

    leaderboard = leaderboard.reset_index(drop=True)

    leaderboard["Rank"] = range(1, len(leaderboard) + 1)

    leaderboard = leaderboard[
        ["Rank", "Driver", "Team", "Points", "Wins", "Podiums"]
    ]

    print(f"\n===== F1 LEADERBOARD BY {column.upper()} =====")
    print(leaderboard.to_string(index=False))


def main():
    print("================================")
    print("       F1 DRIVER ANALYTICS")
    print("================================")

    print("\nAvailable drivers:")
    for name in df["Driver"]:
        print(f"- {name}")

    player1 = input("\nEnter Driver 1 name: ").strip()
    player2 = input("Enter Driver 2 name: ").strip()

    compare_drivers(df, player1, player2)

    show_leaderboard(df)


if __name__ == "__main__":
    main()
