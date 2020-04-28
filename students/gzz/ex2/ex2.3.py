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
ser=serial.Serial(port='COM12')
#ser=serial.Serial(port='/dev/ttymodem542')
#wait 2 seconds for arduino board restart
time.sleep(2)

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

stayed_time=0

while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home x=-30 y=-6 z=-40 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
   
def house(x0,y0,z0,l0,w0,h0):
    for i in range(h0):
        for a in range(l0):
            mc.setBlock(x0+a , y0+i , z0 ,1)
            mc.setBlock(x0+a , y0+i , z0+9, 1)
        for a in range(w0-2):
            mc.setBlock(x0 , y0+i , z0+1+a, 1)
            mc.setBlock(x0+9, y0+i, z0+1+a, 1)
    for x in range(l0):
        for z  in range(w0):
                mc.setBlock(x0+x, y0, z0+z,1)
    for x in range(l0):
        for z  in range(w0):
                mc.setBlock(x0+x, y0+h0, z0+z,1)
    mc.setBlock(x0+5, y0+1, z0,0)
    mc.setBlock(x0+5, y0+2, z0,0)
    mc.setBlock(x0+6,y0+1, z0,0)
    mc.setBlock(x0+6,y0+2, z0,0)
    for z in range(2):
          for y in range(2): 
                mc.setBlock(x0+9, y0+y+2, z0+z+4, 20)
x0=0
y0=0
z0=0
l0=10
w0=10
h0=10
house(x0,y0,z0,l0,w0,h0)

    if pos.x>=x0 and pos.x<x0+l0 and  pos.y>=y0 and pos.y<y0+h0 and pos.z>=z0 and pos.z<z0+w0:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
       
        ser.write("ABCD".encode())
        print("ABCD send")
        time.sleep(1)
        if stayed_time>=30:
            mc.player.setTilePos(-30,10,-40)
            stayed_time=0
          
            ser.write("EFGH".encode())
            print("EFGH send")
            time.sleep(1)
    else:
        stayed_time=0
        
     
