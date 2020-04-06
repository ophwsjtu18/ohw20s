import mcpi.minecraft as minecraft
import mcpi.block as block
import time
from math import *

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
drt = mc.player.getDirection()

# Do this:
# for i in range(0, 10):
#     mc.setBlock(pos.x, pos.y - 1 - i, pos.z, block.STONE.id)

# Or this: 
mc.setBlock(pos.x, pos.y - 1, pos.z, block.STONE.id)
for i in range(0, 3):
    for j in range(0, 3):
        mc.setBlock(pos.x - 1 + i, pos.y - 2, pos.z - 1 + j,
                    block.STONE.id)
