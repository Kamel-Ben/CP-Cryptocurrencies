import discord, config, time, requests
from discord.embeds import Embed
from discord.ext import tasks

client = discord.Client()
adresses = ['0xb218C5D6aF1F979aC42BC68d98A5A0D796C6aB01']
names = ["whale"]
value = [[] for _ in range(len(adresses))]

@tasks.loop(seconds = 1)
async def test():
    channel = client.get_channel(process.env.CHANNEL) #put channel number here 
    while True:
        for position, (adress, name) in enumerate(zip(adresses,names)): 
            url = f"https://api.bscscan.com/api?module=account&action=txlist&address={adress}&startblock=0&endblock=99999999&page=1&offset=1&sort=desc&apikey={process.env.API_KEY}"
            data = requests.get(url.format(adress)).json().get("result")

            time.sleep(1)
            if len(data)>0:
                last_transaction_value = int(data[0].get("value"))/(10**18)
                value[position].append(float(last_transaction_value))
            else:
                continue

            if len(value[position])>1:
                if value[position][-1] != value[position][-2] :
                    last_transaction_from = data[0].get("from")
                    last_transaction_to = data[0].get("to")
                    await channel.send(f"**Alerte - Nouvelle Transaction**\n\n\
**Name**: {name}\n\
**From**: {last_transaction_from}\n\
**BNB amount**: {last_transaction_value}\n\
**To**: {last_transaction_to}\n\
**Link**: <https://bscscan.com/address/{adress}>")

@client.event
async def on_ready():
    print("Le bot est prêt")
    test.start()

client.run(process.env.TOKEN) #run method - BOT'S TOKEN 

