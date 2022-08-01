from binance.um_futures import UMFutures


def monitor(um_futures_client, cate):
    print(cate + "**************")
    flag = False
    rate = 0.0001
    try:
        rate = float(um_futures_client.mark_price(cate)['lastFundingRate']) * 100
        if rate <= -0.05:
            flag = True
    except:
        print(cate + "Error skip")
    return rate, flag, cate

# um_futures_client = UMFutures()
# rate = um_futures_client.mark_price('BTCUSDT')['lastFundingRate']
# print(rate)