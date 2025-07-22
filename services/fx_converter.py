import requests

def convert_currency(amount: float, to: str):
    try:
        res = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=usd,aud,eur")
        rates = res.json().get("ripple", {})
        return { "converted": amount * rates.get(to.lower(), 1), "rate": rates.get(to.lower(), 1) }
    except:
        return {"converted": amount, "rate": 1}
