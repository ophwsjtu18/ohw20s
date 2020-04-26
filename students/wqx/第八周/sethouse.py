import os 
import time
from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()
location = mc.player.getTilePos()
print(location)
def house(x,y,z,l,w,h,mc):
    
    caizhi = (17,2)
    for i in range(w):
        for k in range(l):
            mc.setBlock(x+k,y+h-1,z+i,80)
            if i != 0 and k != 0 and i!=w-1 and k!=l-1:
                mc.setBlock(x+k,y,z+i,(5,2))
            else:
                mc.setBlock(x+k,y,z+i,80)
            
    for i in range(l):
        for k in range(h-2):
            if 1+k <= h//2 or 1+k > h//2 + 2:
                mc.setBlock(x+i,y+1+k,z,caizhi)
                mc.setBlock(x+i,y+1+k,z+w-1,caizhi)
            elif i+1 <= l//2-2 or i+1 >= l//2+2:
                   mc.setBlock(x+i,y+1+k,z,caizhi)
                   mc.setBlock(x+i,y+1+k,z+w-1,caizhi)
            else:
                mc.setBlock(x+i,y+1+k,z,20)
                mc.setBlock(x+i,y+1+k,z+w-1,20)
    for i in range(w-2):
        for k in range(h-2):
            if 1+k <= h//2 or 1+k > h//2 + 2:
                mc.setBlock(x,y+1+k,z+i+1,caizhi)
            elif i+1 <= w//2-2 or i+1 >= w//2+2:
                mc.setBlock(x,y+1+k,z+i+1,caizhi)
            else:
                mc.setBlock(x,y+1+k,z+i+1,20)
    for i in range(w-2):
        for k in range(h-2):
            if (k+1 >=3 and k+1<=6) or k+1 >=8:
                mc.setBlock(x+l-1,y+k+1,z+i+1,caizhi)
            elif k+1 == 7:
                if i+1 <=2 or (i+1>=7 and i+1<=w-8) or i+1>=w-3:
                    mc.setBlock(x+l-1,y+k+1,z+i+1,caizhi)
                else:
                    mc.setBlock(x+l-1,y+k+1,z+i+1,20)
            elif k+1<=5 and (i+1<=w//2-2 or i+1>=w//2+1):
                mc.setBlock(x+l-1,y+k+1,z+i+1,caizhi)
    n = (l+1)//2 if l<w else (w+1)//2 
    l2 = l
    w2 = w
    x2 = x
    z2 = z
    for j in range(n):
       x2 = x2 + 1
       z2 = z2 + 1
       w2 = w2 - 2
       l2 = l2 - 2
       for i in range(l2):
           for k in range(w2):
               mc.setBlock(x2+i,y+j+h,z2+k,80)
    mc.setBlock(x+l,y,z+w//2-1,(53,1))
    mc.setBlock(x+l,y,z+w//2,(53,1))
    mc.setBlock(x+l-1,y+1,z+w//2-1,block.DOOR_WOOD.id,5)
    mc.setBlock(x+l-1,y+2,z+w//2-1,block.DOOR_WOOD.id,8)
    mc.setBlock(x+l-1,y+1,z+w//2,block.DOOR_WOOD.id,2)
    
    mc.setBlock(x+l-1,y+2,z+w//2,block.DOOR_WOOD.id,8)
b=''
while True:
    if os.path.isfile('C:\Apache24\htdocs\house.txt'):
        f=open('C:\Apache24\htdocs\house.txt')
        a = f.read()
        print(a)
        pos = a.split(',')
        x = int(pos[0])
        y = int(pos[1])
        z = int(pos[2])
        l = int(pos[3])
        w = int(pos[4])
        h = int(pos[5])
        if b!=a:
            house(x,y,z,l,w,h,mc)
            b = a
        time.sleep(2)


