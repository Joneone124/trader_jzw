import time

from binance.um_futures import UMFutures

from func.open_interest_little_monitor import monitor
from func.wecaht_little import alert

last_list = []

while True:
    try:

        file = open('data/list_little.txt', 'r')
        content = file.readlines()
        print(content)

        file.close()
        cate_list = map(lambda x: x[0:-1], content)

        um_futures_client = UMFutures()

        alert_dic = {}
        for i in cate_list:
            rate, flag, cate = monitor(um_futures_client, i)
            print(cate + "   " + str(flag) + "   " + str(rate))
            if flag:
                alert_dic[cate] = rate
            time.sleep(0.4)


        sort_list = sorted(alert_dic.items(), key=lambda item: item[1], reverse=True)

        alert_cate = []
        alert_rate = []
        for i in sort_list:
            alert_cate.append(i[0])
            alert_rate.append(str(round(i[1]*100, 2)) + "%")

        print(alert_cate)
        print(alert_rate)
        print(len(alert_cate))
        print(len(alert_rate))

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
            alert(alert_cate_final, alert_rate)

        time.sleep(600)



    except:
        time.sleep(10)

