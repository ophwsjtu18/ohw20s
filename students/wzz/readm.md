# this is wzz's folder
welcome

*italic test*  
**bold test**  
1.mixed list  
  -what is this?  
 ---
 ~~cross the line~~   
 |first header|second header|
 |--------------|---------------|
 |content cell1|content cell2|
 |content column 1|content column 2|

from mcpi.minecraft import Minecraft
import mcpi.block as block
import serial
import serial.tools.list_ports
import time

com = serial.Serial(port='COM2')

mc=Minecraft.create()

pos=mc.player.getTilePos()

stayed_time=0

def housebuild(x,y,z,l,w,h):
    for i in range(l)
        for j in range(w)
            mc.setBlock(x+i,y+h,z+j,5)
            mc.setBlock(x+i,y-1,z+j,5)
    for i in range(l)
        for j in range(h)
            mc.setBlock(x+i,y+j,z,5)
            mc.setBlock(x+i,y+j,z+w,5)
    for i in range(w)
        for j in range(h)
            mc.setBlock(x,y+j,z+i,5)
            mc.setBlock(x+l,y+j,z+i,5)

        
     


def led(x,y,z,l,w,h)
    while 1
        pos = mc.player.getTilePos()
        if(pos.x>=x and pos.x<=x+l and pos.y>=y and pos.y<=y+h-1 and pos.z>=z and pos.z<=z+w-1 )
            inhouse = true
        else:
            inhouse = false
        time.sleep(0.5)
        print(inhouse)
        if inhouse:
            com.write(1)
        else:
            com.write(0)
        time.sleep(0.5)
        
x=0
y=pos.y
z=0
l=200
w=100
h=100
housebuild(x,y,z,l,w,h)
led(z,y,z,l,w,h)
