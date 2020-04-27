import os
import time
from mcpi.minecraft import Minecraft

mc=Minecraft.create()

while True:
    pos=mc.player.getTilePos()
    if os.path.isfile("control.txt"):
        f=open("control.txt")
        a=f.read()
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

