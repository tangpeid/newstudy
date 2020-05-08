#!/usr/bin/python3
# encoding=utf-8

import urllib.request
import json
import pandas as pd
import codecs
import matplotlib.pyplot as plt
from datetime import *


class GetDataFromIdea:
    def __init__(self):
        self.user = 'gmcrzs'
        self.pwd = 'hjjl'
        pass

    # 调用全省雨量数据
    def getRain4Prov(self, ymd, hms, prov, dtfmt):
        # 服务地址
        url = "http://172.22.1.175/di/http.action"
        # 调用参数  #getSurfNewAutoQc4Prov, getRACAutoRain4Prov
        params = "userId=" + self.user + "&pwd=" + self.pwd + \
                 "&interfaceId=getSurfNewAutoQc4Prov" + \
                 "&ymdhms=" + ymd + hms + \
                 "&prov=" + prov + \
                 "&dataFormat="

        return self.getDatasPost(url, params + dtfmt)

    # 调用测试接口
    def getStationDataTest(self, s_ymdhms, e_ymdhms, staNum, dtfmt):
        # 服务地址
        url = "http://172.22.1.175/di/http.action"
        # 调用参数  中国地面观测国家站-质控getSurfNewAutoQcTimeRange4Iiiii
        params = "userId=" + self.user + "&pwd=" + self.pwd + \
                 "&interfaceId=getRACNewAutoTimeRangeZ4Iiiii" + \
                 "&s_ymdhms=" + s_ymdhms + \
                 "&e_ymdhms=" + e_ymdhms + \
                 "&iiiii=" + staNum + \
                 "&dataFormat="

        return self.getDatasPost(url, params + dtfmt)

    # 调用站点数据接口
    def getStationData(self, ymd, hm, city, dtfmt):  # datafmt: html, txt, json, jsonp, xml, xml2, arff
        # 服务地址
        url = "http://172.22.1.175/di/http.action"
        # 调用参数
        params = "userId=" + self.user + "&pwd=" + self.pwd + \
                 "&interfaceId=getRACAuto4City" + \
                 "&ymd=" + ymd + \
                 "&hm=" + hm + \
                 "&city=" + city + \
                 "&dataFormat="

        return self.getDatasPost(url, params + dtfmt)

        # 调用格点数据接口

    def getGridData(self, dtfmt):  # dtfmt: html, txt, json, jsonp, xml, xml2
        # 服务地址
        url = "http://172.22.1.175/di/grid.action"
        # 调用参数
        params = "userId=idc&pwd=qgfvNJ&interfaceId=intGetData2D&modelid=giftdaily&element=t2mm&level=1000&starttime" \
                 "=2018-11-22 00:00:00&leadtime=012&dataFormat= "

        return self.getDatasPost(url, params + dtfmt)

    # 调用图形产品接口
    def getImageData(self, dtfmt):  # dtfmt: html, txt, json, jsonp, xml, xml2
        # 服务地址
        url = "http://172.22.1.175/di/image.action"
        # 调用参数
        params = "userId=gmcrzs&pwd=hjjl&interfaceId=getMaxtempForecastImage_24h&ymdhms=20200218000000&cols=fileName," \
                 "fileUrl,suffix,width,height,size,imgbase64&dataFormat= "

        return self.getDatasPost(url, params + dtfmt)

    # 调用算法服务接口
    def getAlgData(self):
        # 服务地址
        url = "http://172.22.1.175/di/alg.action"
        # 调用参数
        params = "userId=gmcrzs&pwd=hjjl&interfaceId=getSunRiseSetTime&lon=110&lat=22&date=20170602"
        # 调用html格式
        print("--- 返回算法服务数据 ---")
        print(self.getDatasPost(url, params))

    # 调用原始文件接口
    def getFileData(self, dtfmt):  # dtfmt : html, txt, json, xml, xml2
        # 服务地址
        url = "http://172.22.1.175/di/file.action"
        # 调用参数
        params = "userId=gmcrzs&pwd=hjjl&interfaceId=getSevpNqtqyb&ymdhms=20190101000000&issue=12&dataFormat="

        return self.getDatasPost(url, params + dtfmt)

    # 调用卫星数据接口
    def getSateData(self):
        # 服务地址
        url = "http://172.22.1.175/di/sate.action"
        # 调用参数
        params = "userId=gmcrzs&pwd=hjjl&&interfaceId=fy2e&date=201610250615&sateName=FY2E&startX=110&startY=-90&endX=120&endY=90&element=NOMChannelVIS&dataformat="
        # 调用html格式
        print("--- 返回html格式数据 ---")
        print(self.getDatasPost(url, params + "html"))
        # 调用json格式
        print("--- 返回json格式数据 ---")
        print(self.getDatasPost(url, params + "json"))

    def getDatasPost(self, url, params):
        post_data = bytes(params, encoding='utf8')
        response = urllib.request.urlopen(url, data=post_data)
        return response.read().decode()

    def ToDataFrame(self, result):
        dict = json.loads(result)['DATA'][0]
        idx = json.loads(result)['ROWCOUNT']
        return pd.DataFrame(dict, columns=dict.keys(), index=range(int(idx)))

    def Change_name(self, name):
        with codecs.open("data/datainfonew.csv", encoding='gbk') as f:
            for line in f:
                l = line.split(',')
                if l[0].strip() == name:
                    return l[1]
                elif l[1].strip() == name:
                    return l[0]
        return name


