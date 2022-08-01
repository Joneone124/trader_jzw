from binance.um_futures import UMFutures


def monitor(um_futures_client, cate):
    print(cate + "**************")
    flag = False
    rate = 1
    try:
        rate = float(um_futures_client.long_short_account_ratio(symbol=cate, period='15m', limit=1)[0]['longShortRatio'])
        if rate <= 0.8:
            flag = True
    except:
        print(cate + "Error skip")
    return round(rate, 2), flag, cate

# um_futures_client = UMFutures()
# rate = um_futures_client.long_short_account_ratio(symbol='BTCUSDT', period='15m', limit=1)['longShortRatio']
# print(rate)