import requests

def get_wallet_tokens(address: str):
    url = f"https://api.xrpscan.com/api/v1/account/{address}/balances"
    response = requests.get(url)
    if response.status_code != 200:
        return {"error": "Failed to fetch balances"}
    return {"address": address, "tokens": response.json()}