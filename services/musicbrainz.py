import requests


def get_artist_country(artist):

    url = (
        f"https://musicbrainz.org/ws/2/"
        f"artist/?query=artist:{artist}"
        f"&fmt=json"
    )

    response = requests.get(url)

    data = response.json()

    if data["artists"]:
        return data["artists"][0].get(
            "country",
            "Unknown"
        )
    
    return "Unknown"
