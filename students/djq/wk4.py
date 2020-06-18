import os
import time
from mcpi.minecraft import Minecraft
mc=Minecraft.create()

def buildHouse(x,y,z,l,w,h):
    for i in range(l+10):
        for j in range(w+10):
            for k in range(h+10):
                mc.setBlock(x+i,y+j,z+k,0)
    for i in range(l):
        for j in range(w):
            mc.setBlock(x+i,y+j,z,41)
            mc.setBlock(x+i,y+j,z+h-1,41)
    for i in range(l):
        for k in range(h):
            mc.setBlock(x+i,y,z+k,41)
            mc.setBlock(x+i,y+w-1,z+k,41)
    for j in range(w):
        for k in range(h):
            mc.setBlock(x,y+j,z+k,41)
            mc.setBlock(x+l-1,y+j,z+k,41)
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
            print("finish")
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
            buildHouse(ax,ay,az,10,6,10)
            with open('../htdocs/house.txt','w') as f:
                f.write('n')
