import requests


def download_player_data(player_name):
    name = "".join(word.capitalize() for word in player_name.split())
    url = f"https://www.tennisabstract.com/jsmatches/{name}Career.js"

    response = requests.get(url, timeout=60)

    if response.status_code != 200 or "morematchmx" not in response.text:
        raise ValueError(f"Could not find career data for '{player_name}'")

    return response.text