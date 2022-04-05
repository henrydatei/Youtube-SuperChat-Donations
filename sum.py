from sys import api_version
import requests
from chat_downloader import ChatDownloader

apiKey = "apiKey"
url = 'https://www.youtube.com/watch?v=TjsqR-JMTAI'

def convertCurrencyToUSD(amount, symbol):
    if symbol == "USD":
        return amount
    else:
        params = {"access_key": apiKey, "format": 1}
        r = requests.get("http://api.currencylayer.com/live", params = params)
        r.raise_for_status()
        data = r.json()["quotes"]
        conversionRate = data["USD" + symbol]
        return amount / conversionRate

chat = ChatDownloader().get_chat(url, message_groups=['superchat'])
sum = 0
for message in chat:
    try:
        amount = message["money"]["amount"]
        symbol = message["money"]["currency"]
        print(amount, symbol)
        sum = sum + convertCurrencyToUSD(amount, symbol)
    except:
        pass

print("Sum: " + str(sum) + " USD")