from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()

pos=mc.player.getTilePos()
print("player pos is",pos)
stayed_time=0
while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please go to home x=-30 y=16 z=-40 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    if pos.x==-30 and pos.z==-40 and pos.y==16:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        for i in range(10):
            mc.setBlock(-35+i,15,-40,1)
        if stayed_time>=30:
            mc.player.setTilePos(-32,9,-45)
            stayed_time=0
    else:
        stayed_time=0

