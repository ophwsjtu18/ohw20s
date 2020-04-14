import mcpi.minecraft as minecraft
import time
from _ast import For
from mcpi import block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
mc.postToChat("x="+str(pos.x)+" y"+str(pos.y)+" z="+str(pos.z))
print("player pos is",pos)


stayed_time=0


def setHouse(nowX, nowZ, wideX, wideZ, level, height, door = 0, roof = 0):


    for a in range(wideX):
        mc.setBlock(pos.x+a, pos.y, pos.z, block.STONE.id)
        mc.setBlock(pos.x+a, pos.y, pos.z+1+wideZ, block.STONE.id)

    for a in range(wideZ):
        mc.setBlock(pos.x, pos.y, pos.z+1+a, block.STONE.id)
        mc.setBlock(pos.x+wideX-1, pos.y, pos.z+1+a, block.STONE.id)

    for y in range(height):
        for a in range(wideX):
            mc.setBlock(pos.x+a, pos.y+y, pos.z, block.STONE.id)
            mc.setBlock(pos.x+a, pos.y+y, pos.z+1+wideZ, block.STONE.id)
        for a in range(wideZ):
            mc.setBlock(pos.x, pos.y+y, pos.z+1+a, block.STONE.id)
            mc.setBlock(pos.x+wideX-1, pos.y+y, pos.z+1+a, block.STONE.id)
    for x in range(wideX):
        for z  in range(wideZ):
            mc.setBlock(pos.x+x, pos.y, pos.z+z, block.STONE.id)
    for x in range(wideX):
        for z  in range(wideZ):
            mc.setBlock(pos.x+x, pos.y+height-1, pos.z+z, block.STONE.id)
    mc.setBlock(pos.x+door, pos.y+1, pos.z,0)
    mc.setBlock(pos.x+door, pos.y+2, pos.z,0)
    for z in range(2):
        for y in range(2): 
            mc.setBlock(pos.x, pos.y+y+roof, pos.z+z+4, 20)
setHouse(pos.x, pos.z, 10 ,8, pos.y,10,5,2)

while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    
