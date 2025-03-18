from flask import Blueprint, render_template

# Create a Blueprint for the home page
bp = Blueprint("home", __name__)

@bp.route("/")
def home():
    return render_template("home.html")