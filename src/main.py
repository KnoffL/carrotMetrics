from addSupermarket import addSupermarket
from addColumn import addColumn

while(True):
    print("Choose an option")
    print("s = add supermarket, a = add attribute, q = quit")
    answerMain = input()
    if answerMain == "s":
        addSupermarket()
    if answerMain == "a":
        addColumn()
    elif answerMain == "q":
        break

    print("Do you want to do something else? y = yes, n = no")
    answerMain = input()
    if answerMain == "n":
        break
print("Bye, bye - and have fun!")
