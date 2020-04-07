from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
for i in range(10):
    pos=mc.player.getTilePos()
    mc.setBlock(pos.x,pos.y-i,pos.z,1)
    time.sleep(1)
