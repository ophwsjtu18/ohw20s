import socket

s = socket.socket()
s.connect(('localhost', 4711))
s.send('player.getPos()\n'.encode('ascii'))
temp = s.recv(1024)
temps = str(temp)
pos1 = temps.split('\'')
pos2 = pos1[1].split('\\n')
pos = pos2[0].split(',')
x, y, z = float(pos[0]), float(pos[1]), float(pos[2])
for i in range(3):
  for j in range(3):
    tmp = 'world.setBlock('
    tmp += str(x - 1 + i)
    tmp += ','
    tmp += str(y - 1)
    tmp += ','
    tmp += str(z - 1 + j)
    tmp += ',41)\n'
    s.send(tmp.encode('ascii'))
s.close()
