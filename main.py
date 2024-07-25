"""
Imports are being done below.
If you can't find the code you're searching for, take a look at the src/ directory!
"""

import json
import re
import os
from pathlib import Path
import nextcord
from discord import app_commands
from nextcord.ext import *
from re_edge_gpt import Chatbot, ConversationStyle, ImageGen
from dotenv import load_dotenv
from textwrap import wrap

intents = nextcord.Intents.default()
intents.message_content = True
client = nextcord.Client(intents=intents)
chats = 0
bugreports = 0
load_dotenv()
chat_log = float(chats)
channels = []
staff = []
owner = os.getenv("BOT_OWNER")

def updatechannelsjson():
    with open("channels.json", "w", encoding="utf-8") as channelsfile:
        json.dump(channels, channelsfile, indent=2)
        print(channels)
        print("Updated channels.json")


def openchannelsjson():
    with open("channels.json", "r", encoding="utf-8") as channelsfile:
        channels = json.load(channelsfile)
        print("Loaded channels.json")


def updatestaffjson():
    with open("staff.json", "w", encoding="utf-8") as stafffile:
        if owner not in staff:
            staff.append(int(owner))
        print(staff)
        json.dump(staff, stafffile, indent=2)
        print("Updated staff.json")


def openstaffjson():
    with open("staff.json", "r", encoding="utf-8") as stafffile:
        if owner not in staff:
            staff.append(int(owner))
        staff = json.load(stafffile)
        print("Loaded staff.json")


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}!")


if not os.path.isfile("channels.json"):
    with open("channels.json", "w", encoding="utf-8") as channelsfile:
        json.dump(channels, channelsfile, indent=2)
        print("Created channels.json")
else:
    with open("channels.json", "r", encoding="utf-8") as channelsfile:
        channels = json.load(channelsfile)
        print("Loaded channels.json")
if not os.path.isfile("staff.json"):
    with open("staff.json", "w", encoding="utf-8") as stafffile:
        if owner not in staff:
            staff.append(int(owner))
        json.dump(staff, stafffile, indent=2)
        print("Created staff.json")
else:
    with open("staff.json", "r", encoding="utf-8") as stafffile:
        if owner not in staff:
            staff.append(int(owner))
        staff = json.load(stafffile)
        print("Loaded staff.json")
for script in os.listdir("src"):
    fulldir = os.path.join("src", script)
    if os.path.isfile(fulldir):
        with open(fulldir, "r", encoding="utf-8") as pyscript:
            print("Loading file...")
            exec(pyscript.read())
client.run(os.getenv("DISCORD_TOKEN"))
