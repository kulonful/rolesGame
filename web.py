from flask import Flask, request, session

app = Flask(__name__)

@app.route('/admin')
def adminPage():
    return 'adminpage'

@app.route('/user/', methods = ['GET', 'POST'])
def userPage():
    return 'userpage'

app.run(host = '0.0.0.0', port = 80)