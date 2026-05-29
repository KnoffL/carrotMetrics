import pandas as pd

def getData(tableName):
    filePath = "data/" + tableName + ".csv"
    try:
        data = pd.read_csv(filePath)
    except:
        print("Did not find " + tableName + ".csv, returning empty dataframe")
        data = pd.DataFrame()
    return data
