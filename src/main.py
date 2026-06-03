from addSupermarket import addSupermarket
from addColumn import addColumn
from addPurchase import addPurchase
from addCarrotBrand import addCarrotBrand
from changeRating import changeRating

while(True):
    print("Choose an option")
    print("s = add supermarket, a = add attribute, p = add purchase, c = add carrot brand, r = change rating, q = quit")
    answerMain = input()
    if answerMain == "s":
        addSupermarket()
    elif answerMain == "a":
        addColumn()
    elif answerMain == "p":
        addPurchase()
    elif answerMain == "c":
        addCarrotBrand()
    elif answerMain == "r":
        changeRating()
    elif answerMain == "q":
        break
    else:
        print("Invalid entry")

    print("Do you want to do something else? y = yes, n = no")
    answerMain = input()
    if answerMain == "n":
        break
print("Bye, bye - and bon appetit!")
