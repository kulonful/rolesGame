from flask import Flask, request, session
import json
import time

app = Flask(__name__)
users = {}
with open('users.json', 'r') as f:
    print('---------------------')
    users = json.loads(str(f.read()))
    print('Config loaded:\n' + str(users))
    print('---------------------')

def save():
    with open('users.json', 'w') as f:
        f.write(json.dumps(users))

@app.route('/admin')
def adminPage():
    return json.dumps(users)

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