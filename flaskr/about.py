import requests
from flask import Blueprint, render_template

bp = Blueprint('about', __name__, url_prefix='/about')

# TMDb API Key (Replace with your actual API key)
TMDB_API_KEY = "YOUR_API_KEY"


@bp.route('/')
def about():
    # Fetch TMDb logo URL dynamically
    tmdb_logo_url = get_tmdb_logo()

    return render_template('about.html', tmdb_logo=tmdb_logo_url)


def get_tmdb_logo():
    """Fetch TMDb official logo from their API."""
    api_url = f"https://api.themoviedb.org/3/company/174/images?api_key={TMDB_API_KEY}"

    try:
        response = requests.get(api_url)
        data = response.json()

        if "logos" in data and len(data["logos"]) > 0:
            logo_path = data["logos"][0]["file_path"]
            return f"https://image.tmdb.org/t/p/original{logo_path}"  # Use TMDb base URL
    except Exception as e:
        print(f"Error fetching TMDb logo: {e}")

    # Fallback logo URL in case of API failure
    return None

