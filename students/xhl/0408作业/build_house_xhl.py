from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
pos=mc.player.getTilePos()


def buildHouse(x,y,z,l,w,h):
    for i in range(l+10):
        for j in range(w+10):
            for k in range(h+10):
                mc.setBlock(x+i,y+j,z+k,0)
    for i in range(l):
        for j in range(w):
            mc.setBlock(x+i,y+j,z,1)
            mc.setBlock(x+i,y+j,z+h-1,1)
    for i in range(l):
        for k in range(h):
            mc.setBlock(x+i,y,z+k,1)
            mc.setBlock(x+i,y+w-1,z+k,1)
    for j in range(w):
        for k in range(h):
            mc.setBlock(x,y+j,z+k,1)
            mc.setBlock(x+l-1,y+j,z+k,1)
    mc.setBlock(x+(l/2),y+(w/2),z,160)
    mc.setBlock(x+(l/2),y+(w/2),z+h-1,160)
    mc.setBlock(x+(l/2),y+(w/2)-1,z,160)
    mc.setBlock(x+(l/2),y+(w/2)-1,z+h-1,160)
    mc.setBlock(x,y+(w/2),z+(h/2),160)
    mc.setBlock(x+l-1,y+(w/2),z+(h/2),160)
    mc.setBlock(x,y+(w/2)-1,z+(h/2),160)
    mc.setBlock(x+l-1,y+(w/2)-1,z+(h/2),160)
    mc.setBlock(x+(l/2)-1,y+(w/2),z,160)
    mc.setBlock(x+(l/2)-1,y+(w/2),z+h-1,160)
    mc.setBlock(x+(l/2)-1,y+(w/2)-1,z,160)
    mc.setBlock(x+(l/2)-1,y+(w/2)-1,z+h-1,160)
    mc.setBlock(x,y+(w/2),z+(h/2)-1,160)
    mc.setBlock(x+l-1,y+(w/2),z+(h/2)-1,160)
    mc.setBlock(x,y+(w/2)-1,z+(h/2)-1,160)
    mc.setBlock(x+l-1,y+(w/2)-1,z+(h/2)-1,160)
pass
while True:
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    if pos.x == 100 and pos.y == 100 and pos.z == 100:
        mc.postToChat("House has been built")
        buildHouse(100,100,100,10,6,10)
        break
    
    
