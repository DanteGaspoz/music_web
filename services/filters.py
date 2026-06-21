from services.artist_service import get_artist_info
from services.lastfm_service import get_similar_artists
from concurrent.futures import ThreadPoolExecutor
from services.artist_service import get_artist_info
from services.lastfm_service import get_similar_artists


def find_underground_artists(artist, genre, country):

    similar_artists = get_similar_artists(artist)

    # limita antes de paralelizar (IMPORTANTE)
    similar_artists = similar_artists[:15]

    with ThreadPoolExecutor(max_workers=10) as executor:

        results = list(
            executor.map(get_artist_info, similar_artists)
        )

    # filtros después de obtener datos
    filtered = []

    for info in results:

        if genre and genre not in (info["genres"] or []):
            continue

        if country and info["country"] != country:
            continue

        filtered.append(info)

    return filtered
