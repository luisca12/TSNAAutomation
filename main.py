from utils import mkdir

import os
import getpass

def main():
    mkdir()

    from log import authLog
    from utils import checkIsDigit
    from fileHandler import openNDLM
    from strings import greetingString, menuString, inputErrorString
    from httpRequests import getToken, addDevice, delDevice

    greetingString()
    
    while True:
        username = input("Please enter your username: ")
        authLog.info(f"Username successfully saved, username: {username}")
        print(f"INFO: Username successfully saved, username: {username}")
        password = getpass.getpass("Please enter your password: ")
        authLog.info(f"Password successfully saved.")
        print(f"INFO: Password successfully saved")
        
        menuString(username)
        selection = input("Please choose the option that you want: ")

        if checkIsDigit(selection):
            if selection == "1":
                # This option will add and remove devices from TSNA
                tokenOut = getToken(username, password)
                data = openNDLM()
                for item in data:
                    if item == 'ADD/CREATE NEW':
                        addDevice(tokenOut)
                    if item == 'DECOMMISSION':
                        delDevice(tokenOut, '')

            if selection == "2":
                authLog.info(f"User {username} logged out from the program.")
                break
        else:
            authLog.error(f"Wrong option chosen {selection}")
            inputErrorString()
            os.system("PAUSE")

if __name__ == "__main__":
    main()