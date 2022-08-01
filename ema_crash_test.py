import time

from binance.um_futures import UMFutures

from func.ema_crash import monitor
from func.wechat_ema_crash import alert

last_list = []

while True:

    try:

        file = open('data/list.txt', 'r')
        content = file.readlines()
        print(content)

        file.close()
        cate_list = map(lambda x: x[8:-1], content)
        um_futures_client = UMFutures()

        alert_dic = []
        for i in cate_list:
            rate, flag, cate, up_rate = monitor(um_futures_client, i)
            print(cate + "   " + str(flag) + "   " + str(rate) + "   " + str(round(up_rate*100, 3))+"%")
            if flag:
                # alert_dic[cate] = rate
                alert_dic.append([cate, rate, up_rate])
            time.sleep(0.1)

        print(str(alert_dic) + "!!!!!!!!!!!!!!")

        alert_dic.sort(key=lambda x: float(x[1]))
        sort_list =alert_dic
        print(str(sort_list) + "@@@@@@@@@@@@@@@@@")

        # sorted(alert_dic.items(), key=lambda item: item[1], reverse=False)

        alert_cate = []
        alert_rate = []
        alert_up_rate = []

        for i in sort_list:
            alert_cate.append(i[0])
            alert_rate.append(str(i[1]))
            alert_up_rate.append(str(round(i[2]*100, 3)) + "%")

        alert_cate = alert_cate[3: 23]
        alert_rate = alert_rate[3: 23]
        alert_up_rate = alert_up_rate[3:23]

        print(str(alert_up_rate) + "&&&&&&&&&&&&&&&&&&&&&&&&&&&")




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
            alert(alert_cate_final, alert_rate, alert_up_rate)
        time.sleep(600)

    except:
        time.sleep(10)

