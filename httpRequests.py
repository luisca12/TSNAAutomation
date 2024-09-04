import requests
from requests.auth import HTTPBasicAuth
from addDevice import addDevicePy, addDeviceJson
import os

URL = 'https://va10pwvbna304.us.ad.wellpoint.com/bca-networks/api/token'
addDeviceURL = 'https://va10pwvbna304.us.ad.wellpoint.com/bca-networks/api/v4.0/devices'

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

def addDevice(token):
    print(token)
    os.system("PAUSE")
    try:
        addDeviceOut = requests.post(addDeviceURL, data = addDeviceJson,
                    headers = {'accept':'application/json','Authorization':'Bearer ' + token, 'Content-Type':'application/json'})
        if addDeviceOut.status_code == 201:
            print(f"INFO: Device {addDevicePy['name']} added successfully, status code: {addDeviceOut.status_code}")
        else:
            print(f"ERROR: Device {addDevicePy['name']} had an error: {addDeviceOut.text}")
    except requests.RequestException as error:
        print(f"ERROR: {error}")
    
    






