import requests

def get_wallet_nfts(address: str):
    url = f"https://api.xrpldata.com/nftwallet/{address}"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else []