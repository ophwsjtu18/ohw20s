import socket
address = ('127.0.0.1', 4711)  # 服务端地址和端口
s = socket.socket()
s.connect(address) 
s.send('player.getTile()\n'.encode('ascii'))
pos =  str(s.recv(1024))
pos2 = pos.strip('b\'\\n')
pos3 = pos2.split(',')
print(pos3)
for i in range(3):
   for j in range(3):
        trigger = 'world.setBlock({},{},{},89)\n'.format(int(pos3[0])-1+i,int(pos3[1])-2,int(pos3[2])-1+j)
        print(trigger)
        s.sendall(trigger.encode('ascii')) 
                  

s.close()