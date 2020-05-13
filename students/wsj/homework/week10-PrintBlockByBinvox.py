import binvox_rw
from mcpi.minecraft import Minecraft
import mcpi.block as block
import os

mc  = Minecraft.create()
pos = mc.player.getTilePos()

name = str(input('Enter the name of the stl file:'))

# Without any robustness
binvox_name = name.replace('.stl', '.binvox', 1)

if os.path.exists(binvox_name):
  os.remove(binvox_name)

os.system('.\\binvox.exe -d 50 ' + name)

with open(binvox_name, 'rb') as f:
  model = binvox_rw.read_as_3d_array(f)
print(model.dims)
print(model.scale)
print(model.translate)
# print(model.data)

for y in range(model.dims[1]):
  print("layer y = ",y)
  layer_data = model.data[y]
  # stringlayer = ""
  for x in range(model.dims[0]):
    # stringlayer = stringlayer + "\n"
    for z in range(model.dims[2]):
      if model.data[x][y][z] == True:
        # stringlayer = stringlayer + '1'
        mc.setBlock(pos.x + x, pos.y + y, pos.z + z,
					block.STONE.id)
      else:
        # stringlayer = stringlayer + '0'
        mc.setBlock(pos.x + x, pos.y + y, pos.z + z,
					block.AIR.id)
  # print(stringlayer)
