import os

def greetingString():
        os.system("CLS")
        print('  --------------------------------------------------------- ')
        print(f"  Welcome to the automated add/removal of devices in TSNA ")
        print('  --------------------------------------------------------- ')

def menuString():
        print('  -------------------------------------------------------------- ')
        print('\t\t    Menu - Please choose an option')
        print('\t\t     Only numbers are accepted')
        print('  -------------------------------------------------------------- ')
        print('  >\t\t      1. To add/delete devices in TSNA\t\t<\n')   
        print('  >\t\t      2. Exit the program\t\t       <')
        print('  -------------------------------------------------------------- \n')


def inputErrorString():
        os.system("CLS")
        print('  ------------------------------------------------- ')  
        print('>      INPUT ERROR: Only numbers are allowed       <')
        print('  ------------------------------------------------- ')
