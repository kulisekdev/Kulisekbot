import json
import discord
from discord.ext import commands
from discord import app_commands, FFmpegPCMAudio
import dotenv
from dotenv import load_dotenv
import os
load_dotenv()

# intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True


# Bot things.. just dont forget those... luke.. dont!
bot = commands.Bot(intents=intents,command_prefix="!")
bot_token = os.getenv("token2")


# ready event
@bot.event
async def on_ready():
    print(f"Bot online logged in as {bot.user}")

# Level system reforged. cause the other one sucks. cause im a fucking IDIOT!
@bot.event
async def on_message(message):
    user = str(message.author.id)
    username = str(message.author)
    with open("index.json", "r") as xpfile:
        loadedxp = json.load(xpfile)

    if user not in loadedxp:
        loadedxp[user] = {
            "user": username,
            "XP": 0,
            "LEVEL": 1
        }
    else:
        loadedxp[user]["XP"] += 10

    if loadedxp[user]["XP"] >= 100:
        NewLevel = discord.Embed(
        title="Level up! ⬆",
        description=f"Congrats on leveling up to level {loadedxp[user]["LEVEL"]} {message.author}!"
        )
        loadedxp[user]["XP"] -= 100
        loadedxp[user]["LEVEL"] += 1
        await message.channel.send(embed=NewLevel)

    with open("index.json", "w") as xpfile:
        json.dump(loadedxp,xpfile,indent=4)

bot.run(bot_token)
