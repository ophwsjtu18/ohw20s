import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
for i in range(10):
    for a in range(10):
        mc.setBlock(pos.x+a , pos.y+i , pos.z ,1)
        mc.setBlock(pos.x+a , pos.y+i , pos.z+9, 1)
    for a in range(8):
        mc.setBlock(pos.x , pos.y+i , pos.z+1+a, 1)
        mc.setBlock(pos.x+9, pos.y+i, pos.z+1+a, 1)
for x in range(10):
    for z  in range(10):
            mc.setBlock(pos.x+x, pos.y, pos.z+z,1)
for x in range(10):
    for z  in range(10):
            mc.setBlock(pos.x+x, pos.y+9, pos.z+z,1)
