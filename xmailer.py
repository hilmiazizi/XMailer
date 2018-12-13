#import system library
import os
from colorama import Fore, Style
import requests
import time

#import local library
from lib import banner
from lib import normal_mode
from lib import split_mode
from lib import combination

#Main Program
main_select = 1
while(main_select):
    os.system('clear')
    banner.main()
    print (Style.BRIGHT + "Select Mode :")
    print (Fore.GREEN + Style.BRIGHT + "1. Normal Mode")
    print (Fore.GREEN + Style.BRIGHT + "2. Split Mode")
    print (Fore.GREEN + Style.BRIGHT + "3. Auto Make Inbox Combination")
    main_select = input(Style.BRIGHT + "Your Choice : ")
    if main_select == 1:
        os.system('clear')
        normal_mode.main()
        confirm = raw_input(Style.BRIGHT + "Press Enter")
    elif main_select == 2 :
        os.system('clear')
        split_mode.main()
        confirm = raw_input(Style.BRIGHT + "Press Enter")
    elif main_select == 3:
        os.system('clear')
        combination.main()
        confirm = raw_input(Style.BRIGHT + "Press Enter")
    else:
        print ""
