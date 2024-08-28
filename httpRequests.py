import requests
from requests.auth import HTTPBasicAuth

URL = 'https://va10pwvbna304.us.ad.wellpoint.com/bca-networks/api/token'

def token(username, password, URL):
    try:
        headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        }
        data = {
            'grant_type' : 'password',
            'username' : username,
            'password' : password
        }
        response = requests.post(URL, headers=headers, data=data)
        if response.status_code == 200:
            token = response.json().get('access_token')
            print(f"This is the Token: {token}")
            return token
        else:
            print(f"Not found. Error code: {response.status_code}")
    except requests.RequestException as error:
        print(f"Error: {error}")

def addDevice():
    pass