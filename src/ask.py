@client.slash_command(description="Ask copilot a question", dm_permission=True)
async def ask(interaction: nextcord.Interaction, prompt: str):
    await interaction.response.defer()
    cookies = json.loads(
        open(f"{Path.cwd()}/bing_cookies.json", encoding="utf-8").read()
    )
    bot = await Chatbot.create(cookies=cookies)
    response_bing = await bot.ask(
        prompt=prompt,
        conversation_style=ConversationStyle.precise,
        simplify_response=True,
    )
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
    actualtext = str(actualtext)
    if len(actualtext) > 1999:
        try:
            actualtext = actualtext.split('"]')[0]
        except:
            pass
        split = wrap(str(actualtext), 1999)
        interaction.followup.send(split[0])
    elif len(actualtext) < 1999:
        actualtext = re.sub("\[\^\d\^\]", "", actualtext)
        await interaction.followup.send(actualtext)
    if re.search(r"ll ?try ?to ?create ?that", parsed_done["text"]):
        piccookie = ""
        for cookie in cookies:
            if cookie["name"] == "_U":
                piccookie = cookie["value"]
                break
        sync_gen = ImageGen(auth_cookie=piccookie, quiet=True)
        imggenprompt = re.sub("..ll ?try ?to ?create ?that", '', prompt)
        image = sync_gen.get_images(prompt=imggenprompt)
        sync_gen.save_images(image, "images")
        images = []
        for image in os.listdir("images")[:1]:
            img = f = os.path.join("images", image)
            if os.path.isfile(img):
                images.append(
                    nextcord.File(img, filename="image.jpeg")
                )
        embed = nextcord.Embed()
        embed.set_image(url="attachment://image.jpeg")
        await interaction.followup.send(
            files=images, embed=embed
        )
        for image in os.listdir("images"):
            img = f = os.path.join("images", image)
            os.remove(img)