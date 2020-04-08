from mcpi.minecraft import Minecraft
import serial
import serial.tools.list_ports
import time

mc=Minecraft.create()

pos=mc.player.getTilePos()
mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 

while True:
    pos=mc.player.getTilePos()
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    mc.setBlock(pos.x,pos.y,pos.z,1)

#lots of blocks
