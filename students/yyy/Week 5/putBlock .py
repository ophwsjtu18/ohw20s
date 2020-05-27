from mcpi.minecraft import Minecraft
mc=Minecraft.create()

pos=mc.player.getTilePos()
print("player pos is",pos)
for i in range(10):
   mc.setBlock(pos.x+i,pos.y,pos.z)
