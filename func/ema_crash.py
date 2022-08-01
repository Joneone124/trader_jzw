import time
import numpy as np
from binance.um_futures import UMFutures
import pandas as pd

def monitor(um_futures_client, cate):

    kline = um_futures_client.klines(symbol=cate, interval="15m")
    kline_3 = um_futures_client.klines(symbol=cate, interval="3m")

    close_prise = []

    close_prise_3 = []

    for i in kline:
        close_prise.append(i[4])

    close_prise = np.array(close_prise)

    for i in kline_3:
        close_prise_3.append(i[4])

    close_prise_3 = np.array(close_prise_3)
    # print(close_prise)

    def EMA(arr,period=21):
        df = pd.DataFrame(arr)
        return df.ewm(span=period,min_periods=period).mean()


    ema_21_list = EMA(close_prise, 21)[-17:-1].values.tolist() #取前4小时的15分钟ema线
    ema_55_list = EMA(close_prise, 55)[-17:-1].values.tolist()
    ema_144_list = EMA(close_prise, 144)[-17:-1].values.tolist()


    ema_3_3_list = EMA(close_prise_3, 3)[-4:-1].values.tolist() #三根三分钟均线
    ema_3_3_avg = (ema_3_3_list[0][0] + ema_3_3_list[1][0] + ema_3_3_list[2][0]) / 3


    # print(ema_21_list)
    # print(ema_55_list)
    # print(ema_144_list)
    dis_21_144 = 0
    dis_55_144 = 0
    sum_ema_21 = 0
    for i in range(len(ema_144_list)):
        dis_21_144 = dis_21_144 + (ema_21_list[i][0]-ema_144_list[i][0])/ema_144_list[i][0]
        dis_55_144 = dis_55_144 + (ema_55_list[i][0]-ema_144_list[i][0])/ema_144_list[i][0]

        sum_ema_21 = sum_ema_21 + ema_21_list[i][0]

    ema_21_avg = sum_ema_21/len(ema_21_list)

    up_rate = (ema_3_3_avg - ema_21_avg) / ema_21_avg
    print(str(up_rate), "#############################################")

    dis_avg = abs(dis_21_144/16) + abs(dis_55_144/16)

    # print(dis_21_144)
    # print(dis_55_144)
    print(str(dis_avg)+"############")

    return round(dis_avg*1000, 3), True, cate, up_rate


# um_futures_client = UMFutures()
# kline = um_futures_client.klines(symbol="BTCUSDT", interval="15m")
# print(kline)
# close_prise = []
# for i in kline:
#     close_prise.append(i[4])
# print(close_prise)
