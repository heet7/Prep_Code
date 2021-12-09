from os import readlink


with open(f'name.json','r') as name:
    c = name.readline()
    for i in range(len(c)):
        print(c[i])