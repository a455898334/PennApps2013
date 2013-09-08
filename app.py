from flask import Flask, request, render_template
import fdc, fb, foursquare, misc

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route('/gps', methods=['GET', 'POST'])
def gps():
    return render_template("gps.html")

@app.route('/location/')
def handle_location(lat=None, lon=None):
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    return (lat, lon)


if __name__ == '__main__':
    app.run(debug=True)
