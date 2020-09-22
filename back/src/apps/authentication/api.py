from flask import request, jsonify
from flask_classy import FlaskView

from .controller import authenticate


class LoginView(FlaskView):

    def post(self):
        password = request.form.get("password")
        username = request.form.get("username")
        user = authenticate(username, password)
        return jsonify({"username": user.username, "first_name": user.first_name})
