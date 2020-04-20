from mcpi.minecraft import Minecraft
import socket

mc=Minecraft.create()
print("connected")
pos=mc.player.getTilePos()
for i in range(3):
    for j in range(3):
        s=socket.socket()
        s.connect(("127.0.0.1",4711))
        msg="world.setBlock("+str(pos.x+i-1)+","+str(pos.y)+","+str(pos.z+j-1)+",41)"
        s.send(msg.encode("ascii"))
        s.close()
