#import the minecraft library
import mcpi.minecraft as minecraft

#create a connection to minecraft
mc = minecraft.Minecraft.create()

#create a variable for Steve's location
pos = mc.player.getPos()

#change Steve's location to 50 blocks above where he is currently standing
mc.player.setPos(pos.x, pos.y+50, pos.z)

#post a message on the screen
mc.postToChat("Don't Look Down!")
