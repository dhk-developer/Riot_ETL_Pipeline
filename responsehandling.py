import requests
import json



def handle_response(res):
    """Basic response handling for GET requests to riot API
    :return: json response, else exception error.
    """
    try:
        res.raise_for_status()  # Raise HTTPError for bad responses
        return res.json()
    except requests.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except json.JSONDecodeError:
        return "JSON decoding failed"
    except requests.RequestException as err:
        return f"Request failed - issue getting summoner data from API: {err}"
