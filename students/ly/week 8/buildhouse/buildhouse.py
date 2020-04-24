import os
import time
from mcpi.minecraft import Minecraft

mc=Minecraft.create()

def house(x,y,z,l,w,h):
    for i in range (l):
        for j in range (w):
            mc.setBlock(x+i,y,z+j,5)
            mc.setBlock(x+i,y+h-1,z+j,5)
    for i in range (l+2):
        mc.setBlock(x-1+i,y,z-1,126)
        mc.setBlock(x-1+i,y,z+w,126)
        mc.setBlock(x-1+i,y+h-1,z-1,126)
        mc.setBlock(x-1+i,y+h-1,z+w,126)
    for j in range (w):
        mc.setBlock(x-1,y,z+j,126)
        mc.setBlock(x+l,y,z+j,126)
        mc.setBlock(x-1,y+h-1,z+j,126)
        mc.setBlock(x+l,y+h-1,z+j,126)
    for i in range (l):
        for k in range (h-2):
            mc.setBlock(x+i,y+1+k,z,160)
            mc.setBlock(x+i,y+1+k,z+w-1,160)
    for j in range (w-1):
        for k in range (h-2):
            mc.setBlock(x,y+1+k,z+j,160)
            mc.setBlock(x+l-1,y+1+k,z+j,160)
    mc.setBlock(x+l/2-1,y+1,z,0)
    mc.setBlock(x+l/2,y+1,z,0)
    mc.setBlock(x+l/2-1,y+2,z,0)
    mc.setBlock(x+l/2,y+2,z,0)
    while True:
        pos=mc.player.getTilePos()
        mc.postToChat("a house has been built on x:"+str(x)+"y:"+str(y)+"z:"+str(z))
        mc.postToChat(str(pos.x)+","+str(pos.y)+","+str(pos.z))
        time.sleep(1)


if os.path.isfile("buildhouse.txt"):
        f=open("buildhouse.txt")
        a=f.read()
        X,Y,Z,L,W,H=a.split(',',5)
        X=int(X)
        Y=int(Y)
        Z=int(Z)
        L=int(L)
        W=int(W)
        H=int(H)
        house(X,Y,Z,L,W,H)


