#-*- coding:utf-8 -*-
import scipy.io.wavfile
import matplotlib.pyplot as plt
from urllib import request
import numpy as np

url = 'http://www.thesoundarchive.com/austinpowers/smashingbaby.wav'
response = request.urlopen(url)
print (response.info())
WAV_FILE = 'smashingbaby.wav'
#二进制方式打开
filehandle = open(WAV_FILE, 'wb+')
filehandle.write(response.read())
filehandle.close()
sample_rate, data = scipy.io.wavfile.read(WAV_FILE)
print ("Data type", data.dtype,"--", "Shape", data.shape)
#原始图
plt.subplot(2, 1, 1)
plt.title("Original")
plt.plot(data)
#新数据
newdata = data * 0.2
newdata = newdata.astype(np.uint8)
print ("Data type", newdata.dtype,"--", "Shape", newdata.shape)

scipy.io.wavfile.write("quiet.wav",
    sample_rate, newdata)
#新图像
plt.subplot(2, 1, 2)
plt.title("Quiet")
plt.plot(newdata)

plt.show()