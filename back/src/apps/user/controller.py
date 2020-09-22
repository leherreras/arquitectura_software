from src.entities.users import User


def create_user(username, first_name, last_name, password):
    user = User(username=username, first_name=first_name, last_name=last_name)
    user.set_password(password)
    user.save()

    return user
