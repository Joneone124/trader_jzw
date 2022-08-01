from binance.um_futures import UMFutures

um_futures_client = UMFutures()



base_24 = um_futures_client.ticker_24hr_price_change("BTCUSDT")['weightedAvgPrice']
x = um_futures_client.klines("BTCUSDT", "15m")
print(s)
print(x)
print(len(x))