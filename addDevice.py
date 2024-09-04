from datetime import date
import json

addDeviceString = '''
{ 
    "name": "ncdur-ivy-sdw-02",
    "realmId": {
      "componentName": "Anthem",
      "componentType": "Realm",
      "qualifiers": {
        "additionalProp1": null,
        "additionalProp2": null,
        "additionalProp3": null
      }
    },
    "onlineFlag": true,
    "deviceTypeId": {
      "id": "BE2B2D21-1CAA-53C3-05C3-CBB0A5D151B8",
      "componentName": "Cisco IOS Switch/Router",
      "componentType": "DeviceAdapter",
      "qualifiers": {
        "additionalProp1": null,
        "additionalProp2": null,
        "additionalProp3": null
      }
    },
    "categoryId": 1,
    "securityContextName": null,
    "securityContextTypeId": 0,
    "primaryInterface": {
      "address": "ncdur-ivy-sdw-02.mgmt.internal.das",
      "accessModeId": 3,
      "transferModeId": 4,
      "deviceAgentId": {
        "componentName": "Local",
        "componentType": "DeviceAgent",
        "qualifiers": {
          "additionalProp1": null,
          "additionalProp2": null,
          "additionalProp3": null
        }
      },
      "deviceSecurityProfileId": {
        "componentName": "Default",
        "componentType": "DeviceSecurityProfile",
        "qualifiers": {
          "additionalProp1": null,
          "additionalProp2": null,
          "additionalProp3": null
        }
      },
      "autoDiscoverDspFlag": true
    },
    "dynamicFields": [
        {
          "id": "934248822-727",
          "name": "Activity Type",
          "values": [
            "Replace (Refresh)"
          ],
          "dynamicFieldDetailsLink": "https://va10pwvbna304.us.ad.wellpoint.com/bca-networks/api/v4.0/dynamic_fields/934248822-727"
        },
        {
            "id": "1202202334-656",
            "name": "Install Date",
            "values": [
              "09/3/24"
            ],
            "dynamicFieldDetailsLink": "https://va10pwvbna304.us.ad.wellpoint.com/bca-networks/api/v4.0/dynamic_fields/1202202334-656"
          },
          {
            "id": "426945997-208",
            "name": "Serial Number",
            "values": [
              "FLM274711RB"
            ],
            "dynamicFieldDetailsLink": "https://va10pwvbna304.us.ad.wellpoint.com/bca-networks/api/v4.0/dynamic_fields/426945997-208"
          }
    
      ]
  }
'''

todaysDate = date.today()
todaysDate = todaysDate.strftime('%m/%d/%y')
# print(todaysDate,"\n")

addDevicePy = json.loads(addDeviceString)
for items in addDevicePy['dynamicFields']:
    if items['id'] == '1202202334-656':
        items['values'] = [todaysDate]

addDeviceJson = json.dumps(addDevicePy)
          

# print(addDeviceJson)