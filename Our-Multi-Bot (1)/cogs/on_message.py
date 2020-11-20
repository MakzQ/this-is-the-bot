import discord
from discord.ext import commands
import asyncio

class OnMessage(commands.Cog, name = "On_Message"):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
      if self.bot.user == message.author:
        return

      if any((word in message.content.lower() for word in ('hmm', 'hm', 'hmmm', ':thinking:', 'think', 'thonk'))):
        return await message.add_reaction("🤔")

      if any((word in message.content.lower() for word in ('<3', 'love', 'heart', ':heart:'))):
        return await message.add_reaction("💖")


      if any((word in message.content.lower() for word in ('uwu', 'owo'))):
        return await message.add_reaction("🚫")


      if any((word in message.content.lower() for word in ('noice', 'nice'))):
        return await message.add_reaction("👍")

      if any((word in message.content.lower() for word in ('heyo', 'hello', 'hi', 'hey'))):
        await message.channel.send(f'Hello, {message.author.mention}')
        await message.add_reaction("👋")
        return



def setup(bot):
  bot.add_cog(OnMessage(bot))
