import discord
import time
import asyncio
import os
import textwrap

try:
    DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
except KeyError:
    DISCORD_TOKEN = "Discord-Token incorrect."

token = DISCORD_TOKEN

intents = discord.Intents.default()
intents.message_content = True

last_messages = 12
client = discord.Client(intents=intents)

def markdown(string):
    t_string = string.replace('- ','• ')

    string_list = t_string.split("**")
    temp_string = ""
    for i in range(len(string_list)):
        if i == 0:
            temp_string += string_list[i]
        elif i%2 != 0:
            temp_string += ("&b"+string_list[i]+"&r")
        else :
            temp_string += string_list[i]
    t_string = temp_string

    string_list = t_string.split("*")
    temp_string = ""
    for i in range(len(string_list)):
        if i == 0:
            temp_string += string_list[i]
        elif i%2 != 0:
            temp_string += ("&o"+string_list[i]+"&r")
        else :
            temp_string += string_list[i]
    t_string = temp_string

    string_list = t_string.split("__")
    temp_string = ""
    for i in range(len(string_list)):
        if i == 0:
            temp_string += string_list[i]
        elif i%2 != 0:
            temp_string += ("&n"+string_list[i]+"&r")
        else :
            temp_string += string_list[i]
    t_string = temp_string

    print(t_string)
    return t_string

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await asyncio.sleep(5)
#announcement txt
    a_channel = client.get_channel(1172038353185669150)
    a_messages = [message.content async for message in a_channel.history(limit=last_messages)]
    a_messages.reverse()
    fa = open("menu/announcement.txt", "w", encoding="utf-8")
    for items in a_messages:
        fa.write("%s\n" % textwrap.fill(items,80))
    fa.close()
#change-log txt
    c_channel = client.get_channel(1172034193132355635)
    c_messages = [message.content async for message in c_channel.history(limit=last_messages)]
    c_messages.reverse() 
    fc = open("menu/change_logs.txt", "w", encoding="utf-8")
    for items in c_messages:
        fc.write("%s\n" % textwrap.fill(items,80))
    fc.close()
#title txt
    t_channel = client.get_channel(1172640409730682952)
    t_messages = [message.content async for message in t_channel.history(limit=last_messages)]
    t_messages.reverse() 
    ft = open("menu/title.txt", "w", encoding="utf-8")
    for items in t_messages:
        ft.write("%s\n" % textwrap.fill(items,40))
    ft.close()

    await client.close()

    @client.event
    async def on_message(message):
        channels = ["ruler"]
        if str(message.channel) in channels:
            if message.content == "!h":
                messages = [message.content async for message in message.channel.history(limit=last_messages)]
                await message.channel.send(f"Last {last_messages} messages:")
                await message.channel.send(messages)

client.run(token)