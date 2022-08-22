
from imaplib import Commands
import random
from tabnanny import check
import time
from playsound import playsound
import winsound

import discord
import os

from discord.ext import commands
from discord.ext.commands import Bot

client = discord.Client(intents = discord.Intents().all())


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message=str(message.content)
    if message.author==client.user:
        return
    if message.content=='!help':
        await message.channel.send("This bot contains the following commands")
        await message.channel.send("1. !hello or !hi -> Introductory message")
        await message.channel.send("2. !generate_tt -> Genearates a personalised time table. Example ->!generate_tt math-120 physics-120 ")
        await message.channel.send("3. !stop_timer -> Stops the timer and bot goes back to sleep")
        await message.channel.send("4. !bye -> Bot will still be online but sends a goodbye message")                
    if message.content=='!hello' or message.content=='!hi':
        await message.channel.send('Hi there')
        await message.channel.send(f'{username} Please enter !generate_tt "subject 1-number of minutes" "subject 2-number of minutes"... for a timetable')
    elif message.content=='!stop_timer':
        await message.channel.send(f'Goodbye, {username}')
        exit()
    elif message.content=='!bye':
        await message.channel.send(f'Hope you had a good session, see you later, {username}')
    else:
        p=list((message.content).split(" "))
        tasks={}
        tasks2={}
        if(p[0]=="!generate_tt"):
            n=len(p)-1
            s={}
            h={}
            f=[]
            sum_of_min=0
            
            for i in range(1,n+1):
                sub,hrs=p[i].split('-')
                s[i]=sub
                h[i]=int(hrs)
                f.append(i)
                sum_of_min = sum_of_min + int(hrs)
            c=1
            await message.channel.send("Your timetable is here")
            while(len(f)!=0):
                r=random.choice(f)
                await message.channel.send(f"Task number {c} is {s[r]} for {h[r]} minutes")
                tasks[c]=h[r]
                tasks2[c]=s[r]
                f.pop(f.index(r))
                c=c+1
            await message.channel.send("Your timer will start in 10 seconds. Type '!stop_timer' to stop the timer")
            time.sleep(10)
            await message.channel.send("Your time starts now")
            winsound.Beep(440,500)
            i=0
            mins=0
            secs=0
            while(i!=n):
                cd=0
                await message.channel.send(f"Task {i+1} is {tasks2[i+1]}")
                t=int((tasks[i+1]))*60
                while(t):
                    if(cd==3600 and sum_of_min>60):
                        await message.channel.send("Take a break. It's been an hour")
                        winsound.Beep(740,500)
                        cd=0
                        t1=10*60
                        while(t1):
                            mins1=t1//60
                            secs1=t1%60
                            timer1='{:02d}:{:02d}'.format(mins1,secs1)
                            msg1=await message.channel.send(f'{timer1}')
                            await msg1.delete()
                            t1-=1
                        await message.channel.send("Get back to work!!")
                        winsound.Beep(240,500)
                    mins=t//60
                    secs=t%60
                    timer='{:02d}:{:02d}'.format(mins,secs)
                    msg=await message.channel.send(f'{timer}')
                    await msg.delete()
                    t-=1
                    cd+=1
                if(i+1==n):
                    await message.channel.send("Tasks completed!!\n")
                    break
                
                await message.channel.send(f"Task {i+1},completed. Get ready for your next task in 60 sec")
                winsound.Beep(240,500)
                time.sleep(60)
                winsound.Beep(440,500)
                i+=1
        
        else:
            return
client.run('insert your token here')
