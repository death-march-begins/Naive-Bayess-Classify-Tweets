import sys
import os
import subprocess

#Argumen check
if len(sys.argv) !=3 :
    print ("\n\nPenggunaan\n\tjoin.py [pathSource] [Outputname]\n")
    sys.exit(1)

#Argumen
source = sys.argv[1]
output = sys.argv[2]

#get list file from source
data = str(subprocess.getoutput("ls "+source+" -v"))
list_file = data.split("\n") 

out = open(source+"/"+output, "w+")

for x in list_file :
    file = open(source+"/"+x).read()
    data_list = file.split("\n")
    for y in data_list :
        if y == "" :
            continue
        out.write(y+"\n")

out.close    

