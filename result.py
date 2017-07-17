import csv
import numpy as np
with open('bad-words.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    badwords = []
    weight = []
    count = []
    result = []
    for row in readCSV:
        badwords.append(row[0])
        weight.append(row[1])
weight = map(int, weight)
with open('testset.csv') as csvfile1:
    readCSV1 = csv.reader(csvfile1, delimiter=',')
    test = []
    for row in readCSV1:
        templist = row[1].split()
        temp = set(badwords).intersection(templist)
        my_list = list(temp)
        #print my_list
        final = 0
        for i in my_list:
            index = badwords.index(i)
            final = final + weight[index]
            result = final / len(my_list)
            print result
