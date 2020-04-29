  
import os
import time
from mcpi.minecraft import Minecraft
mc=Minecraft.create()


def house(x0,y0,z0,l0,w0,h0):
    for i in range(h0):
        for a in range(l0):
            mc.setBlock(x0+a , y0+i , z0 ,1)
            mc.setBlock(x0+a , y0+i , z0+9, 1)
        for a in range(w0-2):
            mc.setBlock(x0 , y0+i , z0+1+a, 1)
            mc.setBlock(x0+9, y0+i, z0+1+a, 1)
    for x in range(l0):
        for z  in range(w0):
                mc.setBlock(x0+x, y0, z0+z,1)
    for x in range(l0):
        for z  in range(w0):
                mc.setBlock(x0+x, y0+h0, z0+z,1)
    mc.setBlock(x0+5, y0+1, z0,0)
    mc.setBlock(x0+5, y0+2, z0,0)
    mc.setBlock(x0+6,y0+1, z0,0)
    mc.setBlock(x0+6,y0+2, z0,0)
    for z in range(2):
          for y in range(2): 
                mc.setBlock(x0+9, y0+y+2, z0+z+4, 20)
while True:
   pos=mc.player.getTilePos()
   if os.path.isfile("webhouse.txt"):
        f=open("webhouse.txt")
        a=f.read()
        if a=='h':
            pos=mc.player.getTilePos()
            house(pos.x,pos.y,pos.z,10,10,10)  
            break
