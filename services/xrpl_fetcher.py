import requests
from services.token_metadata import fetch_token_symbol  # ✅ Add this line

def get_wallet_tokens(address: str):
    url = f"https://api.xrpscan.com/api/v1/account/{address}/balances"
    response = requests.get(url)
    if response.status_code != 200:
        return {"error": "Failed to fetch balances"}

    tokens = response.json()

    # ✅ Enrich tokens with symbol data
    for token in tokens:
        if token.get("currency") != "XRP":
            token["symbol"] = fetch_token_symbol(token["currency"], token.get("counterparty", ""))
        else:
            token["symbol"] = "XRP"

    return {
        "address": address,
        "tokens": tokens
    }
