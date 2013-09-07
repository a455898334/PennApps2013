from pymongo import Connection

Connection = Connection('mongo2.stuycs.org')
db = Connection.admin
res = db.authenticate('ml7', 'ml7')
db = Connection['PennAppsDemo']
collection = db.collection

def addLocation(user_id, access_token, coords):
    pass
