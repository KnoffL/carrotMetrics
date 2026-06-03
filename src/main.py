from addSupermarket import addSupermarket
from addColumn import addColumn
from addPurchase import addPurchase

while(True):
    print("Choose an option")
    print("s = add supermarket, a = add attribute, p = add purchase, q = quit")
    answerMain = input()
    if answerMain == "s":
        addSupermarket()
    elif answerMain == "a":
        addColumn()
    elif answerMain == "p":
        addPurchase()
    elif answerMain == "q":
        break
    else:
        print("Invalid entry")

    print("Do you want to do something else? y = yes, n = no")
    answerMain = input()
    if answerMain == "n":
        break
print("Bye, bye - and bon appetit!")
