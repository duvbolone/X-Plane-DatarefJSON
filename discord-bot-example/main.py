import discord#py-cord
import json
from discord import option

bot = discord.Bot(intents=discord.Intents.default())

errorc = 0xFF0000#Embed colour for when an error occurs(e.g: dataref not found)
embedc = 0x00FF00#Default embed colour

jsonpath = "defaultDatarefs.json"#Change the path of where the json file is located here

@bot.listen()
async def on_ready():
    print("I'm ready for usage!")

#for autocomplete
async def get_datarefs(ctx: discord.AutocompleteContext):
    global datarefList
    with open(jsonpath) as f:
        datarefLoad = json.load(f)
        datarefList = list(datarefLoad["datarefs"].keys())
    return [dataref for dataref in datarefList if ctx.value in dataref]

#command itself
@bot.command(name="search", description="Find a dataref.")
@option("dataref", description="The dataref you want information about.", autocomplete=get_datarefs)
async def datarefs(ctx, dataref):
    await ctx.defer()#Tell discord to wait a bit(prevents 'Application did not respond' from happening
    if dataref in datarefList:
        with open(jsonpath, "r") as f:
            datarefJson = json.load(f)
        datarefs = datarefJson["datarefs"]
        #Adapt output to type of dataref(older datarefs seem to not have a description)
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
        await ctx.respond(embed=embed)

bot.run('TOKEN')#Change 'TOKEN' to the token of your bot
