#import and others
import discord
from discord.ext import commands
from model import get_class 

# the works of bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}') #login to the server

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!') #if user say " Hello", the bot say Hi!

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh) #if user say "heh", the bot  will repeat it 

#image Classification Bots
# import and others
@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            file_name = file.filename
            file_url = file.url
            await file.save(f'./{file_name}')
            await file.save(f"file telah disimpan dengan nama{file_name}")
            hasil = get_class("keras_model.h5", "labels.txt", file_name) 

            # INFERENSI BAKSO DAN MIE AYAM
            if hasil[0] == "Bakso\n" and hasil[1] >= 0.7:
                await ctx.send("ini adalah Bakso")
                await ctx.send("Bakso terbuat pada tahun 1368-1644 dan berasal dari Dinasti Ming, atau di sebut negara China")
            elif hasil[0] == "Mie Ayam\n" and hasil[1] >= 0.7:
                await ctx.send("ini adalah Mie Ayam")
                await ctx.send("Mie Ayam terbuat pada tahun 1970-an dan berasal dari Indonesia, namun di buat oleh orang Tionghoa")
            else:
                await ctx.send("Gambar tidak terdeteksi apapun")

    else:   
        await ctx.send("GAK ADA FILE YANG DITERIMA")

# to get your own token go to #(https://discord.com/developers/applications)#
bot.run("Privacy!")
