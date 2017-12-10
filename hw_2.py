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
sleep = 15
time = 0.4

volume = 0.5     # range [0.0, 1.0]
fs = 8000      # sampling rate, Hz, must be integer
duration = 16.0*time   # in seconds, may be float
#取聖誕歌前四個音節
#|333-|333-|3512|3---|

#主音為高頻 LEVEL4
#1 == 262, 2 == 278, 3 == 294
f1 = 262.0        # sine frequency, Hz, may be float
f2 = 294.0
f3 = 330.0
f5 = 392.0
f0 = 1.0

samples = 2*np.pi*np.arange(fs*duration)

def setMusic(n, f):
    n = n * time
    for i in range(int((n - time) * fs), int(fs * n)):
        samples[i] = np.sin(samples[i] * f / fs).astype(np.float32)

def setSleep(n):
    n = n * time
    for i in range(int(fs * n - fs / sleep), int(fs * n)):
        samples[i] = np.sin(samples[i] * f0 / fs).astype(np.float32)

setMusic(1,f3)
setSleep(1)

setMusic(2,f3)
setSleep(2)

setMusic(3,f3)

setMusic(4,f3)
setSleep(4)

setMusic(5,f3)
setSleep(5)

setMusic(6,f3)
setSleep(6)

setMusic(7,f3)

setMusic(8,f3)
setSleep(8)

setMusic(9,f3)
setSleep(9)

setMusic(10,f5)
setSleep(10)

setMusic(11,f1)
setSleep(11)

setMusic(12,f2)
setSleep(12)

setMusic(13,f3)

setMusic(14,f3)

setMusic(15,f3)

setMusic(16,f3)
setSleep(16)

newdata = 0.5*samples.astype(np.float32)

f1 = 65.0        # sine frequency, Hz, may be float
f2 = 73.0
f3 = 82.0
f5 = 98.0

samples2 = 2*np.pi*np.arange(fs*duration)

def setMusic(n, f):
    n = n * time
    for i in range(int((n - time) * fs), int(fs * n)):
        samples2[i] = np.sin(samples2[i] * f / fs).astype(np.float32)

def setSleep(n):
    n = n * time
    for i in range(int(fs * n - fs / sleep), int(fs * n)):
        samples2[i] = np.sin(samples2[i] * f0 / fs).astype(np.float32)

setMusic(1,f3)
setSleep(1)

setMusic(2,f3)
setSleep(2)

setMusic(3,f3)

setMusic(4,f3)
setSleep(4)

setMusic(5,f3)
setSleep(5)

setMusic(6,f3)
setSleep(6)

setMusic(7,f3)

setMusic(8,f3)
setSleep(8)

setMusic(9,f3)
setSleep(9)

setMusic(10,f5)
setSleep(10)

setMusic(11,f1)
setSleep(11)

setMusic(12,f2)
setSleep(12)

setMusic(13,f3)

setMusic(14,f3)

setMusic(15,f3)

setMusic(16,f3)
setSleep(16)


newdata2 = 0.3*samples2.astype(np.float32)

scipy.io.wavfile.write("sample1.wav",fs, newdata + newdata2)
#新图像
plt.subplot(3, 1, 1)
plt.title("main")
plt.plot(newdata)

plt.subplot(3, 1, 2)
plt.title("second")
plt.plot(newdata2)

plt.subplot(3, 1, 3)
plt.title("second")
plt.plot(newdata + newdata2)

plt.show()
