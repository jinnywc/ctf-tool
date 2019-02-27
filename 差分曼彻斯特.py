from Crypto.Util.number import *
id1 = 0x8893CA58
msg1 = 0x3EAAAAA56A69AA55A95995A569AA95565556
msg2 = 0x3EAAAAA56A69AA556A965A5999596AA95656
print hex(msg1 ^ msg2).upper()
s = bin(msg2)[6:]
print s
r=""
tmp = 0
for i in xrange(len(s)/2):
c = s[i*2]
if c == s[i*2 - 1]:
r += '1'
else:
r += '0'
print hex(int(r,2)).upper()