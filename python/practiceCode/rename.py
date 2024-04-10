# rename multiple files to access the exact number in order

import os

path = "/home/priyanshu/Desktop/contArrange"
common = "Sigma"

listFile = os.listdir(path)

try:
    for i in listFile:
        index = i.find(common)
        if index != -1:
            os.renames(os.path.join(path, i), os.path.join(path, i[index::]))
            print("renamed")
except:
    print("Error ")
