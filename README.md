# F1 Driver Analytics

A Python project for analyzing Formula 1 driver statistics using Pandas and the OpenF1 API.

## Features

- Compare drivers by points, wins, and podiums using a sample dataset
- Generate leaderboards sorted by different statistics
- Retrieve real Formula 1 driver information through the OpenF1 API
- Retrieve session position observations
- Merge driver and position datasets using Pandas
- Look up historical Formula 1 race sessions

## Technologies

- Python
- Pandas
- Requests
- OpenF1 API

## Installation

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install the dependencies:

   `pip install pandas requests`

## Usage

Run the interactive driver comparison and leaderboard:

`python main.py`

Run the OpenF1 examples:

`python api_test.py`

`python race_results.py`

`python driver_positions.py`

`python real_leaderboard.py`

## Data

The comparison and leaderboard in `main.py` use fictional statistics for learning purposes. The API scripts retrieve historical Formula 1 information from [OpenF1](https://openf1.org/).

## Project Purpose

This project was created to practice Python programming, API integration, and data analysis as part of an AI engineering learning journey.