# -*- coding: cp936 -*-
import requests
import base64

#url= "http://120.24.86.145:8002/web6/index.php"
url = "http://695274641c744c10ab7f83dbf5b92c65096f10be8ba846ff.game.ichunqiu.com/"

a = requests.Session()
response = a.get(url)
head = response.headers
flag = base64.b64decode(head['flag'])
flag = flag.split(':',1)[1]
print flag
flag = base64.b64decode(flag)   #�߱�һ��Ķ���һ�ν��룬�ؼ�����
print flag
postdata = {'ichunqiu':flag}      #marginҳ����ǲ���
result = a.post(url=url,data=postdata)

print result.text
