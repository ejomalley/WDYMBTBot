from discord.ext import commands # for @bot.command() thing
from discord.ext.music import MusicClient, WAVAudio, Track  # to play audio from repl.it
import os  # to get bot token from repl.it env vars
import time  # for to sleep
from keep_alive import keep_alive  # to keep bot server up
keep_alive()
running = False
bot = commands.Bot(command_prefix='?')  # create bot with command prefix '?'

@bot.command()  # command called 'huh'
async def huh(ctx, v = 'druski'):
  global running
  if running: return
  else: running = True
  if ctx.author.voice:  # if user who typed command is in a vc
    voice = 'wdymbt-'+ v +'.wav' # set audio file (def druski)

    try:  # see if audio file exists
      track = Track(WAVAudio(voice), 'huh')  # if it does, create a Track from it
    except:  # if not, notify user 
      await ctx.send(f'nice try, but \'{v}\' is not an available voice')
      running = False
      return

    # try to join voice channel
    try: mc = await ctx.author.voice.channel.connect(cls=MusicClient)
    except: # if cant join vc
      await ctx.send('couldnt join channel :(')  # send chat message
      running = False
      return  # stop command

    await mc.play(track)  # if in vc, play wav audio file
    while mc.is_playing():  # until audio is done playing
      time.sleep(.1)        # wait
    await mc.disconnect()  # leave channel after audio is played
    
    await ctx.message.delete()  # delete command from chat
  else: await ctx.send('youre not in a vc >:(')  # if user is not in vc, send chat
  running = False

bot.run(os.environ['TOKEN'])  # start bot