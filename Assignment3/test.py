import numpy as np
from PIL import Image


def as_array(filepath):
    f = open(filepath, 'r')
    w, h = size = tuple(int(v) for v in next(f).split()[1:3])
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

a = as_array('i1.pgm')
print(a)