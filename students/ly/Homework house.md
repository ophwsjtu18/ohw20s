![image](https://github.com/ophwsjtu18/ohw20s/blob/master/students/ly/IMG_0291.png)
![iamge](https://github.com/ophwsjtu18/ohw20s/blob/master/students/ly/IMG_0293.png)


from mcpi.minecraft import Minecraft
import time
import serial
import serial.tools.list_ports

ser=serial.Serial(port='COM1')
time.sleep(2)
mc=Minecraft.create()

def house(x,y,z,l,w,h):
    for i in range (l):
        for j in range (w):
            mc.setBlock(x+i,y,z+j,5)
            mc.setBlock(x+i,y+h-1,z+j,5)
    for i in range (l+2):
        mc.setBlock(x-1+i,y,z-1,126)
        mc.setBlock(x-1+i,y,z+w,126)
        mc.setBlock(x-1+i,y+h-1,z-1,126)
        mc.setBlock(x-1+i,y+h-1,z+w,126)
    for j in range (w):
        mc.setBlock(x-1,y,z+j,126)
        mc.setBlock(x+l,y,z+j,126)
        mc.setBlock(x-1,y+h-1,z+j,126)
        mc.setBlock(x+l,y+h-1,z+j,126)
    for i in range (l):
        for k in range (h-2):
            mc.setBlock(x+i,y+1+k,z,160)
            mc.setBlock(x+i,y+1+k,z+w-1,160)
    for j in range (w-1):
        for k in range (h-2):
            mc.setBlock(x,y+1+k,z+j,160)
            mc.setBlock(x+l-1,y+1+k,z+j,160)
    mc.setBlock(x+l/2-1,y+1,z,0)
    mc.setBlock(x+l/2,y+1,z,0)
    mc.setBlock(x+l/2-1,y+2,z,0)
    mc.setBlock(x+l/2,y+2,z,0)
    
    while True:
        pos=mc.player.getTilePos()
        if pos.x<=x+l and pos.x>=x and pos.y<=y+h and pos.y>=y and pos.z<=w+z and pos.z>=z:
            ser.write("01234567".encode())
            mc.postToChat("welcome home , light on")
            time.sleep(1)
        else:
            ser.write("abcdefgh".encode())
            mc.postToChat("a house has been built on x:"+str(x)+"y:"+str(y)+"z:"+str(z))
            mc.postToChat(str(pos.x)+","+str(pos.y)+","+str(pos.z))
            time.sleep(1)

house(-400,70,-200,12,12,6)
