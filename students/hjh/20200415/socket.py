import socket

s = socket.socket()

s.connect(('localhost', 4711))

position = s.recv(1024)

pos = str(posiiton)

cordination = pos.split('\'')

cord2 = cordination[1].split('\\n')

cord  = cord2[0].split(',')

x=float(cord[0])

y= float(cord[1])

z= float(cord[2])

for ii in range(3):

  for jj in range(3):

    tout = 'world.setBlock('

    tout += str(x - 1 + i)

    tout += ','

    tout += str(y - 2)

    tout += ','

    tout += str(z - 1 + j)

    tout += ',41)\n'

    s.send(tout.encode('ascii'))
