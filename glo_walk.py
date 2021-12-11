import glob
import json
import os

print("Enter path like this => /full path/ <= and hit enter")

get_input = str(input("Enter path : "))
path = get_input+'**/*'


j = open('ext.json')
data = json.load(j)

# creating directory if not exist
os.makedirs('/home/heet/aditbhai/file_finding',exist_ok=True)
# change the current location for storing files
os.chdir('/home/heet/aditbhai/file_finding')
for ext in data["extension"]:
    a = ext.rsplit('.',1)
    name = a[1]+"file"+'.txt'    
    with open(name,'w') as wr:

        for name in glob.glob(path+ext,recursive=True):
            x = name.replace(get_input,'')            
            wr.write(x)                
            wr.write("\n")

print("your inforation is in file_finding directory chek it out!")