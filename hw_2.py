'''import winsound

for note in [65, 69, 73, 78, 82, 87, 93, 98, 104, 110, 117, 124]:
	winsound.Beep(int(note), 500)'''

import wave
import matplotlib.pyplot as plt
import os
import pyaudio
# -*- coding: utf-8 -*-
import wave
import numpy as np
import scipy.signal as signal
import scipy.io.wavfile

volume = 0.5     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = 10.0   # in seconds, may be float
f = 100.0        # sine frequency, Hz, may be float

# generate samples, note conversion to float32 array
samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float64)
print(samples)

framerate = 44100
time = 10

# 产生10秒44.1kHz的100Hz - 1kHz的频率扫描波
t = np.arange(0, time, 1.0/framerate)
wave_data = signal.chirp(t, 100, time, 1000, method='linear') * 10000
print(wave_data)
wave_data = wave_data.astype(np.short)
print(wave_data)

plt.subplot(211)
plt.plot(wave_data)
plt.show()

#新数据
newdata = samples.astype(np.uint8)
print ("Data type", newdata.dtype,"--", "Shape", newdata.shape)

scipy.io.wavfile.write("quiet.wav",fs, newdata)

# 打开WAV文档
f = wave.open(r"sweep.wav", "wb")

# 配置声道数、量化位数和取样频率
f.setnchannels(1)
f.setsampwidth(2)
f.setframerate(framerate)
# 将wav_data转换为二进制数据写入文件
f.writeframes(wave_data.tostring())
f.close()

'''p = pyaudio.PyAudio()

volume = 0.5     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = 5.0   # in seconds, may be float
f = 440.0        # sine frequency, Hz, may be float

# generate samples, note conversion to float32 array
samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)

# for paFloat32 sample values must be in range [-1.0, 1.0]
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

# play. May repeat with different volume values (if done interactively)
stream.write(volume*samples)

stream.stop_stream()
stream.close()

p.terminate()
plt.subplot(211)
plt.plot(volume*samples)
plt.show()


wave_data = volume*samples
wave_data = wave_data.astype(np.short)

# 打开WAV文档
f = wave.open(r"sweep.wav", "wb")

# 配置声道数、量化位数和取样频率
f.setnchannels(1)
f.setframerate(fs)
f.setsampwidth(2)
f.writeframes(wave_data.tostring())
# 将wav_data转换为二进制数据写入文件
f.close()'''


