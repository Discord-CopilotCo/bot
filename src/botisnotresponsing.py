@client.slash_command(description="Report that the bot is not responding to the staff")
async def botisnotresponding(interaction: discord.Interaction):
    global bugreports
    bugreports = bugreports + 1
    await interaction.response.send_message(
        "Your report has been recorded carefully. Thank you!"
    )
