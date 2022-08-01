from binance.um_futures import UMFutures

def monitor(um_futures_client, cate):
    print(cate + "**************")
    flag = False
    rate = 0.0001
    try:
        response_1h = um_futures_client.open_interest_hist(cate, "1h", **{"limit": 12})
        response_5m = um_futures_client.open_interest_hist(cate, "5m", **{"limit": 1})
        print(response_1h)
        print(response_5m)

        data_1h_list = []
        for i in response_1h:
            data_1h_list.append(float(i['sumOpenInterestValue']))

        data_1h_avg = sum(data_1h_list)/len(data_1h_list)
        data_5m_value = float(response_5m[0]['sumOpenInterestValue'])

        rate = (data_5m_value - data_1h_avg) / data_1h_avg

        if abs(rate) > 0.05:
            flag = True
    except:
        print(cate + "Error skip")
    return rate, flag, cate

