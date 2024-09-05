import requests
from requests.auth import HTTPBasicAuth
from addDevice import addDevicePy, addDeviceJson
import os



def getToken(username, password):

    URL = 'https://va10pwvbna304.us.ad.wellpoint.com/bca-networks/api/token'

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        'grant_type' : 'password',
        'username' : username,
        'password' : password
    }

    try:
       
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

    URL = 'https://va10pwvbna304.us.ad.wellpoint.com/bca-networks/api/v4.0/devices'

    headers = {
        'accept':'application/json',
        'Authorization':'Bearer ' + token,
        'Content-Type':'application/json'
    }

    try:
        addDeviceOut = requests.post(URL, data = addDeviceJson, headers = headers)
        if addDeviceOut.status_code == 201:
            print(f"INFO: Device {addDevicePy['name']} added successfully, status code: {addDeviceOut.status_code}")
        else:
            print(f"ERROR: Device {addDevicePy['name']} had an error: {addDeviceOut.text}")
    except requests.RequestException as error:
        print(f"ERROR: {error}")

def delDevice(token, deviceName=""):

    URL = f'https://va10pwvbna304.us.ad.wellpoint.com/bca-networks/api/v4.0/devices/{deviceName}?clearReferences=false'

    headers = {
        'accept':'application/json',
        'Authorization':'Bearer ' + token
    }

    try:
        deleteDeviceOut = requests.delete(URL, data = deviceName, headers = headers)
        if deleteDeviceOut.status_code == 200:
            print(f"INFO: Device {deviceName} was deleted successfully, status code: {deleteDeviceOut.status_code}")
        else:
            print(f"ERROR: Device {deviceName} had an error: {deleteDeviceOut.text}")
    except requests.RequestException as error:
        print(f"ERROR: {error}")

    






