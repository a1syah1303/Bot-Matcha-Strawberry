from config import token
# This example requires the 'message_content' intent.
from discord.ext import commands
import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(client.command_prefix):
        await client.process_commands(message)
    else:
        await message.channel.send(message.content)

@client.command()
async def about(ctx):
    await ctx.send("Ini adalah echo-bot yang dibuat dengan pustaka discord.py!")

@client.command()
async def hello(ctx):
    await ctx.send(f"Halo, {ctx.author.display_name}!")

import random

@client.command()
async def choose(ctx, *, pilihan):
    daftar_pilihan = pilihan.split(",")
    hasil = random.choice(daftar_pilihan)
    await ctx.send(f"Pilihannya: {hasil.strip()}")

class Car:
    def __init__(self, warna, merek):
        self.warna = warna
        self.merek = merek

    def info(self):
        return f"Warna mobil: {self.warna}, merek mobil: {self.merek}"


@client.command()
async def car(ctx, warna, merek):
    mobil = Car(warna, merek)
    await ctx.send(mobil.info())

@client.command()
async def info(ctx):
    await ctx.send('Daftar perintah \n 1. /about - menampilkan informasi bot\n 2. /hello - menyapa pengguna\n 3. /choose - memilih secara acak dari beberapa pilihan\n 4. /car warna merek - menampilkan informasi mobil\n 5. /info - menampilkan daftar perintah')

client.run(token)
