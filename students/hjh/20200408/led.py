[led]

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
    
    else:
        
        print ("No Arduino Device was found connected to the computer")

#ser=serial.Serial(port='COM4')

#ser=serial.Serial(port='/dev/ttymodem542')

#wait 2 seconds for arduino board restart

time.sleep(2)

mc=Minecraft.create()

stayed_time=0

while True:
    
    print("stay_time"+str(stayed_time))
    
    time.sleep(0.5)
    
    pos=mc.player.getTilePos()
    
    mc.postToChat("please goto home x=-30 y=-6 z=-40 for 15s to fly")
   
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    
    for x in range(3):
        
        for z in range(3):
            
            if mc.getBlock(pos.x-1+x,pos.y,pos.z-1+z)==124:
                
                print("red stone ligh found")
                
                ser.write("y".encode()) 
     if pos.x==-100 and pos.y==2 and pos.z==-52:
        
        mc.postToChat("welcome home")
        
        stayed_time=stayed_time+1
        
        ser.write("y".encode())
        
        print("y send")
        
        time.sleep(1)
        
        if stayed_time>=30:
            
            mc.player.setTilePos(-30,10,-40)
            
            stayed_time=0
            
            ser.write("g".encode())
            
            print("g send")
            
            time.sleep(1)
    
    else:
        
        stayed_time=0
