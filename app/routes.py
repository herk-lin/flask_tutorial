from app import abc
from flask import render_template


@abc.route('/')
@abc.route('/abc')
def home():
    return "Hello World!"


@abc.route('/index')
def index():
    user = { 'username': 'Kl'}
    posts = [ {'author': 'John', 'body': 'A beautiful Day!'},
              {'author': 'Susan', 'body': 'Avengers'}
            ]


    return render_template('index.html',  user=user, posts = posts )
