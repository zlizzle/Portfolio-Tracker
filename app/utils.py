import requests

def fetch_token_price(symbol: str):
    
    coingecko_ids = {
        "BTC": "bitcoin",
        "ETH": "ethereum",
        "SOL": "solana",
        
    }
    token_id = coingecko_ids.get(symbol.upper())
    if not token_id:
        return None

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={token_id}&vs_currencies=usd"
    resp = requests.get(url)
    if resp.status_code != 200:
        return None
    data = resp.json()
    return data.get(token_id, {}).get("usd")
