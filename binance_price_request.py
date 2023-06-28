def binance_usdrate(coin, *additional_coins):
    import requests
    import json
    currency_names = [coin.upper()]
    for i in additional_coins:
        currency_names.append(i.upper())
    currency_rates = []
    for i in currency_names:
        try:
            currency_rates.append(round(float((json.loads(requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={i}USDT").text)["price"])),4))
        except:
            currency_rates.append("Not listed on Binance")
    coin_with_rate = dict(zip(currency_names, currency_rates))
    return coin_with_rate
