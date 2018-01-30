import numpy as np
from matplotlib import pyplot
from PIL import Image
import pdb


def as_array(filepath):
    f = open(filepath, 'r')
    w, h = tuple(int(v) for v in next(f).split()[1:3])
    print(w,h)

    f = open(filepath, 'r')
    f.readline()
    buffer = f.read()
    buffer = buffer.split( )
    f.close()

    # convert binary data to an array of the right shape
    data = np.array(buffer).astype(np.int64)
    print(data)

    data = np.frombuffer(data, dtype=np.int64).reshape((h, w))
    print(data[0].size)


    return data

a = as_array('i1.pgm')
print(a)

pyplot.imshow(a, pyplot.cm.gray)
pyplot.show()