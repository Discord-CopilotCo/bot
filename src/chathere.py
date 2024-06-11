@client.slash_command(description = "Set this channel for the bot to talk here :)")
async def chathere(interaction: discord.Interaction):
  global channels
  if not interaction.channel.id in channels:
    channels.append(interaction.channel.id)
    updatechannelsjson()
    await interaction.response.send_message("Channel set successfully! Have fun! \;-)")
  else:
    await interaction.response.send_message(f"Oops, this channel is set already! If it doesn't works, contact the support team or DM <@{owner}>")
