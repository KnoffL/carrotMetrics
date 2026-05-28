from getData import getData
from pathlib import Path

def addColumn():
    # Get current data from supermarkets.csv
    data = getData()
    
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
        try:
            data.to_csv("data/supermarkets.csv", index=False)
        except OSError:
            Path("data").mkdir(parents=True, exist_ok=True)
            data.to_csv("data/supermarkets.csv", index=False)
        print("Saved!")
    elif answer == "n":
        print("Not saved!")
    else:
        print("Invalid entry")
