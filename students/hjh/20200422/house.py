import os

import time 

from mcpi.minecraft import Minecraft

import mcpi.minecraft as minecraft

from _ast import For

from mcpi import block

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()

mc.postToChat("x="+str(pos.x)+" y"+str(pos.y)+" z="+str(pos.z))

print(pos)



for a in range(X):

    mc.setBlock(x+a, y, z, block.WOOD.id)

    mc.setBlock(x+a, y, z+1+Z, block.WOOD.id)

for a in range(Z):

    mc.setBlock(x, y, z+1+a, block.WOOD.id)

    mc.setBlock(x+X-1, y, z+1+a, block.WOOD.id)

for y in range(height):

    for a in range(X):

        mc.setBlock(x+a, y+y, z, block.WOOD.id)

        mc.setBlock(x+a, y+y, z+1+Z, block.WOOD.id)

    for a in range(Z):

         mc.setBlock(x, y+y, z+1+a, block.WOOD.id)

         mc.setBlock(x+X-1, y+y, z+1+a, block.WOOD.id)

for x in range(X):

    for z  in range(Z):

         mc.setBlock(x+x, y, z+z, block.WOOD.id)

for x in range(X):

    for z  in range(Z):

        mc.setBlock(x+x, y+height-1, z+z, block.WOOD.id)
