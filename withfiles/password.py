import random
from file import pin

auto_pin=pin()

def write(name):
    file=open("random.txt","a")
    psd=auto_pin
    file.write(name)
    file.write("\n")
    file.write(str(psd))
    file.write("\n")

def read():
    usr=input("enter a username:")
    file=open("random.txt","r")
    fol=file.readlines()
    lis=[]
    for line in fol:
        lis.append(line.rstrip())
##    print(lis)
    if usr in lis:
        print("user already exists")
        return 0
    else:
        print("We have sent you an email of password\nlogin with that password.")
        write(usr)
        return 1
read()
        

