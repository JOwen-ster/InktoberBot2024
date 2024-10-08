import asyncio
from utils.embeds import BotMessageEmbed
import cogs
from discord.ext import commands
import __main__


RAW_PROMPTS = [
    "Backpack", "Discover", "Boots", "Exotic", "Binoculars", "Trek", 
    "Passport", "Hike", "Sun", "Nomadic", "Snacks", "Remote", 
    "Horizon", "Roam", "Guidebook", "Grungy", "Journal", "Drive", 
    "Ridge", "Uncharted", "Rhinoceros", "Camp", "Rust", "Expedition", 
    "Scarecrow", "Camera", "Road", "Jumbo", "Navigator", "Violin", "Landmark"
]

INDEXED_PROMPTS = enumerate(RAW_PROMPTS, start=1)

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    async def setup_hook(self) -> None:
        print('Running bot setup_hook...')
        for i, cog in enumerate(cogs.names, 1):
            try:
                await self.load_extension('cogs.' + cog)
                print(F'Loaded {cog} cog ({i}/{len(cogs.names)})')
            except:
                print(F'Could not load cog.{cog} ({i}/{len(cogs.names)})')
        print('Ran bot setup_hook.')
        self.loop.create_task(self.my_background_task()) # add background task

    async def on_ready(self) -> None:
        tree = await self.tree.sync()
        print(F'Synced {len(tree)} tree commands')

    async def my_background_task(self):
        await self.wait_until_ready()
        __main__.logger.info('BACKGROUND TASK STARTED')
        if guild := self.get_guild(1156821909074358423): # guild ID goes here
            __main__.logger.info('GUILD FOUND')
        if channel := guild.get_channel(1219197242011811890): # channel ID goes here
            __main__.logger.info('CHANNEL FOUND')

        while not self.is_closed():
            emb = BotMessageEmbed(description=f'{INDEXED_PROMPTS.__next__()}')
            await channel.send(embed=emb)
            __main__.logger.info('EXECUTED BACKGROUND JOB')
            await asyncio.sleep(86400)  # task runs every X seconds