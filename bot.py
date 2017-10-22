import discord
import asyncio
import sys
from datetime import datetime
import feedparser
import re
import time
import random
import os

client = discord.Client()

latestNum = 0
currentNum = 0
link = 'blank'
title = 'blank'

last = open("/last.txt", "r") 	#This file stores the last thread number so if the bot closes it doesn't post repeat threads
latestNum = int(last.read())	#MAKE SURE TO SET THIS FILE PATH
last.close()


def setLastFile():
    f = open("/last.txt", "w")	#MAKE SURE TO SET THIS FILE PATH
    f.write(str(latestNum))
    f.close()
def setCurr(val):
    global currentNum
    currentNum = val
def setLatest(val):
    global latestNum
    latestNum = val
def setLink(val):
    global link
    link = val
def setTitle(val):
    global title
    title = val
def setEqual(latest, curr):
    global latestNum
    global currentNum
    
    latestNum = currentNum
	
	
def getForumThreads():
    rss = feedparser.parse('http://example.com/syndication.php?limit=1') #Get the RSS feed from the forums, only get the most recent thread
    
    title = rss.entries[0].title #Grab the title of the thread
    link = rss.entries[0].link #Link to thread
    num = int(re.search(r'\d+', link).group()) #Thread id
    
    setCurr(num)
    setLink(link)
    setTitle(title)

@client.event
async def on_ready():
    print('Logged in as ' + client.user.name + ' @ {:%Y-%b-%d %H:%M:%S}'.format(datetime.now()))
    print('--------------------------------------------')

async def rssChecker():
    getForumThreads()
    if(currentNum > latestNum): #Check if the thread that was just aquired is new or not
        mess = 'A new thread has been posted to the forums: **' + title + '** ' + link
        await client.send_message(discord.Object(id='CHANNEL_ID'), mess) #Set the channel ID
        setEqual(latestNum, currentNum)
        setLastFile()
       
async def background(): 
    await client.wait_until_ready()
    while not client.is_closed:
        await rssChecker() #Run RSS Check
        await asyncio.sleep(900) #Wait 900 seconds (15 minutes) - Set this number to what ever you want the refresh rate to be
 
client.loop.create_task(background())
client.run('BOT_ID') #Set bot ID
