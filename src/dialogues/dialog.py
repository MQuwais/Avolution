###
# Author : Muhammad Quwais Saputra
###

from system.clear import *
import sys
import time

from src.dialogues.malbate.hacking import *

class Dialog:
    def first():
        while True:
            Clear()
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
