#!python
#!/usr/bin/env python

import sys
import numpy as np
from pybdm import BDM
from pybdm import options

options.set(raise_if_zero=False)

file = sys.argv[1]

with open(file, 'r') as file:
   data = file.read()

imagelist = data.splitlines()
number_of_lines=len(imagelist[0])
s = ""
image_array = np.empty((0,number_of_lines),dtype=int)
image_buffed_array= np.empty((0,number_of_lines*4),dtype=int)

for line in imagelist:
        for char in line:
            s += char + "-"
        line= np.fromstring(s, dtype=int, sep="-")
        a = np.repeat(line,4, axis=0)
        image_array=np.vstack([image_array,line])

        image_buffed_array=np.vstack([image_buffed_array,a])
        image_buffed_array=np.vstack([image_buffed_array,a])
        image_buffed_array=np.vstack([image_buffed_array,a])
        image_buffed_array=np.vstack([image_buffed_array,a])


        s = ""

print(image_array.shape)
np.savetxt('image.txt', image_array, fmt='%d', delimiter='')
print(image_buffed_array.shape)
np.savetxt('amplified_image.txt', image_buffed_array,fmt='%d', delimiter='')

for x in range(0, 8):
    for y in range(0, 8):
        print(image_array[x][y], end ="  ")
    print()

for x in range(0, 16):
    for y in range(0, 16):
        print(image_buffed_array[x][y], end ="  ")
    print()

bdm = BDM(ndim=2,nsymbols=2)
print(bdm.partition.shape)
val = bdm.bdm(image_array)
value=(val/image_array.size)
print("Original BDM value:", '{:.5f}'.format(val))

bdm_new_value = BDM(ndim=2,nsymbols=2)
val = bdm_new_value.bdm(image_buffed_array)
value = (val/image_buffed_array.size)

print("new BDM value:", '{:.5f}'.format(val))

