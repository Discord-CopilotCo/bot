@client.slash_command(description="OWNER-ONLY: Remove staff from a user")
async def removestaff(interaction: nextcord.Interaction, user: nextcord.Member):
    if str(owner) in str(interaction.user.id):
        if user.id in staff:
            staff.remove(user.id)
            updatestaffjson()
            await interaction.response.send_message(
                f"Staff removed from {user.mention}."
            )
        else:
            await interaction.response.send_message(f"User is not staff.")
    else:
        await interaction.response.send_message("You are not the bot owner.")
