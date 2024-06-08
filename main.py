import asyncio
import nextcord as discord
from nextcord.ext import *
import json
from pathlib import Path
import re
from re_edge_gpt import Chatbot
from re_edge_gpt import ConversationStyle
from dotenv import load_dotenv
import os
intents = discord.Intents.default()
intents.message_content = True
intents = discord.Intents.default()
intents.message_content = True
staff = ['''placeyouruseridhere''', '''placeyourstaffmember'suseridhere''', 1213799919920484364]
client = discord.Client(intents=intents)
chats  =  0
bugreports = 0
load_dotenv()
chat_log = float(chats)
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}!')
@client.event
async def on_message(message):
  if message.content.startswith('cp!stats'):
    if message.author.id in staff:
      global chat_log
      global bugreports
      embed = discord.Embed(title="Copilot's statistics", description="Thank you for being a staff member!", color=0x00ff00)
      embed.add_field(name="Servers I am in:", value=len(client.guilds), inline=True)
      embed.add_field(name="Chats since the bot is up:", value=chat_log, inline=True)
      embed.add_field(name=f"Bug reports(bot is not responding): ", value=bugreports, inline=True)
      await message.channel.send(embed=embed)
    else:
      await message.channel.send(f"You are not staff! Apply by DMing <@{client.owner_id}> with a short reason why you want to be staff.")
      print(f"User {message.author.id} attempted using a owner-only command.")
  if client.user in message.mentions:
    async with message.channel.typing():
      bot = None
      try:
          cookies = json.loads(open(f"{Path.cwd()}/bing_cookies.json", encoding="utf-8").read())
          bot = await Chatbot.create(cookies=cookies)
          response_bing = await bot.ask(
              prompt=message.content,
              conversation_style=ConversationStyle.precise,
              simplify_response=True
          )
          nonparsed = json.dumps(response_bing, indent=2, ensure_ascii=False)
          parsed_done = json.loads(nonparsed)
          global chats
          chats = chats+1
          chat_log = float(chats)
          await message.channel.send(parsed_done["text"])
      except Exception as error:
          raise error
          await message.channel.send(f"Oops, an error occured! Please contact the owner at <@{client.owner_id}>")
      finally:
          if bot is not None:
              await bot.close()
@client.slash_command(description = "Report that the bot is not responding to the staff")
async def botisnotresponding(interaction: discord.Interaction):
  global bugreports
  bugreports = bugreports+1
  await interaction.response.send_message("Your report has been recorded carefully. Thank you!")
client.run(os.getenv('DISCORD_TOKEN'))
