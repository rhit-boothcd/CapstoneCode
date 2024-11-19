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

    #constants for conversion eqs
    a = 8761.5
    b = -3409.4
    c = 331.93

    a2 = 3244.2
    b2 = -545.07
    c2 = -32.041


    for i, rows in enumerate(data):
        for k, cols in enumerate(data[0]):
            if i > 2 and k % 10 != 8 and k % 10 != 9:
                volt = float(data[i][k])
                voltInv = 1/float(data[i][k])

                #data conversion equations
                if volt >=4.75: #underloaded
                    data[i][k] = 0
                elif volt < 0.5:
                    data[i][k] = -1
                elif volt < 2.5: #overload point
                    data[i][k] = 270
                elif volt >= 3.79 and volt < 3.83: #transition curve
                    force = 4908*voltInv - 1245
                    data[i][k] = force
                elif volt < 3.79: #heavy curve (>50#)
                    force = a2*voltInv*voltInv + b2*voltInv + c2
                    data[i][k] = force
                else: #light curve (<40#)
                    force = a*voltInv*voltInv + b*voltInv + c
                    data[i][k] = force

    ## old conversion curves
    # res1 = 10000 #ohms
    # forceSlope = 3.76306*(10^(-5))
    # vIn = 5 #volts

    # for i, rows in enumerate(data):
    #     for k, cols in enumerate(data[0]):
    #         if i > 2 and k %10 != 8 and k % 10 != 9:
    #             voltIn = 5 - float(data[i][k])
    #             if voltIn >=4.97:
    #                 data[i][k] = 110
    #             if voltIn < .15:
    #                 data[i][k] = 0
    #             else:
    #                 resDenom = (voltIn - 5)
    #                 force = forceSlope*voltIn/resDenom
    #                 data[i][k] = force

    with open(filename, 'w', newline= '') as forceCSV:
        csvWrite = csv.writer(forceCSV)
        csvWrite.writerows(data)
    #return data

#voltageConvert("C:\Capstone Code\DataFiles\SESS250.csv")
if __name__ == "__main__":
    voltageConvert("C:/Users/boothcd/Downloads/newVerTest.csv")