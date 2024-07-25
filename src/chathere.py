@client.slash_command(description="Set this channel for the bot to talk here :)")
async def chathere(interaction: nextcord.Interaction):
    if interaction.user.guild_permissions.manage_guild:
        global channels
        if interaction.channel.id not in channels:  
            channels.append(interaction.channel.id)
            updatechannelsjson()
            await interaction.response.send_message(
                "Channel set successfully! Have fun! \;-)"
            ) 
        else:
            await interaction.response.send_message(
                f"Oops, this channel is set already! If it doesn't works, contact the support team or DM <@{owner}>"
            )
