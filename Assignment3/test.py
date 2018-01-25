import numpy as np
from PIL import Image
import pdb


def as_array(filepath):
    f = open(filepath, 'r')
    w, h = size = tuple(int(v) for v in next(f).split()[1:3])
    #print(w,h)
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
i2 = a.astype('uint8')

b = as_array('i1.pgm')
i1 = a.astype('uint8')

w = 320
h = 240
macroblock = 16
p = 15
window = p*2+1

count = 0
for j in range(int(h /macroblock)):
    for i in range(int(w / macroblock)):
        target = i2[i*16:16*(i+1),j*16:16*(j+1)]
        count = count+1
        #print(target)
        #pdb.set_trace()

        ####window = i1[i-15:i+15,j-15:j+15]
        tempPiL = p
        tempPjL = p
        tempPiR = p
        tempPjR = p
        if(i*16 - p < 0):
            tempPiL = i*16
        if(i*16 + p > w):
            tempPiR = w - i*16

        if(j*16 - p < 0):
            tempPjL = j*16
        if (j*16 + p > h):
            tempPjR = w - i*16
        window = i1[i*16 - tempPiL:i*16 + tempPiR+1, j*16 - tempPjL:j*16 + tempPjR+1]
        print(window)
        print(window.size)
        pdb.set_trace()
        referenceNUM = (tempPiR + tempPiL + 1 - macroblock + 1) * (tempPjR + tempPjL + 1 - macroblock + 1)
        #print(referenceNUM)
        #pdb.set_trace()
print(window)
print(count)