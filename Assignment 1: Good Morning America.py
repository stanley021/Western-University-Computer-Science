#This is Stanley Chen(251093164) I created this program.
#This program will basically ask the customer for their choice of breakfast and it will continue until the customer inputs 'q' and wants to stop ordering.
#The three below are combos created for the customer.
small_breakfast = ["egg","hash brown", "toast", "toast","bacon","bacon", "sausage"]
regular_breakfast = ["egg","egg","hash brown", "toast", "toast","bacon","bacon","bacon","bacon", "sausage","sausage"]
big_breakfast = ["egg","egg","egg","hash brown","hash brown", "toast", "toast","toast", "toast","bacon","bacon","bacon","bacon","bacon","bacon", "sausage","sausage", "sausage"]
#Displaying the menu
print("Welcome to Good Morning America!")
print("This is our menu for today:")
cart = []
choices = 0
#This is the function that helps fix the input into something that is more legible for the program.
def formatInput(choices) :
    choices = choices.lower().strip()
    wordList = choices.split()
    choices = " ".join(wordList)
    return choices
#I created a while loop to constantly ask the customer their order, until they want to stop.
while choices != "q":
    choices = formatInput(input("Enter item (q to terminate): small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea: "))
#Breaking the program whenever the customer wants to stop ordering and showing a display message.
    if choices == "q":
        print("Thank you for ordering")
        break
#When it detects a correct input it will ask how many times and append the item to the list accordingly
    elif choices == "egg" or choices == "hash brown" or choices == "toast" or choices == "bacon" or choices == "tea" or choices == "coffee" or choices == "sausage":
        amount = formatInput(input("How many?"))
        if amount.isnumeric():
            for n in range(int(amount)):
                cart.append(choices)
#When the user does not enter a valid number like "Five", (.isnumeric()) is a function inside of python that is able to tell me whether it is a number or not.
        else:
            print("please enter in a numeric number")
#For the different sizes of breakfast there is a different method implemented, the items in the lists are added according to the amount they want
    elif choices == "small breakfast" or choices == "regular breakfast" or choices == "big breakfast" :
        amount = formatInput(input("How many?"))
        if amount.isnumeric():
            if choices == "small breakfast":
                for n in range(int(amount)):
                    for w in small_breakfast:
                        cart.append(w)
            if choices == "regular breakfast":
                for n in range(int(amount)):
                    for w in regular_breakfast:
                        cart.append(w)
            if choices == "big breakfast":
                for n in range(int(amount)):
                    for w in big_breakfast:
                        cart.append(w)
        else:
            print("please enter in a numeric number")
#This invalid input is for when the item entered is not valid and cannot be recognized by the program
    else:
        print("invalid input")

total_price = 0
#Going through the list and accumulating the price of the meal
for n in cart:
    if n == "egg":
        total_price += 0.99
    elif n == "bacon":
        total_price += 0.49
    elif n == "sausage":
        total_price += 1.49
    elif n == "hash brown":
        total_price += 1.19
    elif n == "toast":
        total_price += 0.79
    elif n == "coffee":
        total_price += 1.09
    elif n == "tea":
        total_price += 0.89
#Final statement for the order, showing the tax and total price after tax.
print("Cost: $", round(total_price, 2))
print("Tax: $", round(total_price * 0.13,2))
print("Total price after tax: $", round(total_price * 1.13,2))
