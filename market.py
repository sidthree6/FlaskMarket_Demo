from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h2>Hello, World!</h2>'

@app.route('/about/<username>')
def about_us(username):
    return f'About Me - {username}'