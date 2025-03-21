import sqlite3

from datetime import datetime

import click

from flask import current_app, g

# Sets up connection to database file
def get_db():

    if 'db' not in g:

        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )

        g.db.row_factory = sqlite3.Row

    return g.db

# Closes the connection to the database
def close_db(e=None):

    db = g.pop('db', None)

    if db is not None:

        db.close()

# Calls get db to call schema file
def init_db():

    db = get_db()

    with current_app.open_resource('schema.sql') as f:

        db.executescript(f.read().decode('utf8'))

# Third party package that lets us know the database was initialized
@click.command('init-db')
def init_db_command():

    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

# Controls the time stamp values in the database
sqlite3.register_converter(
    "timestamp", lambda v: datetime.fromisoformat(v.decode())
)

# Closes the application properly to prevent memory leaks
def init_app(app):

    app.teardown_appcontext(close_db)

    app.cli.add_command(init_db_command)

