import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()

for i in range(3):
    for j in range(3):
        mc.setBlock(pos.x+i-1, pos.y-1, pos.z+j-1, 41)

