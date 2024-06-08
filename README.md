![image](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Microsoft_365_Copilot_Icon.svg/240px-Microsoft_365_Copilot_Icon.svg.png)
# Microsoft Copilot is now on Discord! 🤖
## How to use:
1. Make an application
2. Get your discord bot token.
3. Rename the hidden file ".env.example" to ".env"
4. Open it with an editor, write `DISCORD_TOKEN=` and place your token right after `DISCORD_TOKEN=`, then save the file..
5. Install the cookie editor extension for [Chrome](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm) or [Firefox](https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/)
6. Go to https://copilot.microsoft.com/
7. Open the extension
8. Click "Export" on the bottom right, then "Export as JSON" (This saves your cookies to clipboard)
9. Paste your cookies into the file `bing_cookies.json`, remove existing content.
   - NOTE: The **cookies file name MUST follow the regex pattern `bing_cookies.json`**, so that they could be recognized by internal cookie processing mechanisms
10. Finally, place your own UserID in main.py at line 15, so it would look like this: `staff = ['youruserid']`. You can add even more staff members: `staff = [member1userid, member2userid, youruserid]`
11. Install dependencies: `python3 -m pip install -r requirements.txt`
12. Run the bot: `python3 main.py`

To see statistics, use "cp!stats"
### Enjoy your all time favorite AI 👑
If it doesn't works, join our support server at https://discord.com/invite/M2FhPZyq
# _**NOTE: THIS IS NOT A OFFICIAL MICROSOFT PRODUCT**_
