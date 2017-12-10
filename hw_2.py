#-*- coding:utf-8 -*-
import scipy.io.wavfile
import matplotlib.pyplot as plt
import numpy as np

#讀txt
'''path = input('請輸入文字檔路徑+檔名+副檔名：')

try:
    fileTxt = open(path)
except Exception as e:
    print("路徑錯誤")'''
#不使用讀取txt功能，因為音樂有一拍、半拍、三連音...等等，txt較難統一、辨別以上所述的分類
############

volume = 0.5     # range [0.0, 1.0]
fs = 8000      # sampling rate, Hz, must be integer
duration = 4.0   # in seconds, may be float
#取聖誕歌前四個音節
#|333-|333-|3212|3---|

#主音為高頻 LEVEL4
#1 == 262, 2 == 278, 3 == 294
f1 = 262.0        # sine frequency, Hz, may be float
f2 = 278.0
f3 = 294.0
f0 = 1.0

samples = 2*np.pi*np.arange(fs*duration)
temp = samples
print(temp)

sleep = 10

n = 1
for i in range((n-1)*fs,fs*n):
    samples[i] = np.sin(samples[i] * f3 / fs).astype(np.float32)
for i in range(int(fs*n-fs/sleep),fs*n):
    samples[i] = np.sin(samples[i] * f0 / fs).astype(np.float32)

n = 2
for i in range((n-1)*fs,fs*n):
    samples[i] = np.sin(samples[i] * f3 / fs).astype(np.float32)
for i in range(int(fs*n-fs/sleep),fs*n):
    samples[i] = np.sin(samples[i] * f0 / fs).astype(np.float32)

n = 3
for i in range((n-1)*fs,fs*n):
    samples[i] = np.sin(samples[i] * f3 / fs).astype(np.float32)

n = 4
for i in range((n-1)*fs,fs*n):
    samples[i] = np.sin(samples[i] * f3 / fs).astype(np.float32)


newdata = volume*samples.astype(np.float32)

scipy.io.wavfile.write("sample1.wav",fs, newdata)
#新图像
plt.subplot(2, 1, 1)
plt.title("main")
plt.plot(newdata)

plt.show()
