import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
pos.y += 1
direction = mc.player.getDirection()
pos   += direction   * 10
pos.y -= direction.y * 10

def makeHouse(centerX, centerZ, rX, rZ, level, height, doorParam = 0, roofParam = 0):
    level -= 1
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

makeHouse(pos.x, pos.z, 5 ,5, pos.y, 5)
