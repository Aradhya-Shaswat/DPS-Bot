import os
import discord
from discord.ext import commands
import time
import requests
from server import server

client = commands.Bot(command_prefix=".")

client.remove_command('help')

@client.event
async def on_ready():
  print("Started.")

@client.command()
async def help(ctx):
  embed=discord.Embed(title="Help", description="List of Available Commands:", color=0x0062ff)
  embed.add_field(name=".help", value="Shows This Command", inline=True)
  embed.add_field(name=".dashboard", value="Shows the Dashboard", inline=True)
  embed.add_field(name=".pfp {mention}", value="Gets The Profile Pic of a member", inline=True)
  embed.add_field(name=".sqrt", value="Square Root of a Number (Maths)", inline=True)
  embed.add_field(name=".maths", value="Opens a Calculator That Can do Basic Tasks", inline=True)
  embed.add_field(name=".ping", value="Check if Website is Online", inline=True)

  embed.set_thumbnail(url="https://web.whatsapp.com/pp?e=https%3A%2F%2Fpps.whatsapp.net%2Fv%2Ft61.24694-24%2F118541759_336528124467813_5955226882728274624_n.jpg%3Fccb%3D11-4%26oh%3D01_AVy6RDBRDJ1xlTnyYSddru47OW4g0YXHi2xH_zVqTP2PNQ%26oe%3D62389804&t=l&u=918521083557-1596094665%40g.us&i=1601475407&n=619NyK%2FXIrzyJ27r3gQtaiLY3t2elRT6GTQdROtBBtU%3D")
  await ctx.send(embed=embed)

@client.command()
async def sqrt(ctx, number):
    squared_value = int(number) * int(number)
    await ctx.send(str(number) + " squared is " + str(squared_value))

@client.command()
async def maths(ctx):
    def check(m):
        return len(m.content) >= 1 and m.author != client.user

    await ctx.send("First Number: ")
    number_1 = await client.wait_for("message", check=check)
    await ctx.send("Operator: ")
    operator = await client.wait_for("message", check=check)
    await ctx.send("Second Number: ")
    number_2 = await client.wait_for("message", check=check)
    try:
        number_1 = float(number_1.content)
        operator = operator.content
        number_2 = float(number_2.content)
    except:
        await ctx.send("Invalid Input :rolling_eyes:")
        return
    output = None
    if operator == "+":
        output = number_1 + number_2
    elif operator == "-":
        output = number_1 - number_2
    elif operator == "/":
        output = number_1 / number_2
    elif operator == "*":
        output = number_1 * number_2
    else:
        await ctx.send("invalid input")
        return
    await ctx.send("Answer: " + str(output))

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.message.delete()

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")

@client.command()
async def dashboard(ctx):
  await ctx.send("https://dpspatna.edunexttech.com/Index\nLogin Using Your Admission No. and Password.")

@client.command(aliases = ["pfp", "pfp_pic"])
async def profile_pic(ctx, member: discord.User):
    if member == None:
        member == ctx.author

    embed = discord.Embed(title = f"Profile Picture of {member.display_name}", color = member.color)
    embed.set_image(url = member.avatar_url)
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Asked by {ctx.author.name}#{ctx.author.discriminator}")
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
  url = "https://dpspatna.edunexttech.com/Index"
  page = requests.get(url)
  if page.status_code == 200:
    await ctx.send("``Dashboard - DPS Patna`` is Online. Code 200")
  else:
    await ctx.send("``Dashboard - DPS Patna`` is Offline. Code ``SSLError(SSLCertVerificationError)``")

@client.command()
async def info(message):
    if message.author.id == 811966926208237618:
      await message.send(file=discord.File('aradhyashaswat.png'))
    elif message.author.id == 748445042879758366:
      await message.send(file=discord.File('atulprakash.png'))
    elif message.author.id == 742403639666016387:
      await message.send(file=discord.File('yatharthranjan.png'))
    else:
      await message.send("``You are Not in DPS Patna Class 8-I``. If you are in the Class, **DM ``hi#0069``**")


server()
my_secret = os.environ['token']
client.run(my_secret)

