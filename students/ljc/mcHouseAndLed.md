from mcpi.minecraft import Minecraft
import mcpi.block as block
import serial
import serial.tools.list_ports
import time

ser=serial.Serial(port='COM2')

time.sleep(2)

mc=Minecraft.create()
pos=mc.player.getTilePos()
mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 

def housebuild(x,y,z,l,w,h):
    for i in range(l):
        for j in range(w):
            mc.setBlock(x+i,y,z+j,5)#wood plank
            mc.setBlock(x+i,y+h-1,z+j,1)#stone
    for i in range(l):
        for j in range(h):
            mc.setBlock(x+i,y+j,z,1)
            mc.setBlock(x+i,y+j,z+w-1,1)
    for i in range(w):
        for j in range(h):
            mc.setBlock(x,y+j,z+i,1)
            mc.setBlock(x+l-1,y+j,z+i,1)
    dpx=x+l/2   
    for i in range(2):
        for j in range(3):
            mc.setBlock(dpx+i-1,y+j+1,z,0)
    for i in range(2):
        for j in range(2):
            mc.setBlock(x,y+j+2,z+w/2+i-1,0)
            mc.setBlock(x+l-1,y+j+2,z+w/2+i-1,0)
    for i in range(2):
        for j in range(2):
            mc.setBlock(x+l/2+i-1,y+j+2,z+w-1,0)

def led(x,y,z,l,w,h):
    a='0'
    na='1'
    while True:
        pos=mc.player.getTilePos()
        if (pos.x>=x and pos.x<=x+l-1 and pos.y>=y and pos.y<=y+h-1 and pos.z>=z and pos.z<=z+w-1):
            inhouse=True
        else:
            inhouse=False
        time.sleep(0.5)
        print(inhouse)
        if inhouse:
            ser.write(a.encode())
        else:
            ser.write(na.encode())
        time.sleep(0.5)
#need a house larger than 5*5*5 to make doors and windows
x=eval(input('x='))
y=eval(input('y='))
z=eval(input('z='))
l=eval(input('l='))
w=eval(input('w='))
h=eval(input('h='))
housebuild(x,y,z,l,w,h)
led(x,y,z,l,w,h)

