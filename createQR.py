import random 
import string 
import datetime
import hashlib
import os
Lett = string.ascii_letters
system_random = random.SystemRandom()
Letters = []
for r in Lett:
    Letters.append(r)
Sonderzeichen = ["!","$","%","&","#","(",")","=","?"]
for s in (Sonderzeichen):
    Letters.append(s)
password = ""
for i in range(200):
    password = password + Letters[system_random.randint(0,len(Letters)-1)]
    pass
password = password +","
for i in range(50):
    password = password + Letters[system_random.randint(0,len(Letters)-1)]
    pass
encoded=str(datetime.datetime.now()).encode()
hexTime = hashlib.sha256(encoded)

result = password +hexTime.hexdigest()
print(result)