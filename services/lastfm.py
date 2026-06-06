import requests
import os

LASTFM_API_KEY = os.getenv("LASTFM_API_KEY")


def get_artist_info(artist):

    url = (
        f"http://ws.audioscrobbler.com/2.0/"
        f"?method=artist.getinfo"
        f"&artist={artist}"
        f"&api_key={LASTFM_API_KEY}"
        f"&format=json"
    )

    response = requests.get(url)

    return response.json()["artist"]


def get_similar_artists(artist):

    url = (
        f"http://ws.audioscrobbler.com/2.0/"
        f"?method=artist.getsimilar"
        f"&artist={artist}"
        f"&api_key={LASTFM_API_KEY}"
        f"&format=json"
    )

    response = requests.get(url)

    return response.json()["similarartists"]["artist"]
