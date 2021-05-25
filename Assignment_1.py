import hashlib
import time

start = time.time()
inp_string = input()

x = "00000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"  

x = int(x, 16) 
cnt = 1
while 1:
    temp = inp_string + str(cnt)
    cnt = cnt + 1
    encoded = temp.encode() 
    y = hashlib.sha256(encoded).hexdigest()  
    value = int(y, 16)  
    if value < x:
        print(temp)
        break
