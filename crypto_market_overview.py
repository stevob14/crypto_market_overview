import requests 
imports json

def dec_format(value):
    try:
        change = "{0:.2f}".format(float(value))
    except(TypeError):
        change = "N/A"
    return change

def comma_format(value):
    try:
        change = "{:,}".format(float(value))
    except(TypeError, ValueError):
        change = "N/A"
    return change

def cg_global_api():
    api = "https://api.coingecko.com/api/v3/global"
    try:
        raw_data = requests.get(api,timeout=10).json()
        data = raw_data['data']
        return data
    except requests.exceptions.RequestException:
        return False
    except (IndexError, KeyError, TypeError, ValueError):
        return False
        
data = cg_global_api()
output = ""
if data:
    try:
        total_market_cap = comma_format(dec_format(data['total_market_cap']['usd']))
        total_volume = comma_format(dec_format(data['total_volume']['usd']))
        btc_dominance = dec_format(data['market_cap_percentage']['btc'])
        eth_dominance = dec_format(data['market_cap_percentage']['eth'])
        market_cap_change = dec_format(data['market_cap_change_percentage_24h_usd'])
        crypto_overview = [total_market_cap, total_volume, btc_dominance, market_cap_change,eth_dominance]
    except (IndexError, KeyError, TypeError, ValueError):
        pass
else:
    crypto_overview = "There was an error retrieving data from the api :/ Try refreshing the page.<br>"

with open('crypto_market_overview.txt','w') as outfile:
    json.dump(crypto_overview,outfile)
