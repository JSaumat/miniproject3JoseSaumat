'''

INF601 - Programming in Python

Assignment #3:  Mini Project 3

I,     Jose Saumat   , affirm that the work submitted for this assignment is entirely my own.
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism,
or the use of unauthorized materials. I have neither provided nor received unauthorized assistance and have
accurately cited all sources in adherence to academic standards. I understand that failing to comply with this
integrity statement may result in consequences, including disciplinary actions as determined by my course instructor
and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles
of academic integrity.

'''

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

