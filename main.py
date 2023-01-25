import discord
from discord.ext import commands
import sys, traceback, pkgutil


def add_plugin(path : str, prefix : str) -> list[str]:
    return [m.name for m in pkgutil.iter_modules([path], prefix=prefix)]



class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())
        
        self.initial_extensions = []
        self.initial_extensions.extend(add_plugin("src/translator", "src.translator."))
    
    
    async def load_extentions(self):
        for extension in self.initial_extensions:
            try:
               await self.load_extension(extension)
            except Exception as e:
                print(f"Failed to load extension {extension}.", file=sys.stderr)
                traceback.print_exc()
    
    async def setup_hook(self) -> None:
        await self.load_extentions()
        
        
    async def on_ready(self):
        print(self.initial_extensions)
        print("Bot is ready")
        
        

        
        
bot = Bot()



bot.run("OTY3MzQxNTc3MzM5MDMxNTU0.YmO5DA.xhkkk1sFct8H2PNbm1crbVhWCL8")