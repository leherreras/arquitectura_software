from flask import request, jsonify
from flask_classy import FlaskView, route

from .controller import create_user


class UserView(FlaskView):

    def post(self):
        password = request.form.get("password")
        username = request.form.get("username")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        user = create_user(username,first_name, last_name, password)
        return jsonify({"username": user.username, "first_name": user.first_name})
