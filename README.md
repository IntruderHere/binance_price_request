# binance_price_request
This function takes the token name (one or more) and returns the price in USD from Binance.

Use cases:

binance_usdrate("ETH")
returns: {'ETH': 1851.92}

binance_usdrate("ETH", "BTC", "BNB", "XRP")
returns: {'ETH': 1854.2, 'BTC': 30242.75, 'BNB': 231.4, 'XRP': 0.4735}

binance_usdrate("ETH", "StrangeCoin")
returns: {'ETH': 1855.0, 'STRANGECOIN': 'Not listed on Binance'}
