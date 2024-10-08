import discord
import time,os
from discord.ext import commands
from discord.utils import get
import sqlite3
import asyncio
from keep_alive import keep_alive
import flask

token = os.getenv("TOKEN")

prefix_file = open("prefix.txt","r")
prefixes = [i.replace("\n"," ") for i in prefix_file.readlines()]

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=prefixes,
										intents=intents,
										case_insensitive=True)
bot.remove_command("help")

@bot.event
async def on_ready():
	print(f"Logged in as {bot.user}")
#ping
@bot.command()
async def ping(ctx):
	msg = discord.Embed(title="Pong 🏓", description=f"{round(bot.latency*1000)} _ms_!")
	await ctx.send(embed=msg)

#cogs
for files in os.listdir("./cogs"):
	if files.endswith(".py"):
		bot.load_extension(f"cogs.{files[:-3]}")

		
keep_alive()		

bot.run(token)