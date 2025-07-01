import json

def load_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except:
        return {"admin": "admin123"}  # default user

def verify_user(username, password):
    users = load_users()
    return users.get(username) == password
