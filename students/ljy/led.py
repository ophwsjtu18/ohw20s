#home & led
from mcpi.minecraft import Minecraft
import serial
import serial.tools.list_ports
import time

ports = list(serial.tools.list_ports.comports())
print (ports)

for p in ports:
    print (p[1])
    if "SERIAL" in p[1] or "UART" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")
	    
ser=serial.Serial(port='COM2')
 
time.sleep(1)

mc=Minecraft.create()
stayed_time=0

while True:
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please go to home x=-29 y=6 z=380 ")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
    if pos.x==-29 and pos.y==6 and pos.z==380 and stayed_time==0: 
        mc.postToChat("welcome home")
        ser.write("y".encode())
        print("y send")
        stayed_time+=1
    elif pos.x==-29 and pos.y==6 and pos.z==380:
         ser.write("g".encode())
         print("g send")
         time.sleep(1)
         stayed_time=0
     
    

    
    
