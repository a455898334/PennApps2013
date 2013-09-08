from flask import Flask, request, render_template, redirect, url_for, escape, request, session
import fdc, fb, foursquare, misc

app = Flask(__name__)
app.secret_key = ']\x8d3\t\x0bD\xf9\xc5\x13\xb60\xebGdt$\xc0\x1eo\x12\xf1G\xd2\xa9'

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    if 'username' in session:
        message = 'Logged in as %s' % escape(session['username'])
        return render_template('amigo.html', message=message) 
    else: 
        # Connect to facebook
        return render_template('home.html') 
    """
    return render_template('amigo.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Change this to keep track of fb user ID and the access key once
    # a post request has been made
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    else:
        # Change this to return the required facebook oauth stuff.
        return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p[><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # Remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/location/')
def handle_location(lat=None, lon=None):
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    return (lat, lon)

if __name__ == '__main__':
    app.run(debug=True)
