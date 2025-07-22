def calculate_pnl(data: dict):
    results = []
    for token in data.get("tokens", []):
        try:
            amount = float(token["amount"])
            buy_price = float(token["buy_price"])
            price = float(token["price_usd"])
            results.append({
                "currency": token["currency"],
                "issuer": token["issuer"],
                "amount": amount,
                "buy_price": buy_price,
                "price_usd": price,
                "profit_loss": (price - buy_price) * amount,
                "percent_change": ((price - buy_price) / buy_price) * 100
            })
        except:
            continue
    return {"pnl": results}
