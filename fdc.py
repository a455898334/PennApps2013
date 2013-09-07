"""
fdc.py
Frontend for fdc-server backend.
"""
import requests

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

print friends_of_friends_nearby(0.005,0.0)
