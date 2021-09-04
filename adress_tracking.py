import json, requests

#API Key Etherscan
api_key = 'put_the_key'

#ETH Adress 
adress = 'put_the_adress'

#URL Ethscan Api
url = "http://api.etherscan.io/api?module=account&action=txlist&address={}&startblock=0&endblock=99999999&page=1&offset=1&sort=desc&apikey="+api_key

#variable value: list last transactions each second 
value = []
print('Bot starting...')

while True:
    
    #Get Datas and the amount of the last transaction 
    data = requests.get(url.format(adress)).json().get("result")
    if len(data)>0:
        last_transaction_value = int(data[0].get("value"))/(10**18)
        value.append(float(last_transaction_value))
    else:
        continue
    
    #Get the last the "adress" and "to" adress 
    if len(value)>1:
        if value[-1] != value[-2] : 
            last_transaction_from = data[0].get("from")
            last_transaction_to = data[0].get("to")

            #Print Alerte 
            print(f"Alerte Nouvelle Transaction\n\
From: {last_transaction_from}\n\
ETH amount: {last_transaction_value}\n\
To: {last_transaction_to}\n")
