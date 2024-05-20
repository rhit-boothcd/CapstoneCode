import csv
import os

def voltageConvert(filename):
    ## open file and import data
    dataPath = filename
    with open(dataPath, "r") as resistCSV:
        newReader = csv.reader(resistCSV)
        data = []
        for row in newReader:
            data.append(row)

    res1 = 10000 #ohms
    forceSlope = 3.76306*(10^(-5))
    vIn = 5 #volts

    for i, rows in enumerate(data):
        for k, cols in enumerate(data[0]):
            if i > 2 and k %10 != 8 and k % 10 != 9:
                voltIn = 5 - float(data[i][k])
                if voltIn >=5:
                    data[i][k] = 110
                if voltIn < .15:
                    data[i][k] = 0
                else:
                    resDenom = (voltIn - 5)
                    force = forceSlope*voltIn/resDenom
                    data[i][k] = force

    with open(filename, 'w', newline= '') as forceCSV:
        csvWrite = csv.writer(forceCSV)
        csvWrite.writerows(data)
    #return data

#voltageConvert("C:\Capstone Code\DataFiles\SESS250.csv")