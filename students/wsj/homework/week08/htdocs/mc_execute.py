#!/some-path/python.exe
#coding=utf-8

import cgi, cgitb
import mcpi.minecraft as minecraft

mc  = minecraft.Minecraft.create()
pos = mc.player.getPos()
dir = mc.player.getDirection()

form = cgi.FieldStorage()

mc_cmd = form.getvalue('mc_cmd')
mc_prm = form.getvalue('mc_prm')

# mc_cmd = 'move'
# mc_prm = 's'

str_cmd = str(mc_cmd)
str_prm = str(mc_prm)

def makeHouse(centerX, centerZ, rX, rZ, level, height, doorParam = 0, roofParam = 0):
    mc.setBlocks(centerX - rX, level, centerZ - rZ, centerX + rX, level + height, centerZ + rZ, 5)
    mc.setBlocks(centerX - rX + 1, level + 1, centerZ - rZ + 1, centerX + rX - 1, level + height, centerZ + rZ - 1, 0)
    mc.setBlock(centerX - rX, level + 1, centerZ, 0)
    mc.setBlock(centerX - rX, level + 2, centerZ, 0)
    for i in range(rX):
        mc.setBlocks(centerX - rX, pos.y + height + i, centerZ - rZ + i, centerX + rX, pos.y + height + i, centerZ + rZ - i, 5)
        mc.setBlocks(centerX - rX + 1, pos.y + height + i, centerZ - rZ + 1 + i, centerX + rX - 1, pos.y + height + i, centerZ + rZ - 1 - i, 0)
    i += 1
    mc.setBlocks(centerX - rX, pos.y + height + i, centerZ - rZ + i, centerX + rX, pos.y + height + i, centerZ + rZ - i, 5)
    mc.setBlock(centerX - rX, level + 1, centerZ, 0)
    mc.setBlock(centerX - rX, level + 2, centerZ, 0)
    mc.setBlock(centerX - rX - 1, level, centerZ, 53)
    mc.setBlocks(centerX - rX + 1, level + 2, centerZ - rZ, centerX + rX - 1, level + height, centerZ - rZ, 20)


if str_cmd == 'move':
  prmList = str_prm.split(' ')
  if len(prmList) == 1:
    dis = 1
  else:
    dis = float(prmList[1])
  if   prmList[0] == 'w':
    mc.player.setPos(pos.x - dis, pos.y, pos.z)
  elif prmList[0] == 'e':
    mc.player.setPos(pos.x + dis, pos.y, pos.z)
  elif prmList[0] == 's':
    mc.player.setPos(pos.x, pos.y, pos.z + dis)
  elif prmList[0] == 'n':
    mc.player.setPos(pos.x, pos.y, pos.z - dis)
  elif prmList[0] == 'u':
    mc.player.setPos(pos.x, pos.y + dis, pos.z)
  elif prmList[0] == 'd':
    mc.player.setPos(pos.x, pos.y - dis, pos.z)
if str_cmd == 'house':
  pos   += dir   * 10.0
  pos.y -= dir.y * 10.0
  makeHouse(pos.x, pos.z, 5 ,5, pos.y, 5)
