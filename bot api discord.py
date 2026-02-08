import random
import discord
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')

def duck():
    return requests.get("https://random-d.uk/api/random").json()["url"]

def dog():
    return requests.get("https://random.dog/woof.json").json()["url"]

def fox():
    return requests.get("https://randomfox.ca/floof/").json()["image"]

def pikachu():
    return requests.get("https://pokeapi.co/api/v2/pokemon/pikachu").json()["sprites"]["front_default"]

def tokio():
    return requests.get("https://kitsu.io/api/edge/anime?filter[text]=tokyo").json()["data"][0]["attributes"]["posterImage"]["original"]

def propio():
    return "https://i.ibb.co/twjqnC2n/archivo.gif"

def get_meme_categoria(categoria):
    memes = {
        "animales": [
            {"func": duck, "peso": 40},
            {"func": dog, "peso": 40},
            {"func": fox, "peso": 20}
        ],
        "anime": [
            {"func": pikachu, "peso": 50},
            {"func": tokio, "peso": 30},
            {"func": propio, "peso": 20}
        ]
    }

    if categoria not in memes:
        return None

    elegido = random.choices(
        memes[categoria],
        weights=[m["peso"] for m in memes[categoria]],
        k=1
    )[0]

    return elegido["func"]()

@bot.command()
async def meme(ctx, categoria: str):
    image_url = get_meme_categoria(categoria.lower())

    if image_url is None:
        await ctx.send("❌ Categoría no válida. Usa: animales o anime")
        return

    await ctx.send(image_url)

bot.run("TOKEN")
