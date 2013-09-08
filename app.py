from flask import Flask, request, render_template, redirect, url_for, escape, request, session
import fdc, fb, foursquare, misc, simplejson, urllib2

app = Flask(__name__)
app.secret_key = ']\x8d3\t\x0bD\xf9\xc5\x13\xb60\xebGdt$\xc0\x1eo\x12\xf1G\xd2\xa9'

secretKey = "f8d55cc687c3d83b5fca1aaee2f536b8"
appid = 158496954347821

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' in session:
        message = 'Logged in as %s' % escape(session['username'])
        me = fdc.get_user(int(session['username']))
        nearby = fdc.friends_of_friends_nearby(me['lat'], me['lon'])
        for user in nearby:
            user['name'] = fb.get_name(int(user['id']))
            user['last_updated_string'] = misc.pretty_date(int(user['last_updated']))
            #user['num_mutual'] = fb.num_mutual(int(me['id']),int(user['id']))
        return render_template('amigo.html', message=message, myLat=me['lat'], myLon=me['lon'], peopleList=nearby)
    else: 
        #Connect to facebook
        return render_template('home.html') 

@app.route('/logout')
def logout():
    # Remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/location')
def handle_location():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    # Save them to database somewhere?
    fdc.update_user_location(int(session['username']), lat, lon)
    return redirect(url_for('index'))

@app.route('/loginhandler')
def handle_login():
    uid = request.args.get('uid')
    accessToken = request.args.get('accessToken')
    session['username'] = uid
    session['token'] = accessToken

    print "UID %s" % uid
    print "Access Token %s" % accessToken

    fdc.set_fb_access_token(int(uid), accessToken)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
