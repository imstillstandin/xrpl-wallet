import requests

def get_token_price(currency: str, issuer: str):
    try:
        response = requests.get(f"https://api.xpmarket.com/api/v1/token/{currency}:{issuer}")
        return response.json().get("price", {}).get("USD")
    except:
        return None