#MIT License

#Copyright (c) 2024 ᴋᴜɴᴀʟ [AFK]

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

from telethon import __version__, events, Button
from config import KEX1, KEX2, KEX3, KEX4, KEX5, KEX6, KEX7, KEX8, KEX9, KEX10

START_OP = [
    [
        Button.url("ꜱᴇɴꜱᴇɪ 🥀", "https://t.me/Kexx_XD"),
        Button.url("ꜱᴜᴘᴘᴏʀᴛ 🧸", "https://t.me/TORNADO_TRIBE"),
    ],
    [
        Button.url("ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ❄️", "https://github.com/VARC9210/STORM"),
    ],
    [
        Button.url("ꜱᴜᴘᴘᴏʀᴛ ✨", "https://t.me/STORM_CHATZ"),
        Button.url("ᴄʜᴀɴɴᴇʟ ☁️", "https://t.me/STORM_TECHH"),
    ],
]

@KEX1.on(events.NewMessage(pattern="/start"))
@KEX2.on(events.NewMessage(pattern="/start"))
@KEX3.on(events.NewMessage(pattern="/start"))
@KEX4.on(events.NewMessage(pattern="/start"))
@KEX5.on(events.NewMessage(pattern="/start"))
@KEX6.on(events.NewMessage(pattern="/start"))
@KEX7.on(events.NewMessage(pattern="/start"))
@KEX8.on(events.NewMessage(pattern="/start"))
@KEX9.on(events.NewMessage(pattern="/start"))
@KEX10.on(events.NewMessage(pattern="/start"))
async def start(event):
    if event.is_private:
        KEX = await event.client.get_me()
        bot_name = KEX.first_name
        bot_id = KEX.id
        TEXT = f"**ʜᴇʏ [{event.sender.first_name}]\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})​**\n➖➖➖➖➖➖➖➖➖➖➖\n"
        TEXT += f"» **ꜱᴇɴꜱᴇɪ : [⏤͟͞〲ᴋᴇx](https://t.me/kexx_xd)**\n"
        TEXT += f"» **ꜱᴛᴏʀᴍ :** `M3.1.1` \n"
        TEXT += f"» **ᴘʏᴛʜᴏɴ :** `3.11` \n"
        TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ :** `{__version__}`\n➖➖➖➖➖➖➖➖➖➖➖"        
        await event.client.send_file(
                    event.chat_id,  
                    "https://graph.org/file/c3b279aee41f8bbe6466b.jpg",
                    caption=TEXT, 
                    buttons=START_OP
                )
