@client.event
async def on_message(message):
    if message.content.startswith("cp!stats"):
        if message.author.id in staff:
            global chat_log
            global bugreports
            embed = discord.Embed(
                title="Copilot's statistics",
                description="Thank you for being a staff member!",
                color=0x00FF00,
            )
            embed.add_field(
                name="Servers I am in:", value=len(client.guilds), inline=True
            )
            embed.add_field(
                name="Chats since the bot is up:", value=chat_log, inline=True
            )
            embed.add_field(
                name=f"Bug reports(bot is not responding): ",
                value=bugreports,
                inline=True,
            )
            await message.channel.send(embed=embed)
        else:
            await message.channel.send(
                f"You are not staff! Apply by DMing <@{owner}> with a short reason why you want to be staff."
            )
            print(f"User {message.author.id} attempted using a owner-only command.")
    if client.user in message.mentions or message.channel.id in channels:
        if not message.author.bot:
            async with message.channel.typing():
                bot = None
                try:
                    cookies = json.loads(
                        open(f"{Path.cwd()}/bing_cookies.json", encoding="utf-8").read()
                    )
                    bot = await Chatbot.create(cookies=cookies)
                    if not message.attachments:
                        response_bing = await bot.ask(
                            prompt=message.content,
                            conversation_style=ConversationStyle.precise,
                            simplify_response=True,
                        )
                    else:
                        msg = await message.channel.send("🔎Analyzing your image...")
                        attachmentdsc = message.attachments[0]
                        response_bing = await bot.ask(
                            prompt=message.content,
                            conversation_style=ConversationStyle.precise,
                            simplify_response=True,
                            attachment={"image_url": f"{attachmentdsc.url}"},
                        )
                        await msg.edit("✅Done!")
                    nonparsed = json.dumps(response_bing, indent=2, ensure_ascii=False)
                    parsed_done = json.loads(nonparsed)
                    actualtext = str(parsed_done["text"])
                    for match in re.findall(
                        "Analysing the (?:.......??) (.)aces may be (........)to(................)",
                        actualtext,
                    ):
                        actualtext.replace(str(match), "")
                    global chats
                    chats = chats + 1
                    chat_log = float(chats)
                    await message.channel.send(actualtext, reference=message)
                    if re.search(r"ll ?try ?to ?create ?that", parsed_done["text"]):
                        async with message.channel.typing():
                            piccookie = ""
                            for cookie in cookies:
                                if cookie["name"] == "_U":
                                    piccookie = cookie["value"]
                                    break
                            sync_gen = ImageGen(auth_cookie=piccookie, quiet=True)
                            image = sync_gen.get_images(prompt=message.content)
                            sync_gen.save_images(image, "images")
                            images = []
                            for image in os.listdir("images")[:1]:
                                img = f = os.path.join("images", image)
                                if os.path.isfile(img):
                                    images.append(
                                        discord.File(img, filename="image.jpeg")
                                    )
                            embed = discord.Embed()
                            embed.set_image(url="attachment://image.jpeg")
                            await message.channel.send(
                                files=images, embed=embed, reference=message
                            )
                            for image in os.listdir("images"):
                                img = f = os.path.join("images", image)
                                os.remove(img)
                except Exception as error:
                    raise error
                    await message.channel.send(
                        f"Oops, an error occured! Please contact the owner at <@{owner}>"
                    )
                finally:
                    if bot is not None:
                        await bot.close()
