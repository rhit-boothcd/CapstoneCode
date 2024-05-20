import csv
import txtToCsv
import csvMod
import resistToVolt
import avgSens
import os


def txt_to_csv(inputFile: str, newName):
    filename = newName
    
    txtToCsv.txt2csv(inputFile, filename)
    moddedCSV = csvMod.modifyCSV(filename)
    resistCSV = resistToVolt.voltageConvert(filename)
    finalMat = avgSens.averageSensors(filename)
    #print(finalMat)
    # with open(filename, mode = 'w') as forceCSV:
    #     csvWrite = csv.writer(forceCSV)
    #     csvWrite.writerows(finalMat)



if __name__ == "__main__":
    txt_to_csv("C:/Capstone Code/DataFiles/SESS-6.TXT", "testing_session_52124.csv")




