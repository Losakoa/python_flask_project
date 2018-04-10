from flask import render_template
from app import app

# routes allow the app to access a specific URI which in turn returns something (function, method, etc)
@app.route('/')
@app.route('/index')


# defining the /index route with the following method 
def index():
    #define user name as carlos
    user = {'username':'Carlos'}
    return render_template ('index.html', title = 'Home', user=user)
