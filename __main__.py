from routes.player import get_player_info
from routes.matches import get_match_info


if __name__ == '__main__':
    #Add all unit tests here.
    player_name = "Asparagus Stem"

    #For an EUW account
    player = get_player_info(player_name, tagline='euw')
    print(player)

    puuid = get_match_info(player['puuid'], 50)
    print(puuid)


