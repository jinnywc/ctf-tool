# -*- coding: cp936 -*-
a = "QWERTYUIOPASDFGHJKLZXCVBNM"
b ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c ="fAFAFASDASFAS"         #密文
e =""           #明文
i =0
def qwe(d):
    n =0
    if ord(d) > 90:
        d = ord(d) - 32
        d = chr(d)
    while(n < 26):
        if d == a[n]:
            d = b[n]
            break
        n = n +1
    return d

while(i < len(c)):
    f = qwe(c[i])
    i = i +1
    e =e + f


print e
