#a program to liberate data from http://data.visionappraisal.com/SomervilleMA/search.asp
#made by chris peterson, petey [at] mit [dot] edu
#using the python requests library at http://goo.gl/KFfZ5

import requests

r = requests.get('http://data.visionappraisal.com/SomervilleMA/search.asp')
#print r.text

payload = {'number': '31', 'name': 'aberdeen rd'}
r = requests.post("http://data.visionappraisal.com/SomervilleMA/search.asp", data=payload)
print r.text