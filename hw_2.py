'''import winsound

for note in [65, 69, 73, 78, 82, 87, 93, 98, 104, 110, 117, 124]:
	winsound.Beep(int(note), 500)'''

import wave
import matplotlib.pyplot as plt
import numpy as np
import os
import pyaudio
import numpy as np

p = pyaudio.PyAudio()

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
f.close()


