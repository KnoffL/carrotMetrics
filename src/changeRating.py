from getData import getData
from addColumn import addColumn
import pandas as pd
import numpy as np

def changeRating():
    dataRanking = getData("ranking")
    dataCarrotBrand = getData("carrotBrands")

    # Get all names to be ranked
    try:
        rankedBrands = set(dataRanking["name"])
        brands = dataCarrotBrand["name"]
    except:
        try:
            brands = dataCarrotBrand["name"]
        except:
            print("brandCarrots.csv does not contain a column 'name', please add this column first:")
            addColumn()
            changeRating()
        print("ranking does not yet contain a column 'name'")
        columns = dataRanking.columns.values.tolist()
        if columns == []:
            print("ranking does not have any columns, setting 'name' of brandCarrots.csv as 'name' column")
            dataRanking = pd.DataFrame(data={"name": dataCarrotBrand["name"]})
            columns = dataRanking.columns.values.tolist()
            print(columns)
            dataRanking["current ranking"] = np.nan
            for brand in dataRanking["name"]:
                print(brand + " has not been ranked so far.")
                print("What should their future rating be?")
                futureRating = int(input())
                rownumber = dataRanking[dataRanking['name'] == brand].index.tolist()[0]
                for rowindex in range(len(dataRanking)):
                    currentRowRating = dataRanking.at[rowindex, "current ranking"]
                    if currentRowRating >= futureRating:
                        dataRanking.at[rowindex, "current ranking"] += 1
                dataRanking.loc[rownumber, "current ranking"] = futureRating
            rankedBrands = set(dataRanking["name"])

    print("This is the current rating: ")
    try:
        rankingdf = dataRanking[["name", "current ranking"]].sort_values(by="current ranking")
        print(rankingdf)
    except:
        print("So far, the brands have not been ranked.")
    
    unrankedBrands = list(set(brands) - set(rankedBrands))
    if unrankedBrands != []:
        for brand in unrankedBrands:
            print(brand + " has not been ranked so far.")
            print("What should their future rating be?")
            futureRating = int(input())
            for rowindex in range(len(dataRanking)):
                currentRowRating = dataRanking.at[rowindex, "current ranking"]
                if currentRowRating >= futureRating:
                    dataRanking.at[rowindex, "current ranking"] += 1
            dataRanking.loc[len(dataRanking), "current ranking"] = futureRating
            dataRanking.loc[len(dataRanking) - 1, "name"] = brand

            rankingdf = dataRanking[["name", "current ranking"]].sort_values(by="current ranking")
            print("New ranking: ")
            print(rankingdf)

    print("Whose rating would you like to change? Currently in the database: ")
    try:
        rankingdf = dataRanking[["name", "current ranking"]].sort_values(by="current ranking")
        print(rankingdf)
    except:
        print("So far, there are no brands to rank - add brands first.")
        return
    ratingChangeName = input()
    print("What should their future rating be?")
    futureRating = int(input())
    rownumber = dataRanking[dataRanking['name'] == ratingChangeName].index.tolist()[0]
    rankalias = int(dataRanking.at[rownumber, "current ranking"])
    if rankalias == futureRating:
        print("Desired rating is equal to current rating")
    for rowindex in range(len(dataRanking)):
        currentRowRating = dataRanking.at[rowindex, "current ranking"]
        if rankalias > futureRating and (currentRowRating < rankalias and currentRowRating >= futureRating) and rowindex != rownumber:
            dataRanking.at[rowindex, "current ranking"] += 1
        elif rankalias < futureRating and (currentRowRating > rankalias and currentRowRating <= futureRating) and rowindex != rownumber:
            dataRanking.at[rowindex, "current ranking"] -= 1
    dataRanking.at[rownumber, "current ranking"] = futureRating

    rankingdf = dataRanking[["name", "current ranking"]].sort_values(by="current ranking")
    print("New ranking: ")
    print(rankingdf)

    print("Save to csv? y = yes, n = no")
    answer = input()

    # If user wants to save the dataframe, save it, else don't
    if answer == "y":
        # If there is data to be saved, save it. This works because you cannot save an empty 
        # data frame, so to_csv raises ValueError then
        try:
            # Save to csv
            dataRanking.to_csv("data/ranking.csv", index=False)
            print("Saved!")
        except ValueError:
            if columns == []:
                print("Could not save dataframe as it does not contain any data - consider adding columns first")
    elif answer == "n":
        print("Not saved!")
    else:
        print("Invalid entry")
