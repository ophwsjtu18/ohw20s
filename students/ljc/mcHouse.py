import os
import time
from mcpi.minecraft import Minecraft

mc=Minecraft.create()
pos=mc.player.getTilePos()

def housebuild(x,y,z,l,w,h):
    for i in range(l):
        for j in range(w):
            mc.setBlock(x+i,y,z+j,5)#wood plank
            mc.setBlock(x+i,y+h-1,z+j,1)#stone
    for i in range(l):
        for j in range(h):
            mc.setBlock(x+i,y+j,z,1)
            mc.setBlock(x+i,y+j,z+w-1,1)
    for i in range(w):
        for j in range(h):
            mc.setBlock(x,y+j,z+i,1)
            mc.setBlock(x+l-1,y+j,z+i,1)
    dpx=x+l/2   
    for i in range(2):
        for j in range(3):
            mc.setBlock(dpx+i-1,y+j+1,z,0)
    for i in range(2):
        for j in range(2):
            mc.setBlock(x,y+j+2,z+w/2+i-1,0)
            mc.setBlock(x+l-1,y+j+2,z+w/2+i-1,0)
    for i in range(2):
        for j in range(2):
            mc.setBlock(x+l/2+i-1,y+j+2,z+w-1,0)
x=pos.x+2
y=pos.y
z=pos.z+2
if os.path.isfile("house.txt"):
        f=open("house.txt",'w')
        f.truncate()
        f.close()
        
while True:
    if os.path.isfile("house.txt"):
        f=open("house.txt")
        a=f.read()
        if a<'9' and a>'0':
            n=eval(a)
            housebuild(x,y,z,n,n,n)
            print(a)
            break
    time.sleep(0.2)
