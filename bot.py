import asyncio
from utils.embeds import BotMessageEmbed
import cogs
from discord.ext import commands
import __main__


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

    async def on_ready(self) -> None:
        tree = await self.tree.sync()
        print(F'Synced {len(tree)} tree commands')
        self.loop.create_task(self.my_background_task())

    async def my_background_task(self):
        __main__.logger.info('BACKGROUND TASK STARTED')
        if guild := self.get_guild(1156821909074358423): # guild ID goes here
            __main__.logger.info('GUILD FOUND')
        if channel := guild.get_channel(1219197242011811890): # channel ID goes here
            __main__.logger.info('CHANNEL FOUND')
        emb = BotMessageEmbed(description='Hello')
        while not self.is_closed():
            await channel.send(embed=emb)
            __main__.logger.info('EXECUTED BACKGROUND JOB')
            await asyncio.sleep(30)  # task runs every X seconds