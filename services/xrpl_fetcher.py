import requests
from services.token_metadata import fetch_token_symbol  # 

def enrich_token_data(token):
    currency = token.get("currency")
    issuer = token.get("counterparty")

    # Skip XRP
    if currency == "XRP" or issuer is None:
        token["symbol"] = currency
        token["logo"] = None
        return token

    try:
        fl_url = f"https://api.firstledger.io/v1/tokens/{currency}:{issuer}"
        fl_response = requests.get(fl_url)
        if fl_response.status_code == 200:
            fl_data = fl_response.json()
            token["symbol"] = fl_data.get("symbol", currency)
            token["logo"] = fl_data.get("logo_url")
        else:
            token["symbol"] = currency
            token["logo"] = None
    except Exception:
        token["symbol"] = currency
        token["logo"] = None

    return token

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
    "tokens": [enrich_token_data(token) for token in response.json()]
}