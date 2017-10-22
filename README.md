# MyBB New Thread Discord Bot

----
## Installation

You'll need the following python libraries:

* discord

* asyncio

* feedparser

Once you have those installed, open bot.py and setup your bot, put in the bot ID at the bottom and enter the channel ID from the channel you want the bot to post in. Change the wait time to something else if desired (default = 15 minutes)

Also make sure to set the correct URL to your forums URL (everywhere it says example.com change to your website/forums URL).

----
## Usage (Only tested on Python 3.6)

Once the bot is running, it will print in the console and shortly after you should see the bot come online in your discord, then shortly after that it should post a link to the most recent thread. This is normal, even if that thread is not new, the bot needs to determine a basis to run off of. You can skip this initial discord message by setting the value in "last.txt" to the most recent thread number.

After that, the bot will check your forums every defined interval and post a message to discord with a link and the title of the thread.
