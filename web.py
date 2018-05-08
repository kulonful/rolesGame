# -*- coding: utf-8 -*-
from flask import Flask, request, session, render_template
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
    session['anime'] = 25
    return json.dumps(users)

@app.route('/client')
def userPage():
    if 'login' in session:
        print(True)
        # TODO
    else:
        return render_template('cu.html'), 200

@app.route('/reset')
def resetPage():
    global users
    users = {}
    save()
    return 'success reset', 200

app.secret_key = 'hjnfshNcq48cqn@q9nc'
app.run(host = '0.0.0.0', port = 80)