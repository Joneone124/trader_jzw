import time

from binance.um_futures import UMFutures

from func.open_interest_monitor import monitor as open_monitor
from func.long_short_rate_monitor import monitor as long_monitor
from func.wecaht_open_long import alert

last_list = []

while True:

    try:

        file = open('data/list.txt', 'r')
        content = file.readlines()
        print(content)

        file.close()
        cate_list = map(lambda x: x[8:-1], content)
        um_futures_client = UMFutures()

        alert_dic_1 = {}
        for i in cate_list:
            rate, flag, cate = open_monitor(um_futures_client, i)
            print(cate + "   " + str(flag) + "   " + str(rate))
            if flag:
                alert_dic_1[cate] = rate
            time.sleep(0.1)


        sort_list_1 = sorted(alert_dic_1.items(), key=lambda item: item[1], reverse=True)

        alert_cate_1 = []
        alert_rate_1 = []
        for i in sort_list_1:
            alert_cate_1.append(i[0])
            alert_rate_1.append(str(round(i[1]*100, 2)) + "%")

        cate_list = map(lambda x: x[8:-1], content)
        alert_dic_2 = {}
        for i in cate_list:
            rate, flag, cate = long_monitor(um_futures_client, i)
            print(cate + "   " + str(flag) + "   " + str(rate))
            if flag:
                alert_dic_2[cate] = rate
            time.sleep(0.4)

        sort_list_2 = sorted(alert_dic_2.items(), key=lambda item: item[1], reverse=False)

        alert_cate_2 = []
        alert_rate_2 = []
        for i in sort_list_2:
            alert_cate_2.append(i[0])
            alert_rate_2.append(str(round(i[1], 2)))


        alert_cate = []
        alert_rate_open = []
        alert_rate_long = []
        for i in alert_cate_1:
            if i in alert_cate_2:
                alert_cate.append(i)
                alert_rate_open.append(alert_rate_1[alert_cate.index(i)])
                alert_rate_long.append(alert_rate_2[alert_cate.index(i)])

        print(alert_cate)
        print(alert_rate_open)
        print(alert_rate_long)
        print(len(alert_cate))
        print(len(alert_rate_open))
        print(len(alert_rate_long))

        alert_cate_final = []
        for i in alert_cate:
            if i in last_list:
                alert_cate_final.append(i)
            else:
                alert_cate_final.append(i + "  *")

        last_list = alert_cate

        if len(alert_cate) == 0:
            pass
        else:
            alert(alert_cate_final, alert_rate_open, alert_rate_long)
        time.sleep(600)

    except:
        time.sleep(10)


