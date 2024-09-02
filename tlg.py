import discord
from discord.ext import commands

# Replace 'YOUR_BOT_TOKEN' with your bot's token
TOKEN = '1280196542665330760'

# Create an instance of the Bot
intents = discord.Intents.default()
intents.message_content = True  # Enable access to message content
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Respond to a simple message
    if message.content.lower() == 'hello':
        await message.channel.send('Hello! How can I assist you today?')

    # Process commands
    await bot.process_commands(message)

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command(name='repeat')
async def repeat(ctx, *, text: str):
    await ctx.send(text)

# Run the bot
bot.run(TOKEN)
