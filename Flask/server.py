''' pip install Flask
    set FLASK_APP=server.py
    set FLASK_ENV=development # to debug_mode =on so no  need to run server again and again
    flask run
'''
from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello'

@app.route('/blog')
def blog():
    return render_template('index.html')

@app.route('/<username>')
def blog2(username=None):
    return render_template('index.html',name=username)

@app.route('/<username>/<int:post_id>')
def blog3(username=None,post_id=None):
    return render_template('index.html',name=username,id=post_id)

@app.route('/submit_form',methods=['GET','POST'])
def submit_form():
    return 'successfully submitted form'

