import random
import discord

from discord.ext import commands


client = discord.Client()
bot = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    responses = ['Welcome!', 'Hi there!']

    if message.content == 'Hello':
        response = random.choice(responses)
        await message.channel.send(response)


@client.event
async def on_birthday_message(message, member):
    if message.author == client.user:
        return
    if 'happy birthday' in message.content.lower():
        await message.channel.send(f'Happy Birthday! {member.name}')


@bot.command(name='Start')
async def nine_nine(ctx):
    response = 'Hi there! I am a Robot'
    await ctx.send(response)


client.run('API Token')
bot.run('API Token')
