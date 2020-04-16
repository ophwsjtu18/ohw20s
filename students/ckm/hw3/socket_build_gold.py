import socket
from mcpi.minecraft import Minecraft
s=socket.socket();
s.connect(("127.0.0.1",4711))
mc=Minecraft.create()

pos=mc.player.getTilePos()
for i in range(0,3):
    for j in range(0,3):
        s=socket.socket();
        s.connect(("127.0.0.1",4711))
        msg="world.setBlock("+str(pos.x+i)+","+str(pos.y-2)+","+str(pos.z+j)+",41)"
        s.sendall(msg.encode("ascii"));
        s.close()

