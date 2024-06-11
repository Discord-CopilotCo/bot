@client.slash_command(description = "OWNER-ONLY: Make a user staff")
async def addstaff(interaction: discord.Interaction, user: discord.Member):
  if str(owner) in str(interaction.user.id):
   if not user.id in staff:
     staff.append(user.id)
     updatestaffjson()
     await interaction.response.send_message(f"Welcome, {user.mention}, to the Copilot staff team!")
   else:
     await interaction.response.send_message(f"User is staff already.")
  else:
   await interaction.response.send_message(f"""You are not the bot owner. Owner has the uID "{owner}", while you have the uID "{interaction.user.id}""")
