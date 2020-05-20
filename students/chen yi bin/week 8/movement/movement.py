import os
import time 
from mcpi.minecraft import Minecraft
mc=Minecraft.create()


while True:
    pos=mc.player.getTilePos()  
    if os.path.isfile("move.txt"):
        a = open("move.txt")
        b =a.read()
        if b == 'w':
            mc.player.setTilePos(pos.x+1,pos.y,pos.z)
        elif b == 's':
            mc.player.setTilePos(pos.x-1,pos.y,pos.z)
        elif b == 'a':
            mc.player.setTilePos(pos.x,pos.y,pos.z-1)
        elif b == 'd':
            mc.player.setTilePos(pos.x,pos.y,pos.z+1)
        time.sleep(1)
