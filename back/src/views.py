import codecs
import os
from flask_cors import CORS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.secret_key = codecs.encode(os.urandom(32), 'hex')
db_name = 'architecture.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../{}'.format(db_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ROOT_PATH = os.path.abspath(os.path.join(__file__, '..', '..'))
if not os.path.isfile(os.path.join(ROOT_PATH, db_name)):
    db.create_all()
