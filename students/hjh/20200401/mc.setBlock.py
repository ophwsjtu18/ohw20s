[setBlock]

import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()

for a in range(10):
    mc.setBlock(pos.x,pos.y-a,pos.z,1)

