import os
import time
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
def House(x0,y0,z0,L,W,H):
    for y in range(H):
        for x in range(L):
            mc.setBlock(x0+x,y,z0,4)
            mc.setBlock(x0+x,y,z0+W-1,4)
        for x in range(W-2):
            mc.setBlock(x0,y,z0+1+x,4)
            mc.setBlock(x0+L-1,y,z0+1+x,4)
    for x in range(L):
        for z in range(W):
            mc.setBlock(x0+x,y0,z0+z,4)
    for x in range(L):
        for z in range(W):
            mc.setBlock(x0+x,y0+H-1,z0+z,4)
    for z in range(2):
        for y in range(2):
            mc.setBlock(x0+L,y0+y+2,z0+z+4,20)
    mc.setBlock(x0+L/2,y0+1,z0,0)
    mc.setBlock(x0+L/2,y0+2,z0,0)
    mc.setBlock(x0+L/2,y0+3,z0,0)
pos=mc.player.getTilePos()
if os.path.isfile("house_build.txt"):
   f=open("house_build.txt")
   a=f.read()
   print(a)
   l,w,h=a.split(',',2);
House (pos.x,pos.y,pos.z,int(l),int(w),int(h))
