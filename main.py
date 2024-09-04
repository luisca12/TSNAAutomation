from utils import mkdir

import os

def main():
    mkdir()
    from log import authLog
    from utils import checkIsDigit
    from strings import greetingString, menuString, inputErrorString
    from httpRequests import token, addDevice, URL
    import getpass
    greetingString()
    
    while True:
        menuString()
        selection = input("Please choose the option that yyou want: ")
        if checkIsDigit(selection):
            if selection == "1":
                # This option will add and remove devices from TSNA
                username = input("Please enter your username: ")
                password = getpass.getpass("Please enter your password: ")
                tokenOut = token(username, password, URL)
                addDevice(tokenOut)
            if selection == "2":
                # authLog.info(f"User {} disconnected from the devices {}")
                # authLog.info(f"User {} logged out from the program.")
                break
        else:
            authLog.error(f"Wrong option chosen {selection}")
            inputErrorString()
            os.system("PAUSE")

if __name__ == "__main__":
    main()