import random
from generate import pin
from parsing import GetDict
import mysql.connector
cred=GetDict()

conn=mysql.connector.connect(**cred)
cur=conn.cursor()

auto_pin=pin()

def checkEmail(email):
    a="SELECT email FROM data WHERE email=%s"
    b=(email,)
    cur.execute(a,b)
    res=cur.fetchall()
    if len(res)==1:
        return 0
    else:
        return 1


def generate():
    email=input("enter your email:")
    op=checkEmail(email)
    if op==1:
        mobile=int(input("enter your mobile number:"))
        password=auto_pin
        add="INSERT INTO data(email,mobile,password) VALUES (%s,%s,%s)"
        details=(email,mobile,password)
        cur.execute(add,details)
        conn.commit()
        print("Registered Successfully and your password is "+password)
    else:
        print("Email id already exists!")

generate()


