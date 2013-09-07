"""
fdc.py
Frontend for fdc-server backend.
"""
import requests

# For testing
import random
import string

def is_friend_of_friend(id):
    return True

def friends_of_friends_nearby(latitude, longitude):
    payload = {'lat': latitude, 'long': longitude, 'radius': 1}
    r = requests.get('http://ec2-23-20-163-191.compute-1.amazonaws.com/users', params=payload).json()
    if not r['success']:
        print 'fail'
        return []

    users_in_radius = r['users_in_radius']
    friends_of_friends_nearby = [user for user in users_in_radius if is_friend_of_friend(user)]
    return friends_of_friends_nearby

def get_user(id):
    r = requests.get('http://ec2-23-20-163-191.compute-1.amazonaws.com/user/%d' % id).json()

    if not r['success']:
        print 'fail'
        return ''

    user = r['user']
    return user

def update_user_location(id, latitude, longitude):
    payload = {'lat': latitude, 'long': longitude}
    r = requests.put('http://ec2-23-20-163-191.compute-1.amazonaws.com/user/%d' % id, params=payload).json()

    if not r['success']:
        print 'fail'
        return False

    return True

def get_fb_access_token(id):
    r = requests.get('http://ec2-23-20-163-191.compute-1.amazonaws.com/user/%d/fb_access_token' % id).json()

    if not r['success']:
        print 'fail'
        return ''

    token = r['token']
    return token

def set_fb_access_token(id, token):
    payload = {'token': token}
    r = requests.put('http://ec2-23-20-163-191.compute-1.amazonaws.com/user/%d/fb_access_token' % id, params=payload).json()

    if not r['success']:
        print 'fail'
        return False

    return True

if __name__ == '__main__':
    print friends_of_friends_nearby(0.0,0.0)
    test_token = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))
    set_fb_access_token(123, test_token)
    print 'Test token = ' + test_token
    print 'GET value = ' + get_fb_access_token(123)
    update_user_location(123, 39.953333, -75.17)
    print get_user(123)
