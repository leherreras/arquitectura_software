from flask import Flask
import os
import codecs
import requests

app = Flask(__name__)
app.secret_key = codecs.encode(os.urandom(32), 'hex')


@app.route('/')
def index():
    url = "https://pokeapi.co/api/v2/"
    path = "pokemon/ditto"
    res = requests.get(url + path)

    return res.json()


if __name__ == "__main__":
    app.run(debug=True, port=4201, host="0.0.0.0")
