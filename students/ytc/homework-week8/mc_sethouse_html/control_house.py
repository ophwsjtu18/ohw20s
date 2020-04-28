import os
import time 
from mcpi.minecraft import Minecraft

mc=Minecraft.create()

print(1)
def makeHouse(x, y, z, wideX, wideZ, height, door = 0, roof = 0):

    for a in range(wideX):
        mc.setBlock(x+a, y, z, block.STONE.id)
        mc.setBlock(x+a, y, z+1+wideZ, block.STONE.id)

    for a in range(wideZ):
        mc.setBlock(x, y, z+1+a, block.STONE.id)
        mc.setBlock(x+wideX-1, y, z+1+a, block.STONE.id)

    for y in range(height):
        for a in range(wideX):
            mc.setBlock(x+a, y+y, z, block.STONE.id)
            mc.setBlock(x+a, y+y, z+1+wideZ, block.STONE.id)
        for a in range(wideZ):
            mc.setBlock(x, y+y, z+1+a, block.STONE.id)
            mc.setBlock(x+wideX-1, y+y, z+1+a, block.STONE.id)
    for x in range(wideX):
        for z  in range(wideZ):
            mc.setBlock(x+x, y, z+z, block.STONE.id)
    for x in range(wideX):
        for z  in range(wideZ):
            mc.setBlock(x+x, y+height-1, z+z, block.STONE.id)
    mc.setBlock(x+door, y+1, z,0)
    mc.setBlock(x+door, y+2, z,0)
    for z in range(2):
        for y in range(2): 
            mc.setBlock(x, y+y+roof, z+z+4, 20)
pass

while True:
    time.sleep(1)
    if os.path.isfile("house.txt"):
        f = open("house.txt")
        a = f.read()
        fx = open("x.txt")
        ax = int (fx.read())
        fy = open("y.txt")
        ay = int (fy.read())
        fz = open("z.txt")
        az = int (fz.read())
        if a == 'y':
            print(ax,ay,az)
            makeHouse(ax,ay,az,10,6,10)
            with open('../htdocs/house.txt','w') as f:
                f.write('n')



