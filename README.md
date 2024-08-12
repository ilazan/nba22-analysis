# NBA Analysis 2022

This repository contains the code and data for the NBA analysis project conducted as part of an assessment for a course at Hyper Island. The project focuses on analyzing NBA games, teams, and player statistics for the 2022 season.

## Contents

- `nba_analysis_2022.ipynb`: Jupyter Notebook containing the analysis of NBA data for the 2022 season. This notebook includes data exploration, cleaning, and visualizations.
- `pipeline.py`: A Python script that processes raw NBA data and generates the necessary CSV files (`teams.csv`, `stats.csv`, `games.csv`). This script is optional and provided in case you want to regenerate the CSV files.
- `teams.csv`: A CSV file containing information about NBA teams.
- `stats.csv`: A CSV file containing statistics for NBA players.
- `games.csv`: A CSV file containing details of NBA games for the 2022 season.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/ilazan/nba22-analysis.git
    cd nba-analysis-2022
  
## Usage

### Running the Data Processing Pipeline (Optional)

If you want to regenerate the CSV files from raw data, you can use the `pipeline.py` script:

```bash
python pipeline.py
```

This will create the following CSV files:
- **teams.csv**
- **stats.csv**
- **games.csv**

## Running the Jupyter Notebook

To explore the analysis, run the Jupyter Notebook:

```bash
jupyter notebook nba_analysis_2022.ipynb
```

This will open the Jupyter Notebook interface in your browser.

## Data

### teams.csv

Contains information about NBA teams including:
- **team_id**: Unique identifier for each team.
- **team_name**: Name of the team.
- **abbreviation**: Team's abbreviation.

### stats.csv

Contains statistics for NBA players, including:
- **player_id**: Unique identifier for each player.
- **team_id**: Identifier linking the player to a team.
- **points**: Points scored by the player.
- **assists**: Assists made by the player.
- **rebounds**: Rebounds made by the player.
- and more...

### games.csv

Details of NBA games, including:
- **game_id**: Unique identifier for each game.
- **home_team_id**: Identifier of the home team.
- **away_team_id**: Identifier of the away team.
- **home_team_score**: Score of the home team.
- **away_team_score**: Score of the away team.
- **date**: Date when the game was played.

## Contribution

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

The data used in this project is sourced from [API-NBA](api-nba-v1.p.rapidapi.com). 
This project was developed as part of the coursework at Hyper Island.
