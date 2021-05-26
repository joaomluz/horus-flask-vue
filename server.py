import sqlite3
import os.path
from pathlib import Path

from flask import (
    Flask, 
    jsonify,
    request,
    abort,
    g
)
from flask_cors import CORS

from flask_sqlalchemy import * # SQLAlchemy
from pathlib import Path

baseDir = Path(__file__).resolve().parent

# CONFIGS
DEBUG = True
DATABASE = "database/horus.db"
USERNAME = "admin"
PASSWORD = "admin"
SECRET_KEY = "bnatali" # Hey, it`s me
SQLALCHEMY_DATABASE_URI = os.getenv(
    "DATABASE_URL", f"sqlite:///{Path(basedir).joinpath(DATABASE)}"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False

# INSTANTIATE APP
app = Flask(__name__)
app.config.from_object(__name__)

# INITIALIZE DB 
db = SQLAlchemy(app)

#
# DATABASE FUNCTIONS
# 
# connect to database
def connect_db():
    """Connects to the database."""
    rv = sqlite3.connect(app.config["DATABASE"])
    rv.row_factory = sqlite3.Row
    return rv


# create the database
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource("database/schema.sql", mode="r") as f:
            db.cursor().executescript(f.read())
        db.commit()


# open database connection
def get_db():
    if not hasattr(g, "sqlite_db"):
        g.sqlite_db = connect_db()
    return g.sqlite_db


# close database connection
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, "sqlite_db"):
        g.sqlite_db.close()

from project import models

# ENABLE CORS
CORS(app, resources={r'/*': {'origins': '*'}})

#
# MAIN ROUTES
#
@app.route('/', methods=['GET'])
def list_contact():
    """ Root route returns a contact list in JSON form if is GET method"""
    return jsonify(db.session.query(models.Post))

@app.route('/new/', methods=['POST'])
def new_contact():
    """ Route 'new' add a new contat if POST and return result (1|0) in JSON """
    if not request.args.get("contact_name") or not request.args.get("contact_phone"):
        abort(400)

    try:
        new_entry = models.Post(request.args.get("contact_name"), request.args.get("contact_phone"))
        db.session.add(new_entry)
        db.session.commit()
        result = {"status": 1}
    except Exception as e:
        result = {"status": 0}

    return jsonify(result)

@app.route('/update/<int:contact_id>', methods=['GET'])
def remove_contact(contact_id):
    """ Update / Delete route expect contact_id as URL path and set it as deleted """
    if not request.args.get("method"): 
        abort(400)
        
    if request.args.get("method") == 'update':
        if not request.args.get("contact_phone"): 
            abort(400)
        db_update = {"contact_phone": request.args.get("contact_phone")}
    elif request.args.get("method") == 'delete':
        db_update = {"deleted": 1}
    else:
        abort(400)

    try:
        db.session.query.filter_by(id == contact_id).\
            update(db_update)
        db.session.commit()
        result = {"status": 1}
    except Exception as e:
        result = {"status": 0}

    return jsonify(result)


# KNOW IF WAS CALLED FROM TERMINAL OR AS A MODULE
if __name__ == '__main__':
    # Initialize DB if not exists
    if not os.path.isfile('filename.txt'):
        init_db()
    # Listen on any IP
    app.run(host='0.0.0.0', port=5000)
