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
        x = i * 16 + 8
        y = j * 16 + 8
        if(x - p < 0):
            tempPiL = x
        if(x + p > w):
            tempPiR = w - x

        if(y - p < 0):
            tempPjL = y
        if (y + p > h):
            tempPjR = h - y
        windowX = tempPiR+1+ tempPiL
        windowY = tempPjR+1+ tempPjL
        window = i1[x - tempPiL:x + tempPiR+1, y - tempPjL:y + tempPjR+1]
        #print(window)
        #print(window.size)
        #pdb.set_trace()
        referenceNUM = (tempPiR + tempPiL + 1 - macroblock + 1) * (tempPjR + tempPjL + 1 - macroblock + 1)
        #print(referenceNUM)
        #pdb.set_trace()

        ####### window原始位置 X0 = x - tempPiL
        ####### window原始位置 Y0 = y - tempPjL
        window_X0 = x - tempPiL
        window_Y0 = y - tempPjL
        for jj in range(windowY-16):
            for ii in range(windowX-16):
                reference = window[ii:ii+16,jj:jj+16]
                reference_X = window_X0 + ii + 8
                reference_Y = window_Y0 + jj + 8
                #print(reference.size)

                ####MAD####
                sum = 0
                for jjj in range(macroblock):
                    for iii in range(macroblock):
                        diff = abs(target[iii][jjj]-reference[iii][jjj])
                        sum = sum + diff
                MAD = (1/(macroblock * macroblock)) * sum
                print(MAD)
                #pdb.set_trace()


#print(window)
print(target)
print(reference)

print(x,y,reference_X,reference_Y,window.size)
#print(count)