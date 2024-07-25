@client.slash_command(description="Unset channel for chatting with copilot :(")
async def unset(interaction: nextcord.Interaction):
    if interaction.user.guild_permissions.manage_guild:
        if interaction.channel.id in channels:
            channels.remove(interaction.channel.id)
            updatechannelsjson()
            await interaction.response.send_message("Unset.")
        else:
            await interaction.response.send_message("This channel is not set.")
