#-*- coding:utf-8 -*-
import scipy.io.wavfile
import matplotlib.pyplot as plt
from urllib import request
import numpy as np


volume = 0.5     # range [0.0, 1.0]
fs = 8000      # sampling rate, Hz, must be integer
duration = 5.0   # in seconds, may be float
f = 262.0        # sine frequency, Hz, may be float
f2= 65.0
f3= 1.0

#samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
samples = 2*np.pi*np.arange(fs*duration)  #*f/fs)).astype(np.float32)
a = np.arange(fs*duration)
print(len(samples))
for i in range (len(samples)):
    if i >=0 and i<=20000:
        samples[i] = np.sin(samples[i] * 1 / fs).astype(np.float32)
    else:
        samples[i] = np.sin(samples[i] * f / fs).astype(np.float32)
#samples2 = (np.sin(2*np.pi*np.arange(fs*duration)*f2/fs)).astype(np.float32)
newdata = volume*samples.astype(np.float32)
print(samples)
print ("Data type", newdata.dtype,"--", "Shape", newdata.shape)

scipy.io.wavfile.write("quiet.wav",fs, newdata)
#新图像
plt.subplot(2, 1, 2)
plt.title("Quiet")
plt.plot(newdata)

plt.show()