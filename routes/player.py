import requests
import responsehandling as rh
from urllib.parse import urlencode

from dotenv import load_dotenv
import os

load_dotenv()


def get_player_info(gameName=None, tagline=None, region=os.getenv('DEFAULT_REGION')):
    """
    Retrieve player information based on gameName and tagline from the Riot Games API.

    If gameName or tagline are not provided, user input will be requested.

    Parameters:
    - gameName (str, optional): Player's in-game name (default is None).
    - tagline (str, optional): Player's tagline (default is None, exclude the #).
    - region (str, optional): Region for the API request (default is settings.DEFAULT_REGION).

    Returns:
    - dict: Response data from the API request.
    """

    # GET request requires name and tagline of player.
    if not gameName:
        gameName = input("Player name.")
    if not tagline:
        tagline = input("Player tagline (exclude the #).")

    # Params to send to API route.
    params = {
        'api_key': os.getenv('API_KEY')
    }

    API_URL = f"https://{region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gameName}/{tagline}"

    # response handling
    response = requests.get(API_URL, params=urlencode(params))
    return rh.handle_response(response)

