import requests

COINGECKO_IDS= {
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "SOL": "solana",
    "HYPE": "hyperliquid",
    "PEPE": "pepecoin",
    "WIF": "dogwifhat"
}

def fetch_token_price(symbol: str):
    token_id = COINGECKO_IDS.get(symbol.upper())
    if not token_id:
        return None

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={token_id}&vs_currencies=usd"
    resp = requests.get(url)
    if resp.status_code != 200:
        return None
    data = resp.json()
    return data.get(token_id, {}).get("usd")
