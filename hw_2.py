#-*- coding:utf-8 -*-
import scipy.io.wavfile
import matplotlib.pyplot as plt
import numpy as np
import sys

#讀txt
#path = input('請輸入文字檔路徑+檔名+副檔名：')

numberRange = ('1','2','3','4','5','6','7')
symbol = ("-")
music = []

try:
    with open('music.txt','r', encoding='utf-8') as f:
        for mF in f:
            if mF[0] == "-":
                print("格式錯誤，第一個音必須為音符(1~7)")
            for i in range(len(mF)):
                if mF[i] in numberRange or mF[i] in symbol:
                    music.append(mF[i])
                else:
                    print("格式錯誤，範圍1~7與'-'，將自動刪除其餘格式(包括空白)")

    f.close()
    print(music)

    #設置變數
    sleep = 15  #休息間隔，越小越久
    time = 0.4  #一拍代表幾秒

    sleep2 = 15 #主音樂與伴奏錯開時間

    volumeMain = 0.5  # 主音音量 range [0.0, 1.0]
    volumeSecond = 0.3  # 伴奏音量 range [0.0, 1.0]
    fs = 8000  # sampling rate, Hz, must be integer
    duration = len(music) * time  # in seconds

    #頻率table

    f0 = 1.0  #休息時的頻率

    samples = 2 * np.pi * np.arange(fs * duration)
    samples2 = 2 * np.pi * np.arange(fs * duration)


    def setMusic(n, num):
        n = (n+1) * time
        for i in range(int((n - time) * fs), int(fs * n)):
            samples[i] = np.sin(samples[i] * getTable("main", num) / fs).astype(np.float32)
            samples2[i] = np.sin(samples2[i] * getTable("second", num) / fs).astype(np.float32)
    def setStart(n):
        n = (n + 1) * time
        for i in range(int((n - time) * fs), int((n - time) * fs + fs / sleep2)):
            samples2[i] = np.sin(samples2[i] * f0 / fs).astype(np.float32)


    def getTable(type, num):
        # 主音 LEVEL4
        f1 = 262.0  # sine frequency, Hz, may be float
        f2 = 294.0
        f3 = 330.0
        f4 = 349.0
        f5 = 392.0
        f6 = 440.0
        f7 = 494.0

        ff1 = 65.0  # sine frequency, Hz, may be float
        ff2 = 73.0
        ff3 = 82.0
        ff4 = 87.0
        ff5 = 98.0
        ff6 = 110.0
        ff7 = 124.0

        if type == "main":
            if num == "1":
                return f1
            elif num == "2":
                return f2
            elif num == "3":
                return f3
            elif num == "4":
                return f4
            elif num == "5":
                return f5
            elif num == "6":
                return f6
            elif num == "7":
                return f7
        elif type == "second":
            if num == "1":
                return ff1
            elif num == "2":
                return ff2
            elif num == "3":
                return ff3
            elif num == "4":
                return ff4
            elif num == "5":
                return ff5
            elif num == "6":
                return ff6
            elif num == "7":
                return ff7


    def setSleep(n):
        n = (n+1) * time
        for i in range(int(fs * n - fs / sleep), int(fs * n)):
            samples[i] = np.sin(samples[i] * f0 / fs).astype(np.float32)
            samples2[i] = np.sin(samples2[i] * f0 / fs).astype(np.float32)


    tempMusic = "1"
    for j in range(len(music)):
        if music[j] in numberRange:
            setMusic(j,music[j])
            setStart(j) # 主音與伴奏的錯開的時間，個人認為就算不錯開，還是分得清楚高頻與低頻的聲音
        elif music[j] in symbol:
            setMusic(j, tempMusic)

        if j == len(music)-1:
            setSleep(j)
            continue
        else:
            if music[j+1] == "-" and music[j] in numberRange:
                tempMusic = music[j]
            if music[j+1] in numberRange:
                setSleep(j)

    newdata = volumeMain * samples.astype(np.float32)
    newdata2 = volumeSecond * samples2.astype(np.float32)

    scipy.io.wavfile.write("sample2.wav", fs, newdata+ newdata2)
    # 新图像
    plt.subplot(3, 1, 1)
    plt.title("main")
    plt.plot(newdata)

    plt.subplot(3, 1, 2)
    plt.title("second")
    plt.plot(newdata2)

    plt.subplot(3, 1, 3)
    plt.title("all")
    plt.plot(newdata + newdata2)

    plt.show()

except Exception as e:
    s = sys.exc_info()
    e = " Error '%s' happened on line %d" % (s[1],s[2].tb_lineno)
    print(e)





############


'''sleep = 15
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

def setStart(n):
    n = n * time
    for i in range(int((n - time) * fs), int((n - time) * fs + fs / sleep)):
        samples2[i] = np.sin(samples2[i] * f0 / fs).astype(np.float32)

setMusic(1,f3)
setSleep(1)
setStart(1)

setMusic(2,f3)
setSleep(2)
setStart(2)

setMusic(3,f3)
setStart(3)

setMusic(4,f3)
setSleep(4)

setMusic(5,f3)
setSleep(5)
setStart(5)

setMusic(6,f3)
setSleep(6)
setStart(6)

setMusic(7,f3)
setStart(7)

setMusic(8,f3)
setSleep(8)

setMusic(9,f3)
setSleep(9)
setStart(9)

setMusic(10,f5)
setSleep(10)
setStart(10)

setMusic(11,f1)
setSleep(11)
setStart(11)

setMusic(12,f2)
setSleep(12)
setStart(12)

setMusic(13,f3)
setStart(13)

setMusic(14,f3)

setMusic(15,f3)

setMusic(16,f3)
setSleep(16)


newdata2 = 0.3*samples2.astype(np.float32)

scipy.io.wavfile.write("sample2.wav",fs, newdata + newdata2)
#新图像
plt.subplot(3, 1, 1)
plt.title("main")
plt.plot(newdata)

plt.subplot(3, 1, 2)
plt.title("second")
plt.plot(newdata2)

plt.subplot(3, 1, 3)
plt.title("all")
plt.plot(newdata + newdata2)

plt.show()'''
