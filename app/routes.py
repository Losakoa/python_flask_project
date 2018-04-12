from flask import render_template
from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect



# routes allow the app to access a specific URI which in turn returns something (function, method, etc)
@app.route('/')
@app.route('/index')
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



# login routing protocol and methods 
# The first new thing in this version is the methods argument in the route decorator. 
# This tells Flask that this view function accepts GET and POST requests, overriding the default, which is to accept only GET requests
@app.route('/login', methods = ['GET','POST'])

def login():
    form = LoginForm()
    # flash text and pass 
    if form.validate_on_submit(): # does proccessing work | gathers data, runs the validators
        # flash function use way to show message
        flash('Login requested for user {}, remember_me={}'.format( 
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('/login.html', Title='Sign In', form = form)