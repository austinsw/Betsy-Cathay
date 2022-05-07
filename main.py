import discord 
import os
import json
from discord.ext import commands
client = commands.Bot(command_prefix='$', case_insensitive=True)

food_eg = {
  'id': '13512',
  'country': 'HK',
  'city': 'TST',
  'location': 'Pacific Diner, 1/F, 2-1A Pacific\'s Avenue',
  'detail': 'Pacific Diner is famous for its handmade wonton\'s noodles. In fact it\'s one of the top 10 in Hong Kong~'
}

place_eg = {
  'id': '57246',
  'country': 'HK',
  'city': 'TST',
  'location': 'Pacific Habour',
  'detail': 'Pacific Harbout has one of the best view in HK at night. Legend says if two lovers make a wish when they see a plane above them, the wish will come true!!'
}

covid_eg = {
  'id': '98210',
  'country': 'HK',
  'city': 'TST',
  'location': 'Pacific Habour',
  'detail': 'Pacific Harbout has one of the best view in HK at night. Legend says if two lovers make a wish when they see a plane above them, the wish will come true!!'
}

@client.event
async def on_ready():
  print('logged in as {client.user.name}')

@client.command()
async def active(ctx):
	await ctx.send("This is Betsy!")

@client.command()
async def tips(ctx):
  await ctx.send(f'Which country are you searching for?')

  def check(msg):
    return msg.author == ctx.author and msg.channel == ctx.channel #and \
    #msg.content.lower() in ['y','n']

  msg = await client.wait_for('message', check=check, timeout=60)
  country = msg.content
  await ctx.send(f'Which city are you searching for?')
  msg = await client.wait_for('message', check=check,timeout=60)
  city = msg.content
  await ctx.send(f'And the location details?')
  msg = await client.wait_for('message', check=check,timeout=60)
  location = msg.content

  def check2(msg):
    return msg.author == ctx.author and msg.channel == ctx.channel and \
    msg.content.lower() in ['g','s']
  
  await ctx.send(f'Are you giving (g) out suggestion or searaching (s) for info? Type g or s')
  msg = await client.wait_for('message', check=check2,timeout=60)

  def check3(msg):
      return msg.author == ctx.author and msg.channel == ctx.channel and \
      msg.content.lower() in ['c','f','p']

  if msg.content.lower() == 'g':
    
    await ctx.send(f'For reporting COVID cases, temporarily closure of the area or new measures guidlines to follow, type c\nFor recommendation food, type f\nFor providing famous/ secret places to visit, type p')

    msg = await client.wait_for('message', check=check3,timeout=60)
    if msg.content.lower() == 'c':
      await ctx.send(f'Please give the details (Things to be aware/ Time period of closure of places/ New confirmed cases of COVID):')
      msg = await client.wait_for('message', check=check,timeout=60)
      detail = msg.content

      await ctx.send(f'COVID news recorded. After verification, you will be receiving 500 Cathay Points!')
      embed=discord.Embed(title="COVID #91214",description=f"Country: {country}\nCity: {city}\nLocation: {location}\nDetail: {detail}" )
      await ctx.send(embed=embed)

    elif msg.content.lower() == 'f':

      await ctx.send(f'Details:')
      msg = await client.wait_for('message', check=check,timeout=60)
      detail = msg.content

      await ctx.send(f'Food suggestion recorded. After verification, you will be receiving 500 Cathay Points!')
      embed=discord.Embed(title="Food #12311",description=f"Country: {country}\nCity: {city}\nLocation: {location}\nDetail: {detail}" )
      await ctx.send(embed=embed)

    elif msg.content.lower() == 'p':
      
      await ctx.send(f'Details:')
      msg = await client.wait_for('message', check=check,timeout=60)
      detail = msg.content

      await ctx.send(f'Places suggestion recorded. After verification, you will be receiving 500 Cathay Points!')
      embed=discord.Embed(title="Place #56721",description=f"Country: {country}\nCity: {city}\nLocation: {location}\nDetail: {detail}" )
      await ctx.send(embed=embed)

    else:
      await ctx.send('Wrong input...')


  elif msg.content.lower() == 's':
    
    await ctx.send(f'For searching COVID news, type c\nFor searching food, type f\nFor searching secret attractions, type p')

    msg = await client.wait_for('message', check=check3,timeout=60)
    if msg.content.lower() == 'c':
      embed=discord.Embed(title='COVID #'+ covid_eg['id'],description=f"Country: "+ covid_eg['country'] +"\nCity: "+ covid_eg['city'] +"\nLocation: "+ covid_eg['location'] +"\nDetail: "+ covid_eg['detail'] )
      await ctx.send(embed=embed)

    elif msg.content.lower() == 'f':
      embed=discord.Embed(title='Food #'+ food_eg['id'],description=f"Country: "+ food_eg['country'] +"\nCity: "+ food_eg['city']+"\nLocation: "+ food_eg['location'] +"\nDetail: "+ food_eg['detail'] )
      await ctx.send(embed=embed)

    elif msg.content.lower() == 'p':
      embed=discord.Embed(title='Place #'+ place_eg['id'],description=f"Country: "+ place_eg['country'] +"\nCity: "+ place_eg[city] +"\nLocation: "+ place_eg['location'] +"\nDetail: "+ place_eg['detail'] )
      await ctx.send(embed=embed)

  else:
    await ctx.send('Wrong input...')

@client.command()
async def report(ctx, case):
  await ctx.send(f'Please give more details for reporting')

  def check(msg):
    return msg.author == ctx.author and msg.channel == ctx.channel #and \
    #msg.content.lower() in ['y','n']

  msg = await client.wait_for('message', check=check, timeout=60)
  detail = msg.content
  await ctx.send(f'Your report for #{case} has been submitted. 500 Cathay Points will be rewarded to you after verification.')

client.run(os.environ['TOKEN'])