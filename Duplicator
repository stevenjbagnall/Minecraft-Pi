#import the minecraft library
import mcpi.minecraft as minecraft

#create a connection to minecraft
mc = minecraft.Minecraft.create()

#create a variable to identify the position of the block Steve is standing on
pos = mc.player.getTilePos()

#create a variable to indentify what type of block Steve is standing on
below = mc.getBlock(pos.x, pos.y-1, pos.z)

#place a block on Steve's head that is the same as the block he is standing on
mc.setBlock(pos.x, pos.y+2, pos.z, below)
