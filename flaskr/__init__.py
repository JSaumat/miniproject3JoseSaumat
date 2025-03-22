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

import os

from flask import Flask

def create_app(test_config=None):

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(

        SECRET_KEY='dev',

        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),

    )

    if test_config is None:

        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)

    else:

        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:

        os.makedirs(app.instance_path)

    except OSError:

        pass

    # # a simple page that says hello

    # @app.route('/hello')

    # def hello():

    #     return 'Hello, World!'

    # Imports and initializes database
    from . import db

    db.init_app(app)

    # Imports the auth file
    from . import auth

    app.register_blueprint(auth.bp)

    # Imports the home page
    from . import home

    app.register_blueprint(home.bp)

    # Imports the about page
    from . import about

    app.register_blueprint(about.bp)

    # Imports the blog
    from . import blog

    app.register_blueprint(blog.bp)

    app.add_url_rule('/', endpoint='index')

    return app