#-*- coding:utf-8 -*-
import scipy.io.wavfile
import matplotlib.pyplot as plt
import numpy as np

#讀txt
path = input('請輸入文字檔路徑+檔名+副檔名：')

try:
    fileTxt = open(path)
except Exception as e:
    print("路徑錯誤")