import serial
import serial.tools.list_ports
import time
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
ports = list(serial.tools.list_ports.comports())
ser=serial.Serial(port='COM2')
x0=-7
x1=10
z0=-74
z1=-63
while True:
    pos=mc.player.getTilePos()
    mc.postToChat("The position is "+"x="+str(pos.x)+" y="+str(pos.y)+" z="+str(pos.z))
    print(pos.x)
    if (pos.x>=x0 and pos.x<=x1 and pos.z>=z0 and pos.z<=z1):
       ser.write('01234567'.encode())
       print("light")
    else:
       ser.write('ABCDEFGH'.encode())
       print("close")
    time.sleep(3)
