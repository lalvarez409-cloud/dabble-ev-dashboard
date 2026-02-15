import requests
from config import API_KEY

def get_nba_props():
    url = "https://api.the-odds-api.com/v4/sports/basketball_nba/odds"
    
    params = {
        "apiKey": API_KEY,
        "regions": "us",
        "markets": "player_points,player_rebounds,player_assists",
        "oddsFormat": "american"
    }

    response = requests.get(url, params=params)
    return response.json()
