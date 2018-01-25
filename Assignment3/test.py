import numpy as np
from PIL import Image
import pdb


def as_array(filepath):
    f = open(filepath, 'r')
    w, h = size = tuple(int(v) for v in next(f).split()[1:3])
    print(w,h)
    data_size = w * h * 2

    f.seek(0, 2)
    filesize = f.tell()
    f.close()
    i_header_end = filesize - (data_size)

    f = open(filepath, 'rb')
    f.seek(i_header_end)
    buffer = f.read()
    f.close()

    # convert binary data to an array of the right shape
    data = np.frombuffer(buffer, dtype=np.uint16).reshape((w, h))

    return data

a = as_array('i2.pgm')
np3 = a.astype('uint8')

w = 320
h = 240
macroblock = 16
window = 31

count = 0
for j in range(int(h /macroblock)):
    for i in range(int(w / macroblock)):
        target = np3[i*16:16*(i+1),j*16:16*(j+1)]
        count = count+1
        #print(target)
        #pdb.set_trace()
print(count)