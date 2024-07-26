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

import sys
import glob
import asyncio
import logging
import importlib.util
import urllib3
from pathlib import Path
from config import KEX1, KEX2, KEX3, KEX4, KEX5, KEX6, KEX7, KEX8, KEX9, KEX10

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def load_plugins(plugin_name):
    path = Path(f"STORM/modules/{plugin_name}.py")
    try:
        spec = importlib.util.spec_from_file_location(f"STORM.modules.{plugin_name}", path)
        load = importlib.util.module_from_spec(spec)
        load.logger = logging.getLogger(plugin_name)
        spec.loader.exec_module(load)
        sys.modules[f"STORM.modules.{plugin_name}"] = load
        print(f"ꜱᴛᴏʀᴍ ʜᴀꜱ ɪᴍᴘᴏʀᴛᴇᴅ {plugin_name}")
    except Exception as e:
        print(f"ꜰᴀɪʟᴇᴅ ᴛᴏ ʟᴏᴀᴅ ᴘʟᴜɢɪɴ {plugin_name}: {e}")

files = glob.glob("STORM/modules/*.py")
for name in files:
    patt = Path(name)
    plugin_name = patt.stem
    load_plugins(plugin_name)

print("\nꜱᴛᴏʀᴍ ʙᴏᴛ ɪꜱ ᴅᴇᴘʟᴏʏᴇᴅ ꜱᴜᴄᴄᴇꜱꜰᴜʟʟʏ")

async def main():
    await asyncio.gather(
        KEX1.run_until_disconnected(),
        KEX2.run_until_disconnected(),
        KEX3.run_until_disconnected(),
        KEX4.run_until_disconnected(),
        KEX5.run_until_disconnected(),
        KEX6.run_until_disconnected(),
        KEX7.run_until_disconnected(),
        KEX8.run_until_disconnected(),
        KEX9.run_until_disconnected(),
        KEX10.run_until_disconnected()
    )

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
