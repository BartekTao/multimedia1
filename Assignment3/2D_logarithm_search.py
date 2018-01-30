import numpy as np
from matplotlib import pyplot
from PIL import Image
from scipy.fftpack import dct,idct
import pdb


def as_array(filepath):
    f = open(filepath, 'r')
    w, h = tuple(int(v) for v in next(f).split()[1:3])
    #print(w, h)

    f = open(filepath, 'r')
    f.readline()
    buffer = f.read()
    buffer = buffer.split()
    f.close()

    # convert binary data to an array of the right shape
    data = np.array(buffer).astype(np.int64)
    #print(data)

    data = np.frombuffer(data, dtype=np.int64).reshape((h, w))
    #print(data)

    return data

a = as_array('i2.pgm')
i2 = a.astype('uint8')

b = as_array('i1.pgm')
i1 = b.astype('uint8')

p_frame = b.astype('uint8')

w = 320
h = 240
macroblock = 16
p = 15
window = p*2+1

count = 0
for j in range(int(w /macroblock)):
    for i in range(int(h / macroblock)):
        target = i2[i*16:16*(i+1),j*16:16*(j+1)]
        count = count+1
        #print(target)
        #pdb.set_trace()

        ####window = i1[i-15:i+15,j-15:j+15]
        tempPiL = p
        tempPjL = p
        tempPiR = p
        tempPjR = p
        x0 = i * 16
        y0 = j * 16
        x = i * 16
        y = j * 16
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

        min_MAD = 1000000000
        pp = 8
        while pp >=1:
            for jj in range(3):
                for ii in range(3):
                    #print(window.size)
                    #reference = window[ii + ii * pp :ii + ii * pp + macroblock ,jj + jj * pp :jj + jj * pp + macroblock ]
                    reference = i1[x-pp + ii*pp:x-pp + ii*pp + macroblock, y-pp + jj*pp:y-pp + jj*pp + macroblock]
                    reference_X = x-pp + ii*pp
                    reference_Y = y-pp + jj*pp
                    #print(reference_X, reference_Y, ",", x-8 + ii, y-8 + jj)
                    #print(reference)
                    #pdb.set_trace()

                    ####MAD####
                    sum = 0
                    if reference.size == 256:
                        for jjj in range(macroblock):
                            for iii in range(macroblock):
                                diff = abs(target[iii][jjj] - reference[iii][jjj])
                                sum = sum + diff
                        MAD = (1 / (macroblock * macroblock)) * sum
                        # print(MAD)
                        # print(target)
                        # print(reference)
                        # pdb.set_trace()
                        # print(reference_X,reference_Y,",",x,y)

                        if MAD < min_MAD:
                            min_MAD = MAD
                            min_X = reference_X
                            min_Y = reference_Y
                            minReference = reference
                            # print(min_X,min_Y)
            pp = int(pp / 2)
            x = min_X
            y = min_Y
            #print(min_X, min_Y)
            #MV = (min_X - x0, min_Y - y0)
            #print((x0, y0), MV)
            #pdb.set_trace()

        MV = (min_X - x0, min_Y - y0)
        print(str((x0, y0))+">>"+str(MV))
        def dct2(block):
            return dct(dct(block.T, norm='ortho').T, norm='ortho')

        def idct2(block):
            return idct(idct(block.T, norm='ortho').T, norm='ortho')


        quantization = np.round(dct2(target - minReference)/8)
        #print(quantization)
        #pdb.set_trace()
        p_frame[i * 16:16 * (i + 1), j * 16:16 * (j + 1)] = minReference + idct2(quantization*8)

#print(i2)
#print(p_frame)
pyplot.imshow(p_frame, pyplot.cm.gray)
pyplot.show()

sumf = 0
for j in range(w):
    for i in range(h):
        f = i2[i][j] * i2[i][j]
        sumf = sumf + f

sum_f = 0
for j in range(w):
    for i in range(h):
        f = p_frame[i][j] * p_frame[i][j]
        sum_f = sum_f + f
snr = sumf/sum_f
print(snr)







