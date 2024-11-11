import discord
from discord.ext import commands

RECYCLABLE_ITEMS = {
    "kağıt": "Geri dönüştürülebilir.",
    "plastik şişe": "Geri dönüştürülebilir.",
    "cam şişe": "Geri dönüştürülebilir.",
    "metal kutu": "Geri dönüştürülebilir.",
    "pil": "Özel toplama alanlarına bırakılmalı.",
    "gıda atığı": "Kompost yapılabilir.",
    "plastik poşet": "Çoğu geri dönüşüm programı kabul etmiyor.",
    "ampul": "Elektronik atık olarak ayrılmalı."
}

TIPS = [
    "Muslukları kapalı tutarak su tasarrufu yapabilirsin!",
    "Geri dönüşüm kutularını evinde ayrı olarak bulundur.",
    "Enerji tasarruflu ampuller kullanarak elektrikten tasarruf et!",
    "Geri dönüştürülmüş kağıt ürünleri tercih et."
]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yapıldı.')


@bot.command(name='yardim')
async def help_command(ctx):
    help_text = (
        "!ayir [eşya] - Belirtilen eşyanın geri dönüştürülüp dönüştürülemeyeceğini söyler.\n"
        "!ipucu - Çevre dostu bir ipucu verir.\n"
    )
    await ctx.send(help_text)

# !ayir komutu - Belirtilen eşyanın geri dönüşüm durumu hakkında bilgi verir
@bot.command(name='ayir')
async def recycle_command(ctx, *, item: str):
    item = item.lower()
    if item in RECYCLABLE_ITEMS:
        response = f"{item.capitalize()}: {RECYCLABLE_ITEMS[item]}"
    else:
        response = "Bu eşyanın nasıl ayrılacağını bilmiyorum lütfen daha fazla bilgi ver."
    await ctx.send(response)


import random

@bot.command(name='ipucu')
async def tip_command(ctx):
    tip = random.choice(TIPS)
    await ctx.send(tip)

bot.run('DISCORD-TOKEN')
