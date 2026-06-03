from getData import getData
from pathlib import Path

def addColumn():
    # Ask user to which table they want to add a column
    print("To what table do you want to add a column?")
    tableName = input()

    # Get current data from {tableName}.csv
    data = getData(tableName)
    
    print("What is the name of the column you want to add?")
    column = input()

    print("Enter the default value for the column")
    default = input()

    # Set default value to all existing rows in the column
    data[column] = default

    print("Save to csv? y = yes, n = no")
    answer = input()

    # If user wants to save the dataframe, save it, else don't
    if answer == "y":
        filePath = "data/" + tableName + ".csv"
        try:
            data.to_csv(filePath, index=False)
        except OSError:
            Path("data").mkdir(parents=True, exist_ok=True)
            data.to_csv(filePath, index=False)
        print("Saved!")
    elif answer == "n":
        print("Not saved!")
    else:
        print("Invalid entry")
