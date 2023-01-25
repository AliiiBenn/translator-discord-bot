import discord
from discord.ext import commands


from googletrans import Translator



class ExampleEmbedCog(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot
        self.translator = Translator()
        self.lang = "en"
        
        
    @commands.hybrid_command(name="setlanguage")
    async def set_language(self, ctx : commands.Context, language : str) -> discord.Message:
        self.lang = language
        return await ctx.send(f"Language set to {language}")    
    
    @commands.hybrid_command(name="example_embed")
    async def example_embed(self, ctx : commands.Context) -> discord.Message:
        EMBED_TITLE = "You have been warned!"
        EMBED_DESCRIPTION = "You have been warned for breaking the rules. Please read the rules again."
        
        embed = discord.Embed(
            title=self.translator.translate(EMBED_TITLE, dest=self.lang).text,
            description=self.translator.translate(EMBED_DESCRIPTION, dest=self.lang).text,
            color=discord.Color.red()
        )
        
        return await ctx.send(embed=embed)
    
    
async def setup(bot : commands.Bot) -> None:
    await bot.add_cog(ExampleEmbedCog(bot))