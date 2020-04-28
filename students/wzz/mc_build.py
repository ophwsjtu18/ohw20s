import os
import time 
from mcpi.minecraft import Minecraft

mc=Minecraft.create()


l0 = 0
h0 = 0
w0 = 0

while True:
    pos=mc.player.getTilePos()

    if os.path.isfile("width.txt") and os.path.isfile("length.txt") and os.path.isfile("height.txt"):
        f1 = open("width.txt")
        f2 = open("length.txt")
        f3 = open("height.txt")
        w = eval(f1.read())
        l = eval(f2.read())
        h = eval(f3.read())
        pos = mc.player.getTilePos()
        x = pos.x
        y = pos.y
        z = pos.z

        if w != w0 or l != l0 or h != h0:
            l0 = l
            h0 = h
            w0 = w
            for i in range(l):
                for j in range(w):
                    mc.setBlock(x+i,y+h,z+j,5)
                    mc.setBlock(x+i,y-1,z+j,5)
            for i in range(l):
                for j in range(h):
                    mc.setBlock(x+i,y+j,z,5)
                    mc.setBlock(x+i,y+j,z+w,5)
            for i in range(w):
                for j in range(h):
                    mc.setBlock(x,y+j,z+i,5)
                    mc.setBlock(x+l,y+j,z+i,5)
     
