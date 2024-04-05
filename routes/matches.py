import os
from dotenv import load_dotenv

import requests
import responsehandling as rh
from urllib.parse import urlencode

load_dotenv()

def get_match_info(puuid, match_count, region=os.getenv('DEFAULT_REGION')):
    """
    Retrieve match IDs associated with a player's PUUID retrieved from get_player_info.

    Parameters:
    - puuid (str): Player's unique identifier.
    - match_count (int): Number of match IDs to retrieve.
    - region (str, optional): Region for the API request (default is settings.DEFAULT_REGION).

    Returns:
    - dict: Response data from the API request.
    """

    #  parameters to send to API route
    params = {
        'api_key': os.getenv('API_KEY'),
        'count': match_count
    }

    API_URL = f"https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids"

    response = requests.get(API_URL, params=urlencode(params))
    return rh.handle_response(response)




