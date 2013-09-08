import simplejson, urllib2, requests
import fdc

def find_mutual(uid1, uid2):
    uri = urllib2.Request("https://graph.facebook.com/" + uid1 + "/mutualfriends/" + uid2 + "?access_token="+get_fb_access_token(uid))
    f = opener.open(uri)
    simplejson.load(f)
    return f.data

#def num_mutual(uid):
#    uri = urllib2.Request("https://graph.facebook.com/fql?q=SELECT+mutual_friend_count+FROM+user+WHERE+uid="+uid+"&access_token="+get_fb_access_token(uid))
#    f = opener.open(uri)
#    simplejson.load(f);
#    return f.data.mutual_friend_count

def num_mutual(uid1, uid2):
    r = requests.get("https://graph.facebook.com/" + uid1 + "/mutualfriends/" + uid2 + "?access_token="+fdc.get_fb_access_token(uid))
    simplejson.load(f)
    return len(f['data'])

def get_name(id):
    r = requests.get('https://graph.facebook.com/%d' % id).json()
    return r['name']

