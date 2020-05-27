[house]

import mcpi.minecraft as minecraft

import mcpi.block as block

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()

for a in range(10):
    
    mc.setBlock(pos.x+a,pos.y,pos.z,1)
    
    mc.setBlock(pos.x+a,pos.y,pos.z+9,1)

for a in range(8):
    
    mc.setBlock(pos.x,pos.y,pos.z+1+a,1)
    
    mc.setBlock(pos.x+9,pos.y,pos.z+1+a,1)

for y in range(10):
   
    for a in range(10):
        
        mc.setBlock(pos.x+a,pos.y+y,pos.z,1)
        
        mc.setBlock(pos.x+a,pos.y+y,pos.z+9,1)
    
    for a in range(8):
        
        mc.setBlock(pos.x,pos.y+y,pos.z+1+a,1)
        
        mc.setBlock(pos.x+9,pos.y+y,pos.z+1+a,1)
    
for x in range(10):
    
    for z in range(10):
        
        mc.setBlock(pos.x+x,pos.y,pos.z+z,1)
        
        mc.setBlock(pos.x+x,pos.y+9,pos.z+z,1)

mc.setBlock(pos.x+5,pos.y+1,pos.z,0)

mc.setBlock(pos.x+5,pos.y+2,pos.z,0)

for z in range(2):
    
    for y in range(2):
        
        mc.setBlock(pos.x+10,pos.y+y+2,pos.z+z+4,20)

def house(x,y,z,l,w,h):
    
    mc.setBlocks(x + 1, y, z, x+l, y, z+w, block.WOOD.id )
    
    mc.setBlocks(x + 1, y+h, z, x+l, y+h, z+w, block.WOOD.id )
    
    mc.setBlocks(x + 1, y, z, x +1, y + h, z +w, block.WOOD.id )
    
    mc.setBlocks(x + l, y, z, x +l, y + h, z +w, block.WOOD.id )
    
    mc.setBlocks(x + l, y+2, z+4, x +l, y + h-2, z +w-4, block.GLASS.id )
    
    mc.setBlocks(x + 1, y, z, x +l, y + h, z, block.WOOD.id )
    
    mc.setBlocks(x + 1, y, z, x +l, y + h, z, block.WOOD.id )    
    
    return 

from mcpi.minecraft import Minecraft

mc=Minecraft.create()

pos=mc.player.getTilePos()

from mcpi import block

x = pos.x

y = pos.y

z = pos.z

l=30

w=16

h=8

house(x,y,z,l,w,h)
