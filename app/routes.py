from app import app

# routes allow the app to access a specific URI which in turn returns something (function, method, etc)
@app.route('/')
@app.route('/index')


# defining the /index route with the following method 
def index():
    user = {'username':'Carlos'}
    return '''
    <html>
        <head>
            <title>
                Home Page - Carlos's Microblog Bitches!
            </title>
        </head>
        <body>
            <h1>Hello, ''' + user['username'] + '''!</h1>
        </body>
    </html>
    '''
