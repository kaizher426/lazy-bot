#pip3 uninstall googletrans
#pip3 install googletrans==3.1.0a0
import os
import googletrans
from discord.ext.commands import Bot
import math
import random

bot = Bot(command_prefix='!')
translator = googletrans.Translator()
link = "https://www.youtube.com/watch?v=xvFZjo5PgG0"

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event 
async def on_message(message):

      msg = message.content[3:]
      message_destination = translator.detect(msg).lang

      if message.author == bot.user:
        return

      if message.content.lower().startswith("!c "):
        if message_destination == "en":
            translated_message = translator.translate(msg, dest="zh-CN")  
            await message.channel.send(f"`{msg}` -> `{translated_message.text}`")
        else:
          translated_message = translator.translate(msg)
          await message.channel.send(f"`{msg}` -> `{translated_message.text}`")

      if message.content.lower().startswith("!m "):
        if message_destination == "en":
            translated_message = translator.translate(msg, dest="ms")
            await message.channel.send(f"`{msg}` -> `{translated_message.text}`")
        else:
          translated_message = translator.translate(msg)
          await message.channel.send(f"`{msg}` -> `{translated_message.text}`")

      if message.content.lower().startswith("!s "):
        if message_destination == "en":
            translated_message = translator.translate(msg, dest="es")
            await message.channel.send(f"`{msg}` -> `{translated_message.text}`") 
        else:
          translated_message = translator.translate(msg)
          await message.channel.send(f"`{msg}` -> `{translated_message.text}`")

      if message.content.lower().startswith("!h "):
        if message_destination == "en":
            translated_message = translator.translate(msg, dest="hi")
            await message.channel.send(f"`{msg}` -> `{translated_message.text}`")   
        else:
          translated_message = translator.translate(msg)
          await message.channel.send(f"`{msg}` -> `{translated_message.text}`")
      await bot.process_commands(message)

@bot.command(name="calc")
async def calc(ctx):
        def check(m):
          return len(m.content) >= 1 and m.author != bot.user

        await ctx.send("Number 1: ")
        number_1 = await bot.wait_for("message", check=check)
        await ctx.send("Operator: ")
        operator = await bot.wait_for("message", check=check)
        await ctx.send("number 2: ")
        number_2 = await bot.wait_for("message", check=check)
        try:
            number_1 = float(number_1.content)
            operator = operator.content
            number_2 = float(number_2.content)
        except:
            await ctx.send("invalid input")
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

        elif operator == "sin":
            output = math.sin(number_1) + math.sin(number_2)

        elif operator == "cos":
            output = math.cos(number_1) + math.cos(number_2)

        elif operator == "tanh":
            output = math.tan(number_1) + math.tan(number_2)

        elif operator == "log":
            output = math.log(number_1) + math.log(number_2)

        else:
            await ctx.send("invalid input")
            return

        await ctx.channel.send("Answer: " + str(output))   

@bot.command(name='Force')
async def force(ctx):
        mass = random.randint(0, 442)
        acceleration = random.randint(0, 1000)
        force = mass * acceleration
        
        await ctx.channel.send(f"You are running at {acceleration} m/s. This is your fat: {mass} KG.This is your force: {force} N. I will convince you to run slower, be lazy, is ok. If you wan to calm down, go to : <{link}>")

@bot.command(name='KE')
async def kinetic_energy(ctx):
        velocity_squared = (random.randint(0, 10000))**2
        mass = random.randint(0, 442)
        KE = (mass * velocity_squared)/2
        await ctx.channel.send(f"This is your fat: {mass} KG. You run {velocity_squared} meter per sencond square. Your Kinetic energy: {KE} J. If you wan to calm down, go to : <{link}>")

@bot.command(name="E")
async def energy(ctx):
        mass = random.randint(0, 442)
        light_speed = 8.98755179 * 10 ** 16
        most_famous_equation = mass * light_speed
        await ctx.channel.send(f"Einstein help me calculate: {most_famous_equation} J. If you wan to calm down, go to : <{link}>")

bot.run(os.getenv('TOKEN'))
