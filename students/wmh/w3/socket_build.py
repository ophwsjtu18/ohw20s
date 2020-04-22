import socket

s=socket.socket()
s.connect(("127.0.0.1",4711))
msg="player.getTile()\n"
s.send(msg.encode("ascii"))
pos=s.recv(1024)
pos1=str(pos)
s0=pos1.split('\'')
s1=s0[1].split('\\n')
s2=s1[0].split(',')
x=float(s2[0])
y=float(s2[1])
z=float(s2[2])
for i in range(3):
    for j in range(3):
        msg="world.setBlock("+str(x+i-1)+","+str(y)+","+str(z+j-1)+",41)\n"
        s.send(msg.encode("ascii"))
s.close()

