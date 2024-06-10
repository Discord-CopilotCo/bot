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
from re_edge_gpt import ImageGen
intents = discord.Intents.default()
intents.message_content = True
intents = discord.Intents.default()
intents.message_content = True
staff = []
client = discord.Client(intents=intents)
chats  =  0
bugreports = 0
load_dotenv()
chat_log = float(chats)
channels = []
owner = os.getenv("BOT_OWNER")
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
      await message.channel.send(f"You are not staff! Apply by DMing <@{owner}> with a short reason why you want to be staff.")
      print(f"User {message.author.id} attempted using a owner-only command.")
  if client.user in message.mentions or message.channel.id in channels and not message.author.bot and not message.content.startswith("/"):
    async with message.channel.typing():
      bot = None
      try:
          cookies = json.loads(open(f"{Path.cwd()}/bing_cookies.json", encoding="utf-8").read())
          bot = await Chatbot.create(cookies=cookies)
          if not message.attachments:
            response_bing = await bot.ask(
                prompt=message.content,
                conversation_style=ConversationStyle.precise,
                simplify_response=True
            )
          else:
            msg = await message.channel.send("🔎Analyzing your image...")
            attachmentdsc = message.attachments[0]
            response_bing = await bot.ask(
                prompt=message.content,
                conversation_style=ConversationStyle.precise,
                simplify_response=True,
                attachment={"image_url":f"{attachmentdsc.url}"}
            )
            await msg.edit("✅Done!")
          nonparsed = json.dumps(response_bing, indent=2, ensure_ascii=False)
          parsed_done = json.loads(nonparsed)
          actualtext = str(parsed_done["text"])
          for match in re.findall("Analysing the (?:.......??) (.)aces may be (........)to(................)", actualtext):
             actualtext.replace(str(match), "")
          global chats
          chats = chats+1
          chat_log = float(chats)
          await message.channel.send(actualtext)
          if re.search(r"ll ?try ?to ?create ?that", parsed_done["text"]):
            async with message.channel.typing():
              piccookie = ""
              for cookie in cookies:
                  if cookie["name"] == "_U":
                      piccookie =  cookie["value"]
                      break
              sync_gen = ImageGen(auth_cookie=piccookie, quiet=True)
              image = sync_gen.get_images(prompt=message.content)
              sync_gen.save_images(image, "images")
              images = []
              for image in os.listdir("images")[:1]:
                  img = f = os.path.join("images", image)
                  if os.path.isfile(img):
                      images.append(discord.File(img, filename="image.jpeg"))
              embed = discord.Embed()
              embed.set_image(url="attachment://image.jpeg")
              await message.channel.send(files=images, embed=embed)
              for image in os.listdir("images"):
                  img = f = os.path.join("images", image)
                  os.remove(img)
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
@client.slash_command(description = "Set this channel for the bot to talk here :)")
async def chathere(interaction: discord.Interaction):
  global channels
  if not interaction.channel.id in channels:
    channels.append(interaction.channel.id)
    with open("channels.json", 'w') as channelsfile:
        json.dump(channels, channelsfile, indent=2)
        print("Updated channels.json")
    await interaction.response.send_message("Channel set successfully! Have fun! \;-)")
  else:
    await interaction.response.send_message(f"Oops, this channel is set already! If it doesn't works, contact the support team or DM <@{owner}>")
@client.slash_command(description = "OWNER-ONLY: Make a user staff")
async def addstaff(interaction: discord.Interaction, user: discord.Member):
  if str(owner) in str(interaction.user.id):
   if not user.id in staff:
     staff.append(user.id)
     with open("staff.json", 'w') as stafffile:
         if not owner in staff:
           staff.append(owner)
         json.dump(staff, stafffile, indent=2)
         print("Updated staff.json")
     await interaction.response.send_message(f"Welcome, {user.mention}, to the Copilot staff team!")
   else:
     await interaction.response.send_message(f"User is staff already.")
  else:
   await interaction.response.send_message(f"""You are not the bot owner. Owner has the uID "{owner}", while you have the uID "{interaction.user.id}""")
@client.slash_command(description = "Unset channel for chatting with copilot :(")
async def unset(interaction: discord.Interaction):
  if interaction.channel.id in channels:
    channels.remove(interaction.channel.id)
    with open("channels.json", 'w') as channelsfile:
        json.dump(channels, channelsfile, indent=2)
        print("Updated channels.json")
    await interaction.response.send_message("Unset.")
  else:
    await interaction.response.send_message("This channel is not set.")
@client.slash_command(description = "OWNER-ONLY: Remove staff from a user")
async def removestaff(interaction: discord.Interaction, user: discord.Member):
  if str(owner) in str(interaction.user.id):
   if user.id in staff:
     staff.remove(user.id)
     with open("staff.json", 'w') as stafffile:
         if not owner in staff:
           staff.append(owner)
         json.dump(staff, stafffile, indent=2)
         print("Updated staff.json")
     await interaction.response.send_message(f"Staff removed from {user.mention}.")
   else:
     await interaction.response.send_message(f"User is not staff.")
  else:
   await interaction.response.send_message("You are not the bot owner.")
client.run(os.getenv('DISCORD_TOKEN'))
