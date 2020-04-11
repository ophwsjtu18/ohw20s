from mcpi.minecraft import Minecraft
import time
import serial
import serial.tools.list_ports

def house(x,y,z,l,w,h):
    midx = x+l/2
    midy = y+h/2
    mc.setBlocks(x, y, z, x+l, y+h, z+w,4)
    mc.setBlocks(x+1, y, z+1, x+l-1, y+h-1, z+w-1,0)
    mc.setBlocks(midx-1, y, z, midx+1, y+3, z, 0)
    mc.setBlocks(x+l/4-1, y+h-h/4+1, z, midx-l/4+1, midy+h/4-1, z,20)
    mc.setBlocks(midx+l/4-1, y+h-h/4+1, z, x+l-l/4+1, midy+h/4-1, z, 20)
    mc.setBlocks(x, y+h, z, x+l, y+h, z+w, 17)
    mc.setBlocks(x+1, y-1, z+1, x+l-1, y-1, z+w-1, 35, 14)
mc=Minecraft.create()
ser=serial.Serial(port='com20')
pos = mc.player.getPos()
house(pos.x,pos.y,pos.z,20,18,20)
while True:
    pos1=mc.player.getTilePos()
    print("x:"+str(pos1.x)+"y:"+str(pos1.y)+"z:"+str(pos1.z))
    if pos1.x>pos.x and pos1.x<=pos.x+20 and pos1.y>=pos.y-1 and pos1.y<=pos.y+18 and pos1.z>pos.z and pos1.z<=pos.z+20:
        mc.postToChat("welcome home")
        for i in range(8):
            action=str(i)
            ser.write(action.encode())
            time.sleep(1)
        while pos1.x>pos.x and pos1.x<=pos.x+20 and pos1.y>=pos.y-1 and pos1.y<=pos.y+18 and pos1.z>pos.z and pos1.z<=pos.z+20:
            pos1=mc.player.getTilePos()
            print("x:"+str(pos1.x)+"y:"+str(pos1.y)+"z:"+str(pos1.z))
            mc.postToChat("welcome to home")
        mc.postToChat("left home")
        j='A'
        while j<='H':
            action=j
            ser.write(action.encode())
            time.sleep(1)
            i=ord(j)
            i=i+1
            j=chr(i)
        
