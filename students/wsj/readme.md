# Folder of Sj. W.

This is an apple. I like apples. Apples are good for our health. \
生活就像海洋, 只有意志坚强的人才能到达彼岸.

All the homework can be found in the folder `./homework`, and they are supposed to be arranged by dates (or more precisely, week).

Here is an imcomplete table of APIs in the Raspberry Juice below. Its origin is [here][1] and [there][2].

## APIs of Raspberry Juice

### .create()

```
mc = minecraft.Minecraft.create()
```

### .setBlock(x, y, z, id, [data])

```
mc.setblock(0, 0, 0, block.WOOD.id, 1)
```
Note that the last parameter can be left blank.

### .getPos()

Gets the player's position in the world as a Vec3 of floats (decimal numbers), if the player is in the middle of a block x.5 is returned.
```
playerPos = mc.player.getPos()
```

### .getTilePos()

Gets the position of the 'tile' the player is currently on.
```
playerTile = mc.player.getTilePos()
```

### .setPos(x, y, z) & .setTilePos(x, y, z)

```
mc.player.setPos(0.0, 0.0, 0.0)
mc.player.setTilePos(0, 0, 0)
```

### .getRotation()

Gets the rotational angle (0 to 360) for the player, and returns a float type.
```
angle = mc.player.getRotation()
print(angle)
```

### .getPitch()

Gets the pitch angle (-90 to 90) for the player, and returns a float type.
```
pitch = mc.player.getPitch()
print(pitch)
```

### .getDirection()

Gets unit vector of x, y, z for the player's direction, and returns a Vec3 type.
```
direction = mc.player.getDirection()
print(direction)
print(direction.x, ' ', direction.y, ' ', direction.z)
```

### .postToChat(message)

```
mc.postToChat("MCPI and Raspberry Juice are working fine.")
```

## Example Code

Note that the code may be invalid because it replaces all indents with 2 spaces. 
```
import mcpi.minecraft as minecraft
import mcpi.block as block
from math import *

colors = [14, 1, 4, 5, 3, 11, 10]

mc = minecraft.Minecraft.create()
height = 60

mc.setBlocks(-64, 0, 0, 64, height + len(colors), 0, 0)
for x in range(0, 128):
  for colourindex in range(0, len(colors)):
    y = sin((x / 128.0) * pi) * height + colourindex
    mc.setBlock(x - 64, y, 0, block.WOOL.id,
                colors[len(colors) - 1 - colourindex])
```

## Part of Reference Table of '.id' and '.data'

|Block               | .id           |Block               | .id       |
|--------------------|---------------|--------------------|-----------|
|AIR                 | Block(0)      |STONE_SLAB          | Block(44) |
|STONE               | Block(1)      |BRICK_BLOCK         | Block(45) |
|GRASS               | Block(2)      |TNT                 | Block(46) |
|DIRT                | Block(3)      |BOOKSHELF           | Block(47) |
|COBBLESTONE         | Block(4)      |MOSS_STONE          | Block(48) |
|WOOD_PLANKS         | Block(5)      |OBSIDIAN            | Block(49) |
|SAPLING             | Block(6)      |TORCH               | Block(50) |
|BEDROCK             | Block(7)      |FIRE                | Block(51) |
|WATER_FLOWING       | Block(8)      |STAIRS_WOOD         | Block(53) |
|WATER               | WATER_FLOWING |CHEST               | Block(54) |
|WATER_STATIONARY    | Block(9)      |DIAMOND_ORE         | Block(56) |
|LAVA_FLOWING        | Block(10)     |DIAMOND_BLOCK       | Block(57) |
|LAVA                | LAVA_FLOWING  |CRAFTING_TABLE      | Block(58) |
|LAVA_STATIONARY     | Block(11)     |FARMLAND            | Block(60) |
|SAND                | Block(12)     |FURNACE_INACTIVE    | Block(61) |
|GRAVEL              | Block(13)     |FURNACE_ACTIVE      | Block(62) |
|GOLD_ORE            | Block(14)     |DOOR_WOOD           | Block(64) |
|IRON_ORE            | Block(15)     |LADDER              | Block(65) |
|COAL_ORE            | Block(16)     |STAIRS_COBBLESTONE  | Block(67) |
|WOOD                | Block(17)     |DOOR_IRON           | Block(71) |
|LEAVES              | Block(18)     |REDSTONE_ORE        | Block(73) |
|GLASS               | Block(20)     |SNOW                | Block(78) |
|LAPIS_LAZULI_ORE    | Block(21)     |ICE                 | Block(79) |
|LAPIS_LAZULI_BLOCK  | Block(22)     |SNOW_BLOCK          | Block(80) |
|SANDSTONE           | Block(24)     |CACTUS              | Block(81) |
|BED                 | Block(26)     |CLAY                | Block(82) |
|COBWEB              | Block(30)     |SUGAR_CANE          | Block(83) |
|GRASS_TALL          | Block(31)     |FENCE               | Block(85) |
|WOOL                | Block(35)     |GLOWSTONE_BLOCK     | Block(89) |
|FLOWER_YELLOW       | Block(37)     |BEDROCK_INVISIBLE   | Block(95) |
|FLOWER_CYAN         | Block(38)     |STONE_BRICK         | Block(98) |
|MUSHROOM_BROWN      | Block(39)     |GLASS_PANE          | Block(102)|
|MUSHROOM_RED        | Block(40)     |MELON               | Block(103)|
|GOLD_BLOCK          | Block(41)     |FENCE_GATE          | Block(107)|
|IRON_BLOCK          | Block(42)     |GLOWING_OBSIDIAN    | Block(246)|
|STONE_SLAB_DOUBLE   | Block(43)     |NETHER_REACTOR_CORE | Block(247)|


|Value|Color of WOOL |Value|Color of WOOL |
|-----|--------------|-----|--------------|
|0    | White        |8    | Light grey   |
|1    | Orange       |9    | Cyan         |
|2    | Magenta      |10   | Purple       |
|3    | Light Blue   |11   | Blue         |
|4    | Yellow       |12   | Brown        |
|5    | Lime         |13   | Green        |
|6    | Pink         |14   | Red          |
|7    | Grey         |15   | Black        |

[1]: https://www.stuffaboutcode.com/p/minecraft-api-reference.html
[2]: https://github.com/zhuowei/RaspberryJuice
