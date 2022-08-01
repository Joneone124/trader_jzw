import time

from binance.um_futures import UMFutures

from func.long_short_rate_monitor import monitor
from func.wechat_long_short_rate import alert



while True:

    file = open('data/list.txt', 'r')
    content = file.readlines()
    print(content)

    file.close()
    cate_list = map(lambda x: x[8:-1], content)
    um_futures_client = UMFutures()

    alert_dic = {}
    for i in cate_list:
        rate, flag, cate = monitor(um_futures_client, i)
        print(cate + "   " + str(flag) + "   " + str(rate))
        if flag:
            alert_dic[cate] = rate
        time.sleep(0.1)


    sort_list = sorted(alert_dic.items(), key=lambda item: item[1], reverse=False)

    alert_cate = []
    alert_rate = []
    for i in sort_list:
        alert_cate.append(i[0])
        alert_rate.append(str(round(i[1], 2)))

    print(alert_cate)
    print(alert_rate)
    print(len(alert_cate))
    print(len(alert_rate))

    if len(alert_cate) == 0:
        pass
    else:
        alert(alert_cate, alert_rate)
    time.sleep(600)

