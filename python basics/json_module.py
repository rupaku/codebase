'''
json.loads() method. :convert from json to python
json.dumps() method. :convert from python to json
'''

import json
userJson = '{"first_name": "john","last_name": "doe"}' #json

#parse to dict
user=json.loads(userJson)
print(user) #{'first_name': 'john', 'last_name': 'doe'}
print(user['first_name']) #john

car={'make': 'ford', 'model': 'mustang'} #dict
carJson=json.dumps(car)
print(carJson) #{"make": "ford", "model": "mustang"}


