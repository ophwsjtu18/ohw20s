import os
import time
from mcpi.minecraft import Minecraft

mc=Minecraft.create()

while True:
    pos=mc.player.getTilePos()
    if os.path.isfile("move.txt"):
        f=open("move.txt")
        a=f.read()
        print(a)
        if a=='w':
            mc.player.setTilePos(pos.x+1,pos.y,pos.z)
            time.sleep(1)
        elif a=='s':
            mc.player.setTilePos(pos.x-1,pos.y,pos.z)
            time.sleep(1)
        elif a=='a':
            mc.player.setTilePos(pos.x,pos.y,pos.z-1)
            time.sleep(1)
        elif a=='d':
            mc.player.setTilePos(pos.x,pos.y,pos.z+1)
            time.sleep(1)
            
        
