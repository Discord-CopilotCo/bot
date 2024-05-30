import asyncio
import discord
import json
from pathlib import Path

from re_edge_gpt import Chatbot
from re_edge_gpt import ConversationStyle

#SYSTEM_PROMPT
system_prompt = ('Put prompt here')

intents = discord.Intents.default()
intents.message_content = True
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    print(system_prompt)

@client.event
async def on_message(message):
  if client.user.mention in message.content.split():
   # print (message.content)
    bot = None
    try:
        cookies = json.loads(open(
            str(Path(str(Path.cwd()) + "/bing_cookies.json")), encoding="utf-8").read())
        bot = await Chatbot.create(cookies=cookies)
        bot.ask(
            prompt=system_prompt,
            conversation_style=ConversationStyle.precise,
            simplify_response=True
        )
        response_bing = await bot.ask(
            prompt=message.content,
            conversation_style=ConversationStyle.precise,
            simplify_response=True
        )
        nonparsed = json.dumps(response_bing, indent=2, ensure_ascii=False)
       # print(nonparsed)
        parsed_done = json.loads(nonparsed)
       # print(parsed_done)
        await message.channel.send(parsed_done["text"])
    except Exception as error:
        raise error
    finally:
        if bot is not None:
            await bot.close()



client.run('ur token here')
