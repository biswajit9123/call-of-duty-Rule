import discord
import asyncio
from discord.ext.commands import Bot
import platform
import time
import os
import colorsys
import random
import json
 
client = Bot(description="MyBot is best", command_prefix="c!", pm_help = False)
client.remove_command('help')


@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started x10bot')
    print('Created by biswajit')
 
 
@client.event
async def on_message_edit(before, after):
    if before.content == after.content:
      return
    if before.author == client.user:
      return
    else:
      user = before.author
      member = after.author
      for channel in user.server.channels:
        if channel.name == '╰☆☆-cod-log-☆☆╮':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
            embed.set_author(name='Message edited')
            embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
            embed.add_field(name = 'Before:',value ='{}'.format(before.content),inline = False)
            embed.add_field(name = 'After:',value ='{}'.format(after.content),inline = False)
            embed.add_field(name = 'Channel:',value ='{}'.format(before.channel.name),inline = False)
            await client.send_message(channel, embed=embed)
 
@client.event
async def on_message_delete(message):
    if not message.author.bot:
      channelname = '╰☆☆-cod-log-☆☆╮'
      logchannel=None
      for channel in message.server.channels:
        if channel.name == channelname:
          user = message.author
      for channel in user.server.channels:
        if channel.name == '╰☆☆-cod-log-☆☆╮':
          logchannel = channel
          r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
          embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
          embed.set_author(name='Message deleted')
          embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
          embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
          embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
          await client.send_message(logchannel,  embed=embed)
          
          
@client.event
async def on_reaction_add(reaction, user):
  for channel in user.server.channels:
    if channel.name == '╰☆☆-cod-log-☆☆╮':
        logchannel = channel
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Reaction Added')
        embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
        embed.add_field(name = 'Message:',value ='{}'.format(reaction.message.content),inline = False)
        embed.add_field(name = 'Channel:',value ='{}'.format(reaction.message.channel.name),inline = False)
        embed.add_field(name = 'Emoji:',value ='{}'.format(reaction.emoji),inline = False)
        await client.send_message(logchannel,  embed=embed)
        
@client.event
async def on_reaction_remove(reaction, user):
  for channel in user.server.channels:
    if channel.name == '╰☆☆-cod-log-☆☆╮':
        logchannel = channel
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Reaction Removed')
        embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
        embed.add_field(name = 'Message:',value ='{}'.format(reaction.message.content),inline = False)
        embed.add_field(name = 'Channel:',value ='{}'.format(reaction.message.channel.name),inline = False)
        embed.add_field(name = 'Emoji:',value ='{}'.format(reaction.emoji),inline = False)
        await client.send_message(logchannel,  embed=embed)
 
 
