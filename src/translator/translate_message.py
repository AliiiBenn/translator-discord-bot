import discord
from discord.ext import commands

from googletrans import Translator
from enum import Enum, auto


class MessageTranslator(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot
        self.translator = Translator()
        
    
    @commands.hybrid_command(name="translate")
    async def translate_message(self, ctx : commands.Context, language : str, *, message : str) -> discord.Message:
        translated_message = self.translator.translate(message, dest=language)
        
        return await ctx.send(translated_message.text)
    
    
async def setup(bot : commands.Bot) -> None:
    await bot.add_cog(MessageTranslator(bot))