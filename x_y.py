import numpy as np
from PIL import Image

hear = Image.open(r'crop.jpg')
big = Image.open(r'original.jpg')

# convert into array
hear = np.asarray(hear)
big = np.asarray(big)

hearay , hearax = hear.shape[:2]
bigay  , bigax  = big.shape[:2]

stopx = bigax - hearax + 1
stopy = bigay - hearay + 1

# print(stopx)
# print(stopy)

for x in range(0,stopx):
    for y in range(0,stopy):
        x2 = x + hearax
        y2 = y + hearay
        pic = big[y:y2,x:x2]
        test = (pic == hear)
        if test.all():
            print(x,y)