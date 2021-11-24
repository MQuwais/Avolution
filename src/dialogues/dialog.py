###
# Author : Muhammad Quwais Saputra
###

from system.clear import *
from system.delete_all_pycache import *
import sys
import time

from src.dialogues.malbate.hacking import *
from arm.banner import *

class Dialog:
    def first():
        while True:
            Clear()
            Banner()
            print("""
What do you think You gonna do?
   1. Start Hacking
   2. exit
            """)
            x = input("Avolution > ")
            if x == "1":
                Dialog.second()
            elif x == "2":
                DAP()
                sys.exit()
            else:
                print("[!] Wrong Input")
                time.sleep(2)
    def second():
        while True:
            Clear()
            Banner()
            print("""
Hack What?
   1. Facebook
   2. back
            """)
            x = input("Avolution (Hacking) > ")
            if x == "1":
                Hacking.facebook()
            elif x == "2":
                Dialog.first()
            else:
                print("[!] Wrong input")
                time.sleep(2)

