from getData import getData

def addSupermarket():
    # Get current data from supermarkets.csv
    data = getData()

    # Get column names as list
    columns = data.columns.values.tolist()
    
    # Create empty list for new supermarket
    new_supermarket = list()

    # Iterate over columns and request user input for each one
    for column in columns:
        print("Enter value for " + column)
        value = input()
        new_supermarket.append(value)
    
    print("You entered the following: ")
    print(new_supermarket)
    
    print("Save to csv? y = yes, n = no")
    answer = input()

    # If user wants to save the dataframe, save it, else don't
    if answer == "y":
        # If there is data to be saved, save it. This works because you cannot save an empty 
        # data frame, so to_csv raises ValueError then
        try:
            # Append new data to dataframe
            data.loc[len(data)] = new_supermarket

            # Save to csv
            data.to_csv("data/supermarkets.csv", index=False)
            print("Saved!")
        except ValueError:
            if columns == []:
                print("Could not save dataframe as it does not contain any data - consider adding columns first")
    elif answer == "n":
        print("Not saved!")
    else:
        print("Invalid entry")

    return 0
