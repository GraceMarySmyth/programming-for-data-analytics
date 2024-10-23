# Programme to read in the data from data.csv
# Author: Grace Mary Smyth

import csv 

FILENAME= "data.csv" 
DATADIR = "../My work/"

with open (DATADIR + FILENAME, "rt") as fp: 
    reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_ALL) 
    linecount = 0
    total = 0
    for line in reader: 
        if not linecount: #header row
            print(f"{line}\n-----------------") 
        else: # all other rows
            total += int(line[0])           
            print (line) 
    linecount += 1