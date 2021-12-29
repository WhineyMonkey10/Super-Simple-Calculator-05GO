################################

operation = input("What is your calculation type you would like to make? (+, -, /) ")

if operation == ("+"):
    num1a = input("What number would you like to add to your calculation first? ")
    num2a = input("What number would you like to add to your calculation second? ")
    print("Your output is", int(num1a) + int(num2a))
else:
    if operation == ("-"):
        num1b = input("What number would you like to add to your calculation first? ")
        num2b = input("What number would you like to add to your calculation second? ")
        print("Your output is", int(num1b) - int(num2b))
    else:
        if operation == ("/"):
            num1c = input("What number would you like to add to your calculation first? ")
            num2c = input("What number would you like to add to your calculation second? ")
            print("Your output is", int(num1c) / int(num2c))
        else:
            print("Your operation was not found, please try again.")
