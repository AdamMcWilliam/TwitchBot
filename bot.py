# bot.py
import os # for importing env vars for the bot to use
import asyncio
from twitchio.ext import commands
from getBotInsurancePolicy import *
from grovelAttempt import *
from getBotStreetCred import *
from getBotCoolPoints import *
from AppendCubeTime import *
from bestCubeTime import *
from stealFromBot import *
from whosSalty import *
from AverageCubeTime import *
from DailyAverageCubeTime import *
from inflate import *
from switchSides import *
from autoStu import *
import datetime
import sched, time
import binascii
import random

bot = commands.Bot(
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

    #output messages to console  
    print (ctx.author.name.lower() + ":" + ctx.content)
    
     #if 5min cat loop 
    if ctx.content == "CoolCat CoolCat CoolCat":
        await bot._ws.send_privmsg(os.environ['CHANNEL'], f"!props all")

    #stupacTroll
    if ctx.author.name.lower() == "stupac62":
        if "keeb" in ctx.content.lower() or "keyboard" in ctx.content.lower():
            await bot._ws.send_privmsg(os.environ['CHANNEL'], f"@stupac62 Did someone say keyboards? https://puu.sh/GyIa0/8943af5203.png")

    #ErikPromote
    if ctx.author.name.lower() == "erikdotdev":
        promotions = ['Did you know erik co-authored a book called Go in Action: https://www.manning.com/books/go-in-action',
        'Did you know erik is on a podcast, ',
        'Follow Erik on Twitch: https://www.twitch.tv/erikdotdev',
        'Join Eriks Discord: https://discord.gg/FcqTxnw',
        'See Erik at Gophercon: https://www.gophercon.com/',
        'Did you know Erik used to work for Disney?',
        'Did you know Erik works for Microsoft but hates the OS',
        'Did you know Erik started programming when he was 14.',
        'Check out Eriks Github: https://github.com/erikstmartin',
        'Check out Eriks Blog: http://erik.dev/ Yes he does own that domain, cool right?'
        ]

        promotion = random.randint(0, len(promotions))

        #limit how often it triggers
        roll = random.randint(0,10)
        if roll == 10:
            await bot._ws.send_privmsg(os.environ['CHANNEL'], f"{promotions[promotion]}")
        

    if ctx.author.name.lower() == "artmattdank":
        await bot._ws.send_privmsg(os.environ['CHANNEL'], f"beginbArt beginbArt beginbArt")

    #lulbot
    if ctx.content == "LUL":
        await bot._ws.send_privmsg(os.environ['CHANNEL'], f"beginbThis beginbThis beginbThis")


    #hello
    if ctx.content == "hello":
        await bot._ws.send_privmsg(os.environ['CHANNEL'], f"hello @{ctx.author.name.lower()}")


    #whats a google
    searchEngines = ['google ',' bing ', ' yahoo ', ' baidu ', 'aol ', 'ask.com', 'excite.com', 'duckduckgo', 'wolfram alpha', 'yandex', 'lycos ', 'chacha.com', 'searx', 'cc search', 'swisscows', 'startpage ', 'search encrypt', 'gibiru', 'onesearch', 'wiki.com', 'boardreader', 'givewater', 'ekoru', 'ecosia', 'dogpile', 'yippy', 'assjeaves', 'gophero', 'binggo', 'qwant', 'blogsearchengine']

    #ignore commands
    if "!" not in ctx.content.lower(): 
        #ignore bot
        if ctx.author.name.lower() !="beginbotbot":
            #check if message contains a searchengine
            result = [ele for ele in searchEngines if(ele in ctx.content.lower())]

            if result:  
                print(result)
                await bot._ws.send_privmsg(os.environ['CHANNEL'], f"Search engine of choice* ftfy @{ctx.author.name.lower()}")


    #keep color greenscreen
    if "!color" in ctx.content:
        if ctx.author.name.lower() == "adengamesbot":
            await bot._ws.send_privmsg(os.environ['CHANNEL'], f"!color base16-grayscale-light")



    #bot.py, in event_message, below the bot ignore stuffs
    await bot.handle_commands(ctx)


@bot.command(name="!kotd")
async def kotd(ctx):
    keeb = keeboftheday()
    await ctx.send(f'keeb of the day: {keeb}')

@bot.command(name="!bingo")
async def bingo(ctx):
    await ctx.send(f'Begin Bingo: https://codepen.io/Zanuss/pen/BaKVKrX')


@bot.command(name="!bingoadd")
async def bingoAdd(ctx):
    await ctx.send(f'Add to the bingo squares make a PR: https://github.com/AdamMcWilliam/beginbingo')
    

@bot.command(name="!updateSoundeffect")
async def updateSoundeffect(ctx):
    command = "!soundeffect"
    link = "https://www.youtube.com/watch?v=jn3Vv6VYdxw"
    time = "00:02 00:06"

    await ctx.send(f'{command} {link} {time}')


@bot.command(name="!gzbsays")
async def gzbsays(ctx):
    
    gzbSaysArray = ["Do you prefer to spend more time with your SO, family, or friends? Why"
, "What activity calms you down and makes you feel at peace with the world?"
, "How often do you feel overwhelmed?"
, "If you see a homeless person asking for money, do you give them any?"
, "What will immediately disqualify a potential SO?"
, "How adventurous are you? Give some examples."
, "Who do you want to be more like?"
, "Do you think any part of your personality needs to be improved? If so, which part and why?"
, "Which aspect of your life is going really well right now and which aspect could you use some help with?"
, "How politically involved are you?"
, "When was the last time you really panicked?"
, "Where do you go when you want to be alone?"
, "What chokes you up when you think about it?"
, "What was the most awkward conversation you ever had with someone?"
, "What holidays did your family really go all out for when you were growing up?"
, "Would you rather spend the day at an art, history, or science museum?"
, "What seemed normal in your family when you were growing up, but seems weird now?"
, "What’s your favorite scene in a movie?"
, "What is a controversial opinion do you have?"
, "What fact do you try to ignore?"
, "Who in your life always stresses you out and who do you rely on to help you calm down?"
, "Why are you still streaming"]

    randomQ = random.randint(0, len(gzbSaysArray))
    await ctx.send(f'Gzb Says: {gzbSaysArray[randomQ]}???')   

@bot.command(name="!gamble")
async def gamble(ctx):
    if ctx.author.name.lower() == "zanuss":
        avg = AvgCubeTime()
        #convert from timestamp to seconds current 0:00:00
        splitAvg = avg.split(':')
        h = int(splitAvg[0]) * 60 * 60
        m = int(splitAvg[1]) * 60
        s = int(splitAvg[2])
        secs = h+m+s
        await ctx.send(f"!bet {secs}")

    
@bot.command(name="!loadtop8")
async def loadTop8(ctx):
    top8 = ['distributedcache', 'bigedbot', 'disk_bot', 'nomorebot'] 
    if ctx.author.name.lower() == "zanuss":
        for i in top8:
            await ctx.send(f'!top8 {i}')


@bot.command(name="!random")
async def getRandom(ctx):
        msg = ctx.content.split('!random ')
        numbers = msg[1].split(' ')
        start = int(numbers[0])
        end = int(numbers[1])
        randResult = random.randint(start, end)
        if ctx.author.name.lower() !='mccannch':
            await ctx.send(f'Random number from {start} to {end}: {randResult}')
        else:
            await ctx.send(f'Random number from {start} to {end}: 7')


@bot.command(name='!zanussbotgit')
async def manifestozanussbot(ctx):
    await ctx.send('Look at my insides: https://github.com/AdamMcWilliam/TwitchBot ')

@bot.command(name='!manifestozanussbot')
async def manifestozanussbot(ctx):
    await ctx.send('This bot Logs Begins cube times in a google spreadsheet with !cubed 0:00:00 when entered by beginbotbot. The average cube time can be fetched with !!act. The average of begins attempts of the day can be fetched with !!dact.')

@bot.command(name='!botcss')
async def botcss(ctx):
    if(ctx.author.name.lower() !='zanuss'):
        return
    cssLink = ctx.content.split('!!botcss')
    cssLink = cssLink[1]    
    await ctx.send(f'!css {cssLink}')


@bot.command(name='!propsme')
async def propsme(ctx):
    await ctx.send(f'!props {ctx.author.name.lower()}')    


@bot.command(name='!csstemplate')
async def csstemplate(ctx):
    await ctx.send('Here is a css template to help you get started on https://mygeoangelfirespace.city/: https://codepen.io/Zanuss/pen/dyGoamX')    


@bot.command(name='!donateme')
async def donateme(ctx):
    if ctx.author.name.lower() == 'whatsinmyopsec' or ctx.author.name.lower() == 'opsecbot':
        return   
    else:
        await ctx.send(f'!donate {ctx.author.name.lower()}')    


@bot.command(name='!propsall')
async def propsall(ctx):
    if ctx.author.name.lower() == 'whatsinmyopsec' or ctx.author.name.lower() == 'opsecbot':
        return
    else:
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


@bot.command(name='!insure')
async def insure(ctx):
    insured = insureBot()
    if(insured == False):
        await ctx.send(f'!insurance')

@bot.command(name='!salt')
async def salt(ctx):
    salty = whosSalty(ctx.content)
    await ctx.send(f'!buy salt')
    await asyncio.sleep(1)
    await ctx.send(f'!give {salty} salt')  
    await asyncio.gather(salt(ctx), salt(ctx), salt(ctx)) 

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
    dact = DailyAvgCubeTime()
    await ctx.send(f"Begins Daily Average: {dact}")

@bot.command(name="!bestcube")
async def bestcube(ctx):
    bestCube = bestCubeTime()
    await ctx.send(f"Best recorded cube time: {bestCube}")


@bot.command(name='!grovel')
async def grovel(ctx):
    grovelerMessage = grovelAttempt(ctx.author.name.lower())
    await ctx.send(f"{grovelerMessage}")

@bot.command(name="!output")
async def outputTest(ctx):
    print(ctx._get_channel)
    print(dir(ctx))

@bot.command(name='!texttobinary')
async def textToBinary(ctx):
    x = ctx.content.split('!texttobinary ')
    text = str(x[1])

    encoding='utf-8'
    errors='surrogatepass'

    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    result = bits.zfill(8 * ((len(bits) + 7) // 8))

    await ctx.send(f"{text} in binary is: {result}")


@bot.command(name='!binarytotext')
async def binaryToText(ctx):
    x = ctx.content.split('!binarytotext ')
    message = str(x[1])

    encoding='utf-8'
    errors='surrogatepass'

    n = int(message, 2)
    result = int2bytes(n).decode(encoding, errors)
    
    await ctx.send(f"{message} in text is: {result}")


def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))


# bot.py
if __name__ == "__main__":
    bot.run()

