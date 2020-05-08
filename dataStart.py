#!/usr/bin/python3
# encoding=utf-8

import urllib.request
import json
import pandas as pd
import codecs
import matplotlib.pyplot as plt
from datetime import *

df = pd.read_csv("data/2019.csv")
df["DDATETIME"] = pd.to_datetime(df["DDATETIME"],format="")
df.set_index("DDATETIME", inplace=True)

df.rename(columns={"Unnamed: 0" : "id"}, inplace=True)
print(df.head())
print(df.info())
for i in df.columns:
    print(i)
df_rain = df.loc[(df["1小时降水量"].astype(float) != 0)
                 & (df["过去3小时降水量"].astype(float) != 0)
                 & (df["过去6小时降水量"].astype(float) != 0)
                 & (df["过去12小时降水量"].astype(float) != 0)
                 & (df["过去24小时降水量"].astype(float) != 0)]

sumrain = df.resample('M').sum()
print(sumrain)

_x = range(len(df_rain.index))
_y = df_rain["过去24小时降水量"].astype(float)


l = [i.strftime("%m%d%H") for i in df_rain.index]
ll = []
for i in range(len(l))[::50]:
    ll.append(l[i])
print(l)
print(ll)
plt.figure(figsize=(20, 8), dpi=80)
plt.xticks(_x[::50], ll, rotation=45)
plt.yticks(range(int(max(_y))))
plt.plot(_x, _y)
plt.show()