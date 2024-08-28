import requests

def token(username, password):
    try:
        headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'grant_type' : f'=password&username={username}&{password}='
        }
        response = requests.get("https://va10pwvbna304.us.ad.wellpoint.com/bca-networks/api/token", headers=headers)
        if response.status_code == 200:
            token = response.json().get('token')
            print(response)
            return token
        else:
            print(f"Not found. Error code: {response.status_code}")
    except requests.RequestException as error:
        print(f"Error: {error}")

token("al93633","")

# Token:

# curl -X 'POST' \

#   'https://va10pwvbna304.us.ad.wellpoint.com/bca-networks/api/token' \

#   -H 'accept: application/json' \

#   -H 'Content-Type: application/x-www-form-urlencoded' \

#   -d 'grant_type=password&username=al93633&password='

 
# connection: keep-alive

#  content-length: 94

#  content-type: application/json

#  date: Wed,28 Aug 2024 16:03:23 GMT

#  keep-alive: timeout=20

#  server: TrueSight Network Automation Server

#  strict-transport-security: max-age=31536000

#  x-content-type-options: nosniff

#  x-frame-options: SAMEORIGIN

#  x-xss-protection: 1; mode=block