import discord
from discord.ext import commands

TOKEN = "OTQyMDU2MzU0MjI5NjgyMjQ2.Yge8WQ.H1M3l4JxVgOtjn0smfKeTBb4rYY"
bot = discord.Client()

wait_list = []
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="?", intents=intents)


@bot.command(name='qlist')
async def qlist(ctx):
    queue_list = str(ctx.author).split("#")[0]
    await ctx.send(queue_lis

@bot.command(name='queue')
async def queue(ctx):
    await ctx.send(f"Added {ctx.author} to the queue!")
    wait_list.append({ctx.author})


@bot.event
async def on_ready():
    print("we have logged in as {0.user}".format(bot))


bot.run(TOKEN)
