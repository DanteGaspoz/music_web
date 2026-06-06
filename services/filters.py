from services.lastfm import (
    get_artist_info,
    get_similar_artists
)

from services.musicbrainz import (
    get_artist_country
)


def get_artist_data(name):

    info = get_artist_info(name)

    return {
        "name": info["name"],
        "listeners": int(
            info["stats"]["listeners"]
        ),
        "tags": [
            tag["name"].lower()
            for tag in info["tags"]["tag"]
        ],
        "country": get_artist_country(name)
    }


def is_country_match(
    artist,
    country
):

    return (
        artist["country"].lower()
        == country.lower()
    )


def is_genre_match(
    artist,
    genre
):

    return (
        genre.lower()
        in artist["tags"]
    )


def is_underground(
    artist,
    max_listeners=50000
):

    return (
        artist["listeners"]
        < max_listeners
    )


def find_underground_artists(
    base_artist,
    genre_tag,
    country
):

    results = []

    artists = (
        get_similar_artists(
            base_artist
        )
    )

    for artist in artists:

        try:

            data = get_artist_data(
                artist["name"]
            )

            if (
                is_country_match(
                    data,
                    country
                )
                and
                is_genre_match(
                    data,
                    genre_tag
                )
                and
                is_underground(data)
            ):

                results.append(data)

        except Exception as e:

            print(e)

    return results
