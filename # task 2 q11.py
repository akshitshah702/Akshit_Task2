# task 2 q11

counter = 1
while counter <= 5:
   number = input("Guess the " + str(counter) + ". number ")
   if number != 5:
       print ("Try again.")
   else:
       print ("Good guess!")
       break
   counter = counter +1
else:
   print ("Sorry but that was not very successful")