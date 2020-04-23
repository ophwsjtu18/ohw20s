import os
import time
from mcpi.minecraft import Minecraft

mc=Minecraft.create()
def house(x,y,z,l,w,h):
    midx = x+l/2
    midy = y+h/2
    mc.setBlocks(x, y, z, x+l, y+h, z+w,4)
    mc.setBlocks(x+1, y, z+1, x+l-1, y+h-1, z+w-1,0)
    mc.setBlocks(midx-1, y, z, midx+1, y+3, z, 0)
    mc.setBlocks(x+l/4-1, y+h-h/4+1, z, midx-l/4+1, midy+h/4-1, z,20)
    mc.setBlocks(midx+l/4-1, y+h-h/4+1, z, x+l-l/4+1, midy+h/4-1, z, 20)
    mc.setBlocks(x, y+h, z, x+l, y+h, z+w, 17)
    mc.setBlocks(x+1, y-1, z+1, x+l-1, y-1, z+w-1, 35, 14)
pos=mc.player.getTilePos()
if os.path.isfile("house.txt"):
    f=open("house.txt")
    a=f.read()
    while len(a)==0:
        a=f.read()
    l,w,h=a.split(',',2)
house(pos.x,pos.y,pos.z,int(l),int(w),int(h))
