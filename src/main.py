from addSupermarket import addSupermarket

while(True):
    print("Choose an option")
    print("s = add supermarket, q = quit")
    answer = input()
    if answer == "s":
        addSupermarket()
    elif answer == "q":
        break
    else:
        print("Invalid entry")
    print("Do you want to do something else? y = yes, n = no")
    answer = input()
    if answer == "n":
        break
print("Bye, bye - and have fun!")
