import csv
from . import txtToCsv
from . import csvMod
from . import resistToVolt
from . import avgSens
import os


def txt_to_csv(inputFile: str, newName):
    filename = newName
    
    txtToCsv.txt2csv(inputFile, filename)
    moddedCSV = csvMod.modifyCSV(filename)
    # avgCSV = avgSens.averageSensors(filename)
    # finalMat = resistToVolt.voltageConvert(filename)
    resistCSV = resistToVolt.voltageConvert(filename)
    finalMat = avgSens.averageSensors(filename)
    #print(finalMat)
    # with open(filename, mode = 'w') as forceCSV:
    #     csvWrite = csv.writer(forceCSV)
    #     csvWrite.writerows(finalMat)



if __name__ == "__main__":
    txt_to_csv("C:/Users/boothcd/Downloads/SESS8.TXT", "newVerTest.csv")