@client.event
async def on_message(message):
    user = message.author
    if message.author.bot:
      return
    if message.content.startswith('c!say'):
      return
    else:
      if message.server.id == '557572495922823179' and 'https://' in message.content:
          await client.delete_message(message)
          await client.send_message(message.channel, f'Do not post link {message.author.name}')

      if message.server.id == '557572495922823179' and ':http://' in message.content:
          await client.delete_message(message)
          await client.send_message(message.channel, f'Do not post link {message.author.name}')
             
      if 'Who is your creator <@557572697325043713>?' in message.content:
          msg = 'BX10#3762 is my creator'.format(message)
          msg2 = await client.send_message(message.channel, msg)
         
      if 'hi <@557572697325043713>' in message.content:
          msg = 'Hello {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)
         
      if 'bye <@557572697325043713>' in message.content:
          msg = 'Bye {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)

      if 'good night <@557572697325043713>' in message.content:
          msg = 'Good night {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)

      if 'Good night <@557572697325043713>' in message.content:
          msg = 'Giid night {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)

      if 'Good morning <@557572697325043713>' in message.content:
          msg = 'Good Morning {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)

      if 'good morning <@557572697325043713>' in message.content:
          msg = 'Good Morning {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)
         
      if 'Good afternoon <@557572697325043713>' in message.content:
          msg = 'Good afternoon {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)
         
      if 'good afternoon <@557572697325043713>' in message.content:
          msg = 'Good afternoon {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)
         
      if 'Bye <@557572697325043713>' in message.content:
          msg = 'Bye {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)
                 
      if 'hello <@557572697325043713>' in message.content:
          msg = 'Hello {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)
         
      if 'Hi <@557572697325043713>' in message.content:
          msg = 'Hello {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)
          
      if 'Hello <@557572697325043713>' in message.content:
          msg = 'Hello {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)
          
      if 'how are you <@557572697325043713>?' in message.content:
          msg = 'I am fine what about you? {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)
         
      if 'How are you <@557572697325043713>?' in message.content:
          msg = 'I am fine what about you? {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)
          
      if 'sup <@557572697325043713>' in message.content:
          msg = 'I am fine what about you? {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)
         
      if 'Sup <@557572697325043713>' in message.content:
          msg = 'I am fine what about you? {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)         
          
      if 'I am also fine <@557572697325043713>' in message.content:
          msg = 'Cool! {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)          
         
      if 'i am also fine <@557572697325043713>' in message.content:
          msg = 'Cool! {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)          
          
      if 'fuck' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await client.send_message(message.channel, msg)
          await client.delete_message(message)
          await asyncio.sleep(5)
          await client.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == '╰☆☆-cod-log-☆☆╮':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **fuck**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await client.send_message(channel, embed=embed)
      
      if 'FUCK' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await client.send_message(message.channel, msg)
          await client.delete_message(message)
          await asyncio.sleep(5)
          await client.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == '╰☆☆-cod-log-☆☆╮':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **FUCK**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await client.send_message(channel, embed=embed)
                
      
      if 'utiya' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await client.send_message(message.channel, msg)
          await client.delete_message(message)
          await asyncio.sleep(5)
          await client.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == '╰☆☆-cod-log-☆☆╮':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **{}**'.format(message.content),inline = False)
                embed.add_field(name = 'Type of bad word:',value ='Hindi bad word',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                await client.send_message(channel, embed=embed)
        
      if 'asshole' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await client.send_message(message.channel, msg)
          await client.delete_message(message)
          await asyncio.sleep(5)
          await client.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == '╰☆☆-cod-log-☆☆╮':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **asshole**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await client.send_message(channel, embed=embed)
        
      if 'ASSHOLE' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await client.send_message(message.channel, msg)
          await client.delete_message(message)
          await asyncio.sleep(5)
          await client.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == '╰☆☆-cod-log-☆☆╮':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **ASSHOLE**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await client.send_message(channel, embed=embed)
                
      if 'Fuck' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await client.send_message(message.channel, msg)
          await client.delete_message(message)
          await asyncio.sleep(5)
          await client.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == '╰☆☆-cod-log-☆☆╮':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **Fuck**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await client.send_message(channel, embed=embed)
        
      if 'chut' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await client.send_message(message.channel, msg)
          await client.delete_message(message)
          await asyncio.sleep(5)
          await client.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == '╰☆☆-cod-log-☆☆╮':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **chut**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='Hindi bad word',inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                await client.send_message(channel, embed=embed)
        
      if 'chod' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await client.send_message(message.channel, msg)
          await client.delete_message(message)
          await asyncio.sleep(5)
          await client.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == '╰☆☆-cod-log-☆☆╮':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **chod**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='Hindi bad word',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await client.send_message(channel, embed=embed)
        
      if 'Chod' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await client.send_message(message.channel, msg)
          await client.delete_message(message)
          await asyncio.sleep(5)
          await client.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == '╰☆☆-cod-log-☆☆╮':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **Chod**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='Hindi bad word',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await client.send_message(channel, embed=embed)
       
      if 'bsdk' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await client.send_message(message.channel, msg)
          await client.delete_message(message)
          await asyncio.sleep(5)
          await client.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == '╰☆☆-cod-log-☆☆╮':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **bsdk**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='Hindi bad word(Shortform abuse)',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await client.send_message(channel, embed=embed)
       
      if 'bhosd' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await client.send_message(message.channel, msg)
          await client.delete_message(message)
          await asyncio.sleep(5)
          await client.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == '╰☆☆-cod-log-☆☆╮':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **bhosd...**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='Hindi bad word(Short form abuse)',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await client.send_message(channel, embed=embed)
               
      if 'Bhosdi' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await client.send_message(message.channel, msg)
          await client.delete_message(message)
          await asyncio.sleep(5)
          await client.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == '╰☆☆-cod-log-☆☆╮':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **bhosd...**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='Hindi bad word(Short form abuse)',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await client.send_message(channel, embed=embed)
                
      if 'Lund' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await client.send_message(message.channel, msg)
          await client.delete_message(message)
          await asyncio.sleep(5)
          await client.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == '╰☆☆-cod-log-☆☆╮':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **bhosd...**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='Hindi bad word(Short form abuse)',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await client.send_message(channel, embed=embed)
                
      

 

client.run(os.getenv('Token'))
