#!/usr/bin/python3
# encoding=utf-8

import urllib.request
import json
import pandas as pd
import codecs
import matplotlib.pyplot as plt
from datetime import *


def getpos(alist):
    re = []
    temp = [-1, -1]
    for i in range(len(alist)):

        if i != len(alist) - 1:
            if (alist[i] + 1 == alist[i + 1]) & (temp[0] == -1):
                temp[0] = i
            if alist[i] + 1 != alist[i + 1]:
                temp[1] = i
                re.append(temp)
                temp = [-1, -1]
        else:
            if temp[0] == -1:
                temp[0] = len(alist) - 1
            temp[1] = len(alist) - 1
            re.append(temp)
    for pos in re:
        if pos[0] == -1:
            pos[0] = pos[1]
    return re


def plot_rain(df_rain):
    _x = range(len(df_rain.index))
    _y = df_rain.values

    l = [i.strftime("%m%d%H") for i in df_rain.index]


    # plt.xticks(_x[::5], list(l)[::5], rotation=45)
    # plt.yticks(range(1, int(max(_y)) + 1, 5))
    plt.scatter(_x, _y)


if __name__ == "__main__":
    df = pd.read_csv("data/2019.csv")
    df["DDATETIME"] = pd.to_datetime(df["DDATETIME"], format="")
    df.set_index("DDATETIME", inplace=True)

    df.rename(columns={"Unnamed: 0": "id"}, inplace=True)

    df["id"] = range(1, len(df["id"]) + 1, 1)

    df_rain = df.loc[(df["1小时降水量"].astype(float) > 1)]

    testre = getpos(list(df_rain["id"]))
    print(len(testre))
    df_rain = df_rain["1小时降水量"]

    rains = []
    for pos in testre:
        if pos[0] == -1:
            rains.append(df_rain[pos[1]:pos[1] + 1])
        rains.append(df_rain[pos[0]:pos[1] + 1])

    plt.figure(figsize=(20, 8), dpi=80)
    for rain in rains:
        if len(rain) > 0:
            plot_rain(rain)

    plt.show()

