from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET': 
        return render_template('gps.html')
    elif request.method == 'POST':
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        print "latitude %s" % latitude
        print "longitude %s" % longitude
        return "whee!"

if __name__ == '__main__':
    app.run(debug=True)
