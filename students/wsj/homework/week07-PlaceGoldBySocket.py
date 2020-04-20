import socket

s = socket.socket()

s.connect(('localhost', 4711))

s.send('player.getPos()\n'.encode('ascii'))
pos0 = s.recv(1024)
pos = str(pos0)
cord0 = pos.split('\'')
cord1 = cord0[1].split('\\n')
cord  = cord1[0].split(',')
x, y, z = float(cord[0]), float(cord[1]), float(cord[2])
for i in range(3):
  for j in range(3):
    tmp = 'world.setBlock('
    tmp += str(x - 1 + i)
    tmp += ','
    tmp += str(y - 2)
    tmp += ','
    tmp += str(z - 1 + j)
    tmp += ',41)\n'
    print(tmp)
    s.send(tmp.encode('ascii'))
s.close()
