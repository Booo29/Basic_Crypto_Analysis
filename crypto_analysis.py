import requests
import json
import time

def get_crypto_data(crypto_ids):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(crypto_ids)}&vs_currencies=usd&include_24hr_change=true"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print ("Error: ", "Failed to fetch crypto data")
        return None
    
def analyze_crypto_data(data):
    analysis = {}
    for crypto, stats in data.items():
        current_price = stats['usd']
        price_change = stats.get('usd_24h_change', 0)
        analysis[crypto] = {
            'current_price': current_price,
            'price_change_24': price_change,
            'price_trend': 'up' if price_change > 0 else 'down'
        }
    return analysis

def write_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    crypto_ids = ['bitcoin', 'ethereum', 'dogecoin']
    data = get_crypto_data(crypto_ids)
    if data:
        write_data('crypto_data.json', data)
        print ("Data written to crypto_data.json")
        time.sleep(30)
        analysis = analyze_crypto_data(data)
        write_data('crypto_analysis.json', analysis)
        print ("Analysis written to crypto_analysis.json")
    else:
        print ("Failed to fetch crypto data")
    