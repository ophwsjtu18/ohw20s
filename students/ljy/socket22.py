import socket


s=socket.socket()

s.connect(("127.0.0.1",4711))

print("connected")

msg="player.getTile()\n"
s.send(msg.encode())
msg=s.recvfrom(1024) 
p=msg[0].decode()
x=int(p[0]+p[1]+p[2])
y=int(p[4]+p[5]+p[6])
z=int(p[8]+p[9]+p[10])
print(x,y,z)
 
msg="world.setBlocks(%d,%d,%d,%d,%d,%d,41,0)"%(x,y,z,x+2,y,z+2)
s.send(msg.encode())
s.close()
 
