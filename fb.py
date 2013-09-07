import simplejson, urllib2

def find_mutual(uid1, uid2):
		uri = urllib2.Request("https://graph.facebook.com/" + uid1 + "/mutualfriends/" + uid2);
		f = opener.open(uri)
		simplejason.load(f)
		return f.data

def num_mutual(uid):
		uri = urllib2.Request("https://graph.facebook.com/fql?q=SELECT+mutual_friend_count+FROM+user+WHERE+uid="+uid+"&access_token="+getaccesstoken())
		f = opener.opne(uri)
		simplejason.load(f);
		return f.data.mutual_friend_count

	
