import mcpi.minecraft as minecraft
import mcpi.block as block

import serial
import time

Ser12 = serial.Serial(port = 'COM12')
HomePosition = [0, 0, 0]

mc = minecraft.Minecraft.create()

while True:
    pos = mc.player.getTilePos()
    angle = mc.player.getRotation()
    mc.postToChat("The current position is " + str(pos.x) +
                  " " + str(pos.y) + " " + str(pos.z))
    mc.postToChat("The angle is " + str(angle))
    print("The current position is ",
          pos.x, " ", pos.y, " ", pos.z)
    direction = mc.player.getDirection()
    print(direction)
    if [pos.x, pos.y, pos.z] == HomePosition:
      Ser12.write('01234567'.encode())
    else:
      Ser12.write('abcdefgh'.encode())
    time.sleep(2)
