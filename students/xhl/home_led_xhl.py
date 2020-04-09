from mcpi.minecraft import Minecraft
import time
import serial
import serial.tools.list_ports

mc=Minecraft.create()
pos=mc.player.getTilePos()
time.sleep(2)

ports = list(serial.tools.list_ports.comports())
print (ports)
for p in ports:
    print (p[1])
    if "SERIAL" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")
ser=serial.Serial(port='COM1')
time.sleep(2)

while True:
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please go to home x=-30 y=6 z=-40")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    if pos.x >= -30 and pos.x <= -20 and pos.y >= 6 and pos.y <= 12 and pos.z >= -40 and pos.z <= -30:
        action = "01234567"
        ser.write(action.encode())
        time.sleep(0.1)
    else:
        action = "ABCDEFGH"
        ser.write(action.encode())
        time.sleep(0.1)

        
