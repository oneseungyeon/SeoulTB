import os
import glob
from tifffile import tifffile as tf
import numpy as np

file_path = ''
save_path = file_path
files = glob.glob(file_path + "*.tif")
print(files)
i=0
for img in files:
    a = tf.imread(img)
    a = tf.imsave(save_path+str(i)+'.png', a).astype(float32)
    i = i+1
