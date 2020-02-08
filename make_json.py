import json
import hashlib
sha=hashlib.sha1()
sha.update('123456'.encode('utf-8'))
p1= sha.hexdigest()
sha=hashlib.sha1()
sha.update('123456789'.encode('utf-8'))
p2= sha.hexdigest()
data=[{'user':'root','password':p1,'load':'123456','自动登录':0,'记住密码':1},
      {'user':'gk','password':p2,'load':'123456789','自动登录':0,'记住密码':1}]
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)
