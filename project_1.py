print("The currency is USA dollars.")
print("Which sphere will you choose?")
print("· electricity (e)")
print("· hot water (hw)")
print("· cold water (cw)")
print("· water drain (wd)")
print("· gas (g)")
print("· enter your tariff")
print("You are 18 years old?")
b = input("Enter yes or no:", )
while b != "no":
    sphere = input("Enter the sphere:", )
    tariff_1 = input("Enter the tariff:", )
    if "." in tariff_1:
        tariff = float(tariff_1)
    else:
        tariff = int(tariff_1)
    if sphere == "e":
        print("How much kilowatt per hour have you used up?")
    elif sphere == "hw":
        print("How much cubic meters gave you used up?")
    elif sphere == "cw":
        print("How much cubic meters gave you used up?")
    elif sphere == "wd":
        print("How much cubic meters have you used up in total?")
    elif sphere == "g":
        print("How much cubic meters gave you used up?")
    expenses = int(input("enter the expenses:", ))
    if sphere == "e":
        print("you have to pay:", tariff * expenses, "$")
    elif sphere == "hw":
        print("you have to pay:", tariff * expenses, "$")
    elif sphere == "cw":
        print("you have to pay:", tariff * expenses, "$")
    elif sphere == "wd":
        print("you have to pay:", tariff * expenses, "$")
    elif sphere == "g":
        print("you have to pay:", tariff * expenses, "$")
    print("Do you want to transfer to another currency?")
    answer = input("enter yes or no:", )
    a = tariff * expenses
    if answer == "yes":
        print("Enter how much one dollar is worth in your currency.")
        cost = int(input())
        print(cost * a)
    print("Would you like to continue?")
    b = input("Enter yes or no:", )
print("See you!")
