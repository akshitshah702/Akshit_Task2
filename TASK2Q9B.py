# task 2 q9

number = -1
again = "yes"
while number !=5 and again != "no":
    number = input("Guess the lucky number: ")
    if number !=5:
        print ("That is not the lucky number")
        again = input("Would you like to guess again? ")