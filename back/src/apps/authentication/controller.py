from src.entities.users import User


def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user:
        check = user.check_password(password)
        if check:
            return user
    return False


def logout():
    # TODO Close session of user
    return True
