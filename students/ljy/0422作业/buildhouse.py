import os
import time
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
def house(x,y,z,l,w,h):
    for i in range(l):
        for a in range(w):
            mc.setBlock(x+a,y,z+i,3)
    for t in range(h):
        for i in range(l):
            mc.setBlock(x,y+t,z+i,3)
            mc.setBlock(x+w-1,y+t,z+i,3)
        for a in range (w):
            mc.setBlock(x+a,y+t,z,3)
            mc.setBlock(x+a,y+t,z+l-1,3)
    for i in range(l):
        for a in range(w):
            mc.setBlock(x+a,y+h,z+i,2)
    for i in range(3):
        mc.setBlock(x+w/2,y+1+i,z,0)
    for i in range(2):
        for a in range(2):
            mc.setBlock(x+w-1,y+4+i,z+l/2+a,0)

while True:
   pos=mc.player.getTilePos()
   if os.path.isfile("buildhouse.txt"):
        f=open("buildhouse.txt")
        a=f.read()
        if a=='y':
            pos=mc.player.getTilePos()
            house(pos.x+1,pos.y,pos.z+1,5,5,8)
            mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
            break
       
