import discord
from discord.ext import commands

from googletrans import Translator


class TranslateOnMessage(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot
        self.translator = Translator()
        self.lang = "en"
        
    @commands.Cog.listener("on_message")
    async def translate_message(self, message : discord.Message) -> None:
        if message.author.bot:
            return
        
        translated_message = self.translator.translate(message.content, dest=self.lang)
        
        await message.delete()
        await message.channel.send(f"{message.author.name} - *{translated_message.text}*")
        
        
async def setup(bot : commands.Bot) -> None:
    await bot.add_cog(TranslateOnMessage(bot))