#import the minecraft libraries
import mcpi.minecraft as minecraft
import mcpi.block as block
import random

#create a connection to minecraft
mc = minecraft.Minecraft.create()

number = random.randint(0,15)

#create a loop
while True:
  #create a variable to identify the position of the block Steve standing on
  pos = mc.player.getTilePos()
  #place a random coloured wool block under Steve's feet
  mc.setBlock(pos.x, pos.y-1, pos.z, block.WOOL.id, number)
  #change variable 'number' by 1 so the block changes each time through the loop
  number = number + 1
