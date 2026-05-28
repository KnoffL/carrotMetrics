import pandas as pd

def getData():
    try:
        dataSupermarkets = pd.read_csv("data/supermarkets.csv")
    except:
        print("Did not find supermarkets.csv, returning empty dataframe")
        dataSupermarkets = pd.DataFrame()
    return dataSupermarkets