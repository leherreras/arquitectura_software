import json
from functools import wraps

from flask import jsonify


def valid_request():
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except json.decoder.JSONDecodeError:
                return jsonify({"error": "El artefacto no fue encontrado"})

        return inner

    return wrapper
