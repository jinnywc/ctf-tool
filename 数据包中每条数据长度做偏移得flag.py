a = [144,150,139,145,165,120,139,91,160,93,167]
d = ""
i = 0
for b in range(-50,50):
    for i in range(len(a)):
        c = chr(a[i] + b)
        d = d + c
        i = i+1
    if "flag" in d:
        print d
        break
 
    
