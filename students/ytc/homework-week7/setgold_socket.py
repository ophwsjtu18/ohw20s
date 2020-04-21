from mcpi.minecraft import Minecraft
import socket


mc=Minecraft.create()

pos=mc.player.getTilePos()
for i in range(3):
    for j in range(3):
        s=socket.socket()
        s.connect(("127.0.0.1",25566))
        msg="world.setBlock("+str(pos.x+i-1)+","+str(pos.y-1)+","+str(pos.z+j-1)+",41)"
        s.send(msg.encode("ascii"))
        s.close()
