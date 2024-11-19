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
    # for counting sensors that are in differing sets
    count1 = 0
    count2 = 0
    fail1 = 0
    fail2 = 0
    # read through all of the rows
    for i, rows in enumerate(data):
        for k, cols in enumerate(data[0]):
            # read all non-empty rows, convert to numeric
            if i > 2 and k %10 != 8 and k % 10 != 9 :
                data [i][k] = float(data[i][k])
                # separate into the two counters based on patch (L/R), remove shorted sensors
                if k%2 == 0 and k%10 < 8:
                    if data[i][k] == -1:
                        fail1 += 1
                    else:
                        count1 += data[i][k]

                if k%2 == 1 and k%10 < 8:
                    if data[i][k] == -1:
                        fail2 += 1
                    else:
                        count2 += data[i][k]
            # At the end of a Mux (20th column)
            if k%20 == 18:
                # Separate based on spine vs. normal patch
                if k//20 != 1:
                    if 8-fail1 > 0:
                        avg1 = count1/(8-fail1)
                    else: avg1 = 0

                    if 8-fail2 > 0:
                        avg2 = count2/(8-fail2)
                    else: avg2 = 0

                else:
                    if 4-fail1 > 0:
                        avg1 = (count1)/(4-fail1)
                    else: avg1 = 0

                    if 4-fail2 > 0:
                        avg2 = (count2)/(4-fail2)
                    else: avg2 = 0

                # place data in correct avg column, reset counters
                data[i][k-10] = avg1
                data[i][k] = avg2
                count1 = 0
                count2 = 0
                fail1 = 0
                fail2 = 0

    # place data in file
    with open(filename, 'w', newline= '') as forceCSV:
        csvWrite = csv.writer(forceCSV)
        csvWrite.writerows(data)
    return data

#averageSensors("C:\Capstone Code\DataFiles\SESS250_forced.csv")
if __name__ == "__main__":
    averageSensors("C:/Users/boothcd/Downloads/Heavyweight.CSV")