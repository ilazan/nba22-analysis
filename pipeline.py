import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import os
from pathlib import Path

dotenv_path = Path("/Users/ilariazanoni/dev/tools/api-keys/NBA_API_KEY.env")
load_dotenv(dotenv_path=dotenv_path)
NBA_API_KEY = os.getenv("NBA_API_KEY")

headers = {
  "x-rapidapi-key": NBA_API_KEY,
  "x-rapidapi-host": "api-nba-v1.p.rapidapi.com"
}

# Extract - API_1 - Standings
url_standings = "https://api-nba-v1.p.rapidapi.com/standings/standard/2022"
res_standings = requests.get(url_standings, headers=headers)
data_standings = res_standings.json()

# Extract - API_2 - Teams
url_teams = "https://api-nba-v1.p.rapidapi.com/teams/league/standard"
res_teams = requests.get(url_teams, headers=headers)
data_teams = res_teams.json()

# Extract - API_3 - Games
url_games = "https://api-nba-v1.p.rapidapi.com/games/league/standard/2022"
res_games = requests.get(url_games, headers=headers)
data_games = res_games.json()

# Transform Standings
standings = data_standings.get('api', {}).get('standings', [])
team_stats = []

for team_standings in standings:
    stats = {
        "team_id": team_standings.get("teamId"),
        "wins": team_standings.get('win'),
        "losses": team_standings.get("loss"),
        "season": team_standings.get("seasonYear"),
    }
    team_stats.append(stats)

stats_df = pd.DataFrame(team_stats)

# Transform Teams
teams_info = data_teams.get("api", {}).get("teams", [])
teams = []

for team in teams_info:
    stats = {
        "team_id": team.get("teamId"),
        "full_name": team.get("fullName")
    }
    teams.append(stats)

teams_df = pd.DataFrame(teams)

# Transform Games
games_data = data_games.get("api", {}).get("games", [])
games_stats = []

for game in games_data:
    start_time_utc = game.get("startTimeUTC")
    start_time_dt = datetime.strptime(start_time_utc, "%Y-%m-%dT%H:%M:%S.%fZ")
    formatted_date = start_time_dt.strftime("%Y-%m-%d")

    stats = {
        "date": formatted_date,
        "away_team_id": game["vTeam"]["teamId"],
        "away_team": game["vTeam"]["fullName"],
        "home_team_id": game["hTeam"]["teamId"],
        "home_team": game["hTeam"]["fullName"],
        "a_team_score": game["vTeam"]["score"]["points"],
        "h_team_score": game["hTeam"]["score"]["points"],
        "duration": game.get("gameDuration")
    }
    games_stats.append(stats)

games_df = pd.DataFrame(games_stats)

# Load
stats_df.to_csv("dwh/stats.csv", index=False)
teams_df.to_csv("dwh/teams.csv", index=False)
games_df.to_csv("dwh/games.csv", index=False)