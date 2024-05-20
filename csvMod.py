import csv

def sortMuxes(matrix):
    combined_rows = []

    # Loop through the rows in batches of four
    for i in range(0, len(matrix), 4):
        combined_row = [cell for row in matrix[i:i+4] for cell in row]
        combined_rows.append(combined_row)

    return combined_rows


def remove_first_value(filename):
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        rows = [row for row in reader]

    # Remove the first two values from each set of 18 values in each row
    modified_rows = []
    for row in rows:
        modified_row = []
        for i in range(4):
            modified_row.extend(row[i * 17 + 1 : (i + 1) * 17])
        modified_rows.append(modified_row)

    return modified_rows

def modifyCSV(inputFile):
    ## creates copy of data in program
    data_in = inputFile
    with open(data_in, "r") as newCSV:
        newReader = csv.reader(newCSV)
        data = []
        for row in newReader:
            data.append(row)



    ##makes empty cols for formatting, readability
    emptyCol = [''] * len(data)

    data = remove_first_value(data_in)
    data = sortMuxes(data)

    emptyCol = [''] * len(data)

    for i, rows in enumerate(data[0]):
        ##insert 1st col, ave
        if i%10 == 8 :
            for k, emptyVal in enumerate(emptyCol):
                    data[k].insert(i, emptyVal)
        ##insert 2nd col, readable
        if i%10 == 9:
            for k, emptyVal in enumerate(emptyCol):
                    data[k].insert(i, emptyVal)

    for k, emptyVal in enumerate(emptyCol):
        data[k].insert(78, emptyVal)
        data[k].insert(79, '')
    
    del data[0]
    data.pop()

    ##adds empty rows on top to allow for headers
    emptyRow = [''] * len(data[0])
    for i in range(3):
        data.insert(0, emptyRow)

    ## writes formatted data to new file
    with open(data_in, 'w', newline= '') as moddedCSV:
        csvWrite = csv.writer(moddedCSV)
        csvWrite.writerows(data)
    
    return data


if __name__ == "__main__":
    modifyCSV("C:/Capstone Code/DataFiles/SESS250.csv")