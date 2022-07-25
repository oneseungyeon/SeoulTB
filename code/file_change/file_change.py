import os
import glob
from tifffile import tifffile as tf
import numpy as np

file_path = '
allFile_list = list(glob.glob(os.path.join(file_path, '*.tif')))
print(allFile_list)
i =0
for name in allFile_list:
    src = os.path.join(name)
    dst = str(i) + '.png'
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1

