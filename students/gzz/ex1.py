import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
print("player pos is",pos)
for i in range(3):
    for j in range(3):
        mc.setBlock(pos.x-1+i,pos.y,pos.z-1+j,1)
