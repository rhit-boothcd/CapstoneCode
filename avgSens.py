import csv
import os

def averageSensors(filename):
    ## open file and import data
    dataPath = filename
    with open(dataPath, "r") as resistCSV:
        newReader = csv.reader(resistCSV)
        data = []
        for row in newReader:
            data.append(row)
    #print(data)
    for i, rows in enumerate(data):
        for k, cols in enumerate(data[0]):
            if i > 2 and k %10 != 8 and k % 10 != 9 :
                data [i][k] = float(data[i][k])
                if k%10 == 0:
                    count = 0
                count += data[i][k]
                if k%10 == 7:
                    if k/10 != 4 or k/10 != 5:
                        avg = count/8
                    else:
                        avg = count/4
                    data[i][k+1] = avg

    #data_out = "SESS250" + '_avgd.csv'
    with open(filename, 'w', newline= '') as forceCSV:
        csvWrite = csv.writer(forceCSV)
        csvWrite.writerows(data)
    return data

#averageSensors("C:\Capstone Code\DataFiles\SESS250_forced.csv")