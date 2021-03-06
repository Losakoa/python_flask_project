from flask import render_template
from app import app

# routes allow the app to access a specific URI which in turn returns something (function, method, etc)
@app.route('/')
@app.route('/index')
@app.route('/testing')


# defining the /index route with the following method 
def index():
    #define user name as carlos
    user = {'username':'Carlos'}
    # create a posts dictionary with a list inside including username and body.  This info is passed along within the index.html template via a forloop (body only)
    posts = [
        {
            'author': {'username':'Bill'},
            'body'  : 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body'  : 'The Avengers movie was so cool!'
        }
    ]
    return render_template ('index.html', title = 'Home', user = user, posts = posts)


