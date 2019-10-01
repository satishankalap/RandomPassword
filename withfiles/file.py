import random

def pin():
    l1=[i for i in range(10)]
    l2=[chr(i) for i in range(97,107)]
    a=random.sample(l1,4)
    b=random.sample(l2,4)
    c=random.sample(l1,4)
    d=random.sample(l2,4)
    e=a+b+c+d
    new=""
    for i in e:
        new=new+str(i)
    return new
pin()
    
