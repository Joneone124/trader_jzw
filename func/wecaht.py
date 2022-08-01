import json
import time

import requests
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table
from PIL import Image, ImageDraw, ImageFont
import hashlib, base64

def alert(cate, rate):
    xls = pd.DataFrame({'币种': cate, '波动幅度': rate}, index=None)

    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 显示中文
    fig = plt.figure(figsize=(4, 20), dpi=300)  # 图片的长、宽、像素
    ax = fig.add_subplot(111, frame_on=False)  # 111表示只画一张图
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    table(ax, xls, loc='center')
    plt.savefig('pic.jpg')


    data = {
        "msgtype": "text",
        "text": {
            "content": "【持仓异动】",
            # "mentioned_list": ["xiaoming"],
            # "mentioned_mobile_list": ["13456789100"]
        }
    }
    r = requests.post(url='https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=09671de5-6d1c-4260-84da-70f0f1b6530c',
                      json=data)


    file_image = open('pic.jpg', 'rb').read()
    is_f = base64.b64encode(file_image)  # 根据企微api的要求，要把图片编成 base64 编码
    md5 = hashlib.md5(file_image)  # 也是根据企微api要求来编码
    data = {
        'msgtype': 'image',
        'image': {
            'base64': is_f.decode('utf-8'),
            'md5': md5.hexdigest()
        }
    }

    requests.post('https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=09671de5-6d1c-4260-84da-70f0f1b6530c', data=json.dumps(data))
    print(r.text)
