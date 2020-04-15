from mcpi.minecraft import Minecraft
import time
import mcpi.block as block
mc=Minecraft.create()
pos=mc.player.getTilePos()
print("player pos is",pos)

stayed_time=0
house(pos.x,pos.y,pos.z,10,10,10)
def house(x0,y0,z0,L,W,H):

        for x in range(L):
                for z in range(W):
                      mc.setBlock(x0+x,y0,z0+z,block.WOOD.id)

        for x in range(L):
                for z in range(W):
                      mc.setBlock(x0+x,y0+H-1,z0+z,block.WOOD.id)


        for y in range(H):
                for x in range(L):

                      mc.setBlock(x0+x,y0,z0,block.WOOD.id)
                      mc.setBlock(x0+x,y0,z0+W-1,block.WOOD.id)
                for x in range(W-2):
                      mc.setBlock(x0,y0,z0+1+x,block.WOOD.id)
                      mc.setBlock(x0+L-1,y0,z0+1+x,block.WOOD.id)

        for z in range(2):

                for y in range(2): 

                      mc.setBlock(x0+L, y0+y+2, z0+z+4, 20)

        
       mc.setBlock(x0+L/2, y0+1, z0，0)

        mc.setBlock(x0+L/2, y0+2, z0，0)

        mc.setBlock(x0+L/2, y0+3, z0，0)


