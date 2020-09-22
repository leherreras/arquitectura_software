import codecs
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = codecs.encode(os.urandom(32), 'hex')
db_name = 'architecture.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./{}'.format(db_name)

db = SQLAlchemy(app)
