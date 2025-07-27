import requests

FIRSTLEDGER_API = "https://api.firstledger.xyz/api/v1/token"

def fetch_token_symbol(currency: str, issuer: str):
    try:
        response = requests.get(f"{FIRSTLEDGER_API}/{currency}:{issuer}")
        if response.status_code == 200:
            data = response.json()
            return data.get("symbol") or data.get("currency") or currency
    except Exception as e:
        print(f"Error fetching symbol for {currency}:{issuer} - {e}")
    return currency  # fallback if no data