server: 
import socket  

s=socket.socket()  
s.connect(("127.0.0.1",25566))  
print("connected")  

while True:  
    msg=input("how big is the plane?")  
    s.send(msg.encode("ascii"))  
    msg2=input("what's the block id?")  
    s.send(msg2.encode("ascii"))  
---
receiver: 
import socket  
from mcpi.minecraft import Minecraft  
import mcpi.block as block  

s=socket.socket()  
s.bind(("127.0.0.1",25566))  
s.listen(5)  
mc=Minecraft.create()  

c,addr=s.accept()  
print(f"adresss {addr} connected")  

while True:  
    msg=c.recv(1024)  
    pos=mc.player.getTilePos()  
    n=eval(msg)  
    msg2=c.recv(1024)  
    n2=eval(msg2)  
    for i in range (n):  
        for j in range (n):  
            mc.setBlock(pos.x+i,pos.y-1,pos.z+j,n2)  
            print(f"{n}*{n}plane created")  
    
