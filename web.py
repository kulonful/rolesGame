from flask import Flask, request, session
import json

app = Flask(__name__)
users = {'asd': 2143}
with open('users.json', 'r') as f:
    users = json.loads(f.read())

def save():
    with open('users.json', 'w') as f:
        f.write(json.dumps(users))

@app.route('/admin')
def adminPage():
    save()
    return 'adminpage'

@app.route('/user', methods = ['GET', 'POST'])
def userPage():
    if request.method == 'GET':
        print('todo')
        # TODO
    elif request.method == 'POST':
        print('todo')
        # TODO

@app.route('/reset')
def resetPage():
    global users
    users = {}
    save()
    return 'success reset', 200

app.run(host = '0.0.0.0', port = 80)