def add_months(dt, months):
    dr = pd.date_range(start=dt, periods=1, freq='M')
    lastp = pd.date_range(start=dr[-1], periods=2, freq='D')
    return lastp[-1]


def getData(year):
    df = pd.DataFrame()
    httpGeneral = GetDataFromIdea()
    # 调用站点数据接口20191218
    for month in range(1, 13):
        print(str(month) + " month  start...")
        dt = datetime(year, month, 1, 0, 0, 0)
        e_ymdhms = add_months(dt, 1).strftime("%Y%m%d%H%M%S")
        s_ymdhms = dt.strftime("%Y%m%d%H%M%S")
        result = httpGeneral.getStationDataTest(s_ymdhms=s_ymdhms, e_ymdhms=e_ymdhms, staNum='59485',
                                                dtfmt='json')
        dicts = json.loads(result)['DATA']
        idx = json.loads(result)['ROWCOUNT']

        dicts_need = list()
        for dict in dicts:
            dict_need = {}
            for key in dict.keys():
                dict_need[httpGeneral.Change_name(key)] = dict[key]
            dicts_need.append(dict_need)
        temp_df = pd.DataFrame(dicts_need)
        df = df.append(temp_df)
        print(str(month) + " month  end")
        temp_df.to_csv("data/" + str(month) + ".csv")
    df.to_csv("data/" + str(year) + ".csv")


if __name__ == "__main__":
    getData(2019)
    # pd.set_option('display.max_columns', 1000)

    # pd.set_option('display.width', 1000)

    # pd.set_option('display.max_colwidth', 1000)

    # rain = df.loc[:, ["资料时间", "1小时降水量"]]
    # rain1 = pd.Series(df.loc[:, "1小时降水量"])
    # rain1.index = index = df.loc[:, "资料时间"]
    #
    # min = float(rain1.min())
    # max = float(rain1.max())
    # _yticks = []
    # v = (max - min) / 25
    # while min < max:
    #     _yticks.append(min + v)
    #     min = min + v
    #
    # plt.plot(range(1, 26, 1), rain1.values.astype(float))
    # plt.xticks(range(1,26,1))
    # plt.yticks(_yticks)
    # plt.show()

    # print(result)

    # print(tmp_lst)
    # print(json.dumps(result))
    # # 调用格点数据接口
    # httpGeneral.getGridData()
    # # 调用图形产品接口
    # httpGeneral.getImageData()
    # # 调用算法服务接口
    # httpGeneral.getAlgData()
    # # 调用原始文件接口
    # httpGeneral.getFileData()
    # # 调用卫星数据接口
    # httpGeneral.getSateData()
