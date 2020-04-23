import socket
s=socket.socket();
s.connect(("127.0.0.1",4711))
s.send('player.getTile()\n'.encode('ascii'))
pos= str(s.recv(1024))
pos=pos[2:-3]
pos="("+pos+")"
pos=eval(pos)

print(pos)
s.close()
for i in range(0,3):
    for j in range(0,3):
        s=socket.socket();
        s.connect(("127.0.0.1",4711))
        msg="world.setBlock("+str(pos[0]+i)+","+str(pos[1]-2)+","+str(pos[2]+j)+",41)"
        s.sendall(msg.encode("ascii"));
        s.close()
