from flask import (
    Blueprint,
    render_template,
    request
)

from services.filters import (
    find_underground_artists
)

search_bp = Blueprint(
    "search",
    __name__
)


@search_bp.route("/")
def home():

    return render_template(
        "index.html"
    )


@search_bp.route("/search")
def search():

    artist = request.args.get(
        "artist"
    )

    genre = request.args.get(
        "genre"
    )

    country = request.args.get(
        "country"
    )

    results = (
        find_underground_artists(
            artist,
            genre,
            country
        )
    )

    return render_template(
        "results.html",
        results=results
    )
