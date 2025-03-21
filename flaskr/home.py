import requests
from flask import Blueprint, render_template

bp = Blueprint("home", __name__)

# API key
TMDB_API_KEY = "ca268ace47dad3866382126044aa65ed"  # Replace with your actual TMDB API key

# API call to get movie posters with year, because some movies have been remade recently
def get_movie_poster(movie_title, release_year=None):
    """Fetch the movie poster URL from TMDB, prioritizing a specific release year if provided."""
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie_title}"

    if release_year:

        search_url += f"&year={release_year}"

    response = requests.get(search_url)

    if response.status_code == 200:

        data = response.json()

        if data["results"]:

            poster_path = data["results"][0]["poster_path"]

            return f"https://image.tmdb.org/t/p/w500{poster_path}"  # TMDB base URL for images
    return None  # Return None if no image is found

# Links to the YouTube trailers for each option for a movie in the grid on the home page
@bp.route("/")
def home():

    movies = [
        ("The Crow", "https://www.youtube.com/watch?v=otxeOvpc3Rw", 1994),
        ("Terminator 2: Judgment Day", "https://www.youtube.com/watch?v=CRRlbK5w8AE", 1991),
        ("Nightmare on Elm Street", "https://www.youtube.com/watch?v=dCVh4lBfW-c", 1984),
        ("The Matrix", "https://www.youtube.com/watch?v=vKQi3bBA1y8", 1999),
        ("The Lion King", "https://www.youtube.com/watch?v=eHcZlPpNt0Q", 1994),
        ("The Dark Knight", "https://www.youtube.com/watch?v=EXeTwQWrcwY", 2008),
        ("The Nightmare Before Christmas", "https://www.youtube.com/watch?v=wr6N_hZyBCk", 1993),
        ("Ghostbusters", "https://www.youtube.com/watch?v=6hDkhw5Wkas", 1984),
        ("Back to the Future", "https://www.youtube.com/watch?v=qvsgGtivCgs", 1985),
        ("Demolition Man", "https://www.youtube.com/watch?v=0B5v6QZ5R3g", 1993),
    ]

    # Fetch posters for each movie, including the release year when specified
    movies_with_posters = [
        (title, link, get_movie_poster(title, year)) for title, link, year in movies
    ]

    return render_template("home.html", movies=movies_with_posters)