import requests
import json

CLIENT_ID = 'JQEEDSMAW0TCWCOZSQRSUOPZC5L04KXJK23ZSBRQB0WTUJ45'
CLIENT_SECRET = 'WDYFQ4J2MDIUNCC4HN2CK4O124EDRYPZED4RK4WC0MH2G3C5'

def nearby_venues(lat, lon):
    payload = {'ll': '%f,%f' % (lat, lon), 'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET}
    r = requests.get('https://api.foursquare.com/v2/venues/search', params=payload).json()
    return [venue['name'] for venue in r['response']['groups'][0]['items']]

# Tests
if __name__ == '__main__':
    print nearby_venues(39.953333, -75.17)
