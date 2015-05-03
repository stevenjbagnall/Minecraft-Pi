#import the minecraft libraries
import mcpi.minecraft as minecraft
import mcpi.block as block

#create a connection to minecraft
mc = minecraft.Minecraft.create()

#create a loop
while True:
  #create a variable to identify the position of the block Steve is standing on
  pos = mc.player.getTilePos()
  #place a diamond block under Steve's feet
  mc.setBlock(pos.x, pos.y-1, pos.z, block.DIAMOND_BLOCK)
