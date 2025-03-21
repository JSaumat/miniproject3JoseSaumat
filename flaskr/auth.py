import functools

# Handles the authentication functions
from flask import (

    Blueprint, flash, g, redirect, render_template, request, session, url_for

)

from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

# Registration view for the site, checks username and password during registration
@bp.route('/register', methods=('GET', 'POST'))

def register():

    if request.method == 'POST':

        username = request.form['username']

        password = request.form['password']

        firstname = request.form['firstname']

        lastname = request.form['lastname']

        db = get_db()

        error = None

        if not username:

            error = 'Username is required.'

        elif not password:

            error = 'Password is required.'

        elif not firstname:

            error = 'First name is required.'

        elif not lastname:

            error = 'Last name is required.'

        else:

            # Check if username already exists
            existing_user = db.execute(

                'SELECT id FROM users WHERE username = ?', (username,)

            ).fetchone()

            if existing_user:

                error = 'Username is already taken. Please choose a different one.'

        if error is None:

            try:

                db.execute(

                    "INSERT INTO users (username, password, firstname, lastname) VALUES (?, ?, ?, ?)",

                    (username, generate_password_hash(password), firstname, lastname)

                )
                db.commit()

                flash('Registration successful! Please log in.', 'success')  # ✅ Success Message

                print("Flashed message: Registration successful!")  # Debugging

                return redirect(url_for("auth.login"))

            except db.IntegrityError:

                error = f"User {username} is already registered."

        # if error is not None:

        #     flash(error, 'error')  # ✅ Ensure the error message is shown

        #     print(f"Flashed error message: {error}")  # Debugging

        else:

            flash(error, 'error')  # ✅ Ensure this happens when there’s a problem

    return render_template('auth/register.html')


# Log In view for the website, checks username and password entered against the database
@bp.route('/login', methods=('GET', 'POST'))

def login():

    if request.method == 'POST':

        username = request.form['username']

        password = request.form['password']

        db = get_db()

        error = None

        user = db.execute(

            'SELECT * FROM users WHERE username = ?', (username,)

        ).fetchone()

        if user is None:

            error = 'Invalid username or password'

        elif not check_password_hash(user['password'], password):

            error = 'Invalid username or password'

        if error is None:

            session.clear()

            session['user_id'] = user['id']

            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')

# Logged In view that checks to see if the user is already logged in, and gives them the proper view with the cookie
@bp.before_app_request
def load_logged_in_user():

    user_id = session.get('user_id')

    if user_id is None:

        g.user = None

    else:

        g.user = get_db().execute(

            'SELECT * FROM users WHERE id = ?', (user_id,)

        ).fetchone()

# Original Log Out view that removes the logged in cookie and gives the user the default view of the site once again
# @bp.route('/logout')
# def logout():
#     session.clear()
#     return redirect(url_for('index'))

# Checks to make sure user is logged in and only allows the user to change their posts
def login_required(view):

    @functools.wraps(view)

    def wrapped_view(**kwargs):

        if g.user is None:

            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view

# New Logged Out view that lets the user know they have been logged out
@bp.route('/logout')
def logout():

    session.clear()

    return render_template('auth/logged_out.html')  # Redirect to the Logged Out Page