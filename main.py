import asyncio
import nextcord as discord
import json
import re
import os
from dotenv import load_dotenv
from nextcord.ext import *
from pathlib import Path
from re_edge_gpt import Chatbot, ConversationStyle, ImageGen
from re_edge_gpt import ConversationStyle
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
chats  =  0
bugreports = 0
load_dotenv()
chat_log = float(chats)
channels = []
staff = []
owner = os.getenv("BOT_OWNER")
def updatechannelsjson():
  with open("channels.json", 'w') as channelsfile:
       json.dump(channels, channelsfile, indent=2)
       print(channels)
       print("Updated channels.json")
def openchannelsjson():
  with open("channels.json", 'r') as channelsfile:
       channels = json.load(channelsfile)
       print("Loaded channels.json")
def updatestaffjson():
  with open("staff.json", 'w') as stafffile:
       if not owner in staff:
         staff.append(owner)
       json.dump(staff, stafffile, indent=2)
       print(staff)
       print("Updated staff.json")
def openstaffjson():
  with open("staff.json", 'r') as stafffile:
       if not owner in staff:
         staff.append(owner)
       staff = json.load(stafffile)
       print("Loaded staff.json") 
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}!')
    
if not os.path.isfile("channels.json"):
   with open("channels.json", 'w') as channelsfile:
       json.dump(channels, channelsfile, indent=2)
       print("Created channels.json")
else:
   with open("channels.json", 'r') as channelsfile:
       channels = json.load(channelsfile)
       print("Loaded channels.json")
if not os.path.isfile("staff.json"):
   with open("staff.json", 'w') as stafffile:
       if not owner in staff:
         staff.append(owner)
       json.dump(staff, stafffile, indent=2)
       print("Created staff.json")
else:
   with open("staff.json", 'r') as stafffile:
       if not owner in staff:
         staff.append(owner)
       staff = json.load(stafffile)
       print("Loaded staff.json")
for script in os.listdir("src"):
    fulldir = os.path.join("src", script)
    if os.path.isfile(fulldir):
        pyscript = open(fulldir, 'r')
        print("Loading file...")
        exec(pyscript.read())
client.run(os.getenv('DISCORD_TOKEN'))
