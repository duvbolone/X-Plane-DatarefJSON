import discord
import json
from discord import option

bot = discord.Bot(intents=discord.Intents.default())

errorc = 0xFF0000
embedc = 0x00FF00

@bot.listen()
async def on_ready():
    print("I'm ready for usage!")


async def get_datarefs(ctx: discord.AutocompleteContext):
    global datarefList
    with open("dev/aircraft/defaultDatarefs.json") as f:
        datarefLoad = json.load(f)
        datarefList = list(datarefLoad["datarefs"].keys())
    return [dataref for dataref in datarefList if ctx.value in dataref]


@bot.command(name="search", description="Find a dataref.")
@option("dataref", description="The dataref you want information about.", autocomplete=get_datarefs)
async def datarefs(ctx, dataref):
    await ctx.defer()
    if dataref in datarefList:
        with open("dev/aircraft/defaultDatarefs.json", "r") as f:
            datarefJson = json.load(f)
        datarefs = datarefJson["datarefs"]
        if len(list(datarefs[dataref].keys())) == 5:
            embed = discord.Embed(title=f"Found this information for the provided dataref:", colour=embedc)
            embed.add_field(name="Dataref Information:", value=f"""
Path : `{datarefs[dataref]["path"]}`
Type : **{datarefs[dataref]["type"]}**
Writable : **{datarefs[dataref]["writable"]}**
Unit : **{datarefs[dataref]["unit"]}**
Description :

> {datarefs[dataref]["description"]}
                    """)
            if len(list(datarefs[dataref].keys())) == 4:
                        embed = discord.Embed(title=f"Found this information for the provided dataref:", colour=embedc)
                        embed.add_field(name="Dataref Information:", value=f"""
Path : `{datarefs[dataref]["path"]}`
Type : **{datarefs[dataref]["type"]}**
Writable : **{datarefs[dataref]["writable"]}**
Unit : **{datarefs[dataref]["unit"]}**
                    """)
            if len(list(datarefs[dataref].keys())) == 3:
                        embed = discord.Embed(title=f"Found this information for the provided dataref:", colour=embedc)
                        embed.add_field(name="Dataref Information:", value=f"""
Path : `{datarefs[dataref]["path"]}`
Type : **{datarefs[dataref]["type"]}**
Writable : **{datarefs[dataref]["writable"]}**
                    """)
            if len(list(datarefs[dataref].keys())) == 2:
                        embed = discord.Embed(title=f"Found this information for the provided dataref:", colour=embedc)
                        embed.add_field(name="Dataref Information:", value=f"""
Path : `{datarefs[dataref]["path"]}`
Type : **{datarefs[dataref]["type"]}**
                    """)
            await ctx.respond(embed=embed)
    else:
                embed = discord.Embed(title="Error 404!", description=f"Didn't found the dataref `{dataref}`", colour=errorc)

bot.run('TOKEN')
