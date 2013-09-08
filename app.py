from flask import Flask, request, render_template, redirect, url_for, escape, request, session
import fdc, fb, foursquare, misc, simplejson, urllib2

app = Flask(__name__)
app.secret_key = ']\x8d3\t\x0bD\xf9\xc5\x13\xb60\xebGdt$\xc0\x1eo\x12\xf1G\xd2\xa9'

secretKey = "f8d55cc687c3d83b5fca1aaee2f536b8"

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' in session:
        message = 'Logged in as %s' % escape(session['username'])
        return render_template('amigo.html', message=message) 
    else: 
        # Connect to facebook
        return render_template('home.html') 

@app.route('/loginhandler')
def login_handler(uid=None, accessToken=None):
    uri = urllib2.Request("GET /oauth/access_token?grant_type=fb_exchange_token&client_id={app-id}&client_secret={secretKey}&fb_exchange_token={accessToken}")
    set_fb_access_token(uid, uri)

@app.route('/logout')
def logout():
    # Remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/location/')
def handle_location(lat=None, lon=None):
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    # Save them to database somewhere?
    return (lat, lon)

@app.route('/loginhandler')
def handle_login(uid=None, accessToken=None):
    uid = request.args.get('uid')
    accessToken = request.args.get('accessToken')
    session['username'] = uid
    session['token'] = accessToken

    print "UID %s" % uid
    print "Access Token %s" % accessToken
    # Save them to database somewhere?
    return (uid, accessToken)

if __name__ == '__main__':
    app.run(debug=True)
