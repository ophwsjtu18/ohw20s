import os
import time
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
mc.player.setTilePos(-32,9,-45)
while True:
    pos=mc.player.getTilePos()
    if os.path.isfile("move.txt"):
       f=open("move.txt")
       a=f.read()
       print(a)
       if a=='w':
          mc.player.setTilePos(pos.x+1,pos.y+pos.z)
          time.sleep(2)
       elif a=='s':
          mc.player.setTilePos(pos.x-1,pos.y,pos.z)
          time.sleep(2)
       elif a=='a':
          mc.player.setTilePos(pos.x,pos.y,pos.z-1)
          time.sleep(2)
       elif a=='d':
          mc.player.setTilePos(pos.x,pos.y,pos.z+1)
          time.sleep(2)
       elif a=='q':
          break;
