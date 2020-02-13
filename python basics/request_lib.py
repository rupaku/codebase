'''
request : third party library
http://httpbin.org
'''
import requests

r=requests.get('https://xkcd.com/353/comics/python.png')
print(r) #response :200
print(r.text) #html content of url
print(r.content) #byte content
print(r.status_code) #200
print(r.ok) #True
print(r.headers) #header part

with open('comic.png','wb') as f:
    f.write(r.content

## GET ##
payload={'page':2,'count':25}
r=requests.get('https://httpbin.org/get',params=payload)
print(r.text)
print(r.url) #https://httpbin.org/get?page=2&count=25

### POST ##
payload = {'username': 'rupa', 'password': 'password123'}
r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)

r_dict=r.json()
print(r_dict['form']) #{'username': 'rupa', 'password': 'password123'}

### AUTH ###
r=requests.get('https://httpbin.org/basic-auth/rupa/password123',auth=('rupa','password123'))
print(r.text)# user 'rupa' authenticated:True
