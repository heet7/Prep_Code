import os
import sys

x = sys.argv
# print('{}'.format(x))

for i in x[1:]:
    print("you have this much of {} file in this directory".format(str(i)))

    for f in os.listdir('.'):
        if f.endswith(i):
            fn , text = os.path.splitext(f)
            print(fn,text)
    print("*"*40)