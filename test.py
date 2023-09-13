# 토큰 인증

import requests

url = 'http://127.0.0.1:8000/api/auth'

response = requests.post(url, data={'username' : 'hong', 'password' : '1234'})

myToken = response.json()

header = {'Authorization' : 'Token ' + myToken['token']}
requests.get('http://127.0.0.1:8000/api/students', headers=header)
print(response.text)