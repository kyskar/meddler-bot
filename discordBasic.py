import discord
from discord.ext import commands
import random
from PyDictionary import PyDictionary
dictionary=PyDictionary()
import secrets

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

bot = commands.Bot(command_prefix='!')
mainChannel = 846764231332593664
testChannel = 851891160673812531
meddleChannel = testChannel

emojis = {"yellow":'🟨',"orange":'🟧',"red":'🟥',"purple":'🟪',"blue":'🟦',"green":'🟩'}

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='meddleHere', help='Call this in a channel to move meddling there')
async def meddleThis(ctx):
    global meddleChannel
    if ctx.channel.id == meddleChannel:
        await ctx.channel.send("This channel is already meddled")
    else:
        meddleChannel = ctx.channel.id
        await ctx.channel.send("Meddling is moved to this channel")

@bot.event
async def on_raw_reaction_add(payload):
    global emojis
    # print(payload.emoji.name)  # '🟨'
    # print(payload.member)

    if payload.message_id == 855173126208225281:
        guild = bot.get_guild(payload.guild_id)
        for role in emojis:
            if payload.emoji.name == emojis[role]:
                addRole = discord.utils.get(guild.roles, name=role)
                await payload.member.add_roles(addRole)

@bot.event
async def on_message(message):
    print('Message from {0.author}: {0.content}'.format(message))
    await bot.process_commands(message)
    global meddleChannel
    global emojis

    if message.author == bot.user:
        return

    # roleColors = {"yellow": "855167028272955474","orange":"855167419453800529","red":"855167462341214208","purple":"855167508067254342","blue":"855167567945400380","green":"855167595208507454"}
    # print(message.author.roles[1].name)

    if (message.channel.id == meddleChannel) and (message.content[0] != '!' or '@'):    
        currentMessage = '{0.content}'.format(message)
        currentSender = '{0.author}'.format(message)
        userEmoji = ""
        await message.delete()

        for role in emojis:
            if role == (message.author.roles[1].name):
                userEmoji = emojis[role]

        splitUsername = currentSender.split('#')
        username = splitUsername[0]

        sentenceLength = len(currentMessage.split())
        choosingNum = random.randint(0,sentenceLength-1)
        sentenceSplit = (currentMessage.split())
        chosenWord = sentenceSplit[choosingNum]
        # print(chosenWord)
        thesaurus =  (dictionary.synonym(chosenWord))
        # print(thesaurus)
        if (thesaurus != None):
            thesLength = len(thesaurus)
            choosingThesNum = random.randint(0,thesLength-1)
            chosenThesWord = thesaurus[choosingThesNum]

            sentenceSplit.remove(chosenWord)
            sentenceSplit.insert(choosingNum,chosenThesWord)
            sentenceReword = ' '.join(sentenceSplit)
            await message.channel.send(userEmoji + " " + username + ': ' + sentenceReword)
        else:
            await message.channel.send(userEmoji + " " + username + ': ' + message.content)

        
        return

@bot.command()
async def reactmsg(ctx, msgID: int): 
    global emojis

    msg = await ctx.fetch_message(msgID)
    print(msg)

    for emoji in emojis:
        await msg.add_reaction(emoji)

@bot.command()
async def editmsg(ctx):
    channel = bot.get_channel(850527152952705045)
    message = await channel.fetch_message(855171596493783050)
    await message.edit(content="Welcome to this bot testing server! I am a bot who meddles with conversation, inspired by the game Telephone.")

@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

bot.run(secrets.bot_token)


#     on_message - instead of checking for other botcommands, 
#     disable each botcommand from working in the meddled channel  +
#     !meddleHere say 'already meddled if sent in meddled channel




# @bot.command(name='hello', help='Responds to caller')
# async def sayHello(ctx):
#     await ctx.channel.send('Hi there!')

# @bot.event
# async def on_message(message):
#     await bot.process_commands(message)
#     global meddleChannel

#     if message.author == bot.user:
#         return
    
#     await meddleChannel.send(message.content)
                                                                            


# description = '''A prototype bot that will purposefully hinder conversation'''
# intents = discord.Intents(messages=True, guilds=True)
# # intents.members = True
# bot = commands.Bot(command_prefix='!', description=description, intents=intents)

# @client.event
# async def on_ready():
#     test_channel = client.get_channel(851891160673812531)
#     print('logged on')
#     await test_channel.send('hello world')


# @bot.listen('on_message')
# async def on_message_test(message):
#     # print('Logged on as {0}!'.format(self.user))
#     print('Message from {0.author}: {0.content}'.format(message))
#     print('success')
#     if message.author == client.user:
#         return

#     await bot.process_commands(message)


