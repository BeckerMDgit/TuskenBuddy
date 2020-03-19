import discord
from discord.ext import commands
import os
import random

class Sounds(commands.Cog): # cog to hold sound functions

    def __init__(self,bot):
        self.bot = bot
        self._last_member = None
    
    @staticmethod
    async def sound_list(folder): # returns a list of mp3 files from the given file        
        sound_list = sorted([i[:4].lower() for i in os.listdir(folder) if '.mp4' in i])
        if not sound_list:
            raise Exception("No sound files in given folder")
        return sound_list

    @staticmethod
    def randomSound(self):
        thisSound = random.choice(Sounds.sound_list)
        print(thisSound)

    @commands.Cog.listener()
    async def on_ready(self):
        print("sounds cog check")
        thisSound = random.choice(Sounds.sound_list)
        print(thisSound)


"""
    @commands.command()
    async def sup(self, ctx):
      
"""  

def setup(bot):
    bot.add_cog(Sounds(bot))

