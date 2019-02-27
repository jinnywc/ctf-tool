p = 3
q = 11
e = 3

n = p*q
na = long((p-1)*(q-1))

i = 1
for i in range(300000):
    a = i*na +1
    if a%e == 0:
        d = a/e
        print d
        break
    i = i+1
    
