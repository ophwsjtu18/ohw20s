from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()

pos=mc.player.getTilePos()
print("player pos is",pos)
for i in range(10):
  mc.setBlock(pos.x,pos.y-i,pos.z,1)