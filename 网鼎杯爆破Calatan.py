import hashlib
import requests
def get(a):
    for i in range(10000,100000000):
        b = hashlib.sha384(str(i)).hexdigest()
        if b[0:6] == a:
            return i

captcha = get("379430")
print captcha

url = "http://106.75.31.181:9999"
postdata = {'P':captcha}
a = requests.Session()
result = a.post(url,data=postdata)

print result
