from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

for i in range(10):
   pos=mc.player.getTilePos()
   mc.setBlock(pos.x,--pos.y,pos.z,3)
   mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
   time.sleep(2)
 
   
    
