import json

def greet_user():
    """问候用户，并指出其名字"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What's your name?")
        with open(filename, 'w') as f:
            json.dump(username,f)
            print(f"we'll remember you when you come back, {username.title()}!")
    else:
        print(f"welcome back, {username}!")
    
greet_user()