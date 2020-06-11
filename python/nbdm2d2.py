#!python
#!/usr/bin/env python
#Python script:
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

for line in imagelist:
        for char in line:
            s += char + "-"
        image_array=np.vstack([image_array, np.fromstring(s, dtype=int, sep="-")])
        s = ""

bdm = BDM(ndim=2,nsymbols=2)
nbdm = bdm.nbdm(image_array)
print(nbdm)
