![image](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Microsoft_365_Copilot_Icon.svg/480px-Microsoft_365_Copilot_Icon.svg.png)
# Microsoft Copilot is now on Discord! 🤖
## How to use:
1. Make an application
2. Get your discord bot token and go to chat_dsc.py, put your token in client.run.
3. Install the cookie editor extension for [Chrome](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm) or [Firefox](https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/)
5. Go to https://copilot.microsoft.com/
6. Open the extension
7. Click "Export" on the bottom right, then "Export as JSON" (This saves your cookies to clipboard)
8. Paste your cookies into a file `bing_cookies.json`.
   - NOTE: The **cookies file name MUST follow the regex pattern `bing_cookies.json`**, so that they could be recognized by internal cookie processing mechanisms
9. Install dependencies: `python3 -m pip install -r requirements.txt`
10. Run the bot: `python3 chat_dsc.py`
### Enjoy your all time favorite AI 👑
***NOTE: THIS IS NOT A OFFICIAL MICROSOFT PRODUCT
