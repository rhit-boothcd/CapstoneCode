import pandas as pd


def txt2csv(path, filename):
    with open(path, 'r') as file:
        data = file.read()
    modified_data = data.replace('TestSession.txt', '')
    modified_data = data.replace('"', '')
    modified_data = data.replace('  ', '')
    modified_data = data.replace(',', '')
    with open(path, 'w') as file:
        file.write(modified_data)

    df = pd.read_fwf(path)
    writeFile = filename
    df.to_csv(writeFile)
