#!/user/bin/python

import http
import requests
import urllib.request
import json
import unicodedata
import sys

raw_user_info = open(sys.argv[1], 'r').read()
user_info = raw_user_info.split(' ')

AppID = '9ce1f47e-ef63-4d4a-8b78-67bebeff4c94'

USERNAME = user_info[0]
PASSWORD = user_info[1]

print( USERNAME + ' ' + PASSWORD )

URL_root = 'https://www.onenote.com/api/v1.0/me/notes/'

text = 'hello world'

r = requests.get('https://api.github.com/user', auth=(USERNAME, PASSWORD))

ChangeObject_dict = {}

