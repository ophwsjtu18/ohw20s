from mcpi.minecraft import Minecraft
from mcpi import block

mc=Minecraft.create()

pos=mc.player.getTilePos()
print("player pos is",pos)

def house(x0,y0,z0,L,W,H):
    
    for y in range(H):
        for a in range(L):
            mc.setBlock(x0+a, y0+y, z0, block.STONE.id)
            mc.setBlock(x0+a, y0+y, z0+W-1, block.STONE.id)
        for a in range(W-2):
            mc.setBlock(x0, y0+y, z0+1+a, block.STONE.id)
            mc.setBlock(x0+L-1,y0+y, z0+1+a, block.STONE.id)

    for x in range(L):
        for z  in range(W):
            mc.setBlock(x0+x, y0, z0+z, block.STONE.id)

    for x in range(L):
        for z  in range(W):
            mc.setBlock(x0+x, y0+H-1, z0+z,block.STONE.id )
       
    mc.setBlock(x0+L/2, y0+1, z0,0)
    mc.setBlock(x0+L/2, y0+2, z0, 0)

    for z in range(2):
      for y in range(2):
            mc.setBlock(x0+L-1, y0+y+2, z0+z+4,20 )

house(pos.x,pos.y,pos.z,10,10,10)
