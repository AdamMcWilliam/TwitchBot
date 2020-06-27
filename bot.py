# bot.py
import os # for importing env vars for the bot to use
from twitchio.ext import commands
from grovelAttempt import *
from getBotStreetCred import *
from getBotCoolPoints import *
from AppendCubeTime import *
from stealFromBot import *
from AverageCubeTime import *
from DailyAverageCubeTime import *
from inflate import *
from switchSides import *
import datetime

bot = commands.Bot(
    #all this is loaded from the .env file that you need to create
    # set up the bot
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

# bot.py, below bot object
@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} is online!")
   #ws = bot._ws  # this is only needed to send messages within event_ready
   #await ws.send_privmsg(os.environ['CHANNEL'], f"/me has Entered the chat!")


# bot.py, below event_ready
@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat.'
    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        return

    #bot.py, in event_message, below the bot ignore stuffs
    await bot.handle_commands(ctx)



# bot.py, below event_message function
# @bot.command(name='test')
# async def test(ctx):
#     await ctx.send('test passed!')


@bot.command(name='!manifestozanussbot')
async def manifestozanussbot(ctx):
    await ctx.send('This bot Logs Begins cube times in a google spreadsheet with !cubed 0:00:00 when entered by beginbotbot. The average cube time can be fetched with !!act. The average of begins attempts of the day can be fetched with !!dact.')

@bot.command(name='!botcss')
async def botcss(ctx):
    if(ctx.author.name.lower() !='zanuss'):
        return
    await ctx.send('!css https://gist.githubusercontent.com/AdamMcWilliam/5619ec9f7fa83bef75e718e6d7daec22/raw/0376fc54fdfe47a5c71a2b8ea6911d8abb1d58f3/beginZanussBot.css')


@bot.command(name='!propsme')
async def propsme(ctx):
    await ctx.send(f'!props {ctx.author.name.lower()}')    


@bot.command(name='!csstemplate')
async def csstemplate(ctx):
    await ctx.send('Here is a css template to help you get started on https://mygeoangelfirespace.city/: https://codepen.io/Zanuss/pen/dyGoamX')    


@bot.command(name='!donateme')
async def donateme(ctx):
    await ctx.send(f'!donate {ctx.author.name.lower()}')    


@bot.command(name='!propsall')
async def propsall(ctx):
    
    totalProps = getBotStreet()
    #print(f'!props zanuss {totalProps}')
    await ctx.send(f'!props {ctx.author.name.lower()} {totalProps}')   


@bot.command(name='!buyall')
async def buyall(ctx):
    if(ctx.author.name.lower() !='zanuss'):
        return
    totalCool = getBotCool()
    #print(f'!props zanuss {totalProps}')
    await ctx.send(f'!buy random {totalCool}')   



@bot.command(name='cubed')
async def cubed(ctx):
    if(ctx.author.name.lower() !='beginbotbot'):
        return

    message = ctx.content
    timestamp = ctx.message.timestamp

    #remove command text with str split
    x = message.split('!cubed ')
    message = str(x[1])

    message = datetime.datetime.strptime(message, '%H:%M:%S')

    #strip year
    x = str(message).split()
    message = str(x[1])
    print(message)

    #remove everything but the date
    y = str(timestamp).split()
    timestamp = y[0]
    print(timestamp)

    #send to function in AppendCubeTime.py
    AppendCubeTime(str(message),str(timestamp))



@bot.command(name='steal')
async def steal(ctx):
    if(ctx.author.name.lower() !='opsecbot'):
        return
        
    stealCommand = StealFromBot(ctx.content, ctx.author.name.lower())
    print(f"!steal {stealCommand}")
    await ctx.send(f"!steal {stealCommand}")



@bot.command(name='!inflate')
async def inflate(ctx):
    if(ctx.author.name.lower() !='zanuss'):
        return

    inflateSound = inflateSoundFn(ctx.content)    
    await ctx.send(f'!steal {inflateSound} zanuss')


@bot.command(name='la_libre')
async def sideWithWin(ctx):
    majority = sideWithWinners()    
    await ctx.send(f'!{majority}')
    print(f'!{majority}')
 


@bot.command(name='!act')
async def act(ctx):
    act = AvgCubeTime()
    await ctx.send(f"Begins Overall Average: {act}")


@bot.command(name='!dact')
async def dact(ctx):
    dact = DailyAvgCubeTime(10)
    await ctx.send(f"Begins Daily Average: {dact}")


@bot.command(name='!grovel')
async def dact(ctx):
    grovelerMessage = grovelAttempt(ctx.author.name.lower())
    await ctx.send(f"{grovelerMessage}")


# bot.py
if __name__ == "__main__":
    bot.run()

