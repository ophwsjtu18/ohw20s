import serial
import string
import serial.tools.list_ports
import time
from mcpi.minecraft import Minecraft
import mcpi.block as block
mc=Minecraft.create();
pos=mc.player.getTilePos()
def box(x,y,z,l,w,h,num=12):
    for i in range(0,l):
        for j in range(0,w):
            for k in range(0,h):
                mc.setBlock(x+i,y+j,z+k,num);



def run():
    ser=serial.Serial(port='COM4')
    time.sleep(1);
    action="012345678"
    ser.write(action.encode())
def house(x,y,z,l,w,h,q=3):
    box(x,y,z,l,1,h,q)
    box(x,y,z,1,w,h,q)
    box(x,y,z,l,w,1,q)
    box(x,y+w,z,l,1,h,q)
    box(x+l,y,z,1,w,h,q)
    box(x,y,z+h,l,w,1,q)
    windows(x,y+5.0/10*w,z);
    windows(x+4.0/l*10,y+6.0/10*w,z);
    windows(x+8.0/10*l,y+6.0/10*w,z)
    windows(x,y+5.0/10*w,z+h);
    windows(x+4.0/10*l,y+6.0/10*w,z+h);
    windows(x+8.0/10*l,y+6.0/10*w,z+h)
    box(x+6,y,z+h,2,4,1,block.WOOD.id)
    
    
    
    



def windows(x,y,z):
    box(x,y,z,2,2,1,20)





tmpa=pos.x
tmpb=pos.y+10
tmpc=pos.z
house(pos.x,pos.y+10,pos.z,10,10,10)
while 1:
    if(abs(pos.x-tmpa)<=4 and abs(pos.y-tmpb)<=4 and abs(pos.z-tmpc)<=4):
        run()
        break
