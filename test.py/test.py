import os
import sys


def getMenuItem():
    switcher={
            "0":'Exit',
            "1":'Something'
            }
    
    #Display the menu
    os.system('cls')
    print("PyOlympus v0.0")
    print("______________________________________")
    print("Menu Item - Description               ")
    print("---------   --------------------------")
    print(" 0          Exit Oympus               ")
    print("______________________________________")
    menu_selection = input("Select a menu option: ")

    menu_selection = switcher.get(menu_selection,"Invalid Menu Selection")

    return menu_selection


#main menu

#
my_item = getMenuItem()
if (my_item) == "Exit":
    print("Closing application ... ")
    sys.exit()
else:
    print(f"Implementing command: {my_item}")
