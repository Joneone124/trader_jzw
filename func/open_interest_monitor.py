from binance.um_futures import UMFutures

def monitor(um_futures_client, cate):
    print(cate + "**************")
    flag = False
    rate = 0.0001
    try:
        response_2h = um_futures_client.open_interest_hist(cate, "2h", **{"limit": 8})
        response_15m = um_futures_client.open_interest_hist(cate, "15m", **{"limit": 1})
        print(response_2h)
        print(response_15m)

        data_1h_list = []
        for i in response_2h:
            data_1h_list.append(float(i['sumOpenInterestValue']))

        data_1h_avg = sum(data_1h_list)/len(data_1h_list)
        data_15m_value = float(response_15m[0]['sumOpenInterestValue'])

        rate = (data_15m_value - data_1h_avg) / data_1h_avg

        if abs(rate) > 0.05:
            flag = True
    except:
        print(cate + "Error skip")
    return rate, flag, cate